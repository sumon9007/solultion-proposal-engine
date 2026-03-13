# Revolv3 Endpoint Management Requirements

## Document Summary

This file is the normalized intake document for the Revolv3 endpoint management opportunity. It consolidates the customer requirement PDF into a proposal-ready internal brief.

| Field | Value |
|------|-------|
| Client | Revolv3 |
| Opportunity | Endpoint Management & Security Requirements |
| Solution Type | Endpoint management implementation with ongoing managed support and security governance |
| Industry | Financial technology / payment gateway |
| Source Status | Normalized from customer-provided PDF — updated 2026-03-13 with full detail pass; engagement type confirmed by client 2026-03-13 |
| Primary Contact | Revolv3 IT point of contact (name not yet provided) |

---

## Executive Overview

Revolv3 requires a vendor proposal for the deployment and ongoing management of a mixed Windows and macOS corporate laptop estate. The engagement must establish Microsoft Intune as the management platform, enforce a PCI DSS-aligned endpoint security baseline, and define a controlled third-party operating model for any MSP or consultant accessing the environment.

This is not a generic device rollout. The requirement is shaped by compliance obligations, strict access governance, and the need to operate safely within a payment-processing environment. All requirements in the source document are described as non-negotiable unless explicitly agreed in writing by Revolv3 senior management.

---

## Business Context

### Current Challenge

Revolv3 needs to bring its corporate endpoint estate under consistent control across approximately 40 laptops while maintaining security, minimising user disruption, and meeting PCI DSS compliance obligations.

### Business Drivers

- Standardise endpoint management across Windows and macOS
- Enforce security controls through Microsoft Intune and Entra ID
- Support zero-touch provisioning for new devices
- Reduce unmanaged-device and privilege-related risk
- Meet PCI DSS obligations for endpoint security and third-party access

### Risks of Inaction

- Continued inconsistency across managed and unmanaged devices
- Weak compliance posture in a PCI DSS-regulated environment
- Inability to enforce Conditional Access based on device compliance
- Insufficient auditability for third-party administrative access
- Higher operational risk from excessive privileges and uncontrolled support access

### Desired Outcomes

- Approximately 40 corporate laptops managed under a single operating model
- Zero-touch setup for new Windows and macOS devices
- Enforced controls for encryption, endpoint protection, firewall, patching, and screen lock
- Controlled, auditable support access for external providers
- Ongoing compliance visibility and monthly reporting

---

## Opportunity Snapshot

### Stakeholders

- Revolv3 IT point of contact (name TBC — must be confirmed before engagement begins)
- Security and compliance stakeholders
- Senior management
- Prospective MSP or consultant team

### Geographic Distribution

Revolv3's team spans multiple time zones. Any vendor support model must account for this:

| Location | Time Zone | UTC Offset | Core Hours (UTC) |
|----------|-----------|------------|-----------------|
| US (West Coast) | PST/PDT | UTC−8/−7 | 17:00–01:00 |
| Eastern Europe | CET/EET | UTC+1/+2 | 07:00–17:00 |
| Bangladesh | BST | UTC+6 | 02:00–12:00 |

The PST business hours window (approximately 17:00–01:00 UTC) represents the most challenging coverage requirement, as it falls outside normal working hours for vendors based in Asia.

### Why This Opportunity Matters

- Endpoint controls are treated as a direct PCI DSS requirement
- The engagement supports Revolv3's annual compliance posture
- Revolv3 needs a model that allows external support without creating unacceptable audit or access risk

---

## Scope

### In Scope

- Microsoft Intune-based endpoint management for approximately 40 corporate laptops
- Windows Autopilot for new Windows devices
- Apple Automated Device Enrollment through Apple Business Manager for new macOS devices
- Enrollment and remediation of existing laptops already in active use
- Security baseline enforcement through Intune and Entra ID Conditional Access
- Application deployment and application update management
- Privilege management for standard users, developers, and IT support accounts
- Compliance monitoring, monthly reporting, and vendor operating controls
- Third-party access model for any MSP or consultant with Intune access
- Coro decommissioning support (contingent on Revolv3 decision; must be prepared for within the engagement period)

