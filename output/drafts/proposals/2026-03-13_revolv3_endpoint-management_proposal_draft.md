# Endpoint Management & Managed Service Proposal

---

## Cover Page

| Field | Detail |
|-------|--------|
| **Proposal Title** | Endpoint Management Implementation & Managed Service |
| **Prepared for** | Revolv3 |
| **Prepared by** | Cloudbd |
| **Document Reference** | PROP-2026-03-13-REVOLV3 |
| **Date** | 13 March 2026 |
| **Version** | 1.0 |
| **Validity** | Valid for 30 days from date of issue |

---

## Executive Summary

Revolv3 operates a mixed Windows and macOS laptop estate across a geographically distributed team in a PCI DSS-regulated payment gateway environment. Inconsistent endpoint controls across approximately 40 corporate devices create compliance risk, limit visibility, and leave the organisation exposed to privilege and access-related vulnerabilities that are incompatible with a payment processing operation.

We propose a two-phase engagement: a complimentary implementation phase that establishes Microsoft Intune as the central management platform, enforces a PCI DSS-aligned security baseline across every corporate device, and deploys a controlled vendor access model; followed by an ongoing managed service that maintains device compliance, manages application deployments and patching, provides tiered incident support, and delivers monthly compliance reporting.

The outcome is a unified, auditable endpoint estate where every corporate laptop meets Revolv3's security requirements, new devices onboard with zero-touch provisioning, non-compliant devices are automatically blocked from Microsoft 365, and all third-party administrative access is logged, time-limited, and fully traceable.

The implementation is provided at no charge. The ongoing managed service is priced at $15 per device per month — a total investment of $600 per month for 40 devices.

---

## Understanding of Requirements

Revolv3 has provided a detailed internal requirements document defining the technical and operational standards for its endpoint estate. The requirements are clear, specific, and shaped by three interconnected drivers: operational consistency, PCI DSS compliance, and controlled third-party access.

### The Core Challenge

Revolv3 currently uses Microsoft 365 Business Standard and operates a mixed laptop estate without a unified management platform. The absence of enforced endpoint controls means devices may be non-compliant with PCI DSS requirements, third-party support access lacks the auditability a regulated environment demands, and new device onboarding relies on manual processes that introduce inconsistency.

### What Revolv3 Needs

**Unified management:** Approximately 40 corporate Windows and macOS laptops brought under Microsoft Intune, with zero-touch provisioning for new devices and a guided enrolment process for existing ones.

**PCI DSS-aligned security controls:** Full-disk encryption, CrowdStrike as the primary EDR, firewall enforcement (including macOS stealth mode), screen lock, password policy, and Conditional Access blocking non-compliant devices from Microsoft 365.

**Controlled privilege model:** Distinct privilege tiers for standard users, developers, and IT support — with Windows LAPS, macOS hidden admin accounts, and time-limited developer elevation through the SAP Privileges application (macOS) and Microsoft EPM (Windows).

**Auditable vendor access:** All external access through Revolv3-provisioned Windows 365 Cloud PCs, using named Entra ID accounts with PIM-managed Intune Administrator roles — no standing admin access, no Global Administrator access, no shared accounts.

**Ongoing managed service:** Continuous compliance monitoring, monthly reporting, structured patch and application update management, and tiered support across three SLA bands — with PST business hours Tier 3 coverage defined and named in the agreement.

### Requirements We Have Noted as Non-Negotiable

Revolv3's source document explicitly identifies the following as dealbreakers:

- Intune Administrator role only — no Global Administrator access
- PIM required with no standing active admin role
- No shared accounts under any circumstances
- Vendor access exclusively via Revolv3-provisioned Windows 365 Cloud PCs
- No interference with logging or audit infrastructure
- All documentation owned by and accessible to Revolv3 at all times
- Named list of all individuals with access provided before engagement commences
- PST business hours Tier 3 coverage named in the engagement agreement

Our proposal is designed to meet every one of these requirements.

---

## Proposed Solution

We propose deploying **Microsoft Intune** as the single endpoint management platform for Revolv3's entire laptop estate, supported by **Microsoft Entra ID**, **Windows Autopilot**, **Apple Automated Device Enrolment**, and a structured vendor operating model aligned to PCI DSS requirements.

### Phase 1 — Implementation

