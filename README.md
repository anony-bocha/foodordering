# 🍔 Django Food Ordering Application

[![Python](https://img.shields.io/badge/python-3.8%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-4.2-green?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow?style=flat-square)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/anony-bocha/foodordering?style=flat-square)](https://github.com/anony-bocha/foodordering/stargazers)

![Project Banner](screenshots/product_list.png)

A modern, responsive web application for ordering food online, built with **Django** and **Bootstrap 5**. This app provides a seamless user experience for browsing products, managing a shopping cart, and placing orders..

---

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Render-green?style=for-the-badge)](https://foodordering-kgwb.onrender.com)

---

## 📑 Table of Contents

- [🚀 Features](#-features)
- [📸 Screenshots](#-screenshots)
- [🎥 Demo](#-demo)
- [🛠️ Installation](#️-installation)
- [🗂️ Project Structure](#️-project-structure)
- [🚀 Usage](#-usage)
- [🛠️ Technologies Used](#️-technologies-used)
- [🤝 Contributing](#-contributing)
- [📝 License](#-license)
- [📧 Contact](#-contact)

---

## 🚀 Features

✅ **User Authentication:** Registration, login, and logout functionality for secure access.  
✅ **Product Catalog:** Display food products with images, descriptions, and prices.  
✅ **Shopping Cart:** Add, remove, and update quantities of products in the cart.  
✅ **Checkout Process:** Collect customer details and confirm orders.  
✅ **Order Management:** Store order details including items, quantities, and prices.  
✅ **Responsive Design:** Fully responsive UI using Bootstrap 5 for mobile and desktop.  
✅ **Session-Based Cart:** Cart persists across user sessions without login.  
✅ **Real-Time Cart Badge:** Displays current number of items in the cart in navbar.

---

## 📸 Screenshots

| Product List                    | Cart Page                       |
|--------------------------------|--------------------------------|
| ![Product List](screenshots/product_list.png) | ![Cart Page](screenshots/cart.png) |

| Login                   | Register                       |
|--------------------------------|--------------------------------|
| ![Login](screenshots/login.png) | ![Register](screenshots/register.png) |

| Checkout Page                  | Order Success                   |
|-------------------------------|--------------------------------|
| ![Checkout](screenshots/checkout.png) | ![Order Success](screenshots/success.png) |

---

## 🛠️ Installation

### Prerequisites

- Python 3.8+  
- Git  
- Virtual Environment tool (venv)

## 🗂️ Project Structure

- `products/` - Handles product listing and management  
- `cart/` - Manages cart operations, checkout, and orders  
- `templates/` - HTML templates  
- `static/` - CSS, JS, and images  
- `media/` - Uploaded product images

### Setup Steps

1️⃣ **Clone the repository:**

```bash
git clone https://github.com/anony-bocha/foodordering.git
cd foodordering
python -m venv env
source env/bin/activate        # On Windows: env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
