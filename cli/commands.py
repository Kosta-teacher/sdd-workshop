import todo_lib  # Ensure tables are created
import typer
from todo_lib.services import ToDoService

app = typer.Typer()
service = ToDoService()

@app.command()
def add(
    title: str = typer.Argument(None, help="Todo item title"),
    priority: str = typer.Option(None, "--priority", "-p", help="Priority: high, medium, low")
):
    """Add a new todo item"""
    if priority and priority not in ["high", "medium", "low"]:
        typer.echo("Error: Priority must be high, medium, or low")
        raise typer.Exit(1)

    try:
        item = service.add_todo(title=title, priority=priority)
        typer.echo(f"Todo item added with ID: {item['id']}")
    except Exception as e:
        typer.echo(f"Error: {str(e)}")
        raise typer.Exit(1)

@app.command()
def list(
    filter: str = typer.Option(None, "--filter", "-f", help="Filter: done or pending"),
    priority: str = typer.Option(None, "--priority", "-p", help="Filter by priority: high, medium, low")
):
    """List todo items"""
    try:
        items = service.list_todos(filter_status=filter, priority=priority)

        if not items:
            typer.echo("No todo items found.")
            return

        # Print header
        typer.echo(f"{'ID':<3} {'Title':<20} {'Priority':<8} {'Status':<8} {'Created'}")
        typer.echo("-" * 60)

        for item in items:
            status = "Done" if item["completed"] else "Pending"
            priority = item["priority"] or ""
            title = item["title"] or ""
            created = item["created_at"].strftime("%Y-%m-%d") if item["created_at"] else ""
            typer.echo(f"{item['id']:<3} {title:<20} {priority:<8} {status:<8} {created}")

    except Exception as e:
        typer.echo(f"Error: {str(e)}")
        raise typer.Exit(1)

@app.command()
def done(item_id: int = typer.Argument(..., help="Todo item ID")):
    """Mark todo item as done"""
    try:
        if service.mark_todo_done(item_id):
            typer.echo(f"Todo item {item_id} marked as done")
        else:
            typer.echo(f"Error: Todo item {item_id} not found")
            raise typer.Exit(1)
    except Exception as e:
        typer.echo(f"Error: {str(e)}")
        raise typer.Exit(1)

@app.command()
def delete(item_id: int = typer.Argument(..., help="Todo item ID")):
    """Delete todo item"""
    try:
        if service.delete_todo(item_id):
            typer.echo(f"Todo item {item_id} deleted")
        else:
            typer.echo(f"Error: Todo item {item_id} not found")
            raise typer.Exit(1)
    except Exception as e:
        typer.echo(f"Error: {str(e)}")
        raise typer.Exit(1)