The implementation phase establishes the full endpoint management foundation in an estimated 6–8 weeks, subject to Business Premium licensing confirmation.

**Intune and security baseline:** Intune is configured with Windows and macOS enrolment profiles, security baseline policies, Conditional Access, and application deployment pipelines. Every device is brought into a compliant state with BitLocker or FileVault encryption, CrowdStrike Falcon as the sole active AV/EDR (with Microsoft Defender in passive mode), firewall enforcement, auto-lock, and password policy.

**Zero-touch provisioning:** New Windows devices are provisioned via **Windows Autopilot** — shipped directly to the user, enrolled automatically on first boot, and fully configured before the user begins work. New macOS devices are provisioned via **Apple Automated Device Enrolment** through Apple Business Manager, with the same outcome.

**Privilege management:** Standard users have no local admin rights. Developer devices receive the **SAP Privileges application** (macOS, 60-minute elevation with justification logging) and **Microsoft EPM** (Windows). Windows devices are managed by **Windows LAPS** with 30-day password rotation and login screen hiding. macOS devices receive a hidden local admin account (UID below 500) with password stored in Revolv3's designated password manager.

**Application deployment:** All required applications — Microsoft 365 Apps, CrowdStrike Falcon, Coro, Cato Client, Zoom, Slack, and Files.com — are packaged and deployed via Intune Win32 (Windows) and PKG (macOS). Coro will be included in the initial deployment scope; the vendor will be prepared to decommission the Coro agent across all managed devices if Revolv3 makes that decision during the engagement.

**Vendor access model:** The vendor accesses the Intune environment exclusively through Revolv3-provisioned **Windows 365 Cloud PCs** (2 vCPU / 8 GB RAM / 128 GB). Named Entra ID guest accounts with **PIM-managed Intune Administrator** roles (Eligible, not Active; maximum 4-hour activation; phishing-resistant MFA required; justification mandatory). A Conditional Access policy blocks vendor accounts from accessing the Intune admin centre from any device other than the provisioned Cloud PC.

**Documentation:** All configuration runbooks, operational procedures, and a full handover pack are produced and transferred to Revolv3's ownership before Phase 1 closes.

### Phase 2 — Ongoing Managed Service

The managed service maintains and operates the endpoint estate on a continuous basis from Phase 1 completion onwards.

**Compliance monitoring** is continuous via the Intune compliance dashboard. Non-compliant devices trigger automated alerts to the Revolv3 IT point of contact. A monthly compliance report covers fleet compliance rate, non-compliant devices and root cause, patch status, CrowdStrike coverage, and encryption status.

**Patch management** follows defined deferral schedules: Windows quality updates with a 3-day deferral then enforced; Windows feature updates with a 14-day deferral; macOS updates with up to 30 days user deferral then forced; macOS Rapid Security Responses applied immediately with no deferral.

**Application updates** are managed on a monthly cycle. Vendor release notes are monitored and updated packages are redeployed via Intune. Microsoft 365 Apps update automatically via the Monthly Enterprise Channel.

**Tiered support** is delivered via Revolv3's Jira project, shared mailbox, and Teams escalation channel across three SLA tiers: Tier 1 routine (4-hour acknowledgment, next business day resolution), Tier 2 urgent (2-hour acknowledgment, 4-hour response), and Tier 3 critical (1-hour acknowledgment, 2-hour response). PST business hours Tier 3 coverage will be named and documented in the engagement agreement.

**Change management** follows Revolv3's written approval process. All changes are logged as Jira tickets. Emergency changes are executed when necessary and reviewed within 24 hours after the fact.

---

## Scope of Work

This engagement covers two phases across approximately 40 corporate Windows and macOS laptops within Revolv3's Microsoft 365 tenant. All technical work is performed through Revolv3-provisioned Windows 365 Cloud PCs using named, PIM-managed vendor accounts with Intune Administrator role only. No Global Administrator access is used at any point.

