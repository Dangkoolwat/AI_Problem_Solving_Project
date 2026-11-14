---
name: resume
description: Route resume tailoring and job-search work to the smallest relevant set of evidence-safe skills. Use when the user invokes /resume or $resume, asks for end-to-end application help, or has a broad resume, LinkedIn, application, interview, compensation, or employer-evaluation task.
---

# Resume and Job-Search Router

Turn the request into an application decision or artifact, then route it to one primary skill and no more than three companions.

## Route

1. Capture the target role, company, supplied evidence, requested output, constraints, and acceptance test. Mark missing facts as unknown.
2. Choose the primary route below. Add companions only when their output is required.
3. Read the selected sibling `SKILL.md` files before acting.
4. Execute the leaf workflows. Do not return a framework catalog when an artifact was requested.
5. End with the artifact or decision, claim boundaries, verification performed, and the next application action.

| Intent | Primary skill | Typical companions |
|---|---|---|
| Understand a posting or decide whether to apply | `resume-role-targeting` | `resume-application-strategy` |
| Build or audit the factual source | `resume-evidence-ledger` | — |
| Tailor a resume | `resume-tailoring` | `resume-evidence-ledger`, `resume-impact-bullets`, `resume-document-qa` |
| Rewrite achievement bullets | `resume-impact-bullets` | `resume-evidence-ledger` |
| Explain a gap, pivot, layoff, title, or short stint | `resume-risk-framing` | `resume-evidence-ledger` |
| Check parsing or fast-scan readability | `resume-ats-readability` | `resume-document-qa` |
| Align LinkedIn | `resume-linkedin-alignment` | `resume-evidence-ledger` |
| Plan applications, outreach, or follow-up | `resume-application-strategy` | `resume-role-targeting` |
| Write a cover letter | `resume-cover-letter` | `resume-role-targeting`, `resume-evidence-ledger` |
| Prepare interview stories | `resume-interview-narratives` | `resume-role-targeting`, `resume-evidence-ledger` |
| Handle salary expectations or an offer | `resume-compensation` | `resume-role-targeting` |
| Evaluate a manager or team | `resume-employer-due-diligence` | — |
| Export or verify DOCX/PDF | `resume-document-qa` | `resume-evidence-ledger` |

## Non-negotiable evidence policy

- Never invent or silently round metrics, dates, employers, education, credentials, language ability, reporting lines, management scope, tools, or outcomes.
- A translated title is allowed only when it accurately describes the verified work and does not inflate level; retain the official title in the evidence ledger.
- Preserve reverse chronology unless the user explicitly asks for another structure.
- Tailoring selects and translates evidence. It does not manufacture fit.
- Distinguish `executed`, `code-path`, and `assumed` verification. Only executed end-to-end checks prove delivery.
