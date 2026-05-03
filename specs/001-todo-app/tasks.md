# Tasks: Todo 관리 앱

**Input**: Design documents from `/specs/001-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story. Tasks must reflect constitution principles: layer separation, test-first, minimal dependencies, simplicity, CLI focus.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `todo_lib/`, `cli/`, `tests/` at repository root
- Paths shown below follow the plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create pyproject.toml with dependencies (typer, sqlalchemy, pytest, pytest-cov)
- [ ] T002 Create project directory structure (todo_lib/, cli/, tests/)
- [ ] T003 Initialize uv project and install dependencies

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T004 Setup SQLAlchemy database configuration in todo_lib/database.py
- [ ] T005 Create ToDoItem model in todo_lib/models.py (based on data-model.md)
- [ ] T006 Create base repository class in todo_lib/repository.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - ToDo 항목 추가 (Priority: P1) 🎯 MVP

**Goal**: 사용자가 제목과 우선순위를 지정하여 ToDo 항목을 추가할 수 있음

**Independent Test**: 항목 추가 후 목록 조회 시 새 항목이 나타나는지 확인

### Tests for User Story 1 (테스트 우선)

- [ ] T007.1 [P] [US1] Write tests for add method in tests/test_repository.py
- [ ] T008.1 [US1] Write tests for add service in tests/test_services.py
- [ ] T009.1 [US1] Write tests for add CLI command in tests/test_cli.py

### Implementation for User Story 1

- [ ] T007 [P] [US1] Implement add method in todo_lib/repository.py
- [ ] T008 [US1] Implement add service in todo_lib/services.py
- [ ] T009 [US1] Implement add CLI command in cli/commands.py
- [ ] T010 [US1] Update CLI main entry point in cli/main.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - 전체목록 조회 (Priority: P2)

**Goal**: 사용자가 모든 ToDo 항목을 조회하고 완료/미완료/우선순위로 필터링할 수 있음

**Independent Test**: 항목 추가 후 필터 없이 조회 시 모든 항목 표시, 필터 적용 시 해당 항목만 표시

### Tests for User Story 2 (테스트 우선)

- [ ] T011.1 [P] [US2] Write tests for list method in tests/test_repository.py
- [ ] T012.1 [US2] Write tests for list service in tests/test_services.py
- [ ] T013.1 [US2] Write tests for list CLI command in tests/test_cli.py

### Implementation for User Story 2

- [ ] T011 [P] [US2] Implement list method in todo_lib/repository.py
- [ ] T012 [US2] Implement list service in todo_lib/services.py
- [ ] T013 [US2] Implement list CLI command in cli/commands.py
- [ ] T014 [US2] Update CLI main entry point in cli/main.py

**Checkpoint**: At this point, User Story 2 should be fully functional and testable independently

---

## Phase 5: User Story 3 - 항목 완료처리 (Priority: P3)

**Goal**: 사용자가 항목 ID로 ToDo 항목을 완료로 표시할 수 있음

**Independent Test**: 항목 추가 후 완료 처리 시 상태 변경 확인

### Tests for User Story 3 (테스트 우선)

- [ ] T015.1 [P] [US3] Write tests for mark_done method in tests/test_repository.py
- [ ] T016.1 [US3] Write tests for mark_done service in tests/test_services.py
- [ ] T017.1 [US3] Write tests for done CLI command in tests/test_cli.py

### Implementation for User Story 3

- [ ] T015 [P] [US3] Implement mark_done method in todo_lib/repository.py
- [ ] T016 [US3] Implement mark_done service in todo_lib/services.py
- [ ] T017 [US3] Implement done CLI command in cli/commands.py
- [ ] T018 [US3] Update CLI main entry point in cli/main.py

**Checkpoint**: At this point, User Story 3 should be fully functional and testable independently

---

## Phase 6: User Story 4 - 항목 삭제 (Priority: P4)

**Goal**: 사용자가 항목 ID로 ToDo 항목을 삭제할 수 있음

**Independent Test**: 항목 추가 후 삭제 시 목록에서 제거 확인

### Tests for User Story 4 (테스트 우선)

- [ ] T019.1 [P] [US4] Write tests for delete method in tests/test_repository.py
- [ ] T020.1 [US4] Write tests for delete service in tests/test_services.py
- [ ] T021.1 [US4] Write tests for delete CLI command in tests/test_cli.py

### Implementation for User Story 4

- [ ] T019 [P] [US4] Implement delete method in todo_lib/repository.py
- [ ] T020 [US4] Implement delete service in todo_lib/services.py
- [ ] T021 [US4] Implement delete CLI command in cli/commands.py
- [ ] T022 [US4] Update CLI main entry point in cli/main.py

**Checkpoint**: At this point, User Story 4 should be fully functional and testable independently

---

## Final Phase: Polish & Cross-cutting Concerns

**Purpose**: Final touches, documentation, and cross-cutting concerns

- [ ] T023 Add comprehensive error handling across all CLI commands
- [ ] T024 Add input validation for all user inputs
- [ ] T025 Create README.md with usage instructions
- [ ] T026 Add type hints throughout the codebase
- [ ] T027 Configure pytest and add basic test structure
- [ ] T028 Add logging configuration

---

## Dependencies

**Story Completion Order**:
1. US1 (P1) - ToDo 항목 추가
2. US2 (P2) - 전체목록 조회
3. US3 (P3) - 항목 완료처리
4. US4 (P4) - 항목 삭제

**Parallel Opportunities**:
- Repository methods (T007, T011, T015, T019) can be implemented in parallel
- Service methods (T008, T012, T016, T020) can be implemented in parallel after repositories
- CLI commands (T009, T013, T017, T021) can be implemented in parallel after services

**Implementation Strategy**: MVP first with US1, then incremental delivery of remaining stories. Each story is independently testable and deployable.