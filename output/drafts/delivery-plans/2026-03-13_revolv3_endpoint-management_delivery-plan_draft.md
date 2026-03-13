# Delivery Plan
## Revolv3 — Endpoint Management & Managed Service

---

## Engagement Structure

The engagement is structured in two phases:

- **Phase 1 — Implementation:** A time-bounded project to deploy and configure the full endpoint management platform. Complimentary.
- **Phase 2 — Ongoing Managed Service:** A continuous managed service commencing on completion of Phase 1.

Phase 1 cannot begin until Revolv3 confirms that Microsoft 365 Business Premium licensing is active. Application deployment (later in Phase 1) cannot begin until Revolv3 confirms the final application list for developers and AI tool assignments.

---

## Phase 1 — Implementation Plan

Estimated duration: **6–8 weeks** from confirmed start date.

### Milestone Overview

| Milestone | Duration | Key Activities |
|-----------|----------|----------------|
| M1 — Prerequisites & Planning | Week 1–2 | Prerequisites validation; confirm Business Premium active; Autopilot hardware hash collection; ABM prerequisites; vendor access model confirmed; project kickoff |
| M2 — Baseline Configuration | Week 3 | Intune tenant configuration; security baseline policies (encryption, firewall, screen lock, password); Conditional Access policies including vendor Cloud PC enforcement |
| M3 — Privilege Management | Week 4 | Windows LAPS deployment; macOS hidden admin account setup; developer elevation tools (SAP Privileges / EPM); standard user profile configuration |
| M4 — Application Packaging & Testing | Week 5 | Package and test-deploy all required applications in staging: Microsoft 365 Apps, CrowdStrike (Defender passive mode), Coro, Cato Client, Zoom, Slack, Files.com |
| M5 — Device Enrolment | Week 6 | Guided enrolment of existing devices; zero-touch enrolment validation for new devices; remediation of enrolment issues |
| M6 — Application Deployment & Validation | Week 7 | Full application deployment across enrolled devices; compliance dashboard validation; remote management capability testing |
| M7 — Documentation & Handover | Week 8 | Configuration runbooks and operational procedures; handover pack transferred to Revolv3; managed service commencement planning |

### Phase 1 Milestone Detail

#### M1 — Prerequisites & Planning (Weeks 1–2)

- Confirm Microsoft 365 Business Premium licensing is active — **no Intune configuration begins until this is confirmed**
- Conduct project kickoff: introduce team, confirm roles, agree communication channels
- Collect Windows Autopilot hardware hashes for existing and new Windows devices
- Confirm Apple Business Manager integration prerequisites with Revolv3
- Confirm vendor access model: Windows 365 Cloud PC provisioned, named Entra ID accounts created, PIM configured by Revolv3
- Finalise application list for developer and standard user groups (Revolv3 to provide)
- Confirm Coro silent macOS installation support before Coro deployment proceeds

**Gate:** Phase 1 proceeds only when Business Premium licensing is confirmed by Revolv3.

#### M2 — Baseline Configuration (Week 3)

- Configure Intune tenant settings and enrolment restrictions
- Deploy security baseline policies:
  - BitLocker (Windows) — recovery keys escrowed to Entra ID
  - FileVault (macOS) — recovery keys escrowed to Entra ID
  - Windows Defender Firewall — enabled and locked
  - macOS Application Firewall — enabled with stealth mode on
  - Screen auto-lock — 5 minutes on all platforms
  - Password policy — 12-character minimum, 180-day maximum age, 10-attempt lockout (15-minute duration)
  - Microsoft Defender set to passive mode (CrowdStrike as primary AV/EDR)
- Configure Conditional Access:
  - Block non-compliant devices from Microsoft 365
  - Restrict vendor named accounts to Cloud PC-only access for Intune admin centre

#### M3 — Privilege Management (Week 4)

- Deploy Windows LAPS: local admin account with 30-day password rotation; hidden from login screen
- Configure macOS hidden local admin account (UID below 500); password stored in Revolv3 password manager; rotation via Intune shell script
- Deploy SAP Privileges application to developer macOS devices (60-minute elevation window, mandatory justification)
- Configure Microsoft Endpoint Privilege Management (EPM) or equivalent for Windows developer devices
- If permanent local admin for specific developers confirmed by Revolv3: scope to named devices via dedicated device group — not granted broadly

#### M4 — Application Packaging & Testing (Week 5)

