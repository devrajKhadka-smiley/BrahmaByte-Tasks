# Chat Application

A real-time chat application built with FastAPI, featuring JWT-based authentication and WebSocket communication.

---

## Features

- User registration and login with JWT authentication  
- Role-based access control (`user`, `admin`)  
- Real-time messaging using WebSockets  
- Multiple chat rooms support  
- Secure token-based WebSocket connections  

---

## Getting Started

### Prerequisites

- Python 3.8 or higher  
- PostgreSQL (or your preferred database)  

### Setup Instructions

1. **Create the database**

```bash
CREATE DATABASE chat_db;
\q
```

2. **Create and activate a Python virtual environment**

```bash
python3 -m venv venv
venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the application**

```bash
uvicorn app.main:app --reload
```

The app will be available at `http://localhost:8000`

---

## API Usage

### Signup

Register a new user by sending a POST request to `/signup`:

```http
POST http://localhost:8000/signup
Content-Type: application/json

{
  "username": "user2",
  "password": "userpass",
  "role": "user"
}
```

### Login

Authenticate a user by sending a POST request to `/login`:

```http
POST http://localhost:8000/login
Content-Type: application/json

{
  "username": "user1",
  "password": "userpass"
}
```

The response will include a JWT token. Copy this token for WebSocket connection.

---

## WebSocket Usage

Connect to a chat room via WebSocket with the token for authentication.

Example URL format:

```
ws://localhost:8000/ws/{room_name}?token={your_jwt_token}
```

For example:

```
ws://localhost:8000/ws/room1?token=eyJhbGciOiJIUzI1NiIsInR5cCI6...
```

### Sending Messages

Send messages in JSON format over the WebSocket connection:

```json
{
  "message": "Hello, what's up?"
}
```

---

## Tools

- Use **Postman** or any API client for signup and login.  
- Use **WebSocket King**, browser WebSocket extensions, or any WebSocket client to connect and chat.

---
