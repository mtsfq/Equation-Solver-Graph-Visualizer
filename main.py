# (واجهه المستخدم) هذا الملف يحتوي على الكود الرئيسي للتطبيق 

import customtkinter as ctk

from graph import plot_graph

from solver import solve_equation

from calculus import (
    derivative,
    integral
)

ctk.set_appearance_mode("dark")

app = ctk.CTk()

app.geometry("900x700")

app.title("РУМ")


title = ctk.CTkLabel(
    app,
    text="РУМ",
    font=("Arial",30)
)

title.pack(pady=20)


entry = ctk.CTkEntry(
    app,
    width=500,
    height=40,
    placeholder_text="Введите выражение..."
)

entry.pack(pady=20)


result_label = ctk.CTkLabel(
    app,
    text="Результат:",
    font=("Arial",20)
)

result_label.pack(pady=20)


def solve_click():

    expression = entry.get()

    result = solve_equation(
        expression
    )

    result_label.configure(
        text=f"Результат: {result}"
    )

def derivative_click():

    expression = entry.get()

    result = derivative(
        expression
    )

    result_label.configure(
        text=f"Производная: {result}"
    )

def graph_click():

    expression = entry.get()

    plot_graph(
        expression
    )

def integral_click():

    expression = entry.get()

    result = integral(
        expression
    )

    result_label.configure(
        text=f"Интеграл: {result}"
    )

solve_button = ctk.CTkButton(
    app,
    text="Решить",
    command=solve_click
)

solve_button.pack(pady=20)

derivative_button = ctk.CTkButton(
    app,
    text="Производная",
    command=derivative_click
)

derivative_button.pack(
    pady=10
)

integral_button = ctk.CTkButton(
    app,
    text="Интеграл",
    command=integral_click
)

integral_button.pack(
    pady=10
)

graph_button = ctk.CTkButton(
    app,
    text="График",
    command=graph_click
)

graph_button.pack(
    pady=10
)

app.mainloop()