import tkinter as tk
import random

# Sudoku-Generator
def generate_sudoku():
    base = 3
    side = base * base

    def pattern(r, c): return (base * (r % base) + r // base + c) % side
    def shuffle(s): return random.sample(s, len(s))

    rBase = range(base)
    rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums = shuffle(range(1, side + 1))

    board = [[nums[pattern(r, c)] for c in cols] for r in rows]

    # Lücken erzeugen
    squares = side * side
    empties = random.randint(40, 50)
    for _ in range(empties):
        board[random.randint(0, side - 1)][random.randint(0, side - 1)] = 0

    return board

# GUI erstellen
def create_sudoku_gui(board):
    def check_solution():
        for r in range(9):
            for c in range(9):
                val = entries[r][c].get()
                if val.isdigit():
                    board[r][c] = int(val)
                else:
                    board[r][c] = 0
        if all(all(cell != 0 for cell in row) for row in board):
            status.config(text="Fertig (nicht geprüft)")
        else:
            status.config(text="Noch nicht vollständig")

    root = tk.Tk()
    root.title("🧩 Sudoku")

    frame = tk.Frame(root)
    frame.pack()

    global entries
    entries = []

    for r in range(9):
        row = []
        for c in range(9):
            val = board[r][c]
            entry = tk.Entry(frame, width=2, font=("Arial", 18), justify="center")
            if val != 0:
                entry.insert(0, str(val))
                entry.config(state="disabled")
            entry.grid(row=r, column=c, padx=2, pady=2)
            row.append(entry)
        entries.append(row)

    tk.Button(root, text="Prüfen", command=check_solution).pack(pady=10)
    global status
    status = tk.Label(root, text="")
    status.pack()

    root.mainloop()

# Programmstart
sudoku_board = generate_sudoku()
create_sudoku_gui(sudoku_board)