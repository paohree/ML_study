# Agent & Harness 실습 프로젝트

## 목표
ML 스터디 세션을 자동화하고, 역할 분리된 멀티에이전트 구조로 만들어보기.
개념을 직접 손으로 만들어보는 실습.

---

## 하고 싶은 것

### 1. Harness — 자동화
지금은 Claude가 판단해서 하는 것들을 강제 자동화.

| 시점 | 자동화할 것 |
|---|---|
| 세션 시작 | 진행상황.md 자동 로드 |
| md 파일 수정 후 | git add + commit 자동 실행 |
| 세션 종료 | git push 자동 실행 |

→ `settings.json`에 hooks 설정으로 구현

### 2. 멀티에이전트 — 역할 분리
지금은 Claude가 수업 + 평가 + 기록을 혼자 다 함.
역할을 나눠보기:

- **수업 AI** — 소크라테스식 수업 진행
- **평가 AI** — 퀴즈 채점 + 약점 분석 + 진행상황.md 업데이트
- (선택) **기록 AI** — 수업 내용 정리해서 날짜별 md 파일 작성

---

## 어떻게 구현하나

### Harness
1. `~/.claude/settings.json` 또는 프로젝트 `.claude/settings.json` 열기
2. `hooks` 항목에 lifecycle 이벤트별 쉘 명령어 추가
3. 테스트: md 파일 수정 후 자동 commit 되는지 확인

참고: hooks 이벤트 종류
- `PreToolUse` — 툴 실행 전
- `PostToolUse` — 툴 실행 후
- `Stop` — 세션 종료 시

### 멀티에이전트
1. CLAUDE.md에 각 에이전트 역할 정의
2. Claude Code의 Agent 툴로 서브에이전트 호출 구조 설계
3. 수업 AI → 퀴즈 결과 → 평가 AI → 진행상황.md 업데이트 흐름 만들기

---

## 순서
1. Harness 먼저 (더 간단, 효과 바로 보임)
2. 멀티에이전트는 Harness 이후

---

## 참고
- hooks 설정: `update-config` 스킬 사용
- 에이전트 구조: Claude Code Agent 툴 문서
