<a id="top"></a>

<p align="center">
  <img src="assets/header.svg" alt="MediGuard - Caretaker manages, Patient taps, Doctor understands" width="100%">
</p>

<p align="center">
  <a href="#overview"><img src="assets/nav-overview.svg" alt="Overview"></a>
  <a href="#roles"><img src="assets/nav-roles.svg" alt="Roles"></a>
  <a href="#features"><img src="assets/nav-features.svg" alt="Features"></a>
  <a href="#workflow"><img src="assets/nav-workflow.svg" alt="Workflow"></a>
  <a href="#architecture"><img src="assets/nav-architecture.svg" alt="Architecture"></a>
  <a href="#roadmap"><img src="assets/nav-roadmap.svg" alt="Roadmap"></a>
  <a href="#setup"><img src="assets/nav-setup.svg" alt="Setup"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Android-7A1E48?style=for-the-badge&logo=android&logoColor=white" alt="Android">
  <img src="https://img.shields.io/badge/iOS-B04468?style=for-the-badge&logo=apple&logoColor=white" alt="iOS">
  <img src="https://img.shields.io/badge/Offline--first-C8577A?style=for-the-badge" alt="Offline-first">
  <img src="https://img.shields.io/badge/Status-In%20Development-8A2A56?style=for-the-badge" alt="Status">
</p>

<p align="center"><img src="assets/divider.svg" width="100%" alt=""></p>

## Overview

**MediGuard** is a connected medication-care app for families. An elderly patient may forget a dose, get confused about which medicine to take, or struggle with a complicated phone. MediGuard moves the complexity to the caretaker and gives the patient one simple action.

> **Caretaker manages** -> **Patient sees the exact medicine and taps once** -> **Caretakers are informed** -> **Doctor reviews the full history visually**

<p align="center">
  <img src="assets/workflow.svg" alt="MediGuard workflow" width="90%">
</p>

<p align="right"><a href="#top">Back to top</a></p>

<p align="center"><img src="assets/divider.svg" width="100%" alt=""></p>

## Roles

Every account gets a unique ID (for example `MG-251047`, `CT-2045`, `DR-1024`) used to connect people.

| | Patient | Caretaker | Doctor |
|---|---|---|---|
| **Goal** | See the medicine, respond simply | Set up and monitor care | Understand adherence at a glance |
| **Interface** | Huge controls, high contrast, image-first | Detailed and organised | Graphical, clinical, chart-driven |
| **Key actions** | Tick, voice reply, SOS | Add medicine, schedules, stock, history | Calendar, charts, filters |
| **Extra setup** | SOS number + secondary language | Relationship type and permissions | Qualifications, licence, hospital |

Connections are **many-to-many** and **relationship-aware**: one patient can have several caretakers (Primary, Family), and one caretaker can manage several patients. Access is enforced per relationship, never by role alone.

<p align="right"><a href="#top">Back to top</a></p>

<p align="center"><img src="assets/divider.svg" width="100%" alt=""></p>

## Features

Click a section to expand it.

<details>
<summary><b>The Patient alarm</b> (the heart of the app)</summary>
<br>

The alarm is a full screen, not a text notification:

1. Caretaker avatar and name
2. Caretaker's message bubble (optional) and voice note play button
3. **Large medicine photograph** (the dominant visual)
4. Essential info in **English + the patient's chosen language**
5. Big **TICK** and big **MICROPHONE**, with no "Taken / Not taken" wording

Unanswered alarms repeat every 5 minutes. The number of unanswered alarms before caretakers are alerted is configurable.
</details>

<details>
<summary><b>Adding a medicine (Caretaker)</b></summary>
<br>

- Camera or upload, then crop, preview and confirm the medicine photo
- Visual steppers for tablet count and dosage
- Visual calendar for start and end dates
- Interactive circular alarm clock (draggable hand, AM/PM, Morning / Afternoon / Night presets)
- Frequency: one-time, multiple times, daily, selected weekdays, alternate days, weekly, custom
- Schedule preview timeline before saving
- Optional text note and optional voice note
- **Preview as Patient** to see exactly what the alarm will look like
</details>

<details>
<summary><b>Family synchronisation</b></summary>
<br>

- Real-time updates: tick confirmed, missed alarm, voice reply, schedule change
- Notifications always say **who did what, for which patient, and when**
- Activity/change history so nothing changes silently
</details>

<details>
<summary><b>Doctor analytics</b></summary>
<br>

