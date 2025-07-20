## PostgreSQL Persistence

---
## Getting Started


### Setup Instructions

1. **Create the database**

```bash
CREATE DATABASE chat_dbtask2;
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



