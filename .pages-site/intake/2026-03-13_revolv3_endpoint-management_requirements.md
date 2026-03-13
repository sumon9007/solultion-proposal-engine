# Customer Requirements

Use this file as the normalized intake document for each new engagement.

Preferred process:
1. Collect raw source material in `input/raw/`
2. Record the sources in `input/source-register.md`
3. Generate or update this file using `/requirements-build`

## Opportunity Snapshot

- Client name: Revolv3
- Industry: Financial technology / payment gateway
- Primary contact: Revolv3 IT point of contact (name not yet provided)
- Other stakeholders: Revolv3 IT, security/compliance stakeholders, senior management, prospective MSP or consultant team
- Opportunity name: Endpoint Management & Security Requirements
- Solution type: Endpoint management implementation with ongoing managed support and security governance

## Business Context

- Current challenge: Revolv3 needs a vendor proposal for deployment and ongoing management of its corporate endpoint environment across a mixed Windows and macOS laptop fleet, with strong security enforcement and operational controls.
- Business drivers: Standardize endpoint management, enforce security baselines through Microsoft Intune, support zero-touch provisioning, reduce unmanaged-device risk, and meet PCI DSS obligations for endpoint controls and third-party access.
- Risks of inaction: Continued endpoint inconsistency, weak compliance posture, inability to enforce Conditional Access based on device compliance, unmanaged privilege risks, poor auditability for third-party access, and exposure in a PCI DSS-regulated environment.
- Desired outcomes:
  - Bring approximately 40 corporate laptops under consistent management
  - Support zero-touch setup for new Windows and macOS devices
  - Enforce encryption, endpoint protection, firewall, patching, screen lock, and compliance controls
  - Enable controlled support access and auditable vendor operations
  - Establish an operational model that supports ongoing compliance monitoring and monthly reporting

## Scope

- In scope:
  - Microsoft Intune-based endpoint management for approximately 40 corporate laptops
  - Windows Autopilot for new Windows devices
  - Apple Automated Device Enrollment via Apple Business Manager for new macOS devices
  - Enrollment and remediation of existing laptops already in daily use
  - Security baseline enforcement through Intune and Entra ID Conditional Access
  - Application deployment and update management
  - Privilege management for standard users, developers, and IT admin accounts
  - Compliance monitoring, monthly reporting, and vendor operating controls
  - Third-party access model for any MSP or consultant with Intune access
- Out of scope:
  - Mobile phones and tablets
  - Any approach that relies on Microsoft 365 Business Standard without the required upgrade
  - Broad Global Administrator access or unrestricted tenant-wide vendor access
- Users / sites / systems affected:
  - Approximately 40 corporate laptops
  - Mixed Windows and macOS estate
  - Microsoft 365 tenant, Microsoft Intune, Microsoft Entra ID, Windows 365 Cloud PC, Apple Business Manager, CrowdStrike Falcon, Coro, Cato Client, Zoom, Slack, Files.com, and one approved AI desktop tool per relevant user
- Dependencies or assumptions already known:
  - Revolv3 will upgrade from Microsoft 365 Business Standard to Business Premium before work starts
  - Business Premium licensing is a prerequisite and must be active before Intune configuration begins
  - Revolv3 will provision and manage PIM, named accounts, Windows 365 Cloud PCs, Conditional Access, and log retention infrastructure on its side
  - Changes require written approval and must follow the documented change process

## Commercial and Delivery Context

- Budget status: Not stated in source document
- Pricing confirmed: No
- Target timeline: Not explicitly stated; license upgrade must complete before Phase 1 and application list must be finalized before Phase 2
- Hard deadlines:
  - Business Premium licenses active before implementation starts
  - Final application list confirmed before Intune configuration begins
  - Offboarding of vendor access within 24 hours when an individual leaves the engagement
- Procurement or approval constraints:
  - Revolv3 requires written approval for all changes
  - Vendor must disclose legal entity, insurance status, and named individuals before engagement begins
  - Dealbreaker requirements in the source document are non-negotiable unless senior management approves otherwise in writing

