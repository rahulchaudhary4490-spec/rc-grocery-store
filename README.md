# 🛒 RC Grocery Management System

A full-stack web application to manage grocery store orders and products — built with Python Flask, PostgreSQL, and vanilla JavaScript.

🔗 **Live Demo:** [rc-grocery-store](https://rahulchaudhary4490-spec.github.io/rc-grocery-store/ui/index.html)

---

## 📸 Screenshots

> Home Page — Order List  
> Manage Products  
> New Order Form  

---

## 🚀 Features

- 📦 Add, view, and delete products with unit and price
- 🧾 Create new customer orders with multiple items
- 💰 Auto-calculates total price per item and grand total
- 📋 View all past orders on the home dashboard
- 🌐 Fully deployed — accessible from anywhere

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML, CSS, Bootstrap, JavaScript, jQuery |
| Backend | Python, Flask, Flask-CORS |
| Database | PostgreSQL (Render) |
| Deployment | Render (backend), GitHub Pages (frontend) |

---

## 📁 Project Structure

```
rc-grocery-store/
│
├── backend/
│   ├── server.py           # Flask API routes
│   ├── sql_connection.py   # PostgreSQL connection
│   ├── products_dao.py     # Product CRUD operations
│   ├── orders_dao.py       # Order CRUD operations
│   ├── uom_dao.py          # Unit of measurement
│   └── requirements.txt    # Python dependencies
│
└── ui/
    ├── index.html          # Home - Orders list
    ├── manage-product.html # Manage products
    ├── order.html          # New order form
    ├── css/                # Stylesheets
    └── js/                 # JavaScript files
```

---

## ⚙️ API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/getProducts` | Get all products |
| POST | `/insertProduct` | Add new product |
| POST | `/deleteProduct` | Delete a product |
| GET | `/getUOM` | Get units of measurement |
| GET | `/getAllOrders` | Get all orders |
| POST | `/insertOrder` | Create new order |

---

## 🖥️ Run Locally

### Prerequisites
- Python 3.x
- PostgreSQL database

### Steps

```bash
# Clone the repo
git clone https://github.com/rahulchaudhary4490-spec/rc-grocery-store.git
cd rc-grocery-store/backend

# Install dependencies
pip install -r requirements.txt

# Update sql_connection.py with your database URL

# Run the server
python server.py
```

Then open `ui/index.html` with Live Server in VS Code.

---

## 🗄️ Database Schema

```sql
-- Units of Measurement
CREATE TABLE uom (uom_id SERIAL PRIMARY KEY, uom_name VARCHAR(45));

-- Products
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    uom_id INT REFERENCES uom(uom_id),
    price_per_unit DOUBLE PRECISION
);

-- Orders
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100),
    total DOUBLE PRECISION,
    datetime TIMESTAMP
);

-- Order Details
CREATE TABLE order_details (
    order_details_id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(order_id),
    product_id INT REFERENCES products(product_id),
    quantity DOUBLE PRECISION,
    total_price DOUBLE PRECISION
);
```

---

## 👨‍💻 Author

**Rahul Choudhary**  
B.Tech ECE — VIT Vellore  
Aspiring Data Analyst  

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/rahul-choudhary-08766b359/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat&logo=github)](https://github.com/rahulchaudhary4490-spec)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
