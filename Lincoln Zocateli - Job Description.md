---
version: "1.0.0"
last_reviewed: "2026-11-06"
confidentiality: "yellow"
docType: "reference"
audience: ["engineering-leadership", "software-engineers", "human-resources"]
tags: ["job-description", "software-engineering", "architecture", "devsecops"]
keywords: ["Senior Software Engineer", "Software Architect", "Technical Lead", "SSDLC", "Platform Engineering"]
---

<!--
agent.hints:
	intent_examples:
		- "Quais são as responsabilidades deste cargo de Senior Software Engineer?"
		- "Quais competências técnicas e de liderança estão associadas a esta função?"
		- "Como resumir o escopo deste cargo para uma descrição executiva?"
	answer_style: "descrição estruturada por responsabilidades, competências e escopo"
	canonical_section_order: ["Visão Geral", "Objetivo da Função", "Principais Responsabilidades", "Competências Técnicas", "Competências de Liderança e Negócio", "Versão Executiva", "Posicionamento Funcional", "Indicadores de Escala Registrados"]
	strict_citations: false
-->

# Job Description: Senior Software Engineer

## Visão Geral

Este documento descreve o escopo de atuação de um Senior Software Engineer em Information Technology, considerando responsabilidades que abrangem Software Engineering, Solution Architecture, Platform/DevOps Engineering, Application Security, Modernization, Technical Leadership e Engineering Governance.

O conteúdo pode apoiar uma descrição de cargo, currículo interno, promoção, Career Development, LinkedIn ou discussão de evolução de carreira. As métricas e experiências específicas devem ser confirmadas nas fontes corporativas antes de serem reutilizadas externamente.

## Objetivo da Função

Projetar, definir, implementar e evoluir soluções corporativas de software, atuando desde arquitetura e desenvolvimento até segurança, infraestrutura, CI/CD, observabilidade e operação em produção.

A função atua como referência técnica para aplicações empresariais e equipes de desenvolvimento. Estabelece padrões arquiteturais, tecnológicos e de engenharia que promovam segurança, qualidade, escalabilidade, resiliência, manutenibilidade, automação e eficiência operacional.

A atuação abrange todo o Secure Software Development Life Cycle (SSDLC): planejamento, arquitetura, desenvolvimento, testes, segurança, deployment, observabilidade, sustentação e modernização de aplicações. O modelo interno do time também incorpora práticas como OWASP, Zero Trust, DevSecOps e governança de cloud.

## Principais Responsabilidades

### Software Architecture & Solution Design

- Definir arquiteturas para aplicações corporativas modernas.
- Projetar soluções distribuídas com frontend, backend, APIs, workers, mensageria e integrações.
- Definir padrões arquiteturais, conforme a necessidade da solução, utilizando Clean Architecture, DDD, CQRS/CQS, SOLID, Dependency Injection, Repository, Mediator, Factory e Strategy.
- Estabelecer requisitos não funcionais de segurança, disponibilidade, performance, observabilidade e escalabilidade.
- Realizar avaliações técnicas e Architecture Reviews.
- Definir estratégias de modernização para aplicações legadas.
- Avaliar tecnologias, frameworks e padrões antes de sua adoção.

O perfil corporativo registra experiência em arquitetura .NET para Enterprise Applications, DDD, TDD, SOLID, Clean Code e APIs.

### Backend Engineering | .NET

- Arquitetar e desenvolver aplicações com C#, .NET/.NET Core, ASP.NET Core e REST APIs.
- Desenvolver serviços, APIs, Background Services e Worker Services.
- Definir e manter contratos com OpenAPI/Swagger.
- Desenvolver soluções assíncronas e otimizar performance.
- Implementar abstrações e padrões reutilizáveis.
- Desenvolver e manter templates corporativos.
- Evoluir e modernizar aplicações .NET legadas.

### Data Access & Databases

