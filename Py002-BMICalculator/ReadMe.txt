# ⚖️ BMI Calculator
A beginner-friendly Python project that calculates Body Mass Index (BMI) using a user's weight and height, then displays a weight category based on the calculated result.

## 📌 About the Project
The BMI Calculator is a command-line application built using Python. It takes the user's weight in kilograms and height in meters, calculates their BMI, and displays a category based on the result.
This project helps beginners understand mathematical operations, user input, type conversion, and conditional statements in Python.

## ✨ Features
- Displays a welcome message.
- Accepts weight in kilograms.
- Accepts height in meters.
- Calculates BMI using the standard formula.
- Classifies the result using `if`, `elif`, and `else` statements.
- Displays the calculated BMI and the corresponding category.

## 🛠️ Technologies Used
- **Language:** Python 3
- **Concepts:** `print()`, `input()`, variables, `float()`, arithmetic operators, conditional statements, and comparison operators.

## 🧮 BMI Formula
BMI is calculated using the following formula:

**BMI = Weight (kg) / Height (m)²**
For example, if a person weighs 70 kg and has a height of 1.75 m:
```text
BMI = 70 / (1.75 × 1.75)
BMI ≈ 22.86
```

## 🚀 How to Run
1. Install Python 3 on your computer.
2. Download or clone this repository.
3. Open a terminal in the project directory.
4. Run the following command:

```bash
main.py
```

Alternatively, on systems using `python3`:

```bash
main.py
```

## 💻 Example Output
```text
Welcome to BMI Calculator!
Enter your weight (in kgs.) :
70
Enter your height (in meters) : 
1.75
22.857142857142858
You have normal weight!
```

## 📊 BMI Categories in This Program
| BMI value | Displayed category |
|---|---|
| Below 18.5 | Underweight |
| 18.5 to 25, inclusive | Normal weight |
| Above 25 | Overweight |

*Note: These are the categories implemented in this project, not a complete medical assessment. For adults, standard BMI categories generally classify 25.0 and above as overweight. BMI is a screening measure, not a diagnosis.*

## 📚 What I Learned\
By building this project, I practiced:
- Taking user input with `input()`.
- Converting input strings into floating-point numbers with `float()`.
- Performing mathematical calculations using arithmetic operators.
- Using the exponentiation operator (`**`) to square a number.
- Applying `if`, `elif`, and `else` statements.
- Comparing numerical values using comparison operators.

## 🔮 Future Improvements
- Format the BMI output to two decimal places.
- Handle invalid inputs and prevent division by zero.
- Improve BMI category boundaries.
- Add a loop to calculate BMI for multiple users.

## 👨‍💻 Project Status
Completed — beginner Python practice project.

---

**Built with Python 🐍 | Part of my Python beginner projects collection.**