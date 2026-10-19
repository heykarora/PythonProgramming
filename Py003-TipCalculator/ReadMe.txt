# 💸 Tip Calculator
A beginner-friendly Python project that calculates the total bill after adding a tip and splits the amount equally among a group of people.

## 📌 About the Project
The Tip Calculator is a command-line application built using Python. It asks the user for the total bill amount, the desired tip percentage, and the number of people sharing the bill.
It then calculates the bill with the tip included and determines how much each person should pay.

## ✨ Features
- Accepts the total bill amount.
- Allows the user to enter a tip percentage.
- Takes the number of people sharing the bill.
- Calculates the tip amount and adds it to the original bill.
- Splits the final bill equally among all participants.
- Displays the amount each person needs to pay.

## 🛠️ Technologies Used
- **Language:** Python 3
- **Concepts:** `print()`, `input()`, variables, `float()`, `int()`, arithmetic operators, and mathematical calculations.

## 🧮 How It Works
The program uses the following formulas:

**1. Calculate the tip amount**
```text
Tip Amount = Total Bill × Tip Percentage / 100
```

**2. Calculate the bill after adding the tip**
```text
Bill with Tip = Total Bill + Tip Amount
```

**3. Calculate each person's share**
```text
Amount Per Person = Bill with Tip / Number of People
```

## 🚀 How to Run
1. Install Python 3 on your computer.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run the following command:

```bash
python main.py
```

Alternatively, use `python3` if that is the command configured on your system:

```bash
python3 main.py
```

## 💻 Example Output
```text
Welcome to tip calculator!
Enter the total bill amount :
1500
How much tip would you like to leave (10, 12, 15):
12
Among how many people to split the bill? :
3
560.0
```

**Calculation:**
- Total bill: ₹1,500
- Tip percentage: 12%
- Tip amount: ₹180
- Bill including tip: ₹1,680
- Number of people: 3
- **Amount per person: ₹560**
*The example uses rupees, but the program works with other currencies too.*

## 📚 What I Learned
By building this project, I practiced:
- Collecting user input with `input()`.
- Converting strings into numbers using `float()` and `int()`.
- Performing calculations using arithmetic operators.
- Calculating percentages.
- Dividing a total amount equally among multiple people.
- Storing intermediate and final results in variables.

## 🔮 Future Improvements
- Round each person's share to two decimal places.
- Add input validation for invalid bill amounts and the number of people.
- Allow users to choose from preset tip percentages.
- Display the tip amount and total bill separately.
- Improve the output formatting for a cleaner user experience.

## 👨‍💻 Project Status
Completed — beginner Python practice project.

---

**Built with Python 🐍 | Part of my Python beginner projects collection.**
