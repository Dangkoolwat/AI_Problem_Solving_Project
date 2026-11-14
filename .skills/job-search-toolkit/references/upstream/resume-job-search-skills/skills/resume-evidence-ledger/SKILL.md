---
name: resume-evidence-ledger
description: Build or audit the factual source of truth for resume and application claims. Use before generating materials from multiple resumes, notes, portfolios, transcripts, or work artifacts, and whenever metrics, titles, dates, ownership, or credentials could be overstated.
---

# Resume Evidence Ledger

## Ledger schema

For every usable claim, record:

```text
Claim ID:
Employer / project:
Official title and dates:
Candidate contribution:
Outcome and metric:
Evidence source:
Confidence: verified | reported | inferred | unknown
Allowed wording:
Forbidden wording:
```

## Procedure

1. Prefer primary artifacts, official records, existing factual resumes, and direct user corrections.
2. Reconcile conflicts in dates, titles, metrics, and ownership; never pick the more impressive version by default.
3. Split team outcomes from individual contribution. “The product produced X” does not prove “I produced X.”
4. Mark estimates or ranges explicitly and use them only with the user's approval.
5. Create a do-not-claim list for unsupported domains, credentials, direct reports, tools, or research ownership.
6. Lock the ledger before drafting. New language must map back to a claim ID.

## Guardrails

- Never fabricate, interpolate, or silently round a metric.
- Never convert collaboration into ownership or project leadership into people management.
- Never present an internal or translated title as an earned promotion.
- If evidence is missing, ask for it or omit the claim.