**Phase 1 — Implementation** establishes the complete endpoint management platform in an estimated 6–8 weeks. Work includes: Intune tenant configuration and enrolment policies; Windows Autopilot for zero-touch provisioning of new Windows devices; Apple Automated Device Enrolment via Apple Business Manager for new macOS devices; PCI DSS-aligned security baselines covering BitLocker and FileVault full-disk encryption with recovery keys escrowed to Entra ID, CrowdStrike Falcon as primary AV/EDR with Microsoft Defender in passive mode, Windows Defender Firewall enforcement and macOS Application Firewall with stealth mode enabled, 5-minute auto-lock on all platforms, and password policy enforcing 12-character minimum length, 180-day maximum age, and 10-attempt account lockout with a 15-minute lockout duration; Conditional Access policies that block non-compliant devices from Microsoft 365 and restrict vendor named accounts to the Intune admin centre only when accessed via the Revolv3-provisioned Cloud PC; application packaging and deployment via Intune (Win32 on Windows, PKG on macOS) for Microsoft 365 Apps, CrowdStrike Falcon, Coro security agent, Cato Client, Zoom, Slack, and Files.com; privilege management via Windows LAPS with 30-day password rotation and login screen hiding, macOS hidden local admin account with UID below 500 and password manager storage, and developer elevation tools — SAP Privileges application on macOS (60-minute elevation window with mandatory justification) and Microsoft EPM on Windows; guided enrolment of existing laptops currently in active use; compliance dashboard configuration providing real-time visibility of compliance status, OS version, encryption, CrowdStrike status, last check-in, and assigned user for every device; remote management capability validation including remote lock, wipe, force sync, and recovery key retrieval; and a full configuration runbook, device enrolment guide, and operational procedures handbook transferred to Revolv3 ownership at handover.

**Phase 2 — Managed Service** provides continuous operation of the endpoint estate from Phase 1 completion onwards. Work includes: real-time compliance monitoring with automated non-compliance alerts to the Revolv3 IT point of contact; monthly compliance reports covering fleet compliance rate, non-compliant devices and root cause, patch status, CrowdStrike coverage, and encryption state; patch management per defined deferral schedules (Windows quality updates: 3-day deferral then enforced, forced restart at 02:00 UTC; Windows feature updates: 14-day deferral; macOS standard updates: up to 30-day user deferral then forced; macOS Rapid Security Responses: immediate with no deferral); monthly application version review with vendor release note monitoring and Intune redeployment of updated packages; three-tier support via Revolv3's Jira project, shared mailbox, and Teams escalation channel (Tier 1 routine: 4-hour acknowledgment, next business day resolution; Tier 2 urgent: 2-hour acknowledgment, 4-hour response; Tier 3 critical: 1-hour acknowledgment, 2-hour response; PST business hours Tier 3 coverage arrangement named in the engagement agreement); written change management with Jira-logged approvals and 24-hour post-execution review for emergency changes; Coro decommissioning support across all managed devices if Revolv3 decides to retire the platform; and 24-hour security incident notification to Revolv3 for any incident affecting systems, devices, or credentials used in this engagement.

**Change control:** Any extension, reduction, or modification to this scope requires a formal Change Request with written approval from the Revolv3 IT point of contact or Project Sponsor before execution. Emergency changes are permissible and must be reviewed and documented within 24 hours after the fact.

**Client responsibilities:** Revolv3 is responsible for confirming Microsoft 365 Business Premium licensing before Phase 1 begins; provisioning Windows 365 Cloud PCs, named Entra ID guest accounts, PIM configuration, Jira project, shared mailbox, and Teams escalation channel; providing the final developer application list and AI tool assignments before Phase 2 begins; conducting monthly activity log reviews and quarterly access reviews; and off-boarding vendor access within 24 hours when any individual leaves the engagement.

**Out of scope:** Mobile phones, tablets, and non-laptop devices; Microsoft 365 licensing procurement; Windows 365 Cloud PC provisioning and Entra ID account management; PIM configuration, log retention infrastructure, and Jira/Teams/mailbox administration; end-user training programmes; penetration testing and formal security assessments; hardware procurement and physical device preparation; network infrastructure changes.

---

## Deliverables