### Out of Scope

- Mobile phones and tablets
- Any delivery model that relies on Microsoft 365 Business Standard without the required upgrade
- Broad Global Administrator access or unrestricted tenant-wide vendor access

### Users, Platforms, and Systems Affected

- Approximately 40 corporate laptops
- Mixed Windows and macOS estate
- Microsoft 365 tenant (upgrading from Business Standard to Business Premium)
- Microsoft Intune
- Microsoft Entra ID (with PIM)
- Windows 365 Cloud PC (for vendor access only)
- Apple Business Manager
- CrowdStrike Falcon (primary EDR and AV)
- Coro (currently deployed; may be retired during the engagement)
- Cato Client (required on all 40 devices)
- Zoom
- Slack
- Files.com
- One approved AI desktop tool per relevant user group (final list TBC)

### Dependencies and Assumptions

- Revolv3 will upgrade from Microsoft 365 Business Standard to Business Premium before work starts; this is an absolute prerequisite
- Business Premium licensing must be active and confirmed before any Intune configuration begins
- Revolv3 will provision and manage PIM, named accounts, Windows 365 Cloud PCs, Conditional Access, and log retention infrastructure on its side
- All changes require written approval from Revolv3 and must follow the documented change process
- Emergency changes that cannot wait for approval must be documented and reviewed within 24 hours after the fact
- The final application list must be confirmed before Intune configuration and application deployment begins

---

## Technical Requirements — Detail

### OS Patch Management

#### Windows

| Update Type | Deferral Period | Enforcement |
|------------|-----------------|-------------|
| Quality updates | 3 days | Enforced after deferral |
| Feature updates | 14 days | Enforced after deferral |
| Post-deferral restart | 3-day grace period | Forced restart at 02:00 UTC if not actioned |

#### macOS

| Update Type | Deferral Period | Enforcement |
|------------|-----------------|-------------|
| Standard OS updates | Up to 30 days (user-deferrable) | Forced after 30 days |
| Rapid Security Responses | No deferral permitted | Must install immediately |

### Security Baseline Controls

#### Encryption

- Windows: BitLocker full-disk encryption — enabled via Intune, recovery key escrowed to Entra ID
- macOS: FileVault full-disk encryption — enabled via Intune, recovery key escrowed to Entra ID

#### Endpoint Detection and Response

- CrowdStrike Falcon is the primary EDR and antivirus platform on all devices
- Microsoft Defender must be set to passive mode via CrowdStrike deployment policy so that CrowdStrike operates as the sole active AV engine; Defender in passive mode continues to provide supplementary detection reporting

#### Firewall

- Windows: Windows Defender Firewall enabled and locked via Intune
- macOS: macOS Application Firewall enabled with stealth mode on

#### Screen Lock

- All devices must auto-lock after 5 minutes of inactivity

#### Password Policy

| Parameter | Requirement |
|-----------|-------------|
| Minimum length | 12 characters |
| Complexity | Required |
| Maximum age | 180 days |
| Lockout threshold | 10 failed attempts |
| Lockout duration | 15 minutes |

#### Conditional Access

- Non-compliant devices must be blocked from Microsoft 365 access via Conditional Access
- A dedicated Conditional Access policy must enforce that vendor named Entra ID accounts can only access the Intune admin centre from within the Revolv3-provisioned Windows 365 Cloud PC; any attempt to access the Intune portal from an external device must be blocked automatically

### Remote Management Capabilities

IT must be able to perform the following remotely for all managed devices:

- Remote lock
- Remote wipe (full device wipe)
- Sync / force policy refresh
- Retrieve BitLocker or FileVault recovery key
- Retrieve Windows LAPS local admin password
- View device compliance state and installed applications

The Intune compliance dashboard must provide real-time visibility for every managed device, covering at minimum: compliance status, OS version, encryption status, CrowdStrike status, last check-in time, and assigned user.

### Privilege Management

#### Standard Users

- Standard users have no local admin rights
- Software installation requires IT involvement or an approved self-service mechanism

