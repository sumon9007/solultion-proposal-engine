# Microsoft Intune Endpoint Management
## Implementation and Managed Support Proposal

---

**Prepared for:** Contoso Ltd
**Prepared by:** Sigma Technologies Ltd
**Document Reference:** PROP-2026-03-11-CONTOSO
**Date:** 11 March 2026
**Version:** 1.0
**Valid for:** 30 days from date of issue

---

## Executive Summary

Contoso Ltd currently operates 40 corporate devices — Windows laptops and mobile devices — managed through basic Group Policy with no mobile device management capability. This leaves corporate data accessible on unmanaged devices, produces inconsistent security policy enforcement across the fleet, and requires manual effort from the IT team to track and maintain compliance.

We will deploy **Microsoft Intune** as Contoso's unified endpoint management platform, enrolling all 40 devices within a 2–3 week engagement. Intune will enforce security baselines, control application delivery, and provide real-time compliance visibility across every corporate device. Following implementation, our team will provide ongoing managed endpoint support, ensuring Contoso's device estate remains secure, compliant, and current without requiring dedicated in-house resource.

The outcome: all 40 corporate devices enrolled and compliant within 30 days, consistent security policies enforced from day one, and a managed service model that scales as Contoso grows.

---

## Understanding of Requirements

Contoso Ltd operates within the professional services sector and maintains a fleet of 40 corporate devices, comprising Windows laptops and a number of iOS and Android mobile devices used by staff across its UK office.

The current management approach relies on Windows Group Policy for laptop configuration, with no equivalent capability for mobile devices. This creates three specific problems:

**Unmanaged mobile devices.** Corporate email, documents, and business applications are accessible on mobile devices that have no enforced security policies, no remote wipe capability, and no visibility from the IT team. If a device is lost or a staff member leaves the organisation, sensitive data may remain accessible.

**Inconsistent policy enforcement.** Group Policy provides basic control over Windows devices but cannot enforce modern security baselines such as BitLocker encryption status, Windows Defender configuration, or compliance with minimum OS versions. Devices that fall out of policy are not automatically detected.

**Manual compliance overhead.** Without a centralised management platform, the IT team has no consolidated view of device health, patch status, or policy compliance. Identifying and remediating non-compliant devices requires manual, time-consuming investigation.

Contoso requires a solution that places all 40 devices under a single management plane, enforces security policies consistently, provides remote wipe and selective wipe capabilities, and reduces the ongoing operational burden on the IT function. The organisation also requires ongoing managed support to maintain the solution post-implementation, as it does not have dedicated endpoint management resource in-house.

---

## Proposed Solution

We will deploy **Microsoft Intune**, Microsoft's cloud-native endpoint management platform, as Contoso's unified management solution for all corporate devices. Intune is integrated with **Microsoft Entra ID** (formerly Azure Active Directory) to provide identity-driven access control, ensuring that only enrolled, compliant devices can access corporate resources.

### Platform Architecture

The solution will be delivered as a fully cloud-managed deployment. No on-premises infrastructure is required. All devices communicate with Intune via the internet, enabling management of remote workers and devices in any location.

### Endpoint Management Capabilities Deployed

| Capability | Description |
|-----------|-------------|
| **Device Enrolment** | All 40 Windows, iOS, and Android devices enrolled into Intune using appropriate enrolment methods (Windows Autopilot / Company Portal) |
| **Compliance Policies** | Device compliance rules enforced: minimum OS version, encryption status, PIN/password requirements, screen lock timeout |
| **Configuration Profiles** | Security baselines applied: BitLocker (Windows), device restrictions, Wi-Fi and VPN profiles where required |
| **Conditional Access** | Entra ID Conditional Access policies ensure only enrolled, compliant devices access Microsoft 365 services including Exchange Online, SharePoint, and Teams |
| **Application Management** | Required business applications deployed via Intune; Mobile Application Management (MAM) controls applied to protect corporate data within apps on mobile devices |
| **Remote Actions** | IT team gains remote wipe, selective wipe, and device lock capability across the entire fleet |
| **Compliance Dashboard** | Real-time view of device compliance status, policy application, and enrolled device inventory |

### Ongoing Managed Support

Following implementation, we will provide ongoing managed endpoint support under our **Professional** managed service tier. This covers:

