# 🎬 EntertainX — Movie, Song & Review API

EntertainX is a RESTful API built using **Python, Django REST Framework, and SQLite** to manage movies, songs, and audience reviews. It includes token-based authentication, custom permissions, model serializers, and related data serialization.

## 🚀 Features

- **Movie Management** — Manage movie information through REST API endpoints.
- **Song Management** — Store songs and associate them with movies.
- **Review System** — Create and manage movie reviews and ratings.
- **Token Authentication** — Secure API access using Django REST Framework token authentication.
- **Custom Permissions** — Control access to review operations based on ownership.
- **Model Serializers** — Convert model instances into structured API responses and validate incoming data.
- **Related Data Serialization** — Retrieve related movie, song, and review information in structured responses.
- **Organized App Structure** — Separate Django apps for movies, songs, and reviews.

## 🛠️ Tech Stack

- Python
- Django
- Django REST Framework
- SQLite
- Git & GitHub

## 📂 Project Structure

```text
EntertainX/
├── movies/
├── songs/
├── Reviewly/
├── manage.py
├── requirements.txt
├── .env
└── .gitignore
```

*The structure above is a simplified overview; additional Django configuration files may be present.*

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/thefarsin12-afk/Entertain_x.git
cd Entertain_x
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

The development server will be available at `http://127.0.0.1:8000/`.

## 🔐 Authentication

EntertainX uses token-based authentication to protect restricted API endpoints.

Include the authentication token in your request headers:

```http
Authorization: Token YOUR_AUTH_TOKEN
```

## 🧩 Key Learning Outcomes

- Building RESTful APIs with Django REST Framework
- Working with Django models and model serializers
- Managing relationships between related models
- Implementing token authentication and custom permissions
- Structuring Django projects using multiple applications
- Handling API requests and responses

## 🔗 Repository

GitHub: https://github.com/thefarsin12-afk/Entertain_x

## 👨‍💻 Author

**Muhammad Farsin M**

Python Django Developer Trainee | Backend Development

---

*Built as a backend development project to practise REST API development with Django REST Framework.*
