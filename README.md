# 📝 To-Do List API

A simple and clean **RESTful To-Do List API** built with **FastAPI** and **SQLite**, complemented by a user-friendly HTML frontend. This project demonstrates core CRUD functionality, asynchronous handling, Pydantic-based validation, and a Tailwind CSS-powered interface.

---

## 🚀 Features

- **RESTful API** with full **CRUD** support:
  - `POST /tasks` – Create a task
  - `GET /tasks` – Retrieve all tasks
  - `GET /tasks/{id}` – Retrieve a specific task
  - `PUT /tasks/{id}` – Update a task
  - `DELETE /tasks/{id}` – Delete a task

- **Data Validation**: Leveraging **Pydantic** to ensure valid task data (`title`, `description`, `status`)

- **Persistent Storage**: Tasks stored in **SQLite** database (`tasks.db`) with fields:
  - `id`, `title`, `description`, `status`, `created_at`

- **HTML Frontend**:
  - Single-page UI for managing tasks
  - Form for creating and updating tasks
  - Task table with **edit** and **delete** functionality
  - Responsive design using **Tailwind CSS (CDN)**

- **Error Handling**:
  - Returns appropriate HTTP status codes (e.g., `404` for not found)
  - User-friendly error alerts in the UI

- **Dynamic Updates**: Auto-refreshing task list after every operation

---

## 📁 Project Structure

```
todo-list-api/
├── main.py         # FastAPI backend
├── index.html      # Frontend interface
└── tasks.db        # SQLite DB (auto-created)
```

---

## ⚙️ Prerequisites

- **Python 3.8+**
- **Git** (to clone repo)
- **Browser** (for UI and Swagger)
- (Optional) Local HTTP server to serve `index.html`

---

## 🧩 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/vishnu5002/To-Do-List-API.git
cd To-Do-List-API
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install fastapi uvicorn pydantic
```

Optional for CORS support:

```bash
pip install "fastapi[all]"
```

---

## ▶️ Running the Project

### 1. Start the Backend

```bash
uvicorn main:app --reload
```

- API base URL: `http://127.0.0.1:8000`
- Swagger docs: `http://127.0.0.1:8000/docs`

### 2. Access the Frontend

#### Option 1: Using HTTP Server

```bash
python -m http.server 8080
```

Visit: [http://localhost:8080/index.html](http://localhost:8080/index.html)

#### Option 2: Open HTML Directly

Double-click `index.html`  
> ⚠️ May need CORS enabled if accessing from file://

---

## 🌐 CORS Setup (Optional)

To allow frontend access from other origins:

1. Install:
   ```bash
   pip install "fastapi[all]"
   ```

2. Add this to `main.py`:

   ```python
   from fastapi.middleware.cors import CORSMiddleware

   app.add_middleware(
       CORSMiddleware,
       allow_origins=["*"],  # Replace with specific origin(s) in production
       allow_credentials=True,
       allow_methods=["*"],
       allow_headers=["*"],
   )
   ```

3. Restart server:

   ```bash
   uvicorn main:app --reload
   ```

---

## 🔧 Using the Application

- **Add Task**: Fill the form → Click **Add Task**
- **Edit Task**: Click **Edit** → Modify → Click **Update Task**
- **Cancel Edit**: Click **Cancel Update**
- **Delete Task**: Click **Delete** → Confirm
- **View Tasks**: Tasks are shown with title, description, status, and creation date

---

## 🧪 Example API Request

Using `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/tasks" \
     -H "Content-Type: application/json" \
     -d '{"title":"Buy groceries", "description":"Milk, eggs", "status":"pending"}'
```

---

## 🧱 Dependencies

### Python

- `fastapi` – Core API framework
- `uvicorn` – ASGI server
- `pydantic` – Data validation
- `sqlite3` – Built-in DB for persistence
- Optional: `fastapi[all]` – CORS & multipart support

### Frontend

- **Tailwind CSS** (via CDN)
- **Vanilla JavaScript** (Fetch API)

---

## 🔮 Future Improvements

- Add **user authentication**
- Enable **task filtering & sorting**
- Implement **pagination**
- Use **async DB** (e.g., `databases`, `SQLAlchemy`)
- Deploy to **Heroku**, **Render**, or other cloud services
- Host frontend as static site (e.g., GitHub Pages)

---

## 🤝 Contributing

Contributions are welcome!

- Fork the repo
- Create a branch
- Submit a **pull request**

---

## 📬 Contact

For issues or suggestions, open an issue on GitHub or reach out:

**GitHub**: [@vishnu5002](https://github.com/vishnu5002)