- Proactive monitoring of device compliance status
- Management of Intune policy updates and configuration changes
- Monthly compliance reporting
- OS update and patch policy management
- Helpdesk support for Intune-related device issues (remote, business hours)
- Quarterly service review meetings

---

## Scope of Work

### In-Scope

The following activities are included in this engagement:

1. **Assessment and Design** — Review of Contoso's existing Microsoft 365 tenant, Entra ID configuration, and device inventory. Production of a solution design document confirming enrolment methods, compliance policies, and Conditional Access rules.

2. **Intune Tenant Configuration** — Configuration of the Intune portal: enrolment settings, compliance policies, configuration profiles, and application assignments for Windows, iOS, and Android platforms.

3. **Conditional Access Policy Deployment** — Configuration of Entra ID Conditional Access policies to restrict Microsoft 365 access to enrolled, compliant devices.

4. **Device Enrolment** — Enrolment of all 40 corporate devices into Intune. Windows devices via Autopilot or manual enrolment with Company Portal; iOS and Android devices via Company Portal with an assisted self-service model.

5. **Application Deployment** — Configuration and assignment of required applications (as specified by Contoso) through Intune. Mobile Application Management (MAM) policies applied to protect corporate data within mobile apps.

6. **Testing and Validation** — Functional testing of compliance policies, Conditional Access enforcement, remote actions, and application delivery across all three device platforms before go-live.

7. **Handover and Documentation** — Full configuration documentation, administrator guide, and a one-hour handover session with Contoso's IT contact.

8. **Ongoing Managed Support** — Post-implementation managed endpoint support under the Professional service tier, as described in the Proposed Solution section.

### Client Responsibilities

The client will be responsible for the following throughout this engagement:

- Appointing a named IT contact with administrative access to the Microsoft 365 tenant
- Providing administrator credentials for the Intune and Entra ID environments
- Confirming the list of required applications to be deployed via Intune
- Communicating the enrolment schedule to device users and coordinating device availability during the enrolment phase
- Completing any prerequisite licensing activities (Microsoft Intune Plan 1 or equivalent must be active before technical work begins)
- Participating in the sign-off and testing phase to confirm the solution meets requirements

### Change Control

Any work not listed in the In-Scope section above is out of scope. Requests for additional work — including additional device types, additional applications, custom scripting, or additional Conditional Access policies — will be assessed and priced via a formal Change Request before any additional work commences.

### Engagement Model

The implementation phase is priced as a fixed-scope, fixed-price engagement. The ongoing managed support is provided under a monthly recurring service contract with a minimum term of 12 months.

---

## Deliverables

| # | Deliverable | Format | Delivered |
|---|------------|--------|-----------|
| 1 | Solution Design Document | PDF/Word | End of Phase 1 (Day 3) |
| 2 | Configured Intune tenant (policies, profiles, applications) | Live environment | End of Phase 2 (Day 10) |
| 3 | All 40 devices enrolled and compliant in Intune | Live environment | End of Phase 3 (Day 14) |
| 4 | Conditional Access policy — compliant device enforcement | Live environment | End of Phase 2 (Day 10) |
| 5 | Test sign-off report | PDF | End of Phase 3 (Day 14) |
| 6 | Administrator guide — Intune operations | PDF | Handover (Day 15) |
| 7 | Monthly compliance report | PDF/email | Monthly (post go-live) |
| 8 | Quarterly service review meeting | Online meeting | Every 3 months |

---

## Assumptions & Dependencies

The following assumptions have been made in preparing this proposal. If any assumption proves to be incorrect, the scope, timeline, or cost may be affected. Changes will be managed through our formal Change Request process.

1. It is assumed that the client will appoint a named Technical Lead for the duration of the engagement, with sufficient authority to approve configurations and make decisions within agreed timeframes.

2. It is assumed that the client will make relevant stakeholders and device users available for the enrolment phase as required by the project plan. Unavailability of users during enrolment may delay the timeline.

3. It is assumed that Contoso holds, or will obtain, Microsoft Intune Plan 1 licences (included in Microsoft 365 Business Premium, E3, or E5) for all 40 devices before technical work commences. Licence procurement is not included in this proposal.

4. It is assumed that Contoso's Microsoft 365 tenant is in a healthy state with Entra ID functioning correctly. Any remediation of the existing tenant is not included in this scope.

5. It is assumed that the 40 devices in scope are running supported operating system versions: Windows 10 21H2 or later, iOS 16 or later, Android 10 or later. Devices running unsupported OS versions must be upgraded before enrolment; OS upgrade is not included in this scope.

