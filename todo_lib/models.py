from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from .database import Base

class ToDoItem(Base):
    __tablename__ = "todo_items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=True)
    priority = Column(String, nullable=True)  # 'high', 'medium', 'low'
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<ToDoItem(id={self.id}, title='{self.title}', priority='{self.priority}', completed={self.completed})>"