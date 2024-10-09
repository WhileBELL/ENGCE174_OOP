import tkinter as tk


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create the entry field
        self.entry = tk.Entry(master, width=30, justify="right", font=("Arial", 16))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create the buttons
        self.create_button("1", 1, 0)
        self.create_button("2", 1, 1)
        self.create_button("3", 1, 2)
        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("7", 3, 0)
        self.create_button("8", 3, 1)
        self.create_button("9", 3, 2)
        self.create_button("0", 4, 1)
        self.create_button(".", 4, 2)

        self.create_button("+", 1, 3)
        self.create_button("-", 2, 3)
        self.create_button("*", 3, 3)
        self.create_button("/", 4, 3)

        self.create_button("=", 4, 0)
        self.create_button("C", 5, 0)
        self.create_button("CE", 5, 1)
        self.create_button("(", 5, 2)
        self.create_button(")", 5, 3)

        self.decimal_added = (
            False  # Track if decimal has been added to the current number
        )
        self.left_paren_count = 0  # Track the number of open parentheses

        # New variables to track last operation
        self.last_operator = ""
        self.last_operand = ""
        self.result = None

    def create_button(self, text, row, column):
        button = tk.Button(
            self.master,
            text=text,
            width=5,
            height=2,
            font=("Arial", 16),
            command=lambda: self.button_click(text),
        )
        button.grid(row=row, column=column, padx=5, pady=5)

    def button_click(self, text):
        current = self.entry.get()

        if text == "=":
            try:
                if self.result is None:  # First time pressing "="
                    # Validate expression before evaluating
                    if self.is_valid_expression(current):
                        self.result = str(eval(current))
                        self.last_operator, self.last_operand = (
                            self.extract_last_operation(current)
                        )
                        self.entry.delete(0, tk.END)
                        self.entry.insert(0, self.result)
                else:
                    # Reuse the last operation and operand
                    new_expression = (
                        f"{self.result}{self.last_operator}{self.last_operand}"
                    )
                    self.result = str(eval(new_expression))
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, self.result)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")

        elif text == "C":
            self.entry.delete(0, tk.END)
            self.decimal_added = False
            self.left_paren_count = 0
            self.result = None  # Reset result and last operation
            self.last_operator = ""
            self.last_operand = ""

        elif text == "CE":
            self.entry.delete(len(current) - 1, tk.END)
            if current.endswith("."):
                self.decimal_added = False

        elif text == ".":
            if not self.decimal_added:
                self.entry.insert(tk.END, text)
                self.decimal_added = True

        elif text == "(":
            self.entry.insert(tk.END, text)
            self.left_paren_count += 1

        elif text == ")":
            if (
                self.left_paren_count > 0
            ):  # Only allow closing parenthesis if there's an open one
                self.entry.insert(tk.END, text)
                self.left_paren_count -= 1

        else:
            if text in "+-*/":  # Reset decimal flag after an operator
                self.decimal_added = False
            self.entry.insert(tk.END, text)
            self.result = None  # Reset result when a new expression is being entered

    def extract_last_operation(self, expression):
        """Extract the last operation and operand from the expression."""
        operators = "+-*/"
        for i in range(len(expression) - 1, -1, -1):
            if expression[i] in operators:
                return expression[i], expression[i + 1 :]
        return "", ""

    def is_valid_expression(self, expression):
        """Check if the expression is valid before evaluation."""
        # Check if there are equal open and close parentheses
        if expression.count("(") != expression.count(")"):
            return False
        # Avoid evaluating empty expressions or incomplete operations
        if expression and expression[-1] in "+-*/(":
            return False
        return True


root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
