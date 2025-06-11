# 📝 TaskFlow – A Minimal Task Manager

TaskFlow is a simple web-based task manager built using Flask and MySQL. It's perfect for beginners aspiring to become software developers or data analysts.

## 🚀 Features
- Add, update, delete, and view tasks
- Built using Flask (Python Web Framework)
- MySQL database integration
- Clean UI using HTML/CSS

## 🧑‍💻 Setup Instructions

### 1. Clone this repo
```bash
git clone https://github.com/your-username/taskflow-flask.git
cd taskflow-flask
```

### 2. MySQL Setup
```sql
CREATE DATABASE taskflow_db;
USE taskflow_db;
CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT
);
```

### 3. Install dependencies
```bash
pip install flask mysql-connector-python
```

### 4. Run the app
```bash
python app.py
```
Then open `http://127.0.0.1:5000`.

## 📁 Structure
- app.py
- templates/
- static/
- requirements.txt
- README.md
