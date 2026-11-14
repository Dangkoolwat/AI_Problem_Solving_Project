---
name: evidence-check
description: 보고서·회의 기록·표 자료 등 여러 자료의 핵심 주장과 수치를 서로 대조하고 확인할 차이를 정리합니다.
---

# 문서와 자료 대조하기

표 자료의 계산이나 분석 결과를 대조할 때는 `.skills/data-toolkit/references/upstream/knowledge-work-plugins/data/skills/validate-data/SKILL.md`의 원본 절차와 점검 항목을 읽고, 실제 자료에 적용 가능한 부분을 활용한다. 문서 간 사실과 수치의 대조에는 아래 과정을 함께 따른다.

사용자가 확인하려는 주장·수치·결정 사항과 비교할 자료를 먼저 파악한다. 확인 대상이 모호하면 필요한 질문을 하고, 조건이 분명하면 바로 진행한다. 자료가 없거나 접근·저장할 수 없으면 해당 비교를 보류하고 가능한 대안을 알린다. `instructions/자료_마련과_저장.md`에 따라 원본과 분석 자료를 구분하고 분석 전 `data/` 저장과 읽기 가능 여부를 확인한다.

## 확인하기

- 실제 읽을 수 있는 자료와 범위, 출처·날짜·위치를 기록한다. PDF의 표·이미지나 엑셀의 수식·값을 읽지 못했으면 그 한계를 명시한다.
- 사용자가 중요하게 여기는 항목부터 대조한다. 수치는 기간·단위·범위·계산 기준을, 결정 사항은 제안·논의·확정 여부와 시점을 함께 살핀다. 비교 기준이 다른 자료를 같은 값처럼 다루지 않는다.
- 결과를 **확인한 범위에서 일치 / 차이 발견 / 비교·확인 필요**로 나누고 양쪽 근거 위치와 차이의 내용을 표시한다. 원인이 확인되지 않은 차이는 오류나 거짓으로 단정하지 않는다. 확인할 수 없는 부분은 `[확인 필요]`로 남긴다.
- 오탈자나 논리적 빈틈이 요청 범위에 있으면 근거를 붙여 제안한다. 계약서 등 법률 문서는 확인할 조항과 질문을 정리할 수 있으나 법적 효력이나 위험을 확정하지 않고 필요한 경우 전문가 검토를 안내한다.
- 사용자가 원문과 중요한 수치·문맥을 직접 확인하도록 돕는다. 결과는 저장 지침에 따라 `outputs/`에 남기고 원본을 보존한다. AI의 비교는 사람이 확인했다는 뜻이 아니다. 새 자료를 반영할 때는 `.skills/update-workflow/SKILL.md`를 참고한다.

**Source attribution and license** (for the upstream material, not a license declaration for this local skill): [anthropics/knowledge-work-plugins: validate-data](https://github.com/anthropics/knowledge-work-plugins/tree/main/data/skills/validate-data), Apache License, Version 2.0. Its analysis validation workflow is preserved with the [original license](../data-toolkit/references/upstream/knowledge-work-plugins/data/LICENSE) in `data-toolkit`. This local skill adapts applicable checks to comparison across documents and data.