| # | Deliverable | Format | When Delivered |
|---|-------------|--------|---------------|
| 1 | Intune tenant configuration | Deployed configuration in Revolv3 tenant | End of M2 (Week 3) |
| 2 | Security baseline policies | Deployed Intune profiles and Conditional Access policies | End of M2 (Week 3) |
| 3 | Privilege management configuration | Deployed LAPS, macOS admin account, developer elevation tools | End of M3 (Week 4) |
| 4 | Application deployment packages | Tested and deployed via Intune across all enrolled devices | End of M6 (Week 7) |
| 5 | Enrolled device estate | All ~40 corporate laptops enrolled and compliant in Intune | End of M6 (Week 7) |
| 6 | Compliance dashboard | Configured and validated in Revolv3 Intune tenant | End of M6 (Week 7) |
| 7 | Configuration runbook | Markdown document, Revolv3-owned | End of M7 (Week 8) |
| 8 | Device enrolment guide | Markdown document, Revolv3-owned | End of M7 (Week 8) |
| 9 | Operational procedures handbook | Markdown document covering change, incident, update, and offboarding procedures | End of M7 (Week 8) |
| 10 | Monthly compliance report | Monthly summary report | Month 1 of managed service, then monthly |
| 11 | Patch management | Applied per defined Windows and macOS deferral schedules | Ongoing (Phase 2) |
| 12 | Application updates | Redeployed via Intune on monthly cycle | Ongoing (Phase 2) |
| 13 | Tiered support | Via Jira, shared mailbox, Teams per SLA | Ongoing (Phase 2) |

---

## Assumptions & Dependencies

The following assumptions have been made in preparing this proposal. If any assumption proves incorrect, the scope, timeline, or cost may be affected and will be managed through the formal change control process.

1. It is assumed that Revolv3 will confirm Microsoft 365 Business Premium licensing is active before Phase 1 begins. Intune configuration cannot commence until this is confirmed.

2. It is assumed that Revolv3 will provision named Entra ID guest accounts, configure PIM, and provision Windows 365 Cloud PCs for vendor access before technical work commences.

3. It is assumed that Revolv3 will provide the final application list for developers and AI tool assignments before application deployment begins.

4. It is assumed that Revolv3 will confirm Coro silent macOS installation support before Coro is included in the deployment.

5. It is assumed that Revolv3 will appoint a named Project Sponsor and Technical Lead with authority to approve changes throughout the engagement.

6. It is assumed that Revolv3 stakeholders will be available for reviews, approvals, and guided enrolment sessions within the agreed project schedule. Unavailability may affect the delivery timeline.

7. It is assumed that Revolv3 will provision and own the Jira project, shared mailbox, and Teams escalation channel before the managed service commences. The vendor operates within these channels — it does not administer them.

8. It is assumed that all corporate laptops in scope are accessible for guided enrolment. Devices not accessible during the enrolment window will require a separate enrolment exercise.

9. It is assumed that the third-party vendor of the Coro security agent will confirm silent macOS installation capability. If Coro does not support silent macOS installation, Coro deployment will be deferred pending a Revolv3 decision on the approach.

10. It is assumed that the PST business hours Tier 3 coverage arrangement will be agreed and named in the engagement agreement before signing. The vendor will document the named individual or on-call arrangement that covers critical incidents during the PST business hours window.

11. It is assumed that Revolv3 will provide written approval for all changes before execution, and will conduct monthly activity log reviews and quarterly access reviews as required by their internal PCI DSS obligations.

---

## Exclusions

The following items are explicitly excluded from this proposal unless otherwise stated:

1. Any work, system, or service not explicitly described in the Scope of Work above.

2. Mobile phones, tablets, desktops, servers, or any device other than the approximately 40 corporate laptops described.

3. Microsoft 365 Business Premium licensing procurement — this is Revolv3's responsibility and a hard prerequisite.

4. Windows 365 Cloud PC provisioning and management — provisioned and owned by Revolv3.

5. PIM configuration and Entra ID named account creation — provisioned and owned by Revolv3.

6. Log retention infrastructure configuration — Revolv3's responsibility.

7. Jira project administration, shared mailbox provisioning, and Teams escalation channel provisioning — Revolv3's responsibility.

8. End-user training programmes, change management communications, or user adoption activities.

9. Penetration testing, formal security assessments, or compliance auditing.

10. Hardware procurement, imaging, physical device preparation, or courier logistics.

11. Network infrastructure changes, physical cabling, or facilities work.

12. Remediation of pre-existing faults, technical debt, or security vulnerabilities not related to the Intune enrolment and configuration scope.

13. Custom software development or scripting beyond what is explicitly described in the scope (routine Intune shell scripts for macOS admin account password rotation are included).

14. Legal, regulatory, or compliance advice. Where PCI DSS requirements affect technical decisions, we will flag these to Revolv3 for guidance from qualified compliance professionals.

---

