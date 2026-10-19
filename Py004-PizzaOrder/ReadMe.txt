# 🍕 Py Pizza Order
A beginner-friendly Python project that simulates a pizza ordering system and calculates the total bill based on pizza size and optional toppings.

## 📌 About the Project
Py Pizza Order is a command-line application built using Python. It asks customers to choose their pizza size, select whether they want pepperoni, and decide if they would like extra cheese.
The program calculates the final bill based on the customer's choices and displays the total amount.

## ✨ Features
- Offers three pizza sizes: Small, Medium, and Large.
- Allows customers to add pepperoni.
- Provides an option for extra cheese.
- Calculates the price based on the selected size and toppings.
- Accepts uppercase and lowercase inputs for size and topping choices.
- Displays the final bill.

## 🛠️ Technologies Used
- **Language:** Python 3
- **Concepts:** `print()`, `input()`, variables, `lower()`, arithmetic operators, `if`, `elif`, and nested conditional statements.

## 💰 Pricing
| Item | Price |
|---|---:|
| Small pizza | 15 |
| Medium pizza | 20 |
| Large pizza | 25 |
| Pepperoni on small pizza | +2 |
| Pepperoni on medium or large pizza | +3 |
| Extra cheese | +1 |
*Prices are shown in unspecified currency units, matching the original program.*

## 🧮 How It Works
1. The program displays a welcome message.
2. The customer chooses a pizza size.
3. The customer decides whether to add pepperoni.
4. The customer decides whether to add extra cheese.
5. The program calculates the bill using conditional statements.
6. The final bill is displayed.

## 🚀 How to Run
1. Make sure Python 3 is installed on your computer.
2. Open your terminal in the main Git repository.
3. Navigate to the project folder:
```bash
cd py-pizza-order
```

4. Run the Python program:
```bash
python main.py
```

If your system uses `python3`, run:

```bash
python3 main.py
```

## 💻 Example Output
```text
Welcome to PyPizza, please state your order!
What size would you like? (S, M, L) :
M
Would you like pepporoni in your pizza? (y/n)
y
Would you like extra cheese? (y/n) :
y
Your total bill is :
24
```

**Example calculation:**
- Medium pizza: 20
- Pepperoni: +3
- Extra cheese: +1
- **Total bill: 24**

## 📚 What I Learned
Through this project, I practiced:
- Collecting user input using `input()`.
- Converting input to lowercase using `.lower()`.
- Using variables to store customer choices.
- Initializing and updating a bill using `bill = 0` and `+=`.
- Using `if` and `elif` statements to determine prices.
- Applying nested conditional statements.
- Combining multiple conditions to calculate a final amount.

## 🔮 Future Improvements
- Validate pizza sizes and topping choices.
- Display an error message for invalid inputs.
- Allow customers to order multiple pizzas.
- Add more toppings and customization options.
- Display an itemized bill instead of only the total.

## 👨‍💻 Project Status
Completed — beginner Python practice project.

---

**Built with Python 🐍 | Part of my Python beginner projects collection.**
