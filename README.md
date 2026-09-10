# Smart Expense Manager System

## Overview

Smart Expense Manager System is a Python desktop application that helps users manage their personal finances. It allows users to record income and expenses, generate reports, visualize spending with charts, save data to files, and predict expense categories using Machine Learning.

---

## Features

- Add Income
- Add Expense
- View Transactions
- Edit & Delete Transactions
- Calculate Balance
- Search by Category
- Search by Date
- Search by Amount
- Filter Transactions
- Unique Categories
- Set Monthly Budget
- Average Expense
- Highest Expense
- Lowest Expense
- Most Spending Category
- Budget Warning
- Monthly Report
- Save & Load Data (JSON)
- Bar Chart
- Pie Chart
- Machine Learning Expense Category Prediction
- Save Trained Model using Joblib

---

## Technologies Used

- Python
- Tkinter
- Object-Oriented Programming (OOP)
- JSON
- Matplotlib
- Scikit-learn
- Joblib

---

## Project Structure

```text
Smart-Expense-Manager/
│
├── gui.py
├── expense_manager_core.py
├── transactions.json
├── expense_model.pkl
├── README.md
```

---

## Machine Learning

This project uses a Decision Tree Classifier from Scikit-learn.

The model is trained using expense data entered by the user.

**Training Feature:**
- Expense Amount

**Target:**
- Expense Category

After training, the model predicts the most likely expense category for a new expense amount.

The trained model is saved as:

```text
expense_model.pkl
```

using Joblib.

---

## Reports

The application provides:

- Total Income
- Total Expenses
- Current Balance
- Average Expense
- Highest Expense
- Lowest Expense
- Most Spending Category
- Budget Warning

---

## Charts

- Bar Chart for expense categories.
- Pie Chart showing expense distribution.

---

## Data Storage

Transaction data is stored in:

```text
transactions.json
```

The trained Machine Learning model is stored in:

```text
expense_model.pkl
```

---

## How to Run

Install the required libraries:

```bash
pip install matplotlib scikit-learn joblib
```

Run the application:

```bash
python gui.py
```

---

## Author

**Youssef Abdelrahman Ibrahem**
