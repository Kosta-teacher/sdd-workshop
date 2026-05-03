# Research Findings: Todo 관리 앱

**Date**: 2026-05-03
**Feature**: Todo 관리 앱
**Context**: 터미널 CLI 도구, Python 3.12, SQLite 저장소

## Performance Goals

**Decision**: 10개 항목 추가 시 5초 이내 완료 (스펙 기반)

**Rationale**: 스펙의 Success Criteria에서 "사용자가 10개의 ToDo 항목을 5초 이내에 추가할 수 있음"으로 명시. CLI 도구로서의 응답성 보장.

**Alternatives considered**:
- 1초 이내: 너무 엄격, SQLite I/O 오버헤드 고려 시 비현실적
- 10초 이내: 사용자 경험 저하 가능성

## Memory Constraints

**Decision**: 메모리 사용량 100MB 이하

**Rationale**: 개인용 CLI 도구로서 메모리 효율성 중요. SQLite는 인메모리 캐시 제한으로 메모리 사용량 예측 가능.

**Alternatives considered**:
- 50MB 이하: 1000개 항목 관리 시 SQLite 캐시로 인한 제한 초과 가능성
- 200MB 이하: 불필요한 여유, 메모리 누수 위험 증가

## Technology Choices

**Decision**: typer + sqlalchemy 조합 사용

**Rationale**: typer는 CLI 구축에 최적화, sqlalchemy는 SQLite ORM으로 안정적. 최소 의존성 원칙 준수.

**Alternatives considered**:
- click + sqlite3: 직접 SQL 사용으로 복잡성 증가
- argparse + pony.orm: pony.orm은 추가 의존성, argparse는 CLI UX 저하

## Best Practices

**Decision**: pytest-cov로 단위/통합 테스트 커버리지 80% 이상 목표

**Rationale**: 테스트 우선 원칙 준수. CLI 도구의 신뢰성 보장.

**Alternatives considered**:
- unittest: pytest보다 덜 유연
- 100% 커버리지: 유지보수 비용 증가