- Arquitetar camadas de persistência e estratégias de acesso aos dados.
- Utilizar Entity Framework Core, LINQ, Migrations e Fluent API.
- Trabalhar com SQL Server, Oracle, IBM DB2, Postgres
- Avaliar ORM versus micro-ORM conforme os requisitos de performance.
- Projetar aplicações com múltiplos DbContexts quando necessário.
- Definir estratégias de consistência, performance e evolução de schemas.

### Frontend Architecture

- Definir arquitetura para aplicações corporativas SPA com Angular e TypeScript.
- Estabelecer estratégias de componentização e reutilização.
- Definir a organização de features e responsabilidades entre frontend, BFF e backend.
- Orientar padrões de state management, lazy loading e reactive forms.
- Garantir integração segura entre frontend e serviços.
- Estabelecer padrões de qualidade, testes, acessibilidade e performance.
- Angular moderno, componentização, RxJS, Signals/NGRX, testes, WCAG, segurança e integração com BFF como competências da disciplina de arquitetura frontend.

### DevOps, Platform Engineering & Infrastructure

- Projetar e manter pipelines de CI/CD.
- Automatizar build, testes, quality gates, security checks e deployments.
- Trabalhar com Azure DevOps e GitHub Enterprise/GitHub Actions.
- Definir políticas de Git, branches, Pull Requests e Code Review.
- Criar automações com PowerShell, Bash e Python.
- Implementar Infrastructure as Code com Terraform.
- Automatizar configuração com Ansible.
- Administrar ambientes Linux e Windows Server.
- Trabalhar com Docker, Podman e Docker Compose.
- Projetar ambientes com NGINX e HAProxy como reverse proxy e load balancer.

### Cloud & Azure

- Arquitetar workloads e serviços Microsoft Azure.
- Integrar aplicações e infraestrutura com Azure.
- Utilizar serviços de mensageria como Azure Service Bus.
- Definir estratégias de autenticação e identidade com Microsoft Entra ID.
- Gerenciar componentes e recursos utilizados pelas aplicações em diferentes ambientes.
- Aplicar princípios de cloud-native architecture, automação e observabilidade.

### Application Security & DevSecOps

- Incorporar segurança desde o design, conforme princípios de SSDLC.
- Implementar autenticação e autorização com OAuth 2.0, OpenID Connect e JWT.
- Integrar aplicações com Microsoft Entra ID.
- Implementar e orientar arquitetura Backend for Frontend (BFF).
- Gerenciar CORS, CSRF, cookies, sessão e exposição de APIs.
- Aplicar princípios de Zero Trust.
- Gerenciar secrets, certificados, TLS e mTLS.
- Identificar e mitigar vulnerabilidades.
- Trabalhar com SAST, DAST e análise de dependências.
- Considerar OWASP Top 10 e secure coding nas decisões arquiteturais.

### Software Quality & Engineering Governance

- Definir padrões corporativos de desenvolvimento.
- Estabelecer processo estruturado de Code Review.
- Implementar e administrar SonarQube Quality Gates.
- Acompanhar bugs, vulnerabilities, security hotspots, code smells e coverage.
- Integrar ferramentas de análise estática e segurança aos pipelines.
- Implementar políticas de Pull Requests.
- Utilizar SonarQube, Dependabot, ESLint, EditorConfig e GitHub.
- Manter templates corporativos atualizados.
- Promover melhoria contínua utilizando práticas como PDCA.

### Observability & Production Engineering

- Projetar estratégias de monitoramento e observabilidade.
- Implementar métricas, logs, dashboards e alertas.
- Trabalhar com Application Insights, Prometheus, Grafana e Alertmanager.
- Monitorar aplicações containerizadas e infraestrutura.
- Identificar gargalos de performance e capacidade.
- Apoiar troubleshooting e incident response.
- Utilizar dados operacionais para decisões arquiteturais.

### Technical Leadership

Além da atuação hands-on, a função exerce liderança técnica, incluindo:

