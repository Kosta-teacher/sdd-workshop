import todo_lib  # This creates the tables
from cli.commands import app

if __name__ == "__main__":
    # Ensure tables are created
    from todo_lib.database import Base, engine
    Base.metadata.create_all(bind=engine)
    app()