# Revolv3 Endpoint Management Requirements

## Document Summary

This file is the normalized intake document for the Revolv3 endpoint management opportunity. It consolidates the customer requirement PDF into a proposal-ready internal brief.

| Field | Value |
|------|-------|
| Client | Revolv3 |
| Opportunity | Endpoint Management & Security Requirements |
| Solution Type | Endpoint management implementation with ongoing managed support and security governance |
| Industry | Financial technology / payment gateway |
| Source Status | Normalized from customer-provided PDF |
| Primary Contact | Revolv3 IT point of contact (name not yet provided) |

## Executive Overview

Revolv3 requires a vendor proposal for the deployment and ongoing management of a mixed Windows and macOS corporate laptop estate. The engagement must establish Microsoft Intune as the management platform, enforce a PCI DSS-aligned endpoint security baseline, and define a controlled third-party operating model for any MSP or consultant accessing the environment.

This is not a generic device rollout. The requirement is shaped by compliance obligations, strict access governance, and the need to operate safely within a payment-processing environment.

## Business Context

### Current Challenge

Revolv3 needs to bring its corporate endpoint estate under consistent control across approximately 40 laptops while maintaining security, minimizing user disruption, and meeting compliance obligations.

### Business Drivers

- Standardize endpoint management across Windows and macOS
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

## Opportunity Snapshot

### Stakeholders

- Revolv3 IT
- Security and compliance stakeholders
- Senior management
- Prospective MSP or consultant team

### Why This Opportunity Matters

- Endpoint controls are treated as a direct PCI DSS requirement
- The engagement supports Revolv3's annual compliance posture
- Revolv3 needs a model that allows external support without creating unacceptable audit or access risk

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

### Out of Scope

- Mobile phones and tablets
- Any delivery model that relies on Microsoft 365 Business Standard without the required upgrade
- Broad Global Administrator access or unrestricted tenant-wide vendor access

### Users, Platforms, and Systems Affected

- Approximately 40 corporate laptops
- Mixed Windows and macOS estate
- Microsoft 365 tenant
- Microsoft Intune
- Microsoft Entra ID
- Windows 365 Cloud PC
- Apple Business Manager
- CrowdStrike Falcon
- Coro
- Cato Client
- Zoom
- Slack
- Files.com
- One approved AI desktop tool per relevant user

### Dependencies and Assumptions

- Revolv3 will upgrade from Microsoft 365 Business Standard to Business Premium before work starts
- Business Premium licensing is a prerequisite and must be active before Intune configuration begins
- Revolv3 will provision and manage PIM, named accounts, Windows 365 Cloud PCs, Conditional Access, and log retention infrastructure on its side
- Changes require written approval and must follow the documented change process

## Commercial and Delivery Context

| Item | Current Position |
|------|------------------|
| Budget status | Not stated in source document |
| Pricing confirmed | No |
| Target timeline | Not explicitly stated; license upgrade must complete before Phase 1 and the application list must be finalized before Phase 2 |

### Hard Deadlines

- Business Premium licenses must be active before implementation starts
- The final application list must be confirmed before Intune configuration begins
- Vendor access must be offboarded within 24 hours when an individual leaves the engagement

### Procurement and Approval Constraints

- Revolv3 requires written approval for all changes
- The vendor must disclose legal entity, insurance status, and named individuals before the engagement begins
- Dealbreaker requirements in the source document are non-negotiable unless senior management approves otherwise in writing

## Technical Notes

### Current Environment

- Revolv3 currently uses Microsoft 365 Business Standard and plans to move to Business Premium
- The endpoint fleet is mixed Windows and macOS
- Some devices are new, while others are already in active use and need guided enrollment
- CrowdStrike Falcon is the primary EDR and antivirus platform
- Coro is currently deployed but may be retired during the engagement

### Security and Compliance Requirements

- PCI DSS-aligned endpoint controls are mandatory
- Full-disk encryption is required on all devices
- CrowdStrike must be active on all devices
- The host firewall must be enabled and locked
- Devices must auto-lock after 5 minutes of inactivity
- Password policy must enforce:
  - minimum 12 characters
  - complexity requirements
  - maximum age of 180 days
  - lockout after 10 failed attempts for 15 minutes
- Non-compliant devices must be blocked from Microsoft 365 access via Conditional Access
- All third-party administrative activity must be logged and retained for 12 months

### Preferred Platforms and Technologies

- Microsoft Intune
- Microsoft Entra ID with PIM
- Windows Autopilot
- Apple Automated Device Enrollment through Apple Business Manager
- Windows 365 Cloud PC for vendor access
- Windows LAPS for local admin account management
- Microsoft Endpoint Privilege Management or equivalent for Windows developer elevation

### Constraints and Non-Negotiables

- No Global Administrator access for vendor personnel
- Vendor role limited to Intune Administrator unless explicitly approved for named tasks
- PIM is required; no standing admin role
- No shared accounts
- Vendor personnel must access the environment only through Revolv3-provisioned Windows 365 Cloud PCs
- Documentation, scripts, and configuration knowledge must remain owned by Revolv3
- Support coverage must address PST business hours
- Vendors must not interfere with logging or audit controls

## Competitor and Selection Context

### Known Competitors

Not stated in the source document.

### Selection Criteria

- Ability to meet the technical endpoint-management requirements
- Ability to operate within Revolv3's PCI DSS and third-party security constraints
- Willingness to work within named-account, PIM, Cloud PC, logging, and change-control requirements
- Ability to support both implementation and ongoing operational support expectations

## Open Questions

### Clarifications Needed Before Proposal Drafting

- Confirm the named Revolv3 business and technical stakeholders
- Confirm whether the requested proposal is for implementation only, managed service only, or a combined phased engagement
- Confirm whether the vendor is expected to package Jira, Teams, and shared mailbox setup tasks in scope or simply operate within Revolv3-provided tooling
- Confirm desired documentation deliverables, handover expectations, and training expectations

### Commercial Unknowns

- Budget range and pricing model
- Contract term and renewal expectations
- Whether support is priced as business-hours managed service, retainer, or project plus support

### Scope Ambiguities

- Final developer and technical staff application list is still pending
- Final AI desktop tool assignment per user group is still pending
- Coro may be removed during the engagement, which could introduce a change request
- PST-hours support coverage model is still open to negotiation

## Source Traceability

### Primary Source Files Used

- `input/raw/pdf/Endpoint Management Requirements_V10.pdf`
- `input/working/extracted-notes/Endpoint Management Requirements_V10.txt`

### Key Customer Wording To Preserve

- "Endpoint security controls are not optional"
- "This is a laptop-only rollout"
- "The vendor should not commence any Intune configuration work until Revolv3 has confirmed that Business Premium licenses are active"
- "All requirements in this document are non-negotiable unless explicitly agreed in writing by Revolv3 senior management"

### Conflicting Source Details

No direct conflicts were identified in the PDF. Several items are intentionally left open for later confirmation.
