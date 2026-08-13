#!/usr/bin/env python3
"""Atualiza as tabelas dinâmicas de estatísticas no README do perfil."""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta, timezone, tzinfo
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

START_MARKER = "<!-- PROFILE-STATS:START -->"
END_MARKER = "<!-- PROFILE-STATS:END -->"
BAR_SIZE = 24


@dataclass(frozen=True)
class CommitStats:
    periods: Counter[str]
    weekdays: Counter[str]
    total: int


class GitHubApi:
    def __init__(self, token: str | None) -> None:
        self._headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "lzocateli-profile-readme",
        }
        if token:
            self._headers["Authorization"] = f"Bearer {token}"

    def get(self, path: str, params: dict[str, Any] | None = None) -> Any:
        query = urllib.parse.urlencode(params or {})
        url = path if path.startswith("https://") else f"https://api.github.com{path}"
        if query:
            url = f"{url}?{query}"

        request = urllib.request.Request(url, headers=self._headers)
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.load(response)
        except urllib.error.HTTPError as error:
            details = error.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"GitHub API retornou HTTP {error.code}: {details}") from error

    def paginate(self, path: str, params: dict[str, Any] | None = None) -> list[Any]:
        items: list[Any] = []
        page = 1
        while True:
            page_params = {**(params or {}), "per_page": 100, "page": page}
            batch = self.get(path, page_params)
            if not isinstance(batch, list):
                raise TypeError(f"Resposta inesperada da API em {path}")
            items.extend(batch)
            if len(batch) < 100:
                return items
            page += 1


def collect_repositories(api: GitHubApi, username: str) -> list[dict[str, Any]]:
    repositories = api.paginate(
        f"/users/{username}/repos",
        {"type": "owner", "sort": "updated", "direction": "desc"},
    )
    return [
        repository
        for repository in repositories
        if not repository.get("fork") and not repository.get("archived")
    ]


def collect_languages(
    api: GitHubApi, repositories: list[dict[str, Any]]
) -> Counter[str]:
    language_repositories: Counter[str] = Counter()
    for repository in repositories:
        languages = api.get(repository["languages_url"])
        language_repositories.update(languages.keys())
    return language_repositories


def collect_commits(
    api: GitHubApi,
    username: str,
    since: datetime,
    timezone: tzinfo,
) -> CommitStats:
    query = f"author:{username} user:{username} committer-date:>={since.date().isoformat()}"
    periods: Counter[str] = Counter()
    weekdays: Counter[str] = Counter()
    page = 1

    while page <= 10:
        result = api.get(
            "/search/commits",
            {"q": query, "sort": "committer-date", "order": "desc", "per_page": 100, "page": page},
        )
        commits = result.get("items", [])
        for item in commits:
            committed_at = datetime.fromisoformat(
                item["commit"]["committer"]["date"].replace("Z", "+00:00")
            ).astimezone(timezone)
            periods[period_name(committed_at.hour)] += 1
            weekdays[weekday_name(committed_at.weekday())] += 1
        if len(commits) < 100:
            break
        page += 1

    total = sum(periods.values())
    return CommitStats(periods=periods, weekdays=weekdays, total=total)


def period_name(hour: int) -> str:
    if 6 <= hour < 12:
        return "Manhã"
    if 12 <= hour < 18:
        return "Tarde"
    if 18 <= hour < 24:
        return "Noite"
    return "Madrugada"


def weekday_name(weekday: int) -> str:
    return (
        "Segunda-feira",
        "Terça-feira",
        "Quarta-feira",
        "Quinta-feira",
        "Sexta-feira",
        "Sábado",
        "Domingo",
    )[weekday]


def load_timezone(name: str) -> tzinfo:
    try:
        return ZoneInfo(name)
    except ZoneInfoNotFoundError:
        if name == "America/Sao_Paulo":
            return timezone(timedelta(hours=-3), "BRT")
        raise


def percentage(value: int, total: int) -> float:
    return value / total * 100 if total else 0.0