6. It is assumed that administrator-level access to the Microsoft 365 tenant, Intune, and Entra ID will be provided to our team before technical work commences, and that this access will remain available for the duration of the implementation.

7. It is assumed that the client will provide timely responses to information requests, testing participation, and sign-off requests within 1 business day during the implementation phase. Delays in client response may affect the timeline.

8. It is assumed that the device count will not exceed 40 during the implementation phase. Additional devices beyond this number will be subject to a Change Request.

9. It is assumed that all 40 devices are corporate-owned devices. BYOD (personal device) enrolment is not included in this scope. Mobile Application Management (MAM) without device enrolment can be scoped separately if required for personal devices.

10. It is assumed that the client has suitable internet connectivity to support cloud-based device management. Intune requires HTTPS outbound connectivity to Microsoft endpoints from managed devices.

11. It is assumed that any required third-party systems (VPN, Wi-Fi) whose profiles need deploying via Intune will be documented and accessible to the project team during the design phase.

---

## Exclusions

The following items are explicitly excluded from this proposal:

1. Microsoft Intune licence procurement. Licences must be in place before work commences.
2. End-user training or change management communications beyond the administrator handover session.
3. OS upgrades for devices not meeting the minimum version requirements.
4. Custom application packaging, scripting, or Win32 app wrapping beyond standard MSI/MSIX deployment.
5. BYOD (personal device) enrolment without full device management (MAM-only for personal devices is a separate scope item).
6. Microsoft Defender for Endpoint integration or configuration, unless separately scoped.
7. Third-party MDM migration or decommissioning.
8. Hardware procurement, device refresh, or physical device setup.
9. Identity remediation in Entra ID (e.g., hybrid identity configuration, AD Connect issues).
10. Penetration testing or formal security assessments.
11. Any work required to bring Contoso's Microsoft 365 tenant into a baseline-compliant state before implementation begins.
12. Network infrastructure changes, firewall rule modifications, or proxy configuration beyond standard Intune URL allowlisting guidance.

---

## Indicative Pricing

> **INDICATIVE PRICING — Subject to commercial review and sign-off before issue to client.**

| Item | Description | Unit | Qty | Rate | Total |
|------|-------------|------|-----|------|-------|
| Intune Implementation | Assessment, design, configuration, enrolment (40 devices), testing, handover | Fixed price | 1 | £8,500 | £8,500 |
| Ongoing Managed Support | Professional tier managed endpoint support — Intune monitoring, patch management, helpdesk, monthly reporting | Per month | 12 | £650 | £7,800 |
| **Total Investment (Year 1)** | | | | | **£16,300** |

**Notes:**
- All prices are exclusive of VAT, charged at the prevailing rate.
- Implementation is fixed-price. The managed support is a monthly recurring charge with a minimum 12-month term.
- Payment terms: 50% of implementation fee on engagement commencement, 50% on go-live sign-off. Managed support invoiced monthly in advance.
- Renewal of managed support after the initial 12-month term is subject to a separate renewal agreement.

---

## Timeline

### Implementation — 2 to 3 Weeks

| Phase | Activities | Duration | Owner |
|-------|-----------|----------|-------|
| **Phase 1 — Assessment & Design** | Tenant review, device inventory confirmation, solution design document, sign-off | Days 1–3 | Joint |
| **Phase 2 — Configuration** | Intune tenant configuration, compliance policies, configuration profiles, Conditional Access, app assignments | Days 4–10 | Our team |
| **Phase 3 — Enrolment & Testing** | Device enrolment (all 40 devices), functional testing, UAT sign-off | Days 11–14 | Joint |
| **Phase 4 — Handover** | Documentation delivery, administrator handover session, go-live confirmation | Day 15 | Our team |

### Key Milestones

| Milestone | Target | Owner |
|-----------|--------|-------|
| Project kick-off meeting | Day 1 | Joint |
| Solution design sign-off | Day 3 | Client |
| Intune configuration complete | Day 10 | Our team |
| All 40 devices enrolled | Day 14 | Joint |
| Go-live and handover | Day 15 | Our team |
| Managed support commencement | Day 16 | Our team |

### Timing Assumptions

This timeline assumes a confirmed start date and uninterrupted access to the Contoso Microsoft 365 tenant. Device user availability for enrolment during Phase 3 must be coordinated by the client. Any delays in tenant access, design sign-off, or device availability will extend the timeline accordingly.

