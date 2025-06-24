### Late_show_API

 A RESTful flask API with Authentication , Postgresql and an MVC architecture for managing a Late Night TV show system.

 ## 📁 Folder Structure

```
.
├── server/
│   ├── app.py
│   ├── config.py
│   ├── seed.py
│   ├── extensions.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── guest.py
│   │   ├── episode.py
│   │   ├── appearance.py
│   │   └── user.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── base_controller.py
│   │   ├── guest_controller.py
│   │   ├── episode_controller.py
│   │   ├── appearance_controller.py
│   │   └── auth_controller.py
├── migrations/
├── .env
├── Pipfile
├── Pipfile.lock
└── README.md
```


### 🛠 Setup

## CLone the Repo
```bash
git clone https://github.com/Gitkorir/late-show-api-challenge.git

✅ Install dependencies:
  pipenv install
  pipenv shell

pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary pipenv shell

✅ PostgreSQL DB setup

Create your database in Postgres:

CREATE DATABASE late_show_db;

✅ Set your DATABASE_URI in server/config.py

SQLALCHEMY_DATABASE_URI = "postgresql://<user>:<password>@localhost:5432/late_show_db"

✅ Run DB setup
```bash
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "initial migration" 
flask db upgrade 
python server/seed.py
```
### Authentication

JWT-based authentication using `Flask_JWT_Extended`.

### EndPoints
| Route      | Method | Description         |
|------------|--------|---------------------|
| `/register` | POST   | Register a user     |
| `/login`    | POST   | Login & get JWT     |

Add this header to protected routes:
```
Authorization: Bearer <your_token>
```

## 🚀 API Endpoints

### 🎥 Episodes

| Route                | Method | Protected | Description          |
|----------------------|--------|-----------|----------------------|
| `/episodes/`         | GET    | ❌        | List all episodes    |
| `/episodes/`         | POST   | ✅        | Create an episode    |
| `/episodes/<id>`     | GET    | ❌        | Get one episode      |
| `/episodes/<id>`     | DELETE | ✅        | Delete an episode    |

### 👤 Guests

| Route               | Method | Protected | Description       |
|---------------------|--------|-----------|-------------------|
| `/guests/`          | GET    | ❌        | List all guests   |
| `/guests/`          | POST   | ❌        | Create a guest    |
| `/guests/<id>`      | GET    | ❌        | Get one guest     |
| `/guests/<id>`      | DELETE | ✅        | Delete a guest    |

### 🎤 Appearances

| Route            | Method | Protected | Description             |
|------------------|--------|-----------|-------------------------|
| `/appearances/`  | POST   | ✅        | Create an appearance    |

---

## 📫 Sample Request & Response

### Register
```http
POST /register
Content-Type: application/json

{
  "username": "arnold",
  "password": "password123"
}
```

## 🚀 API Endpoints

### 🎥 Episodes

| Route                | Method | Protected | Description          |
|----------------------|--------|-----------|----------------------|
| `/episodes/`         | GET    | ❌        | List all episodes    |
| `/episodes/`         | POST   | ✅        | Create an episode    |
| `/episodes/<id>`     | GET    | ❌        | Get one episode      |
| `/episodes/<id>`     | DELETE | ✅        | Delete an episode    |

### 👤 Guests

| Route               | Method | Protected | Description       |
|---------------------|--------|-----------|-------------------|
| `/guests/`          | GET    | ❌        | List all guests   |
| `/guests/`          | POST   | ❌        | Create a guest    |
| `/guests/<id>`      | GET    | ❌        | Get one guest     |
| `/guests/<id>`      | DELETE | ✅        | Delete a guest    |

### 🎤 Appearances

| Route            | Method | Protected | Description             |
|------------------|--------|-----------|-------------------------|
| `/appearances/`  | POST   | ✅        | Create an appearance    |

---

## 📫 Sample Request & Response

### Register
```http
POST /register
Content-Type: application/json

{
  "username": "arnold",
  "password": "password123"
}
```
## 📎 GitHub

[🔗 GitHub Repo](https://github.com/Gitkorir/late-show-api-challenge)

