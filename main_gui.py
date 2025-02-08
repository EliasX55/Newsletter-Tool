import tkinter as tk
from tkinter import messagebox
from main import send_message
from tkinter import filedialog
import shutil
import os
import csv
import threading

main_path = "the_scv.csv"


def upload_csv():
    file_path = filedialog.askopenfilename(
        title="Wählen Sie eine CSV-Datei aus",
        filetypes=[("CSV-Dateien", "*.csv")]
    )

    if file_path:
        label.config(text=f"Ausgewählte Datei: {file_path}")
        try:
            destination = os.path.join(os.getcwd(), os.path.basename(main_path))
            shutil.copy(file_path, destination)
            label.config(text=f"Datei '{os.path.basename(file_path)}' wurde kopiert!")
        except Exception as e:
            messagebox.showerror("Error", f"{e}")
    else:
        messagebox.showinfo("Keine Datei ausgewaehlt")


def go_through_csv():
    target_data = {}

    with open("the_scv.csv", mode="r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if isinstance(row, dict):
                print("Dies ist ein Dictionary!")
            else:
                print("Dies ist KEIN Dictionary!")

            if 'Name' in row and 'Email' in row:
                name = row['Name']
                email = row['Email']
                target_data[name] = email
            else:
                print("Fehlende Spalte in der Zeile:", row)

    print(target_data)
    for client_name, client_email in target_data.items():
        print(client_name, client_email)
        thread = threading.Thread(target=send_message, args=(client_name, client_email))
        thread.start()


def send_newsletter():
    receiver_name = receiver_name_entry.get()
    receiver_name_entry.delete(0, tk.END)
    receiver_email = receiver_email_entry.get()
    receiver_email_entry.delete(0, tk.END)
    try:
        send_message(receiver_name, receiver_email)
        messagebox.showinfo("Success", "Message sent")
    except Exception as e:
        messagebox.showerror("Error", f"{e}")


def change_receiver_mode_csv():
    custom_receiver_frame.pack_forget()
    csv_receiver_frame.pack()


def change_receiver_mode_custom():
    csv_receiver_frame.pack_forget()
    custom_receiver_frame.pack()


root = tk.Tk()
root.title("Newsletter Program")
root.geometry("500x400")
root.resizable(False, False)

nav_bar_frame = tk.Frame(root)
nav_bar_frame.pack()

main_frame = tk.Frame(root)
main_frame.pack(pady=20)

pick_csv_receiver_button = tk.Button(nav_bar_frame, text="CSV Receiver", width=20,
                                     command=change_receiver_mode_csv, font=('Arial', 12))
pick_csv_receiver_button.grid(column=0, row=0, pady=10)

pick_custom_receiver_button = tk.Button(nav_bar_frame, text="Custom Receiver", width=20,
                                        command=change_receiver_mode_custom, font=('Arial', 12))
pick_custom_receiver_button.grid(column=1, row=0, pady=10)

csv_receiver_frame = tk.Frame(main_frame)
csv_receiver_frame.pack()

custom_receiver_frame = tk.Frame(main_frame)

receiver_label = tk.Label(custom_receiver_frame, text="Receiver Name", font=('Arial', 12))
receiver_label.pack(pady=5)

receiver_name_entry = tk.Entry(custom_receiver_frame, font=('Arial', 12), width=30)
receiver_name_entry.pack(pady=5)

receiver_label = tk.Label(custom_receiver_frame, text="Receiver Email", font=('Arial', 12))
receiver_label.pack(pady=5)

receiver_email_entry = tk.Entry(custom_receiver_frame, font=('Arial', 12), width=30)
receiver_email_entry.pack(pady=5)

start_button = tk.Button(custom_receiver_frame, text="Start", command=send_newsletter,
                         font=('Arial', 12), width=20)
start_button.pack(pady=20)

label = tk.Label(csv_receiver_frame, text="Bitte eine CSV-Datei auswählen", font=('Arial', 12), width=40)
label.pack(pady=10)

upload_button = tk.Button(csv_receiver_frame, text="CSV-Datei auswählen", command=upload_csv,
                          font=('Arial', 12), width=20)
upload_button.pack(pady=10)

start_messaging_button = tk.Button(csv_receiver_frame, text="Start", command=go_through_csv,
                                   font=('Arial', 12), width=20)
start_messaging_button.pack(pady=20)

root.mainloop()
