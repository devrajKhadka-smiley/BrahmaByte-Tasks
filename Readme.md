# BrahmaByte Tasks

## Overview

This repository contains two distinct projects:

- **Chat Application** (Group A) — a real-time chat system implementation.  
- **Task 2** (Group B, Task 1) — an assignment focused on database persistence and API development.

Please navigate to the respective project directories to explore and run each project.

---

## Technologies & Tools

- **Postman** — API testing and development  
- **WebSocket King** — WebSocket client for real-time communication testing  
- **PostgreSQL** — Relational database management system

---

## Installation

Follow these steps to set up and run the projects locally:

1. **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd chatapplication   # or `cd task2` depending on which project to run
    ```

2. **Create and activate a virtual environment:**

    - On macOS/Linux:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```
    - On Windows:
      ```bash
      python -m venv venv
      .\venv\Scripts\activate
      ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure environment variables:**

    - from the a `.env` file edit it in the distinct  project directory.
    - Add necessary environment variables (e.g., database URL, secret keys).

5. **Run the application:**

    ```bash
    uvicorn app.main:app --reload
    ```
---

## API Reference

For a complete list of tested API endpoints and sample requests, please refer to the Postman collection linked below:

🔗 **Postman Collection:**  
[Click here to view on Postman](https://www.postman.com/sye9/workspace/public-sharing-apis/collection/34656822-16c67146-7323-42cd-9925-671fa789aaeb?action=share&creator=34656822)

---

By Deb
