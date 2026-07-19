import tkinter as tk
from tkinter import messagebox

from archiver import archive_site


def start():
    url = entry.get()

    if not url:
        return

    ok, result = archive_site(url)

    if ok:
        messagebox.showinfo(
            "Muffixx Archiver",
            f"Arşiv oluşturuldu:\n{result}"
        )
    else:
        messagebox.showerror(
            "Hata",
            result
        )


root = tk.Tk()
root.title("Muffixx Archiver")
root.geometry("400x180")


label = tk.Label(
    root,
    text="Web adresi:"
)

label.pack(pady=5)


entry = tk.Entry(
    root,
    width=45
)

entry.pack()


button = tk.Button(
    root,
    text="Archive",
    command=start
)

button.pack(pady=20)


root.mainloop()
