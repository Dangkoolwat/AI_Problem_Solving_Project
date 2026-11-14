# 작업 색인

새 대화에서 에이전트가 가장 먼저 읽는 파일입니다. 작업 하나가 한 줄입니다.

- 작업이 생기거나 상태가 바뀔 때만 해당 줄을 고칩니다. 새 작업은 표 맨 아래에 줄을 추가합니다.
- 상태는 `진행 중`, `완료`, `보류` 중에서 적습니다.
- 개인정보와 자료 본문은 적지 않고 경로와 요약만 적습니다.
- `완료` 항목이 10줄을 넘으면 오래된 것부터 `INDEX_보관.md`로 옮기고 표 아래에 보관 건수를 한 줄 남깁니다. `진행 중`·`보류`는 옮기지 않습니다.

| 작업명 | 상태 | 마지막 날짜 | 결과 위치 | 로그 위치 | 다음 행동 |
| --- | --- | --- | --- | --- | --- |
| 문서(docs) 정리와 대안 제시 지침 보강 | 완료 | 2026-11-15 | docs/00_시작하기.md, docs/01_사례집.md, docs/cases/(34개), docs/reference/(5개), AGENTS.md(4·8절), instructions/문제해결_과정.md, instructions/워크플로우_구성과_재사용.md, instructions/방법_메뉴.md, .skills/humanize-korean/, .skills/thinking-toolkit/, .skills/learning-toolkit/, 취업·직장 상황별 안내 14개 | agents_logs/2026-11-14-Claude-Fable-5.2/progress-log.md | 사례 요청문 실제 시험, 시험 키트 기준선 측정, 수강생 배포 전 색인 비우기 |