- Package and test-deploy in a controlled staging group:
  - Microsoft 365 Apps (Monthly Enterprise Channel)
  - CrowdStrike Falcon sensor
  - Coro security agent (macOS silent install confirmed before deployment)
  - Cato Client
  - Zoom
  - Slack
  - Files.com
- Validate application deployment, update mechanisms, and self-update behaviour

**Gate:** Final application list must be confirmed by Revolv3 before production application deployment begins.

#### M5 — Device Enrolment (Week 6)

- Guided enrolment of existing Windows and macOS laptops in active use
- Staggered enrolment to minimise user disruption
- Zero-touch enrolment validation for new Windows (Autopilot) and macOS (ADE) devices
- Remediation of enrolment issues as identified

#### M6 — Application Deployment & Validation (Week 7)

- Full application deployment across all enrolled devices
- Compliance dashboard validation: confirm real-time visibility of compliance status, OS version, encryption, CrowdStrike status, last check-in, assigned user
- Remote management capability testing: remote lock, wipe, force sync, recovery key retrieval, LAPS password retrieval
- Non-compliance alert testing: confirm automated notifications reach Revolv3 IT point of contact
- Sign-off testing with Revolv3 Technical Lead

#### M7 — Documentation & Handover (Week 8)

- Produce and transfer to Revolv3:
  - Intune configuration runbook
  - Conditional Access policy register
  - Application deployment and update procedures
  - Privilege management operational procedures
  - Device enrolment guide (for future new-hire onboarding)
  - Incident and change management procedures aligned to Revolv3's Jira/Teams model
- Managed service commencement date confirmed with Revolv3

---

## Phase 2 — Managed Service Plan

Phase 2 commences on completion of Phase 1 and the agreed managed service start date. There is no defined end date; the service continues under the agreed contract term.

### Monthly Service Cadence

| Activity | Frequency | Detail |
|----------|-----------|--------|
| Compliance monitoring | Continuous | Real-time via Intune; automated alerts to Revolv3 IT for non-compliance events |
| Patch management — Windows | Per policy | Quality updates: 3-day deferral → enforced; Feature updates: 14-day deferral → enforced; forced restart at 02:00 UTC post-grace |
| Patch management — macOS | Per policy | Standard updates: up to 30-day deferral → forced; Rapid Security Responses: immediate, no deferral |
| Application version review and update | Monthly | Monitor vendor release notes; redeploy updated packages via Intune on monthly cycle |
| Monthly compliance report | Monthly | Fleet security posture summary: compliance rate, non-compliant devices, patch status, CrowdStrike coverage, encryption status |
| Support — Tier 1 (Routine) | As raised | Acknowledgment: 4 vendor business hours; resolution: 1 vendor business day |
| Support — Tier 2 (Urgent) | As raised | Acknowledgment: 2 hours; active response: 4 hours |
| Support — Tier 3 (Critical) | As raised | Acknowledgment: 1 hour; active response: 2 hours; PST coverage arrangement named in agreement |
| Change management | As required | Written approval before execution; Jira-logged; emergency changes reviewed within 24 hours |

### Quarterly and Annual Activities

| Activity | Frequency | Detail |
|----------|-----------|--------|
| Quarterly access review support | Quarterly | Vendor provides current named individual list; Revolv3 IT conducts review |
| Vendor security self-assessment | Annually | Complete Revolv3's short self-assessment questionnaire covering device encryption, MFA, password management, and endpoint protection |

---

## Dependencies and Constraints

| Dependency | Owner | Impact if Not Met |
|-----------|-------|------------------|
| Microsoft 365 Business Premium licensing active | Revolv3 | Phase 1 cannot start |
| Final application list confirmed | Revolv3 | Application deployment (M4) cannot proceed |
| Windows 365 Cloud PCs provisioned for vendor access | Revolv3 | Vendor cannot access Intune environment |
| Named Entra ID accounts and PIM configured for vendor | Revolv3 | Vendor cannot access Intune environment |
| Coro silent macOS installation confirmed | Revolv3 | Coro deployment deferred until confirmed |
| PST Tier 3 coverage arrangement named | Vendor | Must be documented in engagement agreement before signing |

---

## Assumptions

- The delivery plan assumes standard access is granted to the Revolv3 Intune environment via the provisioned Windows 365 Cloud PC before Week 1 activities complete
- Delivery timelines assume Revolv3 stakeholders are available for review and approvals within the agreed project cadence
- Device enrolment timelines assume devices are accessible and users are available for the guided enrolment process during the enrolment window
- The timeline will be adjusted if Business Premium licensing confirmation or application list confirmation is delayed; delays in these gates will shift subsequent milestones proportionally
