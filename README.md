# 💰🌐 Finance Tracking Backend System

##  Project Overview

This project is a backend system built using FastAPI that allows users to manage and analyze their financial records. The goal of this project was to design a clean, functional, and logically structured backend that can support a finance tracking application.

The system enables users to store transactions (income and expenses), filter them based on different criteria, and generate meaningful summaries such as total income, expenses, and balance. Additionally, it incorporates basic role-based access control (RBAC) to simulate different user permissions.

The focus of this project was not just on implementing features, but on writing clean, maintainable code and structuring the backend in a way that reflects real-world application design.

---

##  Features Implemented

### 🔹 Financial Records Management (CRUD)

* Create new transactions (income/expense)
* View all transactions
* Update existing records
* Delete records

### 🔹 Filtering

* Filter transactions based on:

  * Type (income / expense)
  * Category
  * Date (optional enhancement)

### 🔹 Summary & Analytics

* Total income calculation
* Total expense calculation
* Current balance (income - expense)

### 🔹 User & Role Handling (RBAC)

* Roles implemented:

  * **Viewer** → Can only view data
  * **Analyst** → Can view + filter + access summaries
  * **Admin** → Full access (create, update, delete)
* Role-based restrictions applied to endpoints

### 🔹 Input Validation & Error Handling

* Used Pydantic schemas for validation
* Proper error responses (e.g., 404 for not found)
* Restricted transaction type to valid values

### 🔹 Database Persistence

* SQLite used for storing data
* SQLAlchemy ORM for database operations

### 🔹 REST API + Documentation

* Clean REST API endpoints
* Automatic Swagger documentation available at `/docs`

---

## 🛠️ Tech Stack

* **Backend Framework:** FastAPI
* **Database:** SQLite
* **ORM:** SQLAlchemy
* **Validation:** Pydantic
* **Server:** Uvicorn
* **Version Control:** Git & GitHub

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/indu706/finance-app.git
cd finance-app
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
uvicorn main:app --reload
```

### 6. Open in browser

```
http://127.0.0.1:8000/docs
```

---

## 🔗 API Endpoints Overview

### 🔹 User APIs

* `POST /users` → Create user with role

### 🔹 Transaction APIs

* `POST /transactions` → Create transaction (Admin only)
* `GET /transactions` → View all transactions
* `PUT /transactions/{id}` → Update transaction (Admin only)
* `DELETE /transactions/{id}` → Delete transaction (Admin only)

### 🔹 Filtering

* `GET /transactions/filter`

  * Query params: `type`, `category`, `date`

### 🔹 Summary

* `GET /summary`

  * Returns income, expense, balance

---

##  Deployment Link

👉 Project can be run through this Render link:

```
https://finance-app-2-sati.onrender.com/docs
```

---

##  Technical Decisions & Trade-offs

### 🔹 Why FastAPI?

I chose FastAPI because it is lightweight, fast, and provides automatic API documentation (Swagger), which made testing and demonstration much easier.

### 🔹 Why SQLite?

SQLite was chosen for simplicity and ease of setup. Since this project is for evaluation purposes, it avoids unnecessary configuration overhead.

### 🔹 Why SQLAlchemy?

Using an ORM like SQLAlchemy helped in keeping database interactions clean and organized, instead of writing raw SQL queries.

### 🔹 RBAC Design Choice

Instead of implementing full authentication, I used a simplified role-based system using query parameters. This keeps the system easy to test while still demonstrating access control logic.

### 🔹 Trade-offs

* No authentication (JWT/session not implemented)
* Role passed manually → not secure for production
* SQLite → not scalable for large systems

---

##  Limitations

* No user authentication system (login/signup not implemented)
* Role-based access is simplified (passed as parameter)
* No frontend (backend-only system)
* Limited analytics (only basic summaries)
* No pagination or search functionality

---

##  Future Improvements

If I continue working on this project, I would:

* Add JWT-based authentication
* Build a frontend dashboard (React)
* Implement advanced analytics (monthly trends, category graphs)
* Add pagination for large datasets
* Use PostgreSQL for scalability
* Add unit tests for better reliability
* Improve role handling with proper middleware

