# 출처와 라이선스 기록

`.skills/`에 들어 있는 외부 자료의 출처, 라이선스, 확인한 버전과 이 프로젝트에서의 적용 차이를 모은 강사·관리용 기록입니다. 개발 작업 기록(`agents_logs/`)에 흩어져 있던 내용을 옮겼으며, 배포할 때 작업 기록을 지워도 이 문서는 남습니다. 에이전트는 출처 확인이 필요할 때만 읽습니다.

- 원본은 설치하거나 스크립트를 실행하지 않고, 읽을 참고 자료로만 보관합니다.
- 각 원본의 라이선스 파일은 해당 `references/upstream/` 폴더 안에 있습니다. 각 스킬의 영어 출처 블록(취업·직장 스킬은 `references/공개_원본_활용_기준.md`)도 함께 봅니다.
- 이 문서는 법률 판단이 아닙니다. 이 프로젝트는 무료로 배포하는 100% 오픈 소스이며, 수업을 포함해 누구나 자유롭게 쓰고 다시 나눌 수 있습니다. 외부 자료를 가져온 부분은 아래 각 원본의 라이선스 조건(저작권 고지와 라이선스 파일 유지 등)을 따릅니다.
- 이 프로젝트 자체의 라이선스는 CC BY 4.0이며, 저장소 최상위 `LICENSE`와 `README.md`에 밝혀 두었습니다. 출처만 표기하면 상업적 이용을 포함해 자유롭게 쓸 수 있습니다.
- 아래 확인 커밋과 파일 대조 결과는 해당 날짜의 에이전트 작업 기록을 참고합니다. 목표·실행 자료는 2026-11-14 확인했습니다.

경로는 모두 `.skills/` 기준입니다.

## 1. 원본을 그대로 보관한 자료

