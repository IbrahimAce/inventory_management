# Django Inventory Management System

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Django](https://img.shields.io/badge/Django-5.2+-green.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

A complete, full-featured **Inventory Management Web Application** built with **Django**. This project leverages Django's **Class-Based Views (CBVs)** to implement a clean, efficient, and scalable **CRUD** (Create, Read, Update, Delete) workflow with minimal boilerplate code.

## 🚀 Features

* **Secure Authentication:** User login/logout functionality protecting all inventory views.
* **Full CRUD Operations:** Complete management workflows for both **Products** and **Categories**.
* **Smart Dashboard:** * Tracks quantity in stock, unit prices, and SKUs.
  * Automatic "Low Stock!" badge indicator when product inventory drops below the defined reorder level.
* **User Tracking:** Automatically tracks which authenticated user created a product, along with timestamp data.
* **Responsive UI:** Clean, modern interface styled completely with Bootstrap 5.
* **User Feedback:** Integrated Django messages framework to provide instant success notifications for create, update, and delete actions.

## 🛠️ Tech Stack

* **Backend:** Python, Django
* **Frontend:** HTML5, Django Templates, Bootstrap 5 (CDN)
* **Database:** SQLite (Development)

## 📂 Project Structure

```text
inventory_management/
├── inventory/                  # Main application app
│   ├── migrations/
│   ├── templates/
│   │   ├── inventory/          # CRUD templates (list, detail, form, confirm_delete)
│   │   └── registration/       # Auth templates (login.html)
│   ├── admin.py                # Admin dashboard configurations
│   ├── forms.py                # Django ModelForms
│   ├── models.py               # Database schemas (Product, Category)
│   ├── urls.py                 # App-level routing
│   └── views.py                # Class-Based Views (ListView, CreateView, etc.)
├── inventory_project/          # Project configuration settings
├── db.sqlite3                  # Local database
├── manage.py                   
└── README.md



# 1. Clone the repository and navigate into it
git clone [https://github.com/IbrahimAce/inventory_management.git](https://github.com/IbrahimAce/inventory_management.git)
cd inventory_management

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install django django-bootstrap5

# 4. Apply database migrations
python3 manage.py makemigrations
python3 manage.py migrate

# 5. Create an admin superuser (follow the prompts)
python3 manage.py createsuperuser

# 6. Start the development server
python3 manage.py runserver
