import tkinter as tk

class IceCreamStand:
    def __init__(self, master):
        self.master = master
        self.master.title("Кафе-мороженое")

        self.flavor_frame = tk.Frame(self.master)
        self.flavor_frame.pack(side=tk.LEFT)

        self.flavors = ["Ванильное", "Шоколадное", "Клубничное", "Мятное"]
        self.flavor_list = tk.Listbox(self.flavor_frame)
        for flavor in self.flavors:
            self.flavor_list.insert(tk.END, flavor)
        self.flavor_list.pack()

        self.add_button = tk.Button(self.flavor_frame, text="Добавить", command=self.add_flavor)
        self.add_button.pack()
        self.remove_button = tk.Button(self.flavor_frame, text="Удалить", command=self.remove_flavor)
        self.remove_button.pack()

        self.order_frame = tk.Frame(self.master)
        self.order_frame.pack(side=tk.RIGHT)

        self.order_list = tk.Listbox(self.order_frame)
        self.order_list.pack()

        self.order_button = tk.Button(self.order_frame, text="Оформить заказ", command=self.place_order)
        self.order_button.pack()

    def add_flavor(self):
        selected_flavor = self.flavor_list.get(tk.ACTIVE)

        self.order_list.insert(tk.END, selected_flavor)

    def remove_flavor(self):
        selected_flavor = self.order_list.get(tk.ACTIVE)

        self.order_list.delete(tk.ACTIVE)

    def place_order(self):
        print("Ваш заказ:")
        for item in self.order_list.get(0, tk.END):
            print(f"- {item}")

root = tk.Tk()

ice_cream_stand = IceCreamStand(root)

root.mainloop()
