# Solution Patterns

Reusable solution patterns for common proposal types. Use these as starting frameworks — adapt scope, phases, and deliverables to the specific client.

---

## Pattern 1: Cloud Migration (Azure IaaS/PaaS)

### Typical Use Case
Client has on-premises infrastructure they want to move to Microsoft Azure — servers, storage, networking, and applications.

### Recommended Phases

| Phase | Name | Duration | Activities |
|-------|------|----------|-----------|
| 1 | Discovery & Assessment | 2–4 weeks | Infrastructure discovery, dependency mapping, migration readiness assessment, wave planning |
| 2 | Foundation Build | 2–4 weeks | Azure Landing Zone deployment, network connectivity (VPN/ExpressRoute), identity integration |
| 3 | Migration — Wave 1 | 2–4 weeks | Pilot migration of non-critical workloads, tooling validation (Azure Migrate) |
| 4 | Migration — Waves 2–N | 4–12 weeks | Production workload migration in planned waves |
| 5 | Optimisation | 2–4 weeks | Right-sizing, Reserved Instances, cost governance, tagging, monitoring |

### Key Deliverables
- Migration Readiness Assessment Report
- Azure Landing Zone (deployed)
- Migration Wave Plan
- Migrated workloads (per wave)
- Azure Cost Optimisation Report

### Standard Assumptions
- Client has Azure subscription(s) or agrees to procure them
- Sufficient internet bandwidth exists for migration traffic (or dedicated circuit is in scope)
- Client will provide inventory data for all in-scope systems

---

## Pattern 2: Microsoft 365 Migration (Exchange Online + SharePoint)

### Typical Use Case
Client is migrating email from on-premises Exchange or another provider to Exchange Online, and SharePoint/Teams for collaboration.

### Recommended Phases

| Phase | Name | Duration | Activities |
|-------|------|----------|-----------|
| 1 | Discovery | 2 weeks | Mailbox inventory, SharePoint content audit, licence sizing, dependency review |
| 2 | Pilot | 2–3 weeks | Pilot user group (IT + key stakeholders), configuration, test migration |
| 3 | Pre-Migration Prep | 2 weeks | Coexistence configuration, mail routing, Teams setup, SharePoint structure |
| 4 | Migration | 4–8 weeks | Mailbox migrations in batches, SharePoint/OneDrive content migration |
| 5 | Cutover & Stabilisation | 1–2 weeks | DNS cutover, decommission legacy, post-migration support |

### Key Deliverables
- M365 Tenant Configuration (Exchange Online, SharePoint, Teams)
- Migrated mailboxes and shared mailboxes
- SharePoint site structure and migrated content
- Post-migration support runbook

### Standard Assumptions
- Client holds or will procure appropriate M365 licences
- DNS access is available to the project team
- Legacy system (on-premises Exchange) will remain available during coexistence period

---

## Pattern 3: Managed IT Services

### Typical Use Case
Client wants to outsource day-to-day IT operations to a managed service provider.

### Recommended Structure

| Service Component | Essentials | Professional | Enterprise |
|-----------------|-----------|--------------|------------|
| Service Desk | Business hours | Business hours | 24x7 |
| Critical incident response | Business hours | 24x7 | 24x7 |
| Monitoring | Basic | Advanced | Advanced + SOC |
| Patching | Monthly | Monthly | Monthly + emergency |
| Reporting | Monthly | Monthly | Monthly + QBR |
| TAM | No | No | Yes |
| Strategic advisory | No | No | Yes |

### Onboarding Phases

| Phase | Name | Duration | Activities |
|-------|------|----------|-----------|
| 1 | Mobilisation | 2 weeks | Environment documentation, tooling deployment, knowledge capture |
| 2 | Hypercare | 4 weeks | Intensive support, daily stand-ups, issue resolution |
| 3 | BAU | Ongoing | Standard service delivery per contract |

---

## Pattern 4: Consultancy / Technology Assessment

### Typical Use Case
Client wants an independent assessment of their technology environment and a prioritised roadmap.

### Recommended Phases

| Phase | Name | Duration | Activities |
|-------|------|----------|-----------|
| 1 | Mobilisation | 1 week | Kickoff, stakeholder mapping, data request |
| 2 | Discovery | 2–3 weeks | Stakeholder interviews, workshops, environment review |
| 3 | Analysis | 1–2 weeks | Gap analysis, risk assessment, benchmarking |
| 4 | Recommendations | 1 week | Roadmap development, business case modelling |
| 5 | Reporting | 1 week | Findings presentation, report finalisation |

### Key Deliverables
- Stakeholder Interview Notes (sanitised)
- Current State Assessment Report
- Gap Analysis and Risk Register
- Technology Roadmap (1–3 year)
- Executive Presentation

### Effort Guide
- Small engagement (up to 50 users): 15–25 days
- Medium engagement (50–250 users): 25–40 days
- Large engagement (250+ users): 40–60 days

---

## Pattern 5: Security Assessment

### Typical Use Case
Client wants to understand their security posture — typically Microsoft 365 and Azure — and get a prioritised remediation plan.

### Recommended Phases

| Phase | Name | Duration | Activities |
|-------|------|----------|-----------|
| 1 | Scoping | 1 week | Define assessment scope, agree access, gather pre-assessment questionnaire |
| 2 | Assessment | 2–3 weeks | Identity review, endpoint review, email security, conditional access, secure score, external attack surface |
| 3 | Analysis | 1 week | Risk rating, priority matrix, remediation effort estimation |
| 4 | Reporting | 1 week | Security Assessment Report, Executive Summary, remediation roadmap |

### Key Deliverables
- Security Assessment Report (technical)
- Executive Summary (board-ready)
- Prioritised Remediation Plan (High/Medium/Low)
- Microsoft Secure Score baseline and target

### Assessment Domains
- Identity & Access Management
- Email Security & Anti-phishing
- Endpoint Security & Compliance
- Data Protection & Information Governance
- Conditional Access Policies
- Privileged Access & Admin Roles
- Monitoring & Alerting