## Indicative Pricing

| Phase | Component | Unit | Qty | Rate | Total |
|-------|-----------|------|-----|------|-------|
| Phase 1 | Endpoint Management Implementation | Project | 1 | Complimentary | $0.00 |
| Phase 2 | Ongoing Managed Service | Per device / month | 40 | $15.00 | $600.00 / month |

**Phase 1 implementation: $0.00 — complimentary**

**Phase 2 monthly investment: $600.00 per month**

The managed service fee is calculated per managed device. If the device count changes, the monthly fee adjusts accordingly from the first day of the following billing month.

**Payment terms:** Phase 2 is invoiced monthly in advance from the managed service commencement date. Payment is due within 30 days of invoice date.

**VAT:** All prices are exclusive of VAT and any applicable local taxes, charged at the prevailing rate.

Contract term and renewal conditions to be confirmed. A minimum initial term is recommended to protect continuity of service and configuration knowledge.

---

## Timeline

### Phase 1 — Implementation (6–8 Weeks from Confirmed Start)

| Week | Milestone | Key Gate |
|------|-----------|----------|
| 1–2 | Prerequisites & Planning — kickoff, Business Premium confirmation, Autopilot/ABM prerequisites, vendor access readiness | Business Premium must be confirmed before proceeding |
| 3 | Baseline Configuration — Intune tenant, security baselines, Conditional Access | |
| 4 | Privilege Management — LAPS, macOS admin, developer elevation tools | |
| 5 | Application Packaging & Testing — all required apps packaged and test-deployed | Final app list must be confirmed by Revolv3 |
| 6 | Device Enrolment — guided enrolment of existing devices; new device zero-touch validation | |
| 7 | Application Deployment & Validation — full deployment; dashboard and remote management testing | |
| 8 | Documentation & Handover — runbooks, operational procedures, handover pack transferred to Revolv3 | |

### Phase 2 — Managed Service (From Month 2 Onwards)

The managed service commences on the agreed date following Phase 1 completion. There is no defined end date; the service continues under the agreed contract term.

Monthly activities: compliance monitoring, patch management, application updates, compliance report, support, and change management.

**Hard prerequisites before Phase 1 can begin:**
- Microsoft 365 Business Premium licensing active and confirmed by Revolv3
- Windows 365 Cloud PCs provisioned for vendor access
- Named Entra ID guest accounts and PIM configured for vendor personnel

---

## About Us

**Cloudbd** is a specialist technology consultancy and managed services provider, delivering cloud transformation, Microsoft 365 solutions, and IT managed services to enterprise and mid-market organisations across the UK and internationally.

Founded in [year], we have built a reputation for delivering complex technology projects on time and within budget. Our team of [X] certified consultants and engineers brings deep expertise across Microsoft Azure, Microsoft 365, endpoint management, network infrastructure, and cybersecurity.

### Our Capabilities

| Practice Area | Key Technologies |
|---------------|-----------------|
| Cloud & Infrastructure | Microsoft Azure, Hybrid Cloud, IaaS, PaaS |
| Modern Workplace | Microsoft 365, Teams, SharePoint, Intune |
| Cybersecurity | Microsoft Sentinel, Defender, Zero Trust, MFA |
| Managed Services | 24x7 monitoring, helpdesk, proactive support |
| Consultancy | Strategy, architecture, programme delivery |

### Why Our Clients Choose Us

**Technical expertise, commercially applied.** We don't recommend technology for its own sake. Every solution we propose is grounded in the business outcome it must deliver.

**Proven delivery.** We have successfully delivered [N]+ technology projects for organisations ranging from 50 to 10,000 users. Our client retention rate of [X]% reflects the quality and consistency of our service.

**Microsoft Partner credentials.** As a Microsoft [Gold/Solutions] Partner, we maintain the highest level of accreditation and have direct access to Microsoft engineering and support resources.

**A team that stays.** Your project will be delivered by the same team that sold it. We do not pass work to junior resources after contract signature.

### Our Certifications

- Microsoft Azure Solutions Architect Expert
- Microsoft 365 Enterprise Administrator Expert
- Microsoft Cybersecurity Architect Expert
- ITIL v4 Foundation
- PRINCE2 Practitioner

### Contact

**Cloudbd**
[Address Line 1], [City], [Postcode]
T: [Phone]
E: [Email]
W: [Website]

