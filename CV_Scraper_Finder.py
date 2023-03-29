import create_venv as venv
import tkinter as tk
import main as M


venv.create_virtual_env()
venv.activate_venv()
venv.install_modules()


def save_information():
    keyword1 = keyword1_entry.get()
    keyword2 = keyword2_entry.get()
    search_type = search_type_var.get()
    region = region_var.get()

    M.main(keyword1, keyword2, search_type, region)

   
def clear_form(root):
    for child in root.winfo_children():
        if isinstance(child, tk.Entry):
            child.delete(0, tk.END) 
            child.insert(0, "") 
        elif isinstance(child, tk.Radiobutton):
            if child["value"] not in ["or", "visa"]:
                child.deselect() 
            else:
                child.select() 


root = tk.Tk()
root.title("CV Scraper Finder")

keyword1_label = tk.Label(root, text="Raktažodis 1:", anchor="w")
keyword1_entry = tk.Entry(root)

keyword2_label = tk.Label(root, text="Raktažodis 2:", anchor="w")
keyword2_entry = tk.Entry(root)

search_type_label = tk.Label(root, text="Raktažodžių paieška:")
search_type_var = tk.StringVar(value="or")

or_radio = tk.Radiobutton(root, text="Arba", variable=search_type_var, value="or")
and_radio = tk.Radiobutton(root, text="Ir", variable=search_type_var, value="and")

region_label = tk.Label(root, text="Kuriam regione ieškote darbo?")
region_var = tk.StringVar(value="visa")

visa_radio = tk.Radiobutton(root, text="Visa Lietuva", variable=region_var, value="visa")
vilnius_radio = tk.Radiobutton(root, text="Vilnius", variable=region_var, value="vilniuje")
kaunas_radio = tk.Radiobutton(root, text="Kaunas", variable=region_var, value="kaune")

save_button = tk.Button(root, text="Save my information", command=save_information)
clear_button = tk.Button(root, text="Clear form", command=lambda: clear_form(root))

keyword1_label.grid(row=0, column=0, sticky="w")
keyword1_entry.grid(row=0, column=1)

keyword2_label.grid(row=1, column=0, sticky="w")
keyword2_entry.grid(row=1, column=1)

search_type_label.grid(row=4, column=0, sticky="w")
or_radio.grid(row=5, column=0, sticky="w")
and_radio.grid(row=6, column=0, sticky="w")

region_label.grid(row=8, column=0)
visa_radio.grid(row=9, column=0, sticky="w")
vilnius_radio.grid(row=10, column=0, sticky="w")
kaunas_radio.grid(row=11, column=0, sticky="w")

save_button.grid(row=13, column=0, pady=10)
clear_button.grid(row=13, column=1, pady=10)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

root.mainloop()