def bar(value: int, maximum: int) -> str:
    filled = round(value / maximum * BAR_SIZE) if maximum else 0
    return "█" * filled + "░" * (BAR_SIZE - filled)


def render_table(title: str, rows: list[tuple[str, int, str]], unit: str) -> str:
    maximum = max((count for _, count, _ in rows), default=0)
    total = sum(count for _, count, _ in rows)
    body = "\n".join(
        "  <tr>"
        f"<td>{label}</td><td align=\"right\">{count} {unit}</td>"
        f"<td><code>{bar(count, maximum)}</code></td>"
        f"<td align=\"right\">{percentage(count, total):05.2f}%</td></tr>"
        for label, count, _ in rows
    )
    return (
        f"### {title}\n\n"
        '<table width="100%">\n'
        "  <thead><tr><th align=\"left\">Categoria</th><th align=\"right\">Total</th>"
        "<th align=\"left\">Distribuição</th><th align=\"right\">Percentual</th></tr></thead>\n"
        f"  <tbody>\n{body}\n  </tbody>\n</table>"
    )


def render_stats(commit_stats: CommitStats, languages: Counter[str], updated_at: datetime) -> str:
    period_icons = {"Manhã": "🌅", "Tarde": "☀️", "Noite": "🌆", "Madrugada": "🌙"}
    period_order = ("Manhã", "Tarde", "Noite", "Madrugada")
    period_rows = [
        (f"{period_icons[name]} {name}", commit_stats.periods[name], "commits")
        for name in period_order
    ]

    language_rows = [
        (language, count, "repositórios")
        for language, count in languages.most_common(10)
    ]

    weekday_order = (
        "Domingo",
        "Segunda-feira",
        "Terça-feira",
        "Quarta-feira",
        "Quinta-feira",
        "Sexta-feira",
        "Sábado",
    )
    weekday_rows = [
        (name, commit_stats.weekdays[name], "commits") for name in weekday_order
    ]

    dominant_period = max(period_rows, key=lambda row: row[1])[0] if commit_stats.total else "sem dados"
    dominant_language = language_rows[0][0] if language_rows else "sem dados"
    dominant_weekday = max(weekday_rows, key=lambda row: row[1])[0] if commit_stats.total else "sem dados"

    sections = [
        render_table(f"🕒 Mais ativo em {dominant_period}", period_rows, "commits"),
        render_table(f"🔥 Mais código em {dominant_language}", language_rows, "repos"),
        render_table(f"🗓️ Mais produtivo na {dominant_weekday}", weekday_rows, "commits"),
        f"<sub>⏳ Atualizado em {updated_at.strftime('%d/%m/%Y %H:%M:%S %Z')} · janela móvel de 12 meses</sub>",
    ]
    return f"{START_MARKER}\n\n" + "\n\n".join(sections) + f"\n\n{END_MARKER}"


def update_readme(readme_path: Path, generated_stats: str) -> None:
    content = readme_path.read_text(encoding="utf-8")
    start = content.find(START_MARKER)
    end = content.find(END_MARKER)
    if start == -1 or end == -1 or end < start:
        raise RuntimeError("Marcadores PROFILE-STATS não encontrados no README")
    end += len(END_MARKER)
    readme_path.write_text(content[:start] + generated_stats + content[end:], encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--username", default="lzocateli")
    parser.add_argument("--readme", type=Path, default=Path("README.md"))
    parser.add_argument("--timezone", default="America/Sao_Paulo")
    parser.add_argument("--dry-run", action="store_true", help="Exibe o bloco sem alterar o README")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    selected_timezone = load_timezone(args.timezone)
    now = datetime.now(UTC)
    api = GitHubApi(os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN"))

    repositories = collect_repositories(api, args.username)
    languages = collect_languages(api, repositories)
    commits = collect_commits(api, args.username, now - timedelta(days=365), selected_timezone)
    generated_stats = render_stats(commits, languages, now.astimezone(selected_timezone))

    if args.dry_run:
        print(generated_stats)
    else:
        update_readme(args.readme, generated_stats)
    return 0


if __name__ == "__main__":
    sys.exit(main())
