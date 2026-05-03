import pytest
from unittest.mock import Mock
from typer.testing import CliRunner
from cli.main import app

@pytest.fixture
def runner():
    """Create CLI runner"""
    return CliRunner()

def test_add_command(runner):
    """Test add CLI command"""
    result = runner.invoke(app, ["add", "Test todo", "--priority", "high"])

    assert result.exit_code == 0
    assert "Todo item added with ID:" in result.output

def test_list_command(runner):
    """Test list CLI command"""
    result = runner.invoke(app, ["list"])

    assert result.exit_code == 0
    # Should show header even with no items
    assert "ID" in result.output
    assert "Title" in result.output

def test_delete_command(runner):
    """Test delete CLI command"""
    result = runner.invoke(app, ["delete", "1"])

    # This will fail because no item exists, but tests the command structure
    assert result.exit_code == 1  # Should fail due to not found
    assert "not found" in result.output