#### Developers (Windows)

- Microsoft Endpoint Privilege Management (EPM) or equivalent approach
- If permanent local admin rights are a hard business requirement for specific developers, this must be scoped explicitly to named developer devices via a targeted Intune configuration profile assigned to a dedicated device group; it must not be granted broadly

#### Developers (macOS)

- The Privileges application (open source, SAP SE) must be deployed to developer devices
- Temporary elevation window: 60 minutes per session
- Developer logs their reason before elevation is granted

#### IT Administrator Account (Windows)

- Windows LAPS manages a local admin account on each Windows device
- LAPS must rotate the local admin password every 30 days
- The IT admin account must be hidden from the standard login screen

#### IT Administrator Account (macOS)

- A hidden local administrator account must be created with a UID below 500 (which causes macOS to hide the account from the login window natively)
- Account password must be strong, unique, stored in Revolv3's designated password manager, and rotated periodically via a redeployed Intune shell script

### Application Deployment

#### Required Applications and Deployment Methods

| Application | Windows Deployment | macOS Deployment |
|------------|-------------------|-----------------|
| Microsoft 365 Apps | Intune M365 Apps deployment | PKG |
| CrowdStrike Falcon sensor | Intune Win32 | PKG |
| Coro security agent | Intune Win32 | PKG |
| Cato Client | Intune Win32 | PKG |
| Zoom | Intune Win32 | PKG |
| Slack | Intune Win32 | PKG |
| Files.com | Intune Win32 | PKG |
| Approved AI tool (per user group) | TBC once final list confirmed | TBC |

#### Application Update Management

| Update Type | Method |
|------------|--------|
| Microsoft 365 Apps | Monthly Enterprise Channel via Office CDN — automatic, no user action required |
| CrowdStrike Falcon | Vendor-managed sensor updates via Falcon console |
| All other required apps | IT packages updated version and redeploys via Intune on a defined monthly cycle |
| Zoom, Slack (native updater) | Native updater permitted for standard users where the app handles elevation correctly |

The vendor is responsible for monitoring vendor release notes and initiating update deployments in a timely manner, particularly for security-relevant updates. Application versions must be reviewed and updated at minimum on a monthly cycle.

### Coro Decommissioning

Coro may be retired within the next 12 months pending a final Revolv3 decision. For the purposes of this engagement, Coro must be included in the initial deployment scope. The vendor must be prepared to handle decommissioning of the Coro agent across all managed devices via Intune if and when Revolv3 makes that decision. Revolv3 will provide reasonable notice.

**Vendor confirmation of silent macOS installation support for Coro must be obtained before initial deployment proceeds.**

---

## Vendor Operating Requirements (Section 2 of Source Document)

### Access Model

- Vendor personnel must access the environment exclusively through Revolv3-provisioned Windows 365 Cloud PCs
- Windows 365 Business — 2 vCPU / 8 GB RAM / 128 GB storage (approximate cost: USD $31–41 per Cloud PC per month — provisioned and paid by Revolv3)
- Access via Windows 365 web portal (windows365.microsoft.com) or the Windows App
- No access from vendor personal or company devices

### Entra ID Account Model

- Revolv3 will provision named Entra ID guest accounts for each vendor individual
- No shared accounts under any circumstances (PCI DSS Req. 8.2.1)
- Vendor role: Intune Administrator — no Global Administrator access
- PIM required for all privileged role activations

### PIM Configuration

| Setting | Requirement |
|---------|------------|
| Assignment type | Eligible — not Active |
| Maximum activation duration | 4 hours per session |
| MFA on activation | Required (phishing-resistant MFA preferred) |
| Justification on activation | Required |
| Activation approval | Recommended; Revolv3 IT point of contact as approver |

### Logging and Audit

- All third-party administrative activity must be logged and retained for 12 months
- Vendors must not interfere with logging or audit controls — this is an immediate termination event
- Revolv3's IT point of contact must perform a monthly review of external party activity logs to confirm:
  - All access occurred as expected
  - All PIM activations had valid justifications
  - No unexpected changes were made
  - This review must be documented
