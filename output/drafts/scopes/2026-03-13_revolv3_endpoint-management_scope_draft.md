# Scope of Work
## Revolv3 — Endpoint Management & Managed Service

---

## Overview

This document defines the scope of work for a two-phase engagement covering the implementation and ongoing managed service of Revolv3's corporate endpoint estate. All work is performed within Revolv3's Microsoft 365 tenant and Intune environment, under Revolv3's access governance and change management framework.

---

## Phase 1 — Implementation

### In Scope

| # | Work Item | Detail |
|---|-----------|--------|
| 1 | Prerequisites validation | Confirm Microsoft 365 Business Premium licensing is active; validate Intune and Entra ID tenant readiness before any configuration begins |
| 2 | Intune tenant configuration | Configure Intune settings, enrolment restrictions, and baseline policies for Windows and macOS |
| 3 | Windows Autopilot | Configure Autopilot for zero-touch provisioning of new Windows devices; register device hashes |
| 4 | Apple Automated Device Enrolment | Configure Apple Business Manager integration with Intune; set up ADE enrolment profiles for macOS |
| 5 | Security baseline — encryption | Deploy BitLocker (Windows) and FileVault (macOS) via Intune; escrow recovery keys to Entra ID |
| 6 | Security baseline — endpoint protection | Configure Microsoft Defender in passive mode; CrowdStrike Falcon integration and deployment confirmed as primary AV/EDR |
| 7 | Security baseline — firewall | Deploy Windows Defender Firewall policy; deploy macOS Application Firewall with stealth mode enabled |
| 8 | Security baseline — screen lock and password | Deploy 5-minute auto-lock; enforce 12-character minimum password, 180-day maximum age, 10-attempt lockout (15-minute lockout duration) |
| 9 | Conditional Access | Configure Conditional Access policies to block non-compliant devices from Microsoft 365; configure vendor-restricted policy to enforce Cloud PC-only access to the Intune admin centre |
| 10 | Application deployment | Package and deploy via Intune Win32 (Windows) and PKG (macOS): Microsoft 365 Apps, CrowdStrike Falcon, Coro security agent, Cato Client, Zoom, Slack, Files.com |
| 11 | Coro deployment (macOS) | Confirm silent macOS installation support for Coro before deployment; include in standard deployment scope |
| 12 | Privilege management — standard users | Configure standard user profiles with no local admin rights |
| 13 | Privilege management — developers (Windows) | Deploy Microsoft Endpoint Privilege Management (EPM) or equivalent; scope any permanent local admin rights to named developer devices via a dedicated device group — not granted broadly |
| 14 | Privilege management — developers (macOS) | Deploy SAP Privileges application to developer devices; configure 60-minute temporary elevation window with mandatory justification logging |
| 15 | Windows LAPS | Deploy Windows LAPS to manage local admin accounts on all Windows devices; configure 30-day password rotation; configure account to be hidden from the standard login screen |
| 16 | macOS local admin account | Create a hidden local administrator account with UID below 500; store password in Revolv3's designated password manager; configure rotation via Intune shell script |
| 17 | Existing device enrolment | Provide guided enrolment process for existing laptops already in active use; remediate enrolment issues where required |
| 18 | Compliance dashboard configuration | Configure Intune compliance dashboard to provide real-time visibility of: compliance status, OS version, encryption status, CrowdStrike status, last check-in time, and assigned user |
| 19 | Remote management capabilities | Validate and document remote lock, remote wipe, force sync, recovery key retrieval, LAPS password retrieval, and compliance state viewing |
| 20 | Documentation and handover | Produce configuration runbooks, operational procedures, and a handover pack; all documentation transferred to Revolv3 ownership |

### Phase 1 — Out of Scope

- Microsoft 365 Business Premium licensing procurement (Revolv3 responsibility)
- Windows 365 Cloud PC provisioning and licensing (Revolv3 responsibility)
- PIM configuration, named Entra ID account creation, and log retention infrastructure (Revolv3 responsibility)
- Conditional Access policy administration beyond the policies listed above (Revolv3 responsibility)
- Mobile phones, tablets, or any non-laptop devices
- Network infrastructure changes, physical cabling, or facilities work
- End-user training programmes or change management communications
- Penetration testing or formal security assessments
- Hardware procurement, imaging, or physical device preparation
- Remediation of pre-existing faults or technical debt not related to Intune enrolment

### Phase 1 — Client Responsibilities