## Technical Notes

- Current environment:
  - Revolv3 currently uses Microsoft 365 Business Standard and plans to move to Business Premium
  - Endpoint fleet is mixed Windows and macOS
  - Some devices are new, while others are already in active use and need guided enrollment
  - CrowdStrike Falcon is the primary EDR/AV platform
  - Coro agent is currently deployed but may be retired during the engagement
- Security or compliance requirements:
  - PCI DSS-aligned endpoint controls are mandatory
  - Full-disk encryption required on all devices
  - CrowdStrike must be active on all devices
  - Host firewall must be enabled and locked
  - Devices auto-lock after 5 minutes of inactivity
  - Password policy: minimum 12 characters, complexity required, maximum age 180 days, lockout after 10 failed attempts for 15 minutes
  - Non-compliant devices must be blocked from Microsoft 365 access via Conditional Access
  - All third-party admin activity must be logged and retained for 12 months
- Preferred platforms or technologies:
  - Microsoft Intune
  - Microsoft Entra ID with PIM
  - Windows Autopilot
  - Apple Automated Device Enrollment via Apple Business Manager
  - Windows 365 Cloud PC for vendor access
  - Windows LAPS for local admin account management
  - Optional Microsoft Endpoint Privilege Management or equivalent for Windows developer elevation
- Constraints or non-negotiables:
  - No Global Administrator access for vendor personnel
  - Vendor role limited to Intune Administrator unless explicitly approved for named tasks
  - PIM required; no standing admin role
  - No shared accounts
  - Vendor must access through Revolv3-provisioned Windows 365 Cloud PCs only
  - Documentation, scripts, and configuration knowledge must remain owned by Revolv3
  - Support coverage must address PST business hours
  - Vendor must not interfere with logging or audit controls

## Competitor and Selection Context

- Known competitors: Not stated
- Selection criteria:
  - Ability to meet the technical endpoint-management requirements
  - Ability to operate within Revolv3's PCI DSS and third-party security constraints
  - Willingness to work within named-account, PIM, Cloud PC, logging, and change-control requirements
  - Ability to support both implementation and ongoing operational support expectations
- Why this opportunity matters:
  - This engagement supports Revolv3's annual compliance posture
  - Endpoint controls are treated as a direct PCI DSS requirement, not an optional improvement
  - The operating model must allow Revolv3 to work safely with an external vendor without creating unacceptable audit or access risk

## Open Questions

- What still needs clarification before proposal drafting:
  - Confirm the named Revolv3 business and technical stakeholders
  - Confirm whether the requested proposal is for implementation only, managed service only, or a combined phased engagement
  - Confirm whether the vendor is expected to package Jira, Teams, and mailbox setup tasks in scope or simply operate within Revolv3-provided tooling
  - Confirm desired documentation deliverables, handover expectations, and training expectations
- Commercial unknowns:
  - Budget range and pricing model
  - Contract term and renewal expectations
  - Whether support is priced as business-hours managed service, retainer, or project plus support
- Scope ambiguities:
  - Final developer and technical staff application list is still pending
  - Final AI desktop tool assignment per user group is still pending
  - Coro may be removed during the engagement, which could introduce a change request
  - PST-hours support coverage model is still open to negotiation

## Source Traceability

- Primary source files used:
  - `input/raw/pdf/Endpoint Management Requirements_V10.pdf`
  - `input/working/extracted-notes/Endpoint Management Requirements_V10.txt`
- Key customer wording to preserve:
  - "Endpoint security controls are not optional"
  - "This is a laptop-only rollout"
  - "The vendor should not commence any Intune configuration work until Revolv3 has confirmed that Business Premium licenses are active"
  - "All requirements in this document are non-negotiable unless explicitly agreed in writing by Revolv3 senior management"
- Conflicting source details, if any:
  - No direct conflicts identified in the PDF; several items are intentionally left open for later confirmation
