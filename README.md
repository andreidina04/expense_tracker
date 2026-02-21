# 💰 ExpenseTracker Pro

A modern, high-performance desktop application for personal finance management. Built with **Python**, **MySQL** and **CustomTkinter**, this tool helps users track income and expenses with a sleek, dark-themed interface and real-time database synchronization.

## 🌟 Key Features

- **User Authentication**: Secure Login and Registration system with input validation (email format & password matching).
- **Real-time Dashboard**: Instantly view Total Balance, Income, and Expenses.
- **Transaction Management (CRUD)**:
  - Add Income/Expenses with categorized tags.
  - Delete transactions with instant UI refresh.
  - Full history log with scrollable view.
- **Smart Filtering**: Filter transaction history by category (e.g., Gym, Food, Salary) using a dynamic dropdown menu.
- **Data Security**: Implementation of `.env` files to protect database credentials and prevent sensitive data leaks on GitHub.
- **Modern UI**: Fully responsive Dark Mode design using the CustomTkinter library.

## 🛠️ Tech Stack

* **Language**: Python 3.x
* **GUI Framework**: [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
* **Database**: MySQL (via PyMySQL)
* **Environment Management**: Python-dotenv

---

## 🚀 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/your-username/ExpenseTracker.git](https://github.com/your-username/ExpenseTracker.git)
   cd ExpenseTracker
Install Dependencies:

Bash
`pip install -r requirements.txt`
Database Configuration:

Create a MySQL database named finance_tracker.

Run the following SQL to create the tables:

SQL
`CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    amount DECIMAL(10,2),
    category VARCHAR(100),
    type ENUM('income', 'expense'),
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);`
Environment Variables:
Create a .env file in the root directory and add your credentials:

Code snippet
`DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=finance_tracker`
Run the Application:

Bash
`python main.py`

🛡️ Security Note
This project uses .gitignore to ensure that sensitive files like .env and __pycache__ are never uploaded to the public repository.