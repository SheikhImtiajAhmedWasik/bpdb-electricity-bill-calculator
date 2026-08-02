<div align="center">

# ⚡ BPDB Electricity Bill Calculator

### 🐍 A Python Console Application for Calculating Residential Electricity Bills (LT-A)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![CLI](https://img.shields.io/badge/Application-Console-success?style=for-the-badge)
![BPDB](https://img.shields.io/badge/BPDB-LT--A-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Personal_Project-red?style=for-the-badge)

</div>

---

# ⚡ Overview

Have you ever wondered:

> **"How much will my electricity bill be this month if I already know my total electricity usage?"**

The Bangladesh Power Development Board (BPDB) publishes electricity tariff rates, but there is no simple calculator or public API to instantly calculate the final bill.

This project solves that problem.

The application calculates the **Residential (LT-A)** electricity bill based on the official BPDB tariff, including:

- ⚡ Step-wise electricity charges
- 💰 Demand Charge
- 🧾 VAT
- 📊 Final payable amount

Simply enter your:

- Total electricity usage (Units)
- Demand Load (KW)

and the program calculates your estimated electricity bill.

---

# 🎯 Objective

Develop a Python console application that accurately calculates **BPDB Residential (LT-A)** electricity bills using the official step tariff system.

The application demonstrates:

- Functions
- Conditional Statements
- Mathematical Calculations
- Modular Programming
- Real-world Problem Solving

---

# ✨ Features

✅ Calculate Residential Electricity Bill

✅ Supports BPDB LT-A Tariff

✅ Automatic Step-wise Unit Calculation

✅ Demand Charge Calculation

✅ VAT Included

✅ Clean Console Interface

✅ Simple User Input

---

# 📋 Tariff Information

## Residential (LT-A)

| Usage | Rate |
|-------:|------|
| Life Line (0–50 Units) | **Tk 4.63 / Unit** |
| Step 1 (0–75 Units) | **Tk 5.26 / Unit** |
| Step 2 (76–200 Units) | **Tk 8.50 / Unit** |
| Step 3 (201–300 Units) | **Tk 9.10 / Unit** |
| Step 4 (301–400 Units) | **Tk 9.62 / Unit** |
| Step 5 (401–600 Units) | **Tk 15.01 / Unit** |
| Step 6 (601+ Units) | **Tk 17.35 / Unit** |

### Demand Charge

```
Tk 42 / KW per month
```

---

# 📥 User Input

The user only needs to provide two values.

```text
Total Units Used

Demand Load (KW)
```

Example

```text
Total Units : 451

Demand Load in KW(Its generally 1 or 2 in LT-A) : 2 
```

---

# 📤 Output

The application calculates and displays

```text
Total Bill

Demand Charge

VAT

Final Payable Amount
```

Example

```text
=================================

Electricity Bill

=================================

Total Units : 451

Demand Load : 2 KW

Energy Charge : xxxx.xx Tk

Demand Charge : xx.xx Tk

VAT : xx.xx Tk

----------------------------

Total Amount : xxxx.xx Tk

=================================
```

---

# ⚙️ Functional Requirements

The calculation follows the official BPDB tariff system.

If the electricity usage qualifies for the **Life Line** tariff (0–50 units), the bill is calculated using the Life Line rate.

Otherwise, the application automatically switches to the **Step Tariff** calculation.

---

## Step Functions

```python
life_line()

step1()

step2()

step3()

step4()

step5()

step6()
```

---

## Step Processing Logic

Each step calculates only its own unit range and then passes the remaining units to the previous tariff step.

Example

```
451 Units
```

Calculation flow

```
Step 5

↓

Remaining Units

↓

Step 4

↓

Step 3

↓

Step 2

↓

Step 1
```

This ensures the bill is calculated exactly according to the BPDB step tariff system.

---

# 🚀 Program Workflow

```text
Start Program
        │
        ▼
Input Total Units
        │
        ▼
Input Demand Load
        │
        ▼
Check Life Line Eligibility
        │
        ├──────────────► Life Line
        │
        ▼
Step-wise Calculation
        │
        ▼
Calculate Demand Charge
        │
        ▼
Calculate VAT
        │
        ▼
Display Final Bill
        │
        ▼
Exit
```

---

# 🧮 Example

Suppose

```text
Units Used : 451

Demand Load : 2 KW
```

The application automatically calculates

- Step 5
- Step 4
- Step 3
- Step 2
- Step 1
- Demand Charge
- VAT

Finally,

```text
Total Amount Payable
```

---

# 🛠 Python Concepts Used

| Concept | Used |
|---------|:----:|
| Variables | ✅ |
| Functions | ✅ |
| User Input | ✅ |
| Mathematical Operations | ✅ |
| Conditional Statements | ✅ |
| Function Chaining | ✅ |
| Modular Programming | ✅ |

---

# 📂 Project Structure

```text
bpdb_bill_calculator.py

│

├── life_line()

├── step1()

├── step2()

├── step3()

├── step4()

├── step5()

├── step6()

├── calculate_vat()

├── calculate_demand_charge()

├── main()
```

---

# ⚠️ Validation

The application validates:

- Negative Units
- Invalid Numbers
- Empty Input
- Invalid Demand Load

The program should never terminate unexpectedly because of invalid user input.

---

# 📚 Data Source

The tariff rates used in this application were collected from the official **Bangladesh Power Development Board (BPDB)** residential electricity tariff notice.

Since BPDB does not currently provide a public API or machine-readable dataset for tariff calculations, the pricing information has been manually incorporated into the application.

---

# 💡 Future Improvements

Possible future enhancements include:

- 📱 Graphical User Interface (GUI)
- 🌐 Web Application
- 📊 Monthly Bill History
- 💾 Save Bills as PDF
- 📈 Consumption Analysis
- 🔄 Automatic Tariff Updates
- ☁️ Online API (if available)

---

<div align="center">

## ⭐ Built with Python

A practical utility application that helps Bangladeshi residential consumers estimate their electricity bills using the official **BPDB LT-A tariff structure**.

If you found this project useful, consider giving it a ⭐ on GitHub!

</div>
