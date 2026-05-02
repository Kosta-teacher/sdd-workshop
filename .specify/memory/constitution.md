<!-- Sync Impact Report
Version change: N/A → 1.0.0
List of modified principles: Added all 5 principles (레이어분리, 테스트우선, 최소 의존성, 단순함 우선, CLI도구 구현)
Added sections: Additional Constraints, Development Workflow
Removed sections: None
Templates requiring updates: plan-template.md (Constitution Check), spec-template.md (no changes), tasks-template.md (task categorization)
Follow-up TODOs: None
-->
# ToDo 관리 앱 Constitution

## Core Principles

### I. 레이어분리
비즈니스 로직은 사용자 인터페이스와 분리된 독립 레이어에서 구현한다.

### II. 테스트우선
테스트 코드가 구현 코드 보다 먼저 작성된다. 테스트 없는 구현 코드는 허용하지 않는다.

### III. 최소 의존성
외부 패키지 설치 전 반드시 필요성을 검토한다. 불필요한 의존성은 추가하지 않는다.

### IV. 단순함 우선
지금 당장 필요하지 않는 추상화 레이어는 만들지 않는다. 명확하고 직접적인 구현을 선호한다.

### V. CLI도구 구현
이 프로젝트는 터미널 CLI도구를 만든다. REST API 서버, GUI, 웹 인터페이스는 이 프로젝트의 범위 밖이다.

## Additional Constraints

Technology stack requirements: Python 기반 CLI 도구, 최소 의존성 준수.

Compliance standards: 테스트 우선 개발, 레이어 분리.

Deployment policies: 터미널 CLI로 배포.

## Development Workflow

Code review requirements: 모든 코드에 테스트 포함.

Testing gates: 테스트 없는 코드는 승인되지 않음.

Deployment approval process: CLI 도구로서의 기능 검증.

## Governance

Constitution supersedes all other practices; Amendments require documentation, approval, migration plan

All PRs/reviews must verify compliance; Complexity must be justified; Use [GUIDANCE_FILE] for runtime development guidance

**Version**: 1.0.0 | **Ratified**: 2026-05-02 | **Last Amended**: 2026-05-02
