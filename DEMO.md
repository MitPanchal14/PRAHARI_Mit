# PRAHARI Demo Script

## 0:00 - Business Impact

"PRAHARI focuses on the highest-value moment in a digital-arrest scam: before payment. The citizen sees one clear instruction, while every report becomes graph intelligence for officers."

## 0:25 - Citizen Check

Open `http://localhost:3000/check`.

Select **Protect me during a call** and click **Run live demo**. Point out that the transcript grows while the call continues, the five scam phases update live, and PRAHARI interrupts as soon as Mit's risk threshold becomes critical - before a payment request is reached.

Show the privacy bar: `0 B` evidence uploaded and nothing shared with PRAHARI. Explain the two capture choices: Fast mode gives instant browser speech with a visible vendor-processing warning; Private mode uses local Whisper segments and keeps microphone audio on the device.

Click **Check another call or message**, select **Paste a message**, and paste:

Paste:

```text
This is CBI officer Sharma. A parcel containing narcotics was booked under your Aadhaar at Mumbai customs. You are under digital arrest. Do not tell your family. Transfer Rs.85,000 to cbi.verify@upi immediately or we will arrest you.
```

Click **Check if this is a scam**. Show that Mit's deterministic pass produces a private local result first. Then open **Help warn other people (optional)** and use **Share selected evidence**. The consented backend analysis reuses `cbi.verify@upi`, creates one incident and audit record, ingests it automatically, and attaches it to the seeded ring.

Before sharing, select the 24-hour retention option. After consent, show the byte counter and download the consent receipt.

## 1:15 - Offline Safety Story

Disconnect the network before the first scan. The private deterministic result still works and SAFE content creates no backend request. Reconnect only for the consented share; the backend can still use Mit's deterministic fallback when the optional LLM is disabled.

## 1:40 - Officer Command

Open `http://localhost:3000/command`.

Show:

- Incident queue and KPI panel.
- Graph ring list.
- Selected ring graph.
- Top suspected mule infrastructure.
- The live ring-join banner, pulsing ring row, and newly highlighted report node.

Show the benchmark strip: 120 reproducible synthetic English/Hindi/Hinglish cases. Say explicitly that it is a prototype benchmark, not field validation.

## 2:20 - Ring Evidence

Open the backend docs or call:

```text
GET http://localhost:8000/api/rings
GET http://localhost:8000/api/rings/{ring_id}/evidence-package
```

Point out that the evidence package says it is for law-enforcement review, not a legal determination.

## 2:45 - Close

"PRAHARI stops the scam before the money moves, keeps the citizen's evidence private until they consent, and turns approved evidence into shared fraud-ring intelligence for officers. The system remains useful even when the LLM or internet is unavailable."

## Simulated vs Real

- Real: FastAPI routes, PostgreSQL persistence, Alembic migration, Neo4j ingestion, ring clustering, dashboard reads.
- Real: Mit's deterministic rules, fusion, offline fallback, consent gate, deletion lifecycle, and `/api/analyze` integration.
- Simulated: Family Shield notification and any hidden-test metrics not produced from a separately held dataset.
- Privacy behavior: local-first text analysis, browser-local Whisper transcription, consent scope, automatic expiry, consent receipt, and deletion lifecycle are implemented.
- Synthetic: Seeded fraud rings and demo transcripts.
