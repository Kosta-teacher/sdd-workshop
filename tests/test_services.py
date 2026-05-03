import pytest
from unittest.mock import Mock
from todo_lib.services import ToDoService

@pytest.fixture
def mock_repo():
    """Create mock repository"""
    return Mock()

@pytest.fixture
def service(mock_repo):
    """Create service with mock repository"""
    return ToDoService(mock_repo)

def test_list_todos_service(service, mock_repo):
    """Test list service calls repository correctly"""
    mock_items = [
        Mock(id=1, title="Item 1", priority="high", completed=False, created_at=None),
        Mock(id=2, title="Item 2", priority="medium", completed=True, created_at=None)
    ]
    mock_repo.get_all.return_value = mock_items

    result = service.list_todos()

    mock_repo.get_all.assert_called_once()
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 2

def test_mark_done_service(service, mock_repo):
    """Test mark_done service calls repository correctly"""
    mock_repo.mark_done.return_value = True

    result = service.mark_todo_done(1)

    mock_repo.mark_done.assert_called_once_with(1)
    assert result == True

def test_delete_service(service, mock_repo):
    """Test delete service calls repository correctly"""
    mock_repo.delete.return_value = True

    result = service.delete_todo(1)

    mock_repo.delete.assert_called_once_with(1)
    assert result == True

def test_delete_service_not_found(service, mock_repo):
    """Test delete service when item not found"""
    mock_repo.delete.return_value = False

    result = service.delete_todo(999)

    assert result == False