- Medication calendar (complete / partial / missed days), tap a date to see that day
- Donut charts (taken vs missed), bar charts (per medicine), line charts (adherence over time)
- Adherence rings, scheduled-vs-actual timing, dose timelines
- Filters: Today, 7 Days, 30 Days, Custom, plus per-medicine
- Charts are driven only by real stored history, with no fake analytics
</details>

<details>
<summary><b>Offline-first reminders</b></summary>
<br>

```text
Online:   Server schedule  ->  Local device schedule
Offline:  Local schedule   ->  Alarm  ->  Response  ->  Local storage
Back on:  Sync queue  ->  Server  ->  Database  ->  Caretakers
```

Offline voice replies get a unique event ID, are marked *Waiting to sync*, are never silently deleted, and are de-duplicated on sync.
</details>

<details>
<summary><b>Inventory, SOS and more</b></summary>
<br>

- **Medicine inventory:** remaining supply bar, days left, refill warning about 2 days before running out
- **SOS:** one large button, one confirmation, calls the number registered at signup
- **Appointments:** search providers, pick doctor, date and time
- **Medical vault and OCR:** store reports and prescriptions; OCR results stay *unverified* until the user confirms
- **Medi_Loaded:** dedicated section for the future physical dispenser (pairing, device ID, status)
- **Light and Dark mode** across the whole app
</details>

<p align="right"><a href="#top">Back to top</a></p>

<p align="center"><img src="assets/divider.svg" width="100%" alt=""></p>

## Workflow

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#F3E1EA','primaryBorderColor':'#8A2A56','primaryTextColor':'#5A1235','lineColor':'#B04468','secondaryColor':'#E8C6D3','tertiaryColor':'#FBF5FB'}}}%%
flowchart LR
    A[Register and choose role] --> B[Connect via unique ID]
    B --> C[Relationship accepted]
    C --> D[Caretaker adds medicine]
    D --> E[Preview as Patient]
    E --> F[Schedule saved]
    F --> G{Alarm time}
    G -->|Tick| H[Event stored]
    G -->|Voice| I[Voice sent to caretakers]
    G -->|No response| J[Repeat every 5 min]
    J -->|Threshold reached| K[Caretaker alert]
    H --> L[(Medication history)]
    I --> L
    K --> L
    L --> M[Doctor calendar and charts]
```

<p align="right"><a href="#top">Back to top</a></p>

<p align="center"><img src="assets/divider.svg" width="100%" alt=""></p>

## Architecture

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#F3E1EA','primaryBorderColor':'#8A2A56','primaryTextColor':'#5A1235','lineColor':'#B04468'}}}%%
flowchart TB
    subgraph Mobile["Mobile app (Android / iOS)"]
        P[Patient UI]
        C[Caretaker UI]
        D[Doctor UI]
        L[(Local DB + sync queue)]
    end
    subgraph Backend
        API[Protected API<br/>role + relationship checks]
        RT[Real-time channel]
        DB[(Persistent database)]
        FS[Secure file storage<br/>photos, voice, documents]
    end
    P & C & D --> L
    L <--> API
    API --> DB
    API --> FS
    API --> RT --> C
```

**Security principles:** password hashing, secure token sessions, role-based **and** relationship-level access control, input validation, protected APIs, secure uploads. Entering a patient ID never grants access on its own; the patient must accept the connection.

<p align="right"><a href="#top">Back to top</a></p>

<p align="center"><img src="assets/divider.svg" width="100%" alt=""></p>

## Roadmap

- [ ] Registration and role-specific profiles
- [ ] ID-based connection requests and relationships
- [ ] Add-medicine flow (photo, clock, calendar, frequency, notes)
- [ ] Patient alarm with tick and voice response
- [ ] Unanswered-alarm escalation
- [ ] Offline-first scheduling and sync queue
- [ ] Real-time notifications and activity history
- [ ] Medicine inventory and refill warnings
- [ ] SOS
- [ ] Doctor calendar and analytics
- [ ] Appointments, medical vault and OCR
- [ ] Medi_Loaded device integration

<p align="right"><a href="#top">Back to top</a></p>

<p align="center"><img src="assets/divider.svg" width="100%" alt=""></p>

## Setup

> Replace this section with your real stack and commands.

```bash
git clone https://github.com/<your-username>/mediguard.git
cd mediguard
# install dependencies
# configure environment variables
# run the app
```

<p align="center"><img src="assets/divider.svg" width="100%" alt=""></p>

<p align="center">
  <sub>Built with care for the people who take care of others.</sub><br>
  <a href="#top">Back to top</a>
</p>
