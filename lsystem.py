import tkinter as tk
import turtle

# ---------------- WINDOW SETUP ----------------
root = tk.Tk()
root.title("L-System Fractal Architect")
root.geometry("1000x700")

canvas = tk.Canvas(root, width=700, height=700, bg="white")
canvas.pack(side=tk.LEFT)

screen = turtle.TurtleScreen(canvas)
t = turtle.RawTurtle(screen)
t.hideturtle()
t.speed(0)

# ---------------- CONTROL PANEL ----------------
control_frame = tk.Frame(root, padx=10)
control_frame.pack(side=tk.RIGHT, fill=tk.Y)

tk.Label(control_frame, text="Axiom").pack(anchor="w")
axiom_entry = tk.Entry(control_frame)
axiom_entry.insert(0, "F")
axiom_entry.pack(fill="x", pady=5)

tk.Label(control_frame, text="Rules (one per line)").pack(anchor="w")
rules_text = tk.Text(control_frame, height=5)
rules_text.insert("1.0", "F:F[+F]F[-F]F")
rules_text.pack(fill="x", pady=5)

tk.Label(control_frame, text="Angle").pack(anchor="w")
angle_entry = tk.Entry(control_frame)
angle_entry.insert(0, "25")
angle_entry.pack(fill="x", pady=5)

tk.Label(control_frame, text="Iterations").pack(anchor="w")
iter_entry = tk.Entry(control_frame)
iter_entry.insert(0, "5")
iter_entry.pack(fill="x", pady=5)

# ---------------- LOGIC ----------------
def expand_lsystem(axiom, rules, iterations):
    current = axiom
    for _ in range(iterations):
        next_string = ""
        for ch in current:
            next_string += rules.get(ch, ch)
        current = next_string
    return current

def parse_rules(text):
    rules = {}
    for line in text.strip().split("\n"):
        if ":" in line:
            k, v = line.split(":")
            rules[k.strip()] = v.strip()
    return rules

def draw(commands, angle):
    t.clear()
    t.penup()
    t.goto(0, -250)
    t.setheading(90)
    t.pendown()

    stack = []
    turtle.tracer(0, 0)

    for i, c in enumerate(commands):
        t.pencolor(0, i / len(commands), 0)

        if c == "F":
            t.forward(10)
        elif c == "+":
            t.right(angle)
        elif c == "-":
            t.left(angle)
        elif c == "[":
            stack.append((t.position(), t.heading()))
        elif c == "]":
            pos, head = stack.pop()
            t.penup()
            t.goto(pos)
            t.setheading(head)
            t.pendown()

    turtle.update()

def generate():
    axiom = axiom_entry.get()
    rules = parse_rules(rules_text.get("1.0", tk.END))
    angle = float(angle_entry.get())
    iterations = int(iter_entry.get())

    final = expand_lsystem(axiom, rules, iterations)
    draw(final, angle)

tk.Button(
    control_frame,
    text="Generate",
    command=generate,
    bg="black",
    fg="white"
).pack(pady=20, fill="x")

# ---------------- START APP ----------------
root.mainloop()