- Mentoria técnica de desenvolvedores e disseminação de boas práticas.
- Definição de padrões técnicos e coordenação de iniciativas arquiteturais.
- Facilitação de decisões técnicas entre squads.
- Planejamento e acompanhamento de iniciativas com práticas Agile/Kanban.
- Organização de responsabilidades de acordo com as especialidades do time.
- Interface técnica com equipes corporativas de infraestrutura, segurança, IAM, cloud e desenvolvimento.

## Competências Técnicas

### Software Engineering

C#; .NET; ASP.NET Core; ASP.NET MVC; REST APIs; Background Services; Angular; TypeScript; JavaScript; HTML5; CSS.

### Software Architecture

Clean Architecture; DDD; CQRS/CQS; SOLID; Design Patterns; Microservices; BFF; API Design; Distributed Systems.

### Data

Entity Framework Core; LINQ; Dapper; SQL Server; Oracle; IBM DB2; Postgres; Migrations; Fluent API.

### Cloud

Microsoft Azure; Azure Service Bus; Azure Web Apps; Azure Container Apps; Microsoft Entra ID; Azure Services.

### DevOps / Platform Engineering

Azure DevOps; GitHub; CI/CD; Git; Docker; Podman; NGINX; HAProxy; Terraform; Ansible; PowerShell; Bash; Linux; Windows Server.

### Security

OAuth 2.0; OpenID Connect; JWT; TLS/mTLS; OWASP; SSDLC; DevSecOps; Zero Trust; SAST; DAST; Dependency Scanning; Secrets Management.

### Quality

SonarQube; Quality Gates; Code Review; Pull Request Governance; Dependabot; Automated Testing.

### Observability

Prometheus; Grafana; Application Insights; Alerting; Logging; Metrics; Dashboards.

## Competências de Liderança e Negócio

- Technical Leadership
- Solution Architecture
- Strategic Technical Decision Making
- Mentoring & Knowledge Sharing
- Agile / Kanban
- Engineering Governance
- Stakeholder Management
- Risk Management
- Continuous Improvement
- Technical Problem Solving
- Cross-team Collaboration
- Technology Evaluation
- Application Lifecycle Management
- Comunicação entre áreas técnicas e negócio
- Planejamento de iniciativas de modernização
- Gestão de dívida técnica e risco tecnológico

## Versão Executiva

Senior Software Engineer especializado em Software Architecture, Cloud, Platform Engineering e DevSecOps, responsável por definir e evoluir arquiteturas corporativas de software ao longo de todo o SSDLC. Atua como referência técnica em .NET, Angular, Azure, containers, CI/CD, segurança, observabilidade e qualidade de código, liderando iniciativas de modernização, automação e padronização de engenharia. Estabelece padrões arquiteturais e práticas que aumentem segurança, disponibilidade, escalabilidade, qualidade e eficiência operacional, além de orientar equipes de desenvolvimento e conectar requisitos de negócio às capacidades tecnológicas da organização.

## Posicionamento Funcional

O título formal registrado é **Senior Software Engineer**. As responsabilidades descritas também abrangem arquitetura, modernização, plataforma, segurança, observabilidade, governança técnica, definição de padrões e liderança técnica em um ecossistema de centenas de aplicações.

Como representação funcional do escopo, podem ser considerados:

- **Senior Software Engineer | Software Architect | Technical Lead**
- **Staff/Principal Software Engineer | Software Architecture & Engineering**, caso a organização utilize posições Staff/Principal.

Essas opções descrevem o escopo técnico evidenciado pelas responsabilidades; não representam uma alteração do nível formal do cargo.

## Indicadores de Escala Registrados

O ambiente documentado chegou a aproximadamente:

- 320 aplicações em produção.
- 320 repositórios Azure DevOps.
- 432 pipelines CI/CD.
- 109 scripts Bash/PowerShell/Terraform.
- 189 Azure Services.

Os números são apresentados conforme registrados nos materiais de origem e devem ser validados antes de uso externo.
