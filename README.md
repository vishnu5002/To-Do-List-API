To-Do List API
A simple, RESTful To-Do List API built with FastAPI and SQLite, accompanied by a user-friendly HTML frontend for managing tasks. This project demonstrates CRUD operations, data validation with Pydantic, and asynchronous API handling, with a clean interface for creating, viewing, updating, and deleting tasks.
Features

RESTful API: Supports Create, Read, Update, and Delete (CRUD) operations for tasks.
Endpoints:
POST /tasks: Create a new task.
GET /tasks: Retrieve all tasks.
GET /tasks/{id}: Retrieve a specific task by ID.
PUT /tasks/{id}: Update a task (partial updates supported).
DELETE /tasks/{id}: Delete a task.




Data Validation: Uses Pydantic models to validate task data (title, description, status).
Persistent Storage: Stores tasks in a SQLite database with fields for id, title, description, status, and created_at.
HTML Frontend: A single-page HTML interface with:
A form to add or update tasks.
A table to display tasks with title, description, status, and creation date.
Buttons to edit or delete tasks, with a confirmation prompt for deletions.
Responsive design using Tailwind CSS (via CDN).


Error Handling: Returns appropriate HTTP status codes (e.g., 404 for non-existent tasks) and displays user-friendly error messages in the frontend.
Dynamic Updates: The task list refreshes automatically after adding, updating, or deleting tasks.

Project Structure
todo-list-api/
├── main.py         # FastAPI backend with SQLite integration
├── index.html      # HTML frontend for task management
└── tasks.db        # SQLite database (created automatically on first run)

Prerequisites

Python 3.8+: Required for running the FastAPI backend.
Git: To clone the repository.
Browser: To access the HTML frontend and Swagger UI.
Optional: A local HTTP server (e.g., Python’s http.server) to serve the HTML file.

Installation

Clone the Repository:
git clone https://github.com/your-username/todo-list-api.git
cd todo-list-api


Set Up a Virtual Environment (recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:Install the required Python packages for the FastAPI backend:
pip install fastapi uvicorn pydantic

Note: The HTML frontend uses Tailwind CSS via CDN, so no additional frontend dependencies are needed.

Optional - Enable CORS (if accessing index.html from a different origin):Install the fastapi[all] package to include CORS middleware:
pip install "fastapi[all]"

Update main.py to add CORS support (see CORS Setup below).


Running the Project

Start the FastAPI Backend:Run the FastAPI server using Uvicorn:
uvicorn main:app --reload

The API will be available at http://127.0.0.1:8000. The SQLite database (tasks.db) will be created automatically on first run.

Access the Frontend:

Option 1: Serve index.html Locally:Serve the HTML file using Python’s built-in HTTP server:python -m http.server 8080

Open http://localhost:8080/index.html in your browser.
Option 2: Open Directly:Open index.html directly in a browser (e.g., double-click the file). Note: You may need CORS enabled (see below) if you encounter issues.


Test the API (optional):Access the Swagger UI at http://127.0.0.1:8000/docs to test API endpoints interactively.


Using the Application

Add a Task: In the HTML interface, enter a title (required), description (optional), and status (Pending, In Progress, or Completed), then click "Add Task".
View Tasks: Tasks are displayed in a table with their title, description, status, and creation date.
Edit a Task: Click "Edit" on a task to populate the form, modify fields, and click "Update Task". Use "Cancel Update" to reset the form.
Delete a Task: Click "Delete" on a task and confirm to remove it.
Example API Request (via Swagger UI or tools like curl):curl -X POST "http://127.0.0.1:8000/tasks" -H "Content-Type: application/json" -d '{"title":"Buy groceries","description":"Milk, eggs","status":"pending"}'



CORS Setup (Optional)
If you encounter CORS issues when accessing index.html (e.g., when opening directly or from a different port), enable CORS in the FastAPI backend:

Install fastapi[all] (includes python-multipart and fastapi-cors):
pip install "fastapi[all]"


Update main.py to include CORS middleware. Add the following code near the top of main.py, after app = FastAPI(...):
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict to specific origins in production (e.g., ["http://localhost:8080"])
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


Restart the FastAPI server:
uvicorn main:app --reload



Dependencies

Python Packages:
fastapi: For building the RESTful API.
uvicorn: For running the FastAPI server.
pydantic: For data validation and serialization.
sqlite3: Built-in with Python, used for the database.
Optional: fastapi[all] for CORS support.


Frontend:
Tailwind CSS (loaded via CDN, no installation required).
No JavaScript frameworks; uses vanilla JavaScript with the Fetch API.



Install Python dependencies:
pip install fastapi uvicorn pydantic

Future Improvements

Add user authentication to secure the API.
Implement task filtering or sorting in the frontend.
Add pagination for the task list.
Use an async database library (e.g., databases or SQLAlchemy with async support) for better performance.
Deploy the API to a cloud platform (e.g., Heroku, Render) and host the frontend on a static file server.

Contributing
Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request with your changes.
Contact
For questions or suggestions, open an issue on GitHub or contact vishnu5002.
