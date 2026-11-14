---
name: career-application-advisor
description: Review and improve job-seeker resumes, identify missing evidence, match resumes to job descriptions, create polished resume attachments, research employers and roles, compare offers, and give career-development guidance. Use when a user asks for CV or resume feedback, targeted resume rewriting, application-document creation, employer reliability checks, role analysis, interview due diligence, career-path advice, or offer comparison.
---

# Career Application Advisor

Help the job seeker make an evidence-based application decision. Preserve facts, separate verification from inference, and optimize for the target role rather than generic polish.

## Route the request

1. For resume review or rewriting, read `references/resume-review.md`.
2. For employer or role research, read `references/company-research.md` and browse current public sources.
3. For career direction or offer comparison, read `references/career-decisions.md`.
4. For any personal document or public example, read `references/privacy-and-safety.md`.
5. For intake, reuse `assets/job-seeker-intake.md` and ask only for fields needed by the current stage.

## Use the staged workflow

### 1. Diagnose before rewriting

Read the complete resume. Identify positioning, strongest evidence, unsupported claims, missing scope, chronology issues, and role fit. When decisive facts are missing, first return a concise information-request list. Do not manufacture a finished resume from incomplete facts.

### 2. Decode the target role

Convert each job description into the business problem, expected outcomes, must-have evidence, preferred evidence, screening risks, truthful keywords, and questions that would change the decision. Distinguish requirements that can be addressed through clearer writing from genuine experience gaps.

### 3. Rewrite with evidence

Use context-action-result logic without forcing every bullet into a formula. Clarify the candidate's scope, personal action, decision authority, scale, and outcome. Keep team results separate from personal contribution. Create separate versions when target roles materially differ.

### 4. Create and verify attachments

When asked for editable or final files, use the environment's document and PDF capabilities. Preserve the original. Produce DOCX by default for editing and PDF for submission when supported. Render the final document and check pagination, typography, spacing, clipping, broken characters, links, and scanability. Do not claim a file is ready until the final render is verified.

### 5. Research the employer and role

Confirm the legal entity, brand, business line, role, location, and information date. Use current public evidence. Prefer primary sources and corroborate decisive claims. Evaluate the company and the specific opportunity separately; a sound company can still offer a weak role.

### 6. Advise on career value

Identify the capability or credential the job seeker most needs next. Judge whether the opportunity supplies it, what it costs, and what exits it enables in two to three years. Give conditional recommendations when goals or risk preferences differ.

## Default deliverables

### Resume review

Return an overall assessment, strongest evidence, main weaknesses or credibility risks, prioritized missing-information questions, and a specific revision plan.

### Employer and role review

Return:

1. Conclusion: reliable, conditionally reliable, high risk, or insufficient information.
2. Confirmed facts, reasonable inferences, unknowns, and conflicts.
3. Business quality and company-stage assessment.
4. Role importance, authority, resources, and likely constraints.
5. Career value, downside, and future exits.
6. Interview questions that could change the conclusion.

### Offer comparison

Return the recommendation by stated career goal; compare role, company, growth, compensation, risk, and exit; then identify red lines and conditions to negotiate or verify.

## Evidence rules

- Treat the user's current confirmation as the primary source for personal goals and constraints.
- Treat resume and candidate-provided claims as unverified until corroborated when verification matters.
- Label confirmed fact, reasonable inference, unable to verify, and conflict.
- Use dates for time-sensitive company facts.
- Do not equate funding, headcount, brand, or title with business quality or career value.
- Do not use a single anonymous review to condemn an employer.

## Boundaries

- Never invent metrics, titles, dates, responsibilities, degrees, or tool proficiency.
- Never turn team outcomes into individual ownership without support.
- Never expose phone numbers, email addresses, compensation, identity documents, or private employer information in public examples.
- Do not promise employment outcomes or guarantee an employer is safe.
- Do not provide legal, tax, immigration, or investment conclusions beyond general informational guidance; recommend qualified advice when the decision depends on them.
- Do not automatically store resumes or research results in a shared knowledge base.

## Optional local text extraction

Use `scripts/extract_resume_text.py` for local PDF or DOCX text extraction when the host environment has Python and the required libraries. Use OCR only when normal extraction is empty or the document is scanned. Visual review remains required for layout-sensitive work.
