import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from myparsers import prom
from myutils.saver import savetoc, savetoj, savetoe

def start_parsing():

    caturl = url_entry.get().strip()
    if not caturl:
        messagebox.showerror("Ошибка", "Введите URL категории")
        return

    maxpagesstr = maxp_entry.get().strip()
    try:
        maxpages = int(maxpagesstr)
    except ValueError:
        messagebox.showerror("Ошибка", "Введите количество страниц")
        return

    try:
        products = prom.parse_prom(caturl, maxpages)
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при парсинге:\n{e}")
        return

    if not products:
        messagebox.showerror("Ошибка", "Не удалось получить товары или их нет")
        return

    filef = format_var.get()

    os.makedirs("output", exist_ok=True)

    default_filename = f"prom_products.{filef}"

    initial_dir = os.path.abspath("output")

    if filef == "csv":
        filetypes = [("CSV файлы", "*.csv")]
    elif filef == "xlsx":
        filetypes = [("XLSX файлы", "*.xlsx")]
    else:
        filetypes = [("JSON файлы", "*.json")]

    filepath = filedialog.asksaveasfilename(
        defaultextension=f".{filef}",
        filetypes=filetypes,
        initialdir=initial_dir,
        initialfile=default_filename,
        title="Сохранить как"
    )

    if not filepath:
        return

    try:
        if filef == "json":
            savetoj(products, filepath)
        elif filef == "csv":
            savetoc(products, filepath)
        else:
            savetoe(products, filepath)
        messagebox.showinfo("Готово", f"Данные успешно сохранены:\n{filepath}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при сохранении:\n{e}")
    try:
        root.destroy()
    except Exception:
        pass

root = tk.Tk()
root.title("Парсер Prom.ua")

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, sticky="EW")

ttk.Label(frame, text="URL категории:").grid(row=0, column=0, sticky="W")
url_entry = ttk.Entry(frame, width=50)
url_entry.grid(row=0, column=1, sticky="EW")
url_entry.insert(0, "")

ttk.Label(frame, text="Сколько страниц:").grid(row=1, column=0, sticky="W")
maxp_entry = ttk.Entry(frame, width=50)
maxp_entry.grid(row=1, column=1, sticky="EW")
maxp_entry.insert(0, "")

ttk.Label(frame, text="Формат файла:").grid(row=2, column=0, sticky="W")
format_var = tk.StringVar(value="csv")
csv_rb = ttk.Radiobutton(frame, text="CSV", variable=format_var, value="csv")
csv_rb.grid(row=2, column=1, sticky="W")
json_rb = ttk.Radiobutton(frame, text="JSON", variable=format_var, value="json")
json_rb.grid(row=2, column=1, sticky="E")
excel_rb = ttk.Radiobutton(frame, text="EXCEL", variable=format_var, value="xlsx")
excel_rb.grid(row=2, column=1)

start_btn = ttk.Button(frame, text="Старт", command=start_parsing)
start_btn.grid(row=3, column=0, columnspan=2, pady=10)

root.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

root.mainloop()