---

## About Us

**Sigma Technologies Ltd** is a specialist technology consultancy and managed services provider, delivering cloud transformation, Microsoft 365 solutions, and IT managed services to enterprise and mid-market organisations across the UK and internationally.

Our team of certified consultants and engineers brings deep expertise across Microsoft Azure, Microsoft 365, endpoint management, network infrastructure, and cybersecurity.

### Our Capabilities

| Practice Area | Key Technologies |
|---------------|-----------------|
| Cloud & Infrastructure | Microsoft Azure, Hybrid Cloud, IaaS, PaaS |
| Modern Workplace | Microsoft 365, Teams, SharePoint, Intune |
| Cybersecurity | Microsoft Sentinel, Defender, Zero Trust, MFA |
| Managed Services | 24x7 monitoring, helpdesk, proactive support |
| Consultancy | Strategy, architecture, programme delivery |

### Microsoft Partner Credentials

As a Microsoft Solutions Partner, we maintain accreditation across the Modern Work and Security solution areas, with direct access to Microsoft engineering and support resources. Our engineers hold Microsoft 365 Endpoint Administrator certifications specific to the Intune platform.

### Our Certifications

- Microsoft 365 Enterprise Administrator Expert
- Microsoft Endpoint Administrator (MD-102)
- Microsoft Azure Solutions Architect Expert
- ITIL v4 Foundation
- PRINCE2 Practitioner

---

## Next Steps

To progress this proposal, we propose the following steps:

### 1. Proposal Review Meeting

We welcome the opportunity to present this proposal and answer any questions. Please contact us to arrange a 60-minute call at a time that suits you.

### 2. Clarifications and Amendments

If any aspect of this proposal requires adjustment — scope, phasing, or commercial terms — please raise this with your named contact. We are happy to revise before contract.

### 3. Formal Acceptance

To formally accept, please sign and return the accompanying Statement of Work, or confirm acceptance in writing by email. We will issue a formal commencement confirmation and confirm your start date.

### 4. Kickoff

Once the agreement is signed, we will schedule a project kick-off meeting within 5 business days. At this meeting we will:

- Introduce the project team
- Confirm roles and responsibilities on both sides
- Agree the detailed enrolment schedule
- Confirm tenant access requirements and prerequisites
- Establish communication and escalation channels

### 5. Mobilisation

Following kick-off, technical work commences immediately according to the agreed plan.

---

We look forward to supporting Contoso Ltd's endpoint management programme. Please do not hesitate to contact us with any questions about this proposal.

---

## Legal Notes

### Validity

This proposal is valid for 30 days from the date of issue. After this period, pricing, availability, and scope are subject to review and may change without notice.

### Confidentiality

This document contains commercially sensitive information and is provided in confidence to Contoso Ltd only. It must not be reproduced, distributed, or disclosed to any third party without the prior written consent of Sigma Technologies Ltd.

### Intellectual Property

All intellectual property created specifically for Contoso Ltd during this engagement will vest in the client upon receipt of full payment. Pre-existing intellectual property, methodologies, tools, templates, and frameworks belonging to Sigma Technologies Ltd remain our property and are licensed to the client for use within the scope of this engagement only.

### Liability

Sigma Technologies Ltd's total aggregate liability to Contoso Ltd under or in connection with this engagement shall not exceed the total fees paid by the client in the 12 months preceding the event giving rise to the claim. In no event shall Sigma Technologies Ltd be liable for any indirect, special, incidental, or consequential loss or damage, including loss of profit, loss of revenue, or loss of data.

### Payment Terms

All invoices are due within 30 days of the invoice date. Late payment may attract interest in accordance with the Late Payment of Commercial Debts (Interest) Act 1998. All prices in this proposal are exclusive of VAT, which will be charged at the prevailing rate.

### Governing Law

This proposal and any resulting contract shall be governed by and construed in accordance with the laws of England and Wales. Any dispute shall be subject to the exclusive jurisdiction of the courts of England and Wales.

### Acceptance

This proposal does not constitute a contract. A binding agreement will only come into effect upon execution of a formal Statement of Work or Master Services Agreement signed by authorised representatives of both parties.

---

*Sigma Technologies Ltd is a company registered in England and Wales. Company Registration Number: 12345678. Registered office: 100 Technology Square, London, EC1A 1BB.*