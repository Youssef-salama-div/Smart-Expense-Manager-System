# Mariam - OOP + Reports & Charts
import json
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
import joblib


class Transaction:
    def __init__(self, transaction_type, amount, category, date, note):
        self.transaction_type = transaction_type
        self.amount = amount
        self.category = category
        self.date = date
        self.note = note


class ExpenseManager:
    def __init__(self):
        self.transaction = []
        self.budget = 0
        try:
            self.model=joblib.load("expense_manager_core.pkl")
        except:
            self.model=DecisionTreeClassifier()

    def add_income(self, amount, category, date, note):
        income = Transaction("Income", amount, category, date, note)
        self.transaction.append(income)

    def add_expense(self, amount, category, date, note):
        expense = Transaction("Expense", amount, category, date, note)
        self.transaction.append(expense)

    def view_transactions(self):
        return self.transaction

    def calculate_balance(self):
        total_income = 0
        total_expense = 0
        for i in self.transaction:
            if i.transaction_type == "Income":
                total_income += i.amount
            elif i.transaction_type == "Expense":
                total_expense += i.amount
        balance = total_income - total_expense
        return total_income, total_expense, balance

    def edit_transaction(self, index, new_amount):
        self.transaction[index].amount = new_amount

    def delete_transaction(self, index):
        self.transaction.pop(index - 1)

    categories = ["Food", "Transport", "Shopping", "Bills", "Health", "Education", "Entertainment", "Other"]

    def serch_by_category(self, search_category):
        result = []
        for i in self.transaction:
            if i.category == search_category:
                result.append(i)
        return result

    def serch_by_date(self, search_date):
        result = []
        for i in self.transaction:
            if i.date == search_date:
                result.append(i)
        return result

    def serch_by_amount(self, search_amount):
        result = []
        for i in self.transaction:
            if i.amount == search_amount:
                result.append(i)
        return result

    def Filter(self, s_transaction_type):
        result = []
        for i in self.transaction:
            if i.transaction_type == s_transaction_type:
                result.append(i)
        return result

    def unique_categories(self):
        unique = set()
        for i in self.transaction:
            unique.add(i.category)
        return unique

    def average_expense(self):
        total = 0
        count = 0
        for i in self.transaction:
            if i.transaction_type == "Expense":
                total += i.amount
                count += 1
        if count > 0:
            return total / count
        else:
            return 0

    def highest_expense(self):
        highest = 0
        for i in self.transaction:
            if i.transaction_type == "Expense":
                if i.amount > highest:
                    highest = i.amount
        return highest

    def lowest_expense(self):
        found = False
        lowest = 0
        for i in self.transaction:
            if i.transaction_type == "Expense":
                if found == False:
                    lowest = i.amount
                    found = True
                elif i.amount < lowest:
                    lowest = i.amount
        if found == False:
            return None
        else:
            return lowest

    def most_spending_category(self):
        category_amount = {}
        for i in self.transaction:
            if i.transaction_type == "Expense":
                if i.category in category_amount:
                    category_amount[i.category] += i.amount
                else:
                    category_amount[i.category] = i.amount
        if len(category_amount) == 0:
            return None, None
        else:
            max_category = max(category_amount, key=category_amount.get)
            return max_category, category_amount[max_category]

    def budget_warning(self):
        total_expense = 0
        for i in self.transaction:
            if i.transaction_type == "Expense":
                total_expense += i.amount
        if total_expense > self.budget:
            return "Warning: You exceeded your budget", None
        elif total_expense == self.budget:
            return "Warning: You reached your budget limit", None
        else:
            remaining = self.budget - total_expense
            return "You are within your budget", remaining

    def save_data(self):
        data = []
        for i in self.transaction:
            data.append({
                "transaction_type": i.transaction_type,
                "amount": i.amount,
                "category": i.category,
                "date": i.date,
                "note": i.note})
        file = open("transactions.json", "w")
        json.dump(data, file, indent=4)
        file.close()

    def load_data(self):
        file = open("transactions.json", "r")
        data = json.load(file)
        file.close()
        self.transaction.clear()
        for i in data:
            t = Transaction(
                i["transaction_type"],
                i["amount"],
                i["category"],
                i["date"],
                i["note"])
            self.transaction.append(t)

    #mariam mohamed sayed
    
    def set_budget(self, amount):
        self.budget = amount

    def get_budget(self):
        return self.budget

    def monthly_report(self):
        total_income = 0
        total_expense = 0
        highest = 0
        lowest = 0
        found = False
        for i in self.transaction:
            if i.transaction_type == "Income":
                total_income += i.amount
            elif i.transaction_type == "Expense":
                total_expense += i.amount
                if found == False:
                    highest = i.amount
                    lowest = i.amount
                    found = True
                if i.amount > highest:
                    highest = i.amount
                if i.amount < lowest:
                    lowest = i.amount
        balance = total_income - total_expense
        if found:
            return total_income, total_expense, balance, highest, lowest
        else:
            return total_income, total_expense, balance, None, None

    def show_chart(self):
        category_amount = {}
        for i in self.transaction:
            if i.transaction_type == "Expense":
                if i.category in category_amount:
                    category_amount[i.category] += i.amount
                else:
                    category_amount[i.category] = i.amount

        plt.bar(category_amount.keys(), category_amount.values())
        plt.title("Expense Categories")
        plt.xlabel("Category")
        plt.ylabel("Amount")
        plt.show()

    def show_pie_chart(self):
        category_amount = {}
        for i in self.transaction:
            if i.transaction_type == "Expense":
                if i.category in category_amount:
                    category_amount[i.category] += i.amount
                else:
                    category_amount[i.category] = i.amount
        plt.pie(
            category_amount.values(),
            labels=category_amount.keys(),
            autopct="%1.1f%%")

        plt.title("Expenses Percentage")
        plt.show()
   
   
   
    def train_model(self):
        X = []
        y = []
        for i in self.transaction:
            if i.transaction_type == "Expense":
                X.append([i.amount])
                y.append(i.category)

        if len(X) < 2:
            print("Not Enough Data to Train Model")
            return
        self.model.fit(X, y)
        joblib.dump(self.model,"expense_manager_core.pkl")
        print("Model Trained Successfully")
    
    
    def predict_category(self, amount):
        result = self.model.predict([[amount]])
        return result[0]
            