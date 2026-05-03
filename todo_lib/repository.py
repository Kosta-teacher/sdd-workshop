from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import ToDoItem

class ToDoRepository:
    def __init__(self, db: Session = None):
        self.db = db or SessionLocal()

    def add(self, title: str = None, priority: str = None) -> ToDoItem:
        """Add a new todo item"""
        item = ToDoItem(title=title, priority=priority)
        self.db.add(item)
        self.db.commit()
        # Get the item back since refresh might not work with RETURNING
        return self.db.query(ToDoItem).filter(ToDoItem.id == item.id).first()

    def get_all(self) -> list[ToDoItem]:
        """Get all todo items"""
        return self.db.query(ToDoItem).all()

    def get_by_id(self, item_id: int) -> ToDoItem | None:
        """Get todo item by ID"""
        return self.db.query(ToDoItem).filter(ToDoItem.id == item_id).first()

    def mark_done(self, item_id: int) -> bool:
        """Mark todo item as done"""
        item = self.get_by_id(item_id)
        if item:
            item.completed = True
            self.db.commit()
            return True
        return False

    def delete(self, item_id: int) -> bool:
        """Delete todo item"""
        item = self.get_by_id(item_id)
        if item:
            self.db.delete(item)
            self.db.commit()
            return True
        return False