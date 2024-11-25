import tkinter as tk
from tkinter import messagebox
import os

def quick_sort(arr, text_widget, depth=0):
    """
    Implementación del algoritmo Quick Sort.
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    less_than_pivot = [x for x in arr[:-1] if x <= pivot]
    greater_than_pivot = [x for x in arr[:-1] if x > pivot]

    # Mostrar el estado actual del arreglo
    text_widget.insert(tk.END, f"{'  ' * depth}Pivot: {pivot}, Menores: {less_than_pivot}, Mayores: {greater_than_pivot}\n")
    text_widget.update_idletasks()

    sorted_less = quick_sort(less_than_pivot, text_widget, depth + 1)
    sorted_greater = quick_sort(greater_than_pivot, text_widget, depth + 1)

    return sorted_less + [pivot] + sorted_greater

def sort_numbers():
    elements_list = entry_elements.get()
    arr = list(map(int, elements_list.split(',')))

    text_result.delete(1.0, tk.END)
    sorted_arr = quick_sort(arr, text_result)

    text_result.insert(tk.END, f"\nArreglo ordenado: {sorted_arr}")

def open_main_window():
    splash_screen.destroy()

    global root
    root = tk.Tk()
    root.title("Quick Sort")
    root.attributes('-fullscreen', True)

    tk.Label(root, text="Ingrese los elementos del arreglo separados por comas:", font=("Helvetica", 18)).pack(pady=20)
    global entry_elements
    entry_elements = tk.Entry(root, width=60, font=("Helvetica", 18))
    entry_elements.pack(pady=20)

    btn_sort = tk.Button(root, text="Ordenar", font=("Helvetica", 18), command=sort_numbers)
    btn_sort.pack(pady=20)

    btn_pdf = tk.Button(root, text="Abrir PDF", font=("Helvetica", 18), command=open_pdf)
    btn_pdf.pack(pady=20)

    global text_result
    text_result = tk.Text(root, height=20, width=100, font=("Helvetica", 18))
    text_result.pack(pady=5)

    root.mainloop()

def open_pdf():
    pdf_path = "QuickSortDocument.pdf"  # Ruta del archivo PDF existente
    os.system(f"open {pdf_path}")

splash_screen = tk.Tk()
splash_screen.title("Bienvenido")

tk.Label(splash_screen, text="Método Quick Sort", font=("Helvetica", 30)).pack(pady=20)
tk.Label(splash_screen, text="El Quick Sort (ordenamiento rápido) es un algoritmo de ordenamiento muy eficiente que utiliza el enfoque divide y vencerás. Es ampliamente utilizado por su rapidez en la mayoría de los casos, aunque su rendimiento puede degradarse si los datos no se dividen de manera balanceada.", wraplength=800, font=("Helvetica", 20)).pack(pady=20)

btn_pdf = tk.Button(splash_screen, text="Conozca más sobre el método QuickSort", font=("Helvetica", 20), command=open_pdf)
btn_pdf.pack(pady=20)

tk.Label(splash_screen, text="Integrantes del equipo:", font=("Helvetica", 25)).pack(pady=20)
tk.Label(splash_screen, text="1. Negron, Danna\n2. Patiño, Hugo\n3. Rios, Sebastian", font=("Helvetica", 20)).pack(pady=20)

btn_proceed = tk.Button(splash_screen, text="Continuar", font=("Helvetica", 20), command=open_main_window)
btn_proceed.pack(pady=20)

splash_screen.mainloop()