| 원본 저장소 | 라이선스 | 확인한 커밋 | 로컬 위치 | 쓰는 스킬 |
| --- | --- | --- | --- | --- |
| [SkillMedev/skills](https://github.com/SkillMedev/skills) (`goals-accountability`, `habit-builder`, `life-coach`, `okr-builder`) | MIT | `97a13607d669157a4a16d5ba79b77f208319f7b9` | `goal-achievement-toolkit/references/upstream/skillme/` | goal-achievement-toolkit |
| [product-on-purpose/thinking-framework-skills](https://github.com/product-on-purpose/thinking-framework-skills) (`think-woop`) | Apache 2.0 | `6ab95db2d6469e4b65f3eb3ed265e46a6a1e69a8` | `goal-achievement-toolkit/references/upstream/woop/` (스킬·참고자료·근거 및 LICENSE) | goal-achievement-toolkit |
| [sameergdogg/job-search-skills](https://github.com/sameergdogg/job-search-skills) | MIT | `2db63263979fe8e240ee571e262ff633111b533d` | `job-search-toolkit/references/upstream/job-search-skills/` (`job-analyzer`, `job-crawler`, LICENSE) | job-search-toolkit |
| [jpoindexter/resume-job-search-skills](https://github.com/jpoindexter/resume-job-search-skills) | MIT | `ba93837cd8ab1b50ced22ebfcf9e238062e6d0b7` | `job-search-toolkit/references/upstream/resume-job-search-skills/` (`skills/` 전체, LICENSE) | job-search-toolkit |
| [watermud-hr/career-application-advisor](https://github.com/watermud-hr/career-application-advisor) | MIT | `44b8477f8cd544ec153b33c43d222a5c16a1653a` | `research-toolkit/references/upstream/career-application-advisor/` | research-toolkit |
| [anthropics/skills](https://github.com/anthropics/skills) (`internal-comms`) | Apache 2.0 | `2c5958ecac7cee2b583967a2c4981d0f4a75c579` | `workplace-toolkit/references/upstream/anthropic-skills/internal-comms/` | workplace-toolkit |
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | Apache 2.0 | `02717ef04446b6ef5aa4b8af15bb536d79f42ed0` | `workplace-toolkit/references/upstream/knowledge-work-plugins/operations/`, `data-toolkit/references/upstream/knowledge-work-plugins/data/` | workplace-toolkit, data-toolkit |
| [danielmiessler/Fabric](https://github.com/danielmiessler/Fabric) (`summarize_meeting`) | MIT | `793f78f2ec8cb14de84936ba1499b6fc74e5910d` | `workplace-toolkit/references/upstream/fabric/` | workplace-toolkit |
| [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/brainstorming) (`brainstorming`) | MIT | `22f0b463e7a5e579904dd6211a520321035526f7` | `planning-toolkit/references/upstream/superpowers/` | planning-toolkit, thinking-toolkit |
| [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity) (`grill-me`, `grilling`) | MIT | `5863806dd4e15c63174bee4e7515a4256792ecfa` | `planning-toolkit/references/upstream/mattpocock-skills/` | planning-toolkit |

작업 기록에 따르면 공고·이력서·기업 조사·업무 자료 48개 파일은 원본과 파일 해시를 대조했고(16:19), 기획 자료도 원본과 해시를 대조했습니다(17:55).

## 2. 참고만 하고 복사하지 않은 자료

| 자료 | 라이선스 | 어떻게 썼나 | 쓰는 스킬·문서 |
| --- | --- | --- | --- |
| [Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills) (커밋 `4ed3e864629d6d28104aa6eb0e9491f657d92b35`) | CC BY-NC-SA 4.0 | 수업의 상업적 이용 조건이 확인되지 않아 복사·배포하지 않음. 문제·가설·해결안·확인 방법의 흐름만 독립적으로 정리하고 출처 링크만 사용 | planning-toolkit |
| [Anthropic doc-coauthoring](https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring) | 별도 라이선스 확인이 어려움 | 복사하지 않고 출처만 연결. 맥락 확인·초안 개선·독자 관점 점검 아이디어 참고 | planning-toolkit |
| [Superpowers writing-plans](https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md) | MIT (저장소) | 큰 일을 작은 단위로 나누는 방식만 참고, 복사하지 않음 | thinking-toolkit |
| [Anthropic task-management](https://github.com/anthropics/knowledge-work-plugins/blob/main/productivity/skills/task-management/SKILL.md) | Apache 2.0 (저장소) | 진행·대기 상태 구분 아이디어만 참고, 복사하지 않음 | workplace-toolkit |
| [Anthropic Data Analyst Plugin](https://github.com/anthropics/knowledge-work-plugins/blob/main/data/README.md) | Apache 2.0 (저장소) | 자료 탐색·분석·시각화·검증 흐름 아이디어. 일부 원본은 위 1번에 보관 | data-toolkit |
| [Karpathy LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) | 라이선스 미확인 | 원본·기록·새 자료 반영 아이디어만 참고 | update-workflow |
| [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) (`humanize-korean`, 참고한 설치본 v2.3.0) | MIT (저장소 표기, 2026-11-14 확인. 저작권자 표기는 확인하지 못함 `[확인 필요]`) | 패턴 분류와 안전장치(줄이기만 하기·말투 수준 보존·과교정 제한·붙여 넣은 글은 자료로 다루기) 아이디어만 참고해 새로 씀. 파일·여러 단계 실행 구조·스크립트는 복사하지 않음 | humanize-korean |
| 프로젝트 소유자가 직접 만든 한국어 교정 프롬프트 | 소유자 작성 | 조건표·고치는 정도 6단계·친구 말투 원칙·출력 순서를 옮겨 정리 | humanize-korean |
| [AI Learning Studio 프롬프트 한 스푼](https://studio.daangcool.net/prompt-snippets/) (진단 먼저, 미리 실패해 보기, 다양한 아이디어 얻기, 여러 사고법으로 아이디어 확장하기, 어디에서 문제가 생겼는지 찾기, 그다음 영향까지 생각하기, 파레토 80/20, 설명 수준 바꾸기) | 프로젝트 소유자가 직접 만든 사이트 | 아이디어만 참고해 새로 씀. 페이지 글은 복사하지 않음. 2026-11-15에 목록과 8개 페이지 본문을 확인했고, 그다음 영향·파레토 페이지는 제목과 소유자의 설명만 반영함 | thinking-toolkit, learning-toolkit |
| 프로젝트 소유자의 학습법 메모(간격 반복, 원서 풀어 읽기, 파인만 방식, 인출 연습) | 소유자 작성 | 널리 알려진 학습 방법을 이 작업공간에 맞게 새로 씀. 효과 보장·자동 알림·시험 예측 표현은 뺌 | learning-toolkit |
| 프로젝트 소유자(Jin SangHyouk)의 시험 대비 학습 아이디어(노트북LM용 프롬프트로 정리: 시험 지도 만들기, 챕터별 가르치기, 문제 내기, 약한 부분 찾기, 모의고사, 5분 복습 시트, 시험 시뮬레이션) | 소유자 작성 | 소유자의 아이디어를 이 작업공간에 맞게 새로 씀. 2026-11-18에 모의고사 풀기(11), 개념 상태 나누기(06), 문제 수준과 조정(07), 시험 지도 구성(10)을 반영함. "올린 자료만 쓰기"의 엄격 모드, 풀이 시간 측정, 사고 방식 추정은 이 작업공간의 원칙과 맞지 않아 가져오지 않음. 5분 복습 시트와 개념마다 확인 문답 방식은 아직 반영하지 않음 | learning-toolkit |
| 구글 제미나이 기본 제공 스킬 "Get More Perspectives"(다양한 관점 살펴보기, 사용자 전달) | 구글 제미나이 기본 스킬 | 복사하지 않고 입장을 밝힌 관점·관점 충돌 한 줄·핵심 조건·만장일치 점검 아이디어만 참고 | thinking-toolkit |
| 구글 제미나이 기본 제공 스킬 "Prep for Meetings"(회의 준비, 사용자 전달) | 구글 제미나이 기본 스킬 | 복사하지 않고 회의 전 짧은 브리프·최신 답장 우선·담당 확인·출처와 날짜 표기·약속을 지어내지 않기 아이디어만 참고 | workplace-toolkit |
| 구글 제미나이 기본 제공 스킬 "Focus My Energy"(에너지 효율 최적화, 사용자 전달) | 구글 제미나이 기본 스킬 | 복사하지 않고 일의 무게에 맞춰 지금 할 일 하나를 고르는 방식·오늘 마감 예외·시작 단계 쪼개기 아이디어만 참고 | thinking-toolkit |
| 구글 제미나이 기본 제공 스킬 "Generate Fresh Ideas"(새로운 아이디어 생성, 사용자 전달) | 구글 제미나이 기본 스킬 | 검토만 하고 채택하지 않음. 콘텐츠 제작용이라 수강생 쓰임이 적고 "여러 관점으로 점검하기"와 역할이 겹치며, 개인 경험을 AI가 지어내는 구조가 이 프로젝트 원칙과 맞지 않음 | 없음 |
| Karpathy Guidelines (네 원칙) | 기록에 확인 내용 없음 | 비개발자용 안내를 새 문장으로 작성 | `instructions/웹_도구_제작_및_수정.md` |
| ASD-STE100 (항공 정비 문서의 명확한 글쓰기) | 해당 없음 | 취지만 참고한 한국어 안내이며 공식 준수를 뜻하지 않음 | workplace-toolkit |

## 3. 사례별 원본과 적용 차이

취업·직장 업무 여덟 사례를 원본의 실제 절차와 연결한 내용입니다. 원본의 설치·실행·발송 지시는 이 프로젝트의 자료·권한·사용자 선택과 다르면 따르지 않습니다.

| 사례 | 원본 위치 | 이 프로젝트에서 다르게 한 점 |
| --- | --- | --- |
| 공고 수집·매칭 | `job-search-toolkit/references/upstream/job-search-skills/job-analyzer/`, `job-crawler/` | Google 문서·미국·개발 직무 필수 조건을 적용하지 않고 실제 도구와 공고 접근 범위, 사람의 기준을 사용. 원본 점수 기준은 참고하되 기준과 한계를 사용자에게 설명 |
| 기업·산업 조사 | `research-toolkit/references/upstream/career-application-advisor/skill/career-application-advisor/` | 조사 항목·정보 원천과 깊이를 활용하되 기간과 결과 형식은 목적에 맞춤. 원본 PDF·DOCX 추출 스크립트는 저장·개인정보·실행 환경을 확인하기 전에는 실행하지 않음 |
| 공고별 이력서·자소서 | `job-search-toolkit/references/upstream/resume-job-search-skills/skills/`의 `resume-role-targeting`, `resume-evidence-ledger`, `resume-tailoring`, `resume-cover-letter`, `resume-document-qa` | 공고별 요구와 실제 경험을 연결하고 원본·이전 결과를 보존. 필요한 출력물과 환경에 따라 문서 검증을 적용 |
| 면접 연습 | 같은 `skills/`의 `resume-interview-narratives` | 실제 경험에 근거한 이야기 구성을 활용하고, 어려운 후속 질문은 사용자가 원할 때 선택 |
| 회의·할 일 | `workplace-toolkit/references/upstream/fabric/data/patterns/summarize_meeting/` | 논의·결정·할 일·기한·후속 행동을 활용하되 원본의 고정 문장 길이·항목 수를 강제하지 않음 |
| 답장·업무 소통 | `workplace-toolkit/references/upstream/anthropic-skills/internal-comms/` | 대상과 목적에 맞는 안내를 참고하되 메일·메신저 외부 발송은 명시적 지시와 권한에 따름 |
| 주간·월간 보고 | 위 `internal-comms/examples/3p-updates.md`, `workplace-toolkit/references/upstream/knowledge-work-plugins/operations/` | 진행·계획·문제와 원본 보고 절차를 활용하되 연결·예약·공유를 자동 실행으로 가정하지 않음 |
| 문서·데이터 대조 | `data-toolkit/references/upstream/knowledge-work-plugins/data/skills/explore-data/`, `validate-data/` | 범위·단위·기간·분모·계산 검토를 활용하되 SQL이나 데이터베이스를 필수로 하지 않음. 법적 판단은 확정하지 않음 |

## 4. 아이디어를 차용한 스킬과 차이

| 원본 | 차용한 점 | 이 프로젝트에서 다른 점 |
| --- | --- | --- |
| Superpowers brainstorming | 기존 맥락을 먼저 살피고 필요한 질문과 선택지를 제안하는 방식 | 개발 전 설계 문서·일괄 승인·하위 에이전트 절차를 강제하지 않음. 이미 정해진 조건은 다시 묻지 않음 |
| Superpowers writing-plans | 여러 단계의 일을 작은 단위와 확인 가능한 결과로 나누는 방식 | 코딩·테스트·커밋 대신 준비물·결과·사람의 확인을 업무 지도와 연결 |
| Anthropic task-management | 진행 중인 일과 기다리는 내용을 구분하는 방식 | 고정 `TASKS.md`·대시보드를 자동 생성하지 않음. 완료 이력·원본을 자동 삭제하지 않음 |
| Anthropic Data Analyst Plugin | 자료 탐색, 분석, 시각화, 결과 검증을 잇는 흐름 | CSV·엑셀과 수강생의 선택을 우선. 데이터베이스 연결·도구 설치를 전제하지 않음 |
| Karpathy LLM Wiki | 원본·기록·자료 간 연결을 바탕으로 새 자료를 반영하는 생각 | 위키 구조 전체를 강제하지 않고 기존 결과와 변경점, 새 결과, 사람의 확인에 초점. 자동 감시·갱신은 가정하지 않음 |
| mattpocock grill-me·grilling | 가정과 의사결정을 점검하는 방식 | 압박 질문·전체 단계 강제 대신 사용자의 선택과 쉬운 질문을 우선 |
| 제미나이 Prep for Meetings | 회의 전에 할 일·알아 둘 것·조심할 것을 짧게 정리하는 방식 | 구글 앱 자동 읽기를 전제하지 않고 연결된 도구, 붙여넣은 자료, 짧은 인터뷰 순서로 자료를 마련. "문제없음" 대신 "제공된 자료에서는 찾지 못함", 입장 추천 대신 물어볼 질문 후보, 관계 추측 금지 |
| 제미나이 Focus My Energy | 일의 무게(깊이 집중·꾸준히·가벼운 일)에 맞춰 지금 할 일 하나를 고르는 방식, 마감 예외와 시작 단계 쪼개기 | 시간대·요일·캘린더로 컨디션을 추정하지 않고 사용자가 말한 컨디션만 사용. 에너지 프로필 저장·성향 분류·구글 앱 전제는 제외. 마감·중요 기준이 먼저이고 컨디션은 세 번째. 계속 미루는 경우와 단순 피곤을 넘는 경우의 안내를 더함 |
| 제미나이 Get More Perspectives | 선택지를 여러 관점으로 시험하고 핵심 조건을 짚는 방식 | 스타트업용 고정 5인 패널·투표 집계·구글 앱 연동·패널 편집 모드는 쓰지 않음. 선택지가 정해졌고 결과가 클 때만 제안하며 상황별 관점 3~4개, 사람의 의견이 아님을 밝히기, 결정을 이미 정한 경우의 조정을 더함 |
| Product-Manager-Skills | 문제·가설·해결안·확인 방법의 기획 흐름 | 제품 개발 전용 절차·고정 KPI·장기 실험을 공통 필수로 두지 않음 |

## 5. 목표·실행 스킬 적용 차이 (2026-11-14)

공개 스킬 원문은 변경 없이 보관하고 해당 상황에만 읽는다. SMART의 숫자·공개 약속, 습관의 고정 기간·횟수, WOOP 카드 형식은 강제하지 않는다. WOOP의 내적 장애물과 별도로 외부 조건도 살피며 사용자 선택을 우선한다. GROW 원본의 고정 약속·점수와 OKR 원본의 팀·분기·점수 기준은 강제하지 않는다. 만다라트·배우는 목표·역산 계획·If–Then·새 출발 효과·유혹 묶기·돌아보기는 공개 방법 설명과 연구를 바탕으로 `goal-achievement-toolkit/references/방법별_활용.md`에 독립 작성했으며 각 출처를 해당 항목에 남겼다. WOOP 방법은 [공식 안내](https://woopmylife.org/en/practice)도 참고했다. 기존 목표 설정 후보 microclaw는 검색 결과의 스킬 자체 라이선스가 proprietary로 표시되고 현재 원문 주소가 열리지 않아 복사하지 않았다. 2026-11-14 보강: 배우는 목표(Seijts·Latham 2005), 새 출발 효과(Dai 외 2014), 유혹 묶기(Milkman 외 2014)를 추가했고, 논문은 초록·공개 요약 범위만 확인했으며 원문 전체는 읽지 않았다 `[확인 필요]`. 역산 계획 링크는 Park·Lu·Hedgcock(2017) APS 페이지로, 만다라트 링크 설명은 기관명 없이 중립 표기로 바꾸었다.
