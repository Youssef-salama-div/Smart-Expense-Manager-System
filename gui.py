import tkinter as tk
from tkinter import messagebox
from expense_manager_core import ExpenseManager

manager = ExpenseManager()

root = tk.Tk()
root.title("Smart Expense Manager")
root.geometry("400x550")

current_frame = None


def switch_frame(new_frame_func):
    global current_frame
    if current_frame is not None:
        current_frame.destroy()
    current_frame = new_frame_func()
    current_frame.pack(fill="both", expand=True)


def main_screen():

    frame = tk.Frame(root)

    tk.Label(frame,text="Smart Expense Manager",font=("Arial",16)).pack(pady=20)

    tk.Button(frame,text="Add Income",width=25,command=lambda:switch_frame(add_income_screen)).pack(pady=5)
    tk.Button(frame,text="Add Expense",width=25,command=lambda:switch_frame(add_expense_screen)).pack(pady=5)
    tk.Button(frame,text="View Transactions",width=25,command=lambda:switch_frame(view_transactions_screen)).pack(pady=5)
    tk.Button(frame,text="Reports",width=25,command=lambda:switch_frame(reports_screen)).pack(pady=5)

    tk.Button(frame,text="Train ML Model",width=25,command=train_ml).pack(pady=5)
    tk.Button(frame,text="Predict Category",width=25,command=lambda:switch_frame(predict_screen)).pack(pady=5)


    def load_and_notify():
        try:
            manager.load_data()
            messagebox.showinfo("Success","Data Loaded Successfully")
        except FileNotFoundError:
            messagebox.showerror("Error","No saved data found")


    tk.Button(frame,text="Save Data",width=25,command=manager.save_data).pack(pady=5)
    tk.Button(frame,text="Load Data",width=25,command=load_and_notify).pack(pady=5)

    return frame



def add_income_screen():

    frame=tk.Frame(root)

    tk.Label(frame,text="Add Income",font=("Arial",14)).pack(pady=10)

    tk.Label(frame,text="Amount").pack()
    amount_entry=tk.Entry(frame)
    amount_entry.pack()

    tk.Label(frame,text="Category").pack()
    category_entry=tk.Entry(frame)
    category_entry.pack()

    tk.Label(frame,text="Date").pack()
    date_entry=tk.Entry(frame)
    date_entry.pack()

    tk.Label(frame,text="Note").pack()
    note_entry=tk.Entry(frame)
    note_entry.pack()


    def save():

        try:
            amount=int(amount_entry.get())
        except:
            messagebox.showerror("Error","Enter valid number")
            return

        manager.add_income(amount,category_entry.get(),date_entry.get(),note_entry.get())

        messagebox.showinfo("Success","Income Added")
        switch_frame(main_screen)


    tk.Button(frame,text="Save",command=save).pack(pady=10)
    tk.Button(frame,text="Back",command=lambda:switch_frame(main_screen)).pack()

    return frame



def add_expense_screen():

    frame=tk.Frame(root)

    tk.Label(frame,text="Add Expense",font=("Arial",14)).pack(pady=10)

    tk.Label(frame,text="Amount").pack()
    amount_entry=tk.Entry(frame)
    amount_entry.pack()

    tk.Label(frame,text="Category").pack()
    category_entry=tk.Entry(frame)
    category_entry.pack()

    tk.Label(frame,text="Date").pack()
    date_entry=tk.Entry(frame)
    date_entry.pack()

    tk.Label(frame,text="Note").pack()
    note_entry=tk.Entry(frame)
    note_entry.pack()


    def save():

        try:
            amount=int(amount_entry.get())
        except:
            messagebox.showerror("Error","Enter valid number")
            return

        manager.add_expense(amount,category_entry.get(),date_entry.get(),note_entry.get())

        messagebox.showinfo("Success","Expense Added")
        switch_frame(main_screen)


    tk.Button(frame,text="Save",command=save).pack(pady=10)
    tk.Button(frame,text="Back",command=lambda:switch_frame(main_screen)).pack()

    return frame



def view_transactions_screen():

    frame=tk.Frame(root)

    tk.Label(frame,text="All Transactions",font=("Arial",14)).pack(pady=10)

    listbox=tk.Listbox(frame,width=45)
    listbox.pack(fill="both",expand=True)

    for i in manager.view_transactions():
        listbox.insert(tk.END,f"{i.transaction_type} | {i.amount} | {i.category} | {i.date}")


    tk.Button(frame,text="Back",command=lambda:switch_frame(main_screen)).pack(pady=5)

    return frame





def reports_screen():

    frame=tk.Frame(root)

    tk.Label(frame,text="Reports",font=("Arial",14)).pack(pady=10)

    total_income,total_expense,balance=manager.calculate_balance()

    tk.Label(frame,text=f"Total Income: {total_income}").pack()
    tk.Label(frame,text=f"Total Expense: {total_expense}").pack()
    tk.Label(frame,text=f"Balance: {balance}").pack()


    average=manager.average_expense()
    highest=manager.highest_expense()
    lowest=manager.lowest_expense()
    category,amount=manager.most_spending_category()


    tk.Label(frame,text=f"Average Expense: {average}").pack()
    tk.Label(frame,text=f"Highest Expense: {highest}").pack()
    tk.Label(frame,text=f"Lowest Expense: {lowest}").pack()
    tk.Label(frame,text=f"Most Spending Category: {category}").pack()


    tk.Button(frame,text="Bar Chart",command=manager.show_chart).pack(pady=5)
    tk.Button(frame,text="Pie Chart",command=manager.show_pie_chart).pack(pady=5)

    tk.Button(frame,text="Back",command=lambda:switch_frame(main_screen)).pack(pady=10)

    return frame


# Ml


def train_ml():

    try:
        manager.train_model()
        messagebox.showinfo("ML","Model Trained Successfully")

    except Exception as e:
        messagebox.showerror("Error",str(e))



def predict_screen():

    frame=tk.Frame(root)

    tk.Label(frame,text="Predict Expense Category",font=("Arial",14)).pack(pady=10)


    tk.Label(frame,text="Enter Amount").pack()

    amount_entry=tk.Entry(frame)
    amount_entry.pack(pady=5)


    result=tk.Label(frame,text="")
    result.pack(pady=10)


    def predict():

        try:
            amount=int(amount_entry.get())

            category=manager.predict_category(amount)

            result.config(text="Predicted Category: "+category)

        except Exception as e:
            messagebox.showerror("Error",str(e))



    tk.Button(frame,text="Predict",command=predict).pack(pady=5)

    tk.Button(frame,text="Back",command=lambda:switch_frame(main_screen)).pack(pady=5)


    return frame



switch_frame(main_screen)

root.mainloop()