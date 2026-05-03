# Data Model: Todo 관리 앱

**Date**: 2026-05-03
**Feature**: Todo 관리 앱

## Entities

### ToDoItem

**Description**: ToDo 항목을 나타내는 엔티티

**Fields**:
- `id`: 고유 식별자 (Integer, Auto-increment, Primary Key)
- `title`: 제목 (String, Optional, Max 200 chars)
- `priority`: 우선순위 (String, Optional, Enum: 'high', 'medium', 'low')
- `completed`: 완료 상태 (Boolean, Default: False)
- `created_at`: 생성 시각 (DateTime, Auto-set)
- `updated_at`: 수정 시각 (DateTime, Auto-update)

**Validation Rules**:
- `title`: 빈 문자열 허용, None 불허
- `priority`: 'high', 'medium', 'low' 중 하나 또는 None
- `completed`: Boolean 값만 허용

**Relationships**:
- 없음 (단일 엔티티)

**State Transitions**:
- Pending → Completed: `completed` 필드 True로 변경
- Completed → Pending: `completed` 필드 False로 변경 (재사용 가능)

## Database Schema

```sql
CREATE TABLE todo_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    priority TEXT CHECK (priority IN ('high', 'medium', 'low')) OR priority IS NULL,
    completed BOOLEAN DEFAULT FALSE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

## Indexes

- Primary Key on `id`
- Optional: Index on `completed` (필터링용)
- Optional: Index on `priority` (필터링용)