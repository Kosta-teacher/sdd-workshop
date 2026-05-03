import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from todo_lib.database import Base
from todo_lib.models import ToDoItem
from todo_lib.repository import ToDoRepository

@pytest.fixture
def test_db():
    """Create in-memory test database"""
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture
def repo(test_db):
    """Create repository with test database"""
    return ToDoRepository(test_db)

def test_add_todo_item(repo):
    """Test adding a todo item"""
    item = repo.add(title="Test todo", priority="high")

    assert item.id is not None
    assert item.title == "Test todo"
    assert item.priority == "high"
    assert item.completed == False

def test_add_todo_item_without_priority(repo):
    """Test adding a todo item without priority"""
    item = repo.add(title="Test todo")

    assert item.id is not None
    assert item.title == "Test todo"
    assert item.priority is None
    assert item.completed == False

def test_get_all_todo_items(repo):
    """Test getting all todo items"""
    # Add some items
    repo.add(title="Item 1", priority="high")
    repo.add(title="Item 2", priority="medium")

    items = repo.get_all()

    assert len(items) == 2
    assert items[0].title == "Item 1"
    assert items[1].title == "Item 2"

def test_get_by_id_existing(repo):
    """Test getting todo item by existing ID"""
    item = repo.add(title="Test item")
    found = repo.get_by_id(item.id)

    assert found is not None
    assert found.id == item.id
    assert found.title == "Test item"

def test_mark_done_existing_item(repo):
    """Test marking existing item as done"""
    item = repo.add(title="Test item")
    assert not item.completed

    result = repo.mark_done(item.id)

    assert result == True
    updated_item = repo.get_by_id(item.id)
    assert updated_item.completed == True

def test_delete_existing_item(repo):
    """Test deleting existing item"""
    item = repo.add(title="Test item")
    item_id = item.id

    result = repo.delete(item_id)

    assert result == True
    # Verify item is gone
    found = repo.get_by_id(item_id)
    assert found is None

def test_delete_nonexistent_item(repo):
    """Test deleting nonexistent item"""
    result = repo.delete(999)

    assert result == False