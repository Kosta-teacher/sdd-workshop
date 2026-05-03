# CLI Interface Contract

**Date**: 2026-05-03
**Feature**: Todo 관리 앱
**Type**: Command Line Interface

## Command Structure

### Base Command
```bash
todo [OPTIONS] COMMAND [ARGS]...
```

### Commands

#### 1. Add Todo Item
```bash
todo add "<title>" [--priority {high,medium,low}]
```

**Parameters**:
- `title`: Todo 제목 (필수, 따옴표로 묶음)
- `--priority`: 우선순위 (선택, high/medium/low)

**Response**: 성공 시 "Todo item added with ID: {id}" 출력

**Error Cases**:
- 제목 누락: "Error: Missing title"
- 잘못된 우선순위: "Error: Invalid priority value"

#### 2. List Todo Items
```bash
todo list [--filter {done,pending}] [--priority {high,medium,low}]
```

**Parameters**:
- `--filter`: 완료 상태 필터 (선택, done/pending)
- `--priority`: 우선순위 필터 (선택, high/medium/low)

**Response**: 테이블 형식으로 항목 목록 출력
```
ID | Title | Priority | Status | Created
---|-------|----------|--------|---------
1  | Buy milk | high    | Pending| 2026-05-03
```

#### 3. Mark Todo as Done
```bash
todo done <id>
```

**Parameters**:
- `id`: Todo 항목 ID (필수, 정수)

**Response**: 성공 시 "Todo item {id} marked as done"

**Error Cases**:
- ID 누락: "Error: Missing ID"
- 존재하지 않는 ID: "Error: Todo item not found"

#### 4. Delete Todo Item
```bash
todo delete <id>
```

**Parameters**:
- `id`: Todo 항목 ID (필수, 정수)

**Response**: 성공 시 "Todo item {id} deleted"

**Error Cases**:
- ID 누락: "Error: Missing ID"
- 존재하지 않는 ID: "Error: Todo item not found"

## Exit Codes

- 0: 성공
- 1: 일반 오류 (잘못된 입력, 항목 없음)
- 2: 시스템 오류 (DB 연결 실패 등)

## Data Formats

### Input Validation
- Title: 최대 200자, 특수문자 허용
- Priority: 정확히 'high', 'medium', 'low' 또는 생략
- ID: 양의 정수

### Output Format
- 성공 메시지: 영어 텍스트
- 오류 메시지: "Error: {description}" 형식
- 목록: 마크다운 테이블 형식