- Revolv3 will conduct a quarterly access review to confirm that only current, named individuals have access and that no standing privileged roles exist

### Documentation and Knowledge Ownership

- All documentation, scripts, and configuration knowledge must remain owned by Revolv3 and be accessible at all times
- Loss of documentation is treated as a loss of the environment — a dealbreaker requirement

### Vendor Legal Entity and Insurance

- Before the engagement begins, the vendor must confirm:
  - Legal entity: registered company name, country of registration, and registration number (or state if sole trader or individual)
  - Professional liability or errors and omissions insurance status; absence of insurance is not automatically a dealbreaker but must be disclosed and documented as a known accepted risk

### Vendor Security Self-Assessment

- Revolv3 will ask the vendor annually to complete a short self-assessment questionnaire covering:
  - Whether vendor devices are encrypted
  - Whether MFA is used on personal accounts used for work
  - Whether a secure password management process exists
  - Whether endpoint protection is running on vendor machines

### Third-Party Service Provider Acknowledgment

- The vendor must sign Revolv3's Third-Party Service Provider (TPSP) acknowledgment — a short document confirming that the vendor understands they are operating in a PCI DSS environment and accepts responsibility for operating within the access controls Revolv3 has defined

### Security Incident Notification

- The vendor must notify Revolv3 within 24 hours of any security incident affecting systems, devices, or credentials used to access Revolv3's environment — including device theft or loss, credential compromise, or any unauthorized access event

---

## Support Model and SLA

### Support Channels

- All support requests, change requests, and ongoing tasks must be logged as Jira tickets in a dedicated Jira project provisioned by Revolv3
- Every issue must be logged in Jira regardless of how it was first raised
- Revolv3 will provision a dedicated shared mailbox (e.g. it-endpointmgmt@revolv3.com) monitored by both the Revolv3 IT point of contact and the vendor's named individuals
- For Tier 2 and Tier 3 issues requiring immediate attention, Revolv3 will create a dedicated private channel in Microsoft Teams with named external guests using Revolv3 Entra ID accounts
- Ad-hoc messages via personal email, personal WhatsApp, or any informal channel outside Revolv3's controlled environment are not acceptable for a PCI DSS environment

### SLA Tiers

| Priority | Definition | Acknowledgment | Active Response |
|----------|------------|----------------|----------------|
| Tier 1 — Routine | Non-urgent requests, changes, questions | Within 4 vendor business hours | Within 1 vendor business day |
| Tier 2 — Urgent | Productivity impact, not business-critical | Within 2 hours | Within 4 hours |
| Tier 3 — Critical | Security incident, users locked out, data risk | Within 1 hour | Within 2 hours |

### PST Hours Critical Incident Coverage

Revolv3 acknowledges that the Tier 3 SLA window during PST business hours is challenging for vendors based in Asia. The vendor must define and document who covers critical incidents during the PST business hours window — whether through a named Bangladesh-based team member, an on-call arrangement, or another agreed solution. This must be named in the engagement agreement.

### Ticket Governance

- No ticket may be closed by the vendor unilaterally — closure requires confirmation from Revolv3's IT point of contact

---

## Reporting Requirements

### Monthly Compliance Reports

- Monthly compliance reports must be produced summarising the fleet's overall security posture and any outstanding remediation items
- Reports must cover at minimum: device compliance rate, non-compliant devices and root cause, patch status, CrowdStrike coverage, encryption status

### Real-Time Compliance Notifications

- Devices that fall out of compliance must trigger an automated notification to the Revolv3 IT point of contact

---

## Commercial and Delivery Context

| Item | Current Position |
|------|-----------------|
| Budget status | Not stated in source document |
| Pricing confirmed | Yes — implementation is complimentary; managed service $15/device/month |
| Pricing model | Implementation: complimentary (no charge). Managed service: $15 per device per month (40 devices = $600/month recurring). |
| Engagement type | Combined — implementation (Phase 1) followed by ongoing managed service (Phase 2) |
| Target timeline | Not explicitly stated; Business Premium license upgrade must complete before Phase 1; final application list must be confirmed before Phase 2 |

