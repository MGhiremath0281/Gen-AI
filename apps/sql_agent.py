from langchain_ollama import ChatOllama
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit

db = SQLDatabase.from_uri("sqlite:///my_task.db")

print("DB connected successfully")

db.run(
    """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        status TEXT DEFAULT 'pending',
        due_date TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
)

print("Tasks table created successfully")

llm = ChatOllama(model="gemma4:e2b")

# llm , tool , memory , systemprompt

systemprompt = """
You are a task management assistant.

Your job is to help the user manage their tasks using the SQL database.

You can:
- Create new tasks
- View existing tasks
- Update tasks
- Mark tasks as completed
- Delete tasks
- Search and filter tasks
- Check task status and due dates

Rules:
1. Always use the SQL database tools when the user asks about tasks.
2. Never invent task information.
3. Before modifying or deleting data, make sure you understand which task the user means.
4. Use the database schema to generate valid SQL queries.
5. After performing an operation, clearly tell the user what happened.
6. Keep responses concise and easy to understand.
7. If the user's request is unclear, ask for clarification.
"""