---

## Next Steps

We are ready to begin work as soon as Revolv3's prerequisites are in place. We propose the following next steps:

### 1. Proposal Review

We welcome the opportunity to present this proposal and answer any questions. Please contact us to arrange a 60-minute review call at a time that suits you.

**Contact:** [Name], [Title]
**Email:** [email]
**Phone:** [phone]

### 2. Clarifications and Amendments

If any aspect of this proposal requires adjustment, please raise it with your named contact above. We are happy to revise scope, phasing, or terms to meet your requirements.

### 3. Engagement Agreement

To formally proceed, please sign the accompanying Statement of Work or confirm acceptance in writing by email. Before signing, the following must be documented in the agreement:

- Named list of all vendor individuals who will have access to Revolv3's environment
- Vendor legal entity name, country of registration, and registration number (or sole trader declaration)
- Professional liability or insurance status
- PST business hours Tier 3 critical incident coverage arrangement (named individual or on-call arrangement)
- Revolv3's Third-Party Service Provider (TPSP) acknowledgment signed by the vendor

### 4. Prerequisites Confirmation

Revolv3 confirms before project commencement:

- Microsoft 365 Business Premium licensing is active
- Windows 365 Cloud PCs provisioned for vendor access
- Named Entra ID guest accounts created and PIM configured

### 5. Kickoff

Once the agreement is signed and prerequisites are confirmed, we will schedule a project kickoff within five business days. At kickoff we will introduce the project team, confirm roles and responsibilities, agree the detailed project plan, and establish communication channels.

---

## Legal Notes

### Validity

This proposal is valid for 30 days from the date of issue. After this period, pricing, availability, and scope are subject to review and may change without notice.

### Confidentiality

This document contains commercially sensitive information and is provided in confidence to Revolv3 only. It must not be reproduced, distributed, or disclosed to any third party without the prior written consent of Cloudbd. This obligation of confidentiality applies regardless of whether a contract is subsequently agreed.

### Intellectual Property

All intellectual property created specifically for Revolv3 during this engagement will vest in Revolv3 upon receipt of full payment. Pre-existing intellectual property, methodologies, tools, templates, and frameworks belonging to Cloudbd remain our property and are licensed to Revolv3 for use within the scope of this engagement only.

All documentation, scripts, configuration knowledge, and runbooks produced during this engagement are owned by Revolv3 and must remain accessible to Revolv3 at all times, including upon termination of the engagement.

### Liability

Cloudbd's total aggregate liability to Revolv3 under or in connection with this engagement, whether arising in contract, tort (including negligence), breach of statutory duty, or otherwise, shall not exceed the total fees paid by Revolv3 in the 12 months preceding the event giving rise to the claim.

In no event shall Cloudbd be liable for any indirect, special, incidental, or consequential loss or damage, including loss of profit, loss of revenue, loss of data, or loss of business opportunity, even if advised of the possibility of such loss.

### Payment Terms

Phase 2 managed service invoices are due within 30 days of the invoice date. Late payment may attract interest in accordance with the Late Payment of Commercial Debts (Interest) Act 1998. Cloudbd reserves the right to suspend services in the event of non-payment.

All prices in this proposal are exclusive of VAT (or applicable local sales tax), which will be charged at the prevailing rate.

### PCI DSS Operating Commitment

The vendor acknowledges that Revolv3 operates in a PCI DSS-regulated environment and accepts responsibility for operating within the access controls Revolv3 has defined. This acknowledgment is formalised through Revolv3's Third-Party Service Provider (TPSP) acknowledgment document, which must be signed before the engagement commences.

### Security Incident Notification

The vendor will notify Revolv3 within 24 hours of any security incident affecting systems, devices, or credentials used to access Revolv3's environment, including device theft or loss, credential compromise, or any unauthorised access event.

### Governing Law

This proposal and any resulting contract shall be governed by and construed in accordance with the laws of England and Wales. Any dispute shall be subject to the exclusive jurisdiction of the courts of England and Wales.

### Acceptance

This proposal does not constitute a contract. A binding agreement will only come into effect upon execution of a formal Statement of Work, Master Services Agreement, or equivalent contract document signed by authorised representatives of both parties.

---

*Cloudbd is a company registered in England and Wales. Company Registration Number: [XXXXXXXX]. Registered office: [Address].*
