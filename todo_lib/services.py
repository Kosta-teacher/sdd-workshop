from .repository import ToDoRepository

class ToDoService:
    def __init__(self, repo: ToDoRepository = None):
        self.repo = repo or ToDoRepository()

    def add_todo(self, title: str = None, priority: str = None) -> dict:
        """Add a new todo item and return result"""
        item = self.repo.add(title=title, priority=priority)
        return {
            "id": item.id,
            "title": item.title,
            "priority": item.priority,
            "completed": item.completed
        }

    def list_todos(self, filter_status=None, priority=None) -> list[dict]:
        """List todo items with optional filters"""
        items = self.repo.get_all()

        # Apply filters
        if filter_status == "done":
            items = [item for item in items if item.completed]
        elif filter_status == "pending":
            items = [item for item in items if not item.completed]

        if priority:
            items = [item for item in items if item.priority == priority]

        return [{
            "id": item.id,
            "title": item.title,
            "priority": item.priority,
            "completed": item.completed,
            "created_at": item.created_at
        } for item in items]

    def mark_todo_done(self, item_id: int) -> bool:
        """Mark todo item as done"""
        return self.repo.mark_done(item_id)

    def delete_todo(self, item_id: int) -> bool:
        """Delete todo item"""
        return self.repo.delete(item_id)