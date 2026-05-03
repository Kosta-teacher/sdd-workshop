# Quick Start Guide: Todo 관리 앱

**Date**: 2026-05-03
**Feature**: Todo 관리 앱

## Prerequisites

- Python 3.12+
- uv 패키지 매니저

## Installation

```bash
# Clone repository
git clone <repository-url>
cd todo-app

# Install dependencies
uv sync

# Activate virtual environment
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

## Basic Usage

### 1. Add Todo Items

```bash
# 기본 항목 추가
todo add "Buy groceries"

# 우선순위 지정
todo add "Fix bug #123" --priority high
```

### 2. List Items

```bash
# 모든 항목 조회
todo list

# 완료된 항목만
todo list --filter done

# 높은 우선순위 항목만
todo list --priority high
```

### 3. Mark as Done

```bash
# ID로 완료 표시
todo done 1
```

### 4. Delete Items

```bash
# ID로 삭제
todo delete 2
```

## Example Workflow

```bash
# 1. 항목 추가
$ todo add "Write documentation" --priority medium
Todo item added with ID: 1

# 2. 목록 확인
$ todo list
ID | Title               | Priority | Status  | Created
---|---------------------|----------|---------|---------
1  | Write documentation | medium   | Pending | 2026-05-03

# 3. 완료 처리
$ todo done 1
Todo item 1 marked as done

# 4. 완료된 항목 필터링
$ todo list --filter done
ID | Title               | Priority | Status   | Created
---|---------------------|----------|----------|---------
1  | Write documentation | medium   | Completed| 2026-05-03
```

## Data Storage

- 데이터는 `todo.db` 파일에 SQLite 형식으로 저장
- 프로젝트 루트에 자동 생성
- 수동 백업/복원 가능

## Troubleshooting

### Common Issues

1. **Command not found**: `uv sync` 실행 후 가상환경 활성화 확인
2. **Permission denied**: Windows에서 실행 권한 문제 시 관리자 권한으로 실행
3. **Database error**: `todo.db` 파일 삭제 후 재시작 (데이터 손실 주의)

### Getting Help

```bash
todo --help          # 메인 도움말
todo add --help      # add 명령어 도움말
todo list --help     # list 명령어 도움말
```