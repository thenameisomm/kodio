# ⚙️ Kodio – A Django-Based GitHub Clone

**Kodio** is a code-hosting platform built using the Django web framework, inspired by GitHub. It allows users to create repositories, upload files, and manage projects through a powerful web interface and Django's admin panel.

---

## 🌟 Features

- 🧑‍💻 User registration and authentication
- 🗂️ Create and manage code repositories
- 📁 Upload, store, and view code files
- 🛡️ Admin interface with full user and repo control
- 🧱 SQLite database for development
- 🧩 Modular Django app structure

---

## 🚀 Getting Started

Follow these steps to get Kodio running on your local machine.

### 🖥️ 1. Clone the Repository

```bash
git clone https://github.com/thenameisomm/kodio.git
cd kodio
```

### 🐍 2. Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 📦 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 🛠️ 4. Apply Database Migrations

```bash
python manage.py migrate
```

### 👑 5. Create a Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to set up your admin account.

### 🌐 6. Start the Development Server

```bash
python manage.py runserver
```

Access your app:

- 🌍 App: http://127.0.0.1:8000/
- 🔐 Admin: http://127.0.0.1:8000/admin/

---

## 🧪 Project Structure

```
kodio/
├── manage.py
├── README.md
├── requirements.txt
├── .gitignore
├── your_app/               # Your Django app (e.g., repositories, users, etc.)
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
└── templates/              # HTML templates
```

---

## 🧾 .gitignore Highlights

Included to prevent pushing unwanted files:

```
venv/
db.sqlite3
__pycache__/
*.pyc
media/
.env
```

---

## 📜 License

This project is licensed under the **MIT License** – free to use, modify, and distribute.

```

MIT License

Copyright (c) 2025 Om

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction...
```

---

## 💬 Want to Contribute?

Feel free to fork the repo, make changes, and submit a pull request.

---

## 🛠️ Future Enhancements (Ideas)

- ✅ Public/private repo toggle
- ✅ File versioning
- ✅ User profile pages
- ✅ Git-style file history

---

## 🙌 Made with ❤️ by [Om Badgujar](https://github.com/thenameisomm)