| Responsibility | Owner | Timing |
|---------------|-------|--------|
| Confirm Microsoft 365 Business Premium licensing is active | Revolv3 IT | Before Phase 1 begins |
| Confirm final application list for developers and AI tool assignments | Revolv3 IT | Before application deployment |
| Provision Windows 365 Cloud PCs for vendor access | Revolv3 IT | Before vendor access is required |
| Provide named Entra ID guest accounts for vendor personnel | Revolv3 IT | Before vendor access is required |
| Configure PIM for vendor accounts | Revolv3 IT | Before vendor access is required |
| Nominate a named Project Sponsor and Technical Lead | Revolv3 | At engagement start |
| Approve all changes in writing before execution | Revolv3 IT | Throughout Phase 1 |
| Confirm Coro silent macOS installation support | Revolv3 IT | Before Coro deployment |

---

## Phase 2 — Ongoing Managed Service

### In Scope

| # | Service Item | Detail |
|---|-------------|--------|
| 1 | Compliance monitoring | Continuous monitoring of all 40 managed devices via Intune compliance dashboard; automated non-compliance alerts to Revolv3 IT point of contact |
| 2 | Monthly compliance report | Monthly report summarising fleet compliance status, non-compliant devices and root cause, patch status, CrowdStrike coverage, and encryption status |
| 3 | Patch management — Windows | Quality updates: 3-day deferral then enforced; Feature updates: 14-day deferral then enforced; forced restart at 02:00 UTC after 3-day post-deferral grace period |
| 4 | Patch management — macOS | Standard OS updates: up to 30-day user deferral then forced; Rapid Security Responses: no deferral, installed immediately |
| 5 | Application update management | Monthly review of application versions; vendor release note monitoring; Intune redeployment of updated packages on monthly cycle; Microsoft 365 Apps auto-updated via Monthly Enterprise Channel |
| 6 | Tiered support — Tier 1 (Routine) | Non-urgent requests, changes, and questions; acknowledgment within 4 vendor business hours; resolution within 1 vendor business day; via Jira |
| 7 | Tiered support — Tier 2 (Urgent) | Productivity-impacting issues; acknowledgment within 2 hours; active response within 4 hours; via Jira and Teams escalation channel |
| 8 | Tiered support — Tier 3 (Critical) | Security incidents, users locked out, data risk; acknowledgment within 1 hour; active response within 2 hours; via Teams escalation channel; PST-hours Tier 3 coverage to be named in the agreement |
| 9 | Change management | All changes requested and approved via Revolv3's written approval process; changes logged as Jira tickets; emergency changes documented and reviewed within 24 hours |
| 10 | Coro decommissioning support | If Revolv3 decides to retire Coro during the engagement, the vendor will remove and clean up the Coro agent across all managed devices via Intune; Revolv3 to provide reasonable notice |
| 11 | Security incident notification | Vendor notifies Revolv3 within 24 hours of any security incident affecting systems, devices, or credentials used to access Revolv3's environment |

### Phase 2 — Out of Scope

- Jira project administration (Revolv3 provisions and owns the Jira project)
- Shared mailbox and Teams escalation channel administration (Revolv3 provisions and owns)
- Quarterly access review (Revolv3 IT conducts; vendor provides information on request)
- Monthly activity log review (Revolv3 IT conducts)
- PIM administration and Entra ID account management (Revolv3 responsibility)
- Windows 365 Cloud PC management (Revolv3 responsibility)
- Any work outside the agreed device scope of 40 corporate laptops without a Change Request

### Phase 2 — Client Responsibilities

| Responsibility | Owner | Timing |
|---------------|-------|--------|
| Provision and maintain Jira project for all support requests | Revolv3 IT | Before managed service commences |
| Provision shared mailbox (e.g. it-endpointmgmt@revolv3.com) | Revolv3 IT | Before managed service commences |
| Provision Teams escalation channel with vendor as named guests | Revolv3 IT | Before managed service commences |
| Review and approve all change requests in writing | Revolv3 IT | Throughout Phase 2 |
| Conduct monthly review of vendor activity logs | Revolv3 IT | Monthly |
| Conduct quarterly access review of vendor accounts | Revolv3 IT | Quarterly |
| Off-board vendor access within 24 hours when an individual leaves the engagement | Revolv3 IT | On departure |
| Notify vendor with reasonable notice of Coro decommissioning decision | Revolv3 IT | If/when decided |

---

## Change Control

Any request to extend, reduce, or modify the scope of work defined in this document must be submitted as a formal Change Request. A Change Request must include:

- Description of the proposed change
- Reason for the change
- Impact on timeline, resources, and cost
- Written approval from the Revolv3 IT point of contact or named Project Sponsor

No change will be executed without written approval from Revolv3. Emergency changes that cannot wait for prior approval must be documented immediately and reviewed within 24 hours after the fact.

---

## Supported Devices and Platforms

| Platform | Version | Notes |
|----------|---------|-------|
| Windows (laptop) | Windows 10 / 11 | Managed via Intune; Autopilot for new devices |
| macOS (laptop) | Current and N-1 | Managed via Intune ADE; ABM for new devices |

Devices outside these platforms and form factors (mobile phones, tablets, desktops, servers) are not in scope.