### Hard Deadlines

- Business Premium licenses must be active before implementation starts
- The final application list must be confirmed before Intune configuration begins
- Vendor access must be offboarded within 24 hours when an individual leaves the engagement

### Procurement and Approval Constraints

- Revolv3 requires written approval for all changes
- The vendor must disclose legal entity, insurance status, and named individuals before the engagement begins
- Dealbreaker requirements in the source document are non-negotiable unless senior management approves otherwise in writing

---

## Dealbreaker Requirements Summary

The following requirements are explicitly flagged as dealbreakers in the source document. These cannot be negotiated without written sign-off from Revolv3 senior management:

| Requirement | PCI DSS Reference |
|------------|------------------|
| Intune Administrator role only — no Global Admin | PCI DSS risk |
| PIM required — no standing active admin role | PCI DSS Req. 7 & 8 |
| No shared accounts under any circumstances | PCI DSS Req. 8.2.1 |
| Windows 365 Cloud PC as exclusive access method | Revolv3 risk assessment |
| No interference with logging or audit infrastructure | Immediate termination event |
| Documentation owned by Revolv3, accessible at all times | Loss of environment risk |
| Support hours must cover PST business hours | Business continuity |
| Named list of all individuals with access before engagement begins | PCI DSS third-party accountability |
| Vendor identity and legal entity confirmed in writing | Third-party risk |
| 24-hour notification of any security incident | Contractual obligation |

---

## Open Questions

### Clarifications Needed Before Proposal Drafting

- Confirm the named Revolv3 business and technical stakeholders
- ~~Confirm whether the requested proposal is for implementation only, managed service only, or a combined phased engagement~~ **Confirmed 2026-03-13: combined phased engagement — implementation then ongoing managed service**
- ~~Confirm whether the vendor is expected to set up Jira, the shared mailbox, and the Teams escalation channel~~ **Confirmed 2026-03-13: Revolv3 will provision and own all tooling; vendor operates within it**
- Confirm desired documentation deliverables, handover expectations, and training expectations
- ~~Confirm Coro silent macOS installation support before initial deployment can proceed~~ **Confirmed 2026-03-13: Coro included in scope; vendor to include in deployment**

### Commercial Unknowns

- ~~Pricing model~~ **Confirmed 2026-03-13: $15/device/month managed service (40 devices = $600/month recurring)**
- ~~Implementation project fee~~ **Confirmed 2026-03-13: complimentary — no charge**
- Contract term and renewal expectations

### Scope Ambiguities

- Final developer and technical staff application list: Revolv3 will provide before Phase 2 begins
- Final AI desktop tool assignment per user group: Revolv3 will provide before Phase 2 begins
- Coro may be removed during the engagement — vendor must be prepared for decommissioning task
- PST-hours Tier 3 coverage model must be named in the agreement before signing

---

## Source Traceability

### Primary Source Files Used

- `input/raw/pdf/Endpoint Management Requirements_V10.pdf`
- `input/working/extracted-notes/Endpoint Management Requirements_V10.txt`

### Key Customer Wording To Preserve

- "Endpoint security controls are not optional"
- "This is a laptop-only rollout"
- "The vendor should not commence any Intune configuration work until Revolv3 has confirmed that Business Premium licenses are active"
- "All requirements in this document are non-negotiable unless explicitly agreed in writing by Revolv3 senior management"
- "No ticket may be closed by the vendor unilaterally. Closure requires confirmation from Revolv3's IT point of contact."
- "Ad-hoc messages via personal email, personal WhatsApp, or any informal channel outside Revolv3's controlled environment are not acceptable for a PCI DSS environment."

### Conflicting Source Details

No direct conflicts were identified in the PDF. Several items are intentionally left open for later confirmation.

### Normalization Status

- Source reviewed: Yes
- Gaps identified and incorporated: Yes (full detail pass completed 2026-03-13)
- Reviewed by human: No
- Ready for proposal creation: Yes, subject to open questions review
