# Backend Intern CRUD — Blog API (FastAPI)

A simple blog management system built with **FastAPI** that supports:

* Blog Post CRUD operations
* Like functionality
* Comment functionality
* JWT-based authentication
* SQLite database

---

## 📌 Features

1. **Authentication**

   * User registration (`/api/auth/register`)
   * User login (`/api/auth/login`) with JWT token

2. **Blog Posts**

   * Create, read, update, delete blog posts
   * Retrieve all posts or a single post by ID

3. **Likes**

   * Like a post (`/api/posts/{id}/like`)
   * Fetch all likes for a post (`/api/posts/{id}/likes`)

4. **Comments**

   * Add a comment to a post (`/api/posts/{id}/comment`)
   * Fetch comments for a post (`/api/posts/{id}/comments`)

---

## 📂 Project Structure

```
backend-intern-crud/
│
├── src/
│   ├── main.py          # FastAPI entry point
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   ├── database.py      # Database config
│   ├── routes/
│   │   ├── auth.py
│   │   ├── posts.py
│   │   ├── likes.py
│   │   ├── comments.py
│
├── backend-intern-crud.postman_collection.json  # Postman collection
├── README.md
├── requirements.txt
└── blog.db            # SQLite database file
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/backend-intern-crud.git
cd backend-intern-crud
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
uvicorn src.main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

## 🔑 Authentication

All write operations (**POST**, **PUT**, **DELETE**) require authentication.
Use the `/api/auth/login` endpoint to get a JWT token, and pass it in the header:

```
Authorization: Bearer <your_token_here>
```

---

## 🧪 API Endpoints

### Auth

| Method | Endpoint             | Description         |
| ------ | -------------------- | ------------------- |
| POST   | `/api/auth/register` | Register a new user |
| POST   | `/api/auth/login`    | Login and get token |

### Posts

| Method | Endpoint          | Description        |
| ------ | ----------------- | ------------------ |
| POST   | `/api/posts`      | Create post (auth) |
| GET    | `/api/posts`      | Get all posts      |
| GET    | `/api/posts/{id}` | Get single post    |
| PUT    | `/api/posts/{id}` | Update post (auth) |
| DELETE | `/api/posts/{id}` | Delete post (auth) |

### Likes

| Method | Endpoint                | Description          |
| ------ | ----------------------- | -------------------- |
| POST   | `/api/posts/{id}/like`  | Like a post (auth)   |
| GET    | `/api/posts/{id}/likes` | Get likes for a post |

### Comments

| Method | Endpoint                   | Description             |
| ------ | -------------------------- | ----------------------- |
| POST   | `/api/posts/{id}/comment`  | Add comment (auth)      |
| GET    | `/api/posts/{id}/comments` | Get comments for a post |

---

## 📬 Postman Collection

A Postman collection is included in:

```
backend-intern-crud.postman_collection.json
```

You can import it into Postman to test all endpoints (with and without authentication).

---