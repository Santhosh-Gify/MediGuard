---
name: MediGuard QR connection
description: The connection QR flow currently supports displaying a deterministic usercode QR and a manual-code fallback while native camera decoding remains separate work.
---

The QR connection flow should preserve a manual usercode fallback when camera permission is denied or native scanning is unavailable.

**Why:** The mobile preview must remain usable on web and on devices where camera access is unavailable.

**How to apply:** If native QR decoding is added, keep the existing Show my QR / Scan QR modes and manual code entry as a fallback.