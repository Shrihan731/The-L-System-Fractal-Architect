# 🌿 L-System Fractal Architect

## 📌 Project Overview
The **L-System Fractal Architect** is a Python-based graphical application that generates **fractal patterns** such as trees and plants using **Lindenmayer Systems (L-systems)**.  
The project combines **Tkinter** for the graphical user interface and **Turtle Graphics** for rendering fractals inside the same window.

This project demonstrates concepts from:
- Formal grammars
- Recursion and iteration
- Stack-based state management
- Computer graphics
- GUI programming

---

## 🧠 What is an L-System?
An **L-System (Lindenmayer System)** is a rule-based system used to model natural growth processes like plants and trees.

An L-System consists of:
- **Axiom**: The starting string
- **Production Rules**: Rules that replace symbols
- **Iterations**: Number of times rules are applied
- **Angle**: Rotation angle for drawing

Each iteration expands the string, increasing the complexity of the structure.

---

## ✨ Features
- Interactive GUI built using **Tkinter**
- Turtle graphics embedded inside Tkinter using `RawTurtle`
- User-defined:
  - Axiom
  - Production rules
  - Angle
  - Iterations
- Branching using `[` and `]` symbols (stack-based)
- Gradient coloring for visual depth
- Animated drawing using controlled tracer settings
- Efficient rendering without GUI freezing
- Single-file Python implementation
- No external libraries required

---

## 🛠️ Technologies Used
- **Python 3**
- **Tkinter** (built-in GUI library)
- **Turtle Graphics** (built-in drawing module)

> ⚠️ No external packages are required.

---

## 📂 Project Structure


---

## ▶️ How to Run the Project

### Step 1: Install Python
Download and install Python from:
https://www.python.org



✔️ Make sure to check **“Add Python to PATH”** during installation.

---

### Step 2: Run the Program
Open a terminal or command prompt in the project folder and run:
python lsystem.py


---

## 🎮 How to Use the Application

1. **Axiom**  
   - Starting symbol (e.g., `F`)

2. **Rules**  
   - One rule per line  
   - Format:  
     ```
     Symbol:Replacement
     ```
   - Example:
     ```
     F:F[+F]F[-F]F
     ```

3. **Angle**  
   - Rotation angle in degrees (e.g., `25`)

4. **Iterations**  
   - Number of times rules are applied  
   - Recommended: `4 – 6`

5. Click **Generate** to draw the fractal.

---

## 🌳 Example Input (Tree)
Axiom: F
Rules:
F:FF[-F]F
Angle: 25
Iterations: 5


---

## ❄️ Example Input (Koch Snowflake)
Axiom: F--F--F
Rules:
F:F+F--F+F
Angle: 60
Iterations: 4

---

## ⚠️ Important Notes
- Iterations grow **exponentially**
- Very high values (e.g., 50 or 100) will freeze the system
- Recommended maximum iterations:
  - Trees: 5–6
  - Koch Snowflake: 4–5

---

## 🧠 Key Concepts Demonstrated
- Parallel string rewriting
- Exponential growth
- Stack-based branching
- Event-driven GUI programming
- Embedded turtle graphics
- Performance optimization using tracer control

---

## 🧪 Performance Optimization
The project uses:
```python
screen.tracer(1, 10)
This allows smooth animation while maintaining responsiveness
