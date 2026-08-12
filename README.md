# ✈️ Aircraft Flight Performance Calculator

A physics-based Python application for analyzing fundamental aircraft flight-performance parameters using atmospheric conditions, wing geometry, angle of attack, and aircraft weight.

The calculator models a simplified International Standard Atmosphere (ISA), calculates aerodynamic lift and drag, estimates stall speed, and evaluates whether the available lift is sufficient to support the aircraft's weight under the entered flight conditions.

> **Project Type:** Aerospace Engineering / Aerodynamics / Python
> **Model:** Simplified educational aerodynamic model
> **Language:** Python 3.x

---

## 🚀 Key Features

### 🌡️ Atmospheric Model

Calculates atmospheric properties based on altitude using a simplified ISA model:

* Temperature
* Atmospheric pressure
* Air density
* Temperature conversion to °C

### 📐 Wing Geometry Analysis

Calculates fundamental wing parameters from the entered geometry:

* Wing area
* Aspect ratio

### 🛫 Angle of Attack & Stall Analysis

Evaluates the entered angle of attack against a defined stall-angle assumption.

* Angle-of-attack based lift coefficient
* Stall warning
* Critical flight-condition detection

### ⬆️ Lift Force Calculation

Calculates aerodynamic lift using:

[
L = \frac{1}{2}\rho V^2 S C_L
]

Where:

* (L) = Lift force (N)
* (\rho) = Air density (kg/m³)
* (V) = Velocity (m/s)
* (S) = Wing area (m²)
* (C_L) = Lift coefficient

### ⬇️ Drag Analysis

The calculator estimates induced drag and total aerodynamic drag using:

* Baseline parasite drag coefficient
* Aspect ratio
* Oswald efficiency factor
* Induced drag coefficient

### 🛬 Stall Speed Estimation

Estimates minimum stall speed from:

* Aircraft weight
* Air density
* Wing area
* Assumed maximum lift coefficient

### ⚖️ Lift-to-Weight Analysis

Calculates the ratio between generated lift and aircraft weight to evaluate the entered flight condition.

### 📊 Flight Performance Report

Generates a formatted command-line report containing:

* Temperature
* Pressure
* Air density
* Wing area
* Aspect ratio
* Calculated lift coefficient
* Lift force
* Total drag
* Estimated stall speed
* Lift-to-weight ratio
* Flight-condition evaluation

---

## 🧮 Aerodynamic Model

The project uses several simplified aerodynamic relationships.

### Lift

[
L = \frac{1}{2}\rho V^2 S C_L
]

### Wing Aspect Ratio

[
AR = \frac{b^2}{S}
]

### Induced Drag Coefficient

[
C_{D_i} = \frac{C_L^2}{\pi AR e}
]

### Total Drag Coefficient

[
C_D = C_{D0} + C_{D_i}
]

### Total Drag

[
D = \frac{1}{2}\rho V^2 S C_D
]

### Stall Speed

[
V_{stall} =
\sqrt{\frac{2W}{\rho S C_{L_{max}}}}
]

---

## 🧠 Concepts Demonstrated

This project demonstrates practical use of Python programming concepts together with fundamental aerospace engineering calculations.

### Python

* Functions
* Variables and constants
* User input
* Floating-point calculations
* Mathematical operations
* Conditional logic
* Formatted output
* The `math` module

### Aerospace Engineering

* Aerodynamic lift
* Aerodynamic drag
* Air density
* ISA atmospheric model
* Wing geometry
* Aspect ratio
* Angle of attack
* Stall conditions
* Stall speed
* Lift-to-weight ratio

---

## 📥 User Inputs

The calculator requires the following flight parameters:

| Parameter       | Unit    |
| --------------- | ------- |
| Velocity        | m/s     |
| Altitude        | m       |
| Wingspan        | m       |
| Mean Chord      | m       |
| Angle of Attack | degrees |
| Aircraft Weight | N       |

---

## 📤 Output

The program generates a **Flight Performance Report** containing the calculated aerodynamic and atmospheric parameters.

Example output categories:

```text
FLIGHT PERFORMANCE REPORT

Temperature
Pressure
Density
Wing Area
Aspect Ratio
Calculated CL
Lift Force
Total Drag
Minimum Stall Speed
Lift-to-Weight Ratio
Flight Evaluation
```

---

## ⚙️ How to Run

### Option 1 — Python

Make sure Python 3.x is installed.

Run:

```bash
python lift_calculator.py
```

Follow the prompts and enter the required aircraft parameters.

### Option 2 — Google Colab

1. Open Google Colab.
2. Create a new notebook.
3. Paste the Python code into a code cell.
4. Run the cell.
5. Enter the requested parameters when prompted.

---

## 📁 Project Structure

```text
Aircraft-Flight-Performance-Calculator/
│
├── lift_calculator.py
├── README.md
└── screenshots/
```

---

## ⚠️ Model Limitations

This project is an **educational aerodynamic model**, not a certified aircraft-performance analysis tool.

Several aerodynamic parameters are simplified or assumed, including:

* Linearized (C_L) relationship with angle of attack
* Fixed stall-angle assumption
* Fixed maximum lift coefficient
* Simplified parasite drag coefficient
* Constant Oswald efficiency factor
* ISA atmosphere model within its applicable simplified range

Real aircraft performance analysis requires experimentally validated aerodynamic data, airfoil characteristics, Reynolds/Mach number effects, compressibility, aircraft configuration, propulsion performance, and additional flight conditions.

---

## 🔮 Future Improvements

Planned improvements may include:

* 📈 Lift and drag performance graphs
* 📊 Dynamic (C_L) vs. angle-of-attack curves
* 🛩️ Aircraft-specific aerodynamic profiles
* 🌡️ Extended atmospheric modeling
* 📉 Drag polar visualization
* 📐 More detailed wing geometry calculations
* 🖥️ Graphical user interface
* 📄 Automated performance-report generation
* 🧪 Validation against published/reference aircraft data

---

## 🎯 Project Purpose

The purpose of this project is to combine **Python programming with fundamental aerospace engineering principles** to create a practical aircraft-performance analysis tool.

It was developed as a learning project to explore how programming can be applied to aerodynamic calculations and flight-performance analysis.

---

## 👨‍💻 Author

**Muhammad Talha**

Aspiring Aerospace Engineer | Python & C++ Developer | RC Aircraft Designer & Builder

---

## 📜 License

This project is available under the **MIT License**.

---

> **Disclaimer:** This software is intended for educational and experimental purposes only. The calculations are based on simplified aerodynamic assumptions and should not be used for real-world aircraft certification, flight-safety decisions, or operational planning.
