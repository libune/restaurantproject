import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random
from datetime import date, datetime

# Prices of the menu items
prices = {
    "Chops": 12,
    "Sandwich": 8,
    "Fish": 18,
    "Shrimps": 20,
}

# Initialize the main window
root = tk.Tk()
root.title("TTC - Restaurant")

# Configure the main window
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# ------------------------------------FUNCTIONS--------------------------------------------- #

def ORDER_ID():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    order_id = "BIN_"
    random_letters = ''.join(random.choice(letters) for _ in range(3))
    random_digits = ''.join(str(random.choice(numbers)) for _ in range(3))
    order_id += random_letters + random_digits
    return order_id

def add():
    current_order = orderTransaction.cget("text")
    added_dish = displayLabel.cget("text") + "...." + str(prices[displayLabel.cget("text")]) + "$ "
    updated_order = current_order + added_dish
    orderTransaction.configure(text=updated_order)
    order_total = orderTotalLabel.cget("text").replace("TOTAL : ", "").replace("$", "")
    updated_total = int(order_total) + prices[displayLabel.cget("text")]
    orderTotalLabel.configure(text="TOTAL : " + str(updated_total) + "$")

def remove():
    dish_to_remove = displayLabel.cget("text") + "...." + str(prices[displayLabel.cget("text")])
    transaction_list = orderTransaction.cget("text").split("$ ")
    transaction_list.pop()
    if dish_to_remove in transaction_list:
        transaction_list.remove(dish_to_remove)
        updated_order = "".join(item + "$ " for item in transaction_list)
        orderTransaction.configure(text=updated_order)
        order_total = orderTotalLabel.cget("text").replace("TOTAL : ", "").replace("$", "")
        updated_total = int(order_total) - prices[displayLabel.cget("text")]
        orderTotalLabel.configure(text="TOTAL : " + str(updated_total) + "$")

def display_item(item, image, frame):
    for f in [chopsDishFrame, sandwichDishFrame, fishDishFrame, shrimpsDishFrame]:
        f.configure(style="DishFrame.TFrame")
    frame.configure(relief="sunken", style="SelectedDish.TFrame")
    displayLabel.configure(image=image, text=item, font=('Helvetica', 14, "bold"), foreground="white", compound="bottom", padding=(5, 5, 5, 5))

def displayChops():
    display_item("Chops", chopsImage, chopsDishFrame)

def displaySandwich():
    display_item("Sandwich", sandwichImage, sandwichDishFrame)

def displayFish():
    display_item("Fish", fishImage, fishDishFrame)

def displayShrimps():
    display_item("Shrimps", shrimpsImage, shrimpsDishFrame)

def order():
    new_receipt = orderIDLabel.cget("text").replace("ORDER ID : ", "")
    transaction_list = orderTransaction.cget("text").split("$ ")
    transaction_list.pop()
    order_day = date.today()
    order_time = datetime.now()
    with open(new_receipt, 'w') as file:
        file.write("The Binary\n")
        file.write("________________________________________________________\n")
        file.write(order_day.strftime("%x") + "\n")
        file.write(order_time.strftime("%X") + "\n\n")
        for item in transaction_list:
            file.write(item + "$ \n")
        file.write("\n\n" + orderTotalLabel.cget("text"))
    orderTotalLabel.configure(text="TOTAL : 0$")
    orderIDLabel.configure(text="ORDER ID: " + ORDER_ID())
    orderTransaction.configure(text="")

# ---------------------------------- STYLING AND IMAGES ------------------------------------ #

# Style configurations
s = ttk.Style()
s.configure('MainFrame.TFrame', background="#2B2B28")
s.configure('MenuFrame.TFrame', background="#4A4A48")
s.configure('DisplayFrame.TFrame', background="#0F1110")
s.configure('OrderFrame.TFrame', background="#B7C4CF")
s.configure('DishFrame.TFrame', background="#4A4A48", relief="raised")
s.configure('SelectedDish.TFrame', background="#C4DFAA")
s.configure('MenuLabel.TLabel', background="#0F1110", font=("Arial", 13, "italic"), foreground="white", padding=(5, 5, 5, 5), width=21)
s.configure('orderTotalLabel.TLabel', background="#0F1110", font=("Arial", 10, "bold"), foreground="white", padding=(2, 2, 2, 2), anchor="w")
s.configure('orderTransaction.TLabel', background="#4A4A48", font=('Helvetica', 12), foreground="white", wraplength=170, anchor="nw", padding=(3, 3, 3, 3))

# Load images
# Ensure the image paths are correct
LogoImageObject = Image.open("Images/Restaurant Logo.png").resize((130, 130))
LogoImage = ImageTk.PhotoImage(LogoImageObject)
TopBannerImageObject = Image.open("Images/restaurant top banner.jpg").resize((800, 130))
TopBannerImage = ImageTk.PhotoImage(TopBannerImageObject)
displayDefaultImageObject = Image.open("Images/display - Default.png").resize((350, 360))
displayDefaultImage = ImageTk.PhotoImage(displayDefaultImageObject)
chopsImageObject = Image.open("Images/menu/chops.png").resize((350, 334))
chopsImage = ImageTk.PhotoImage(chopsImageObject)
sandwichImageObject = Image.open("Images/menu/sandwich.png").resize((350, 334))
sandwichImage = ImageTk.PhotoImage(sandwichImageObject)
fishImageObject = Image.open("Images/menu/fish.png").resize((350, 334))
fishImage = ImageTk.PhotoImage(fishImageObject)
shrimpsImageObject = Image.open("Images/menu/shrimps.png").resize((350, 334))
shrimpsImage = ImageTk.PhotoImage(shrimpsImageObject)

#----------------------------------- WIDGETS ----------------------------------------------- #

# Main Frames
mainFrame = ttk.Frame(root, width=800, height=580, style='MainFrame.TFrame')
mainFrame.grid(row=0, column=0, sticky="NSEW")
topBannerFrame = ttk.Frame(mainFrame)
topBannerFrame.grid(row=0, column=0, sticky="NSEW", columnspan=3)
menuFrame = ttk.Frame(mainFrame, style='MenuFrame.TFrame')
menuFrame.grid(row=1, column=0, padx=3, pady=3, sticky="NSEW")
displayFrame = ttk.Frame(mainFrame, style="DisplayFrame.TFrame")
displayFrame.grid(row=1, column=1, padx=3, pady=3, sticky="NSEW")
orderFrame = ttk.Frame(mainFrame, style="OrderFrame.TFrame")
orderFrame.grid(row=1, column=2, padx=3, pady=3, sticky="NSEW")

# Dish Frames
chopsDishFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
chopsDishFrame.grid(row=1, column=0, sticky="NSEW")
sandwichDishFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
sandwichDishFrame.grid(row=2, column=0, sticky="NSEW")
fishDishFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
fishDishFrame.grid(row=3, column=0, sticky="NSEW")
shrimpsDishFrame = ttk.Frame(menuFrame, style="DishFrame.TFrame")
shrimpsDishFrame.grid(row=4, column=0, sticky="NSEW")

# Labels and Buttons
logoLabel = ttk.Label(topBannerFrame, image=LogoImage)
logoLabel.grid(row=0, column=0, padx=5, pady=5, sticky="W")
topBannerLabel = ttk.Label(topBannerFrame, image=TopBannerImage)
topBannerLabel.grid(row=0, column=1, padx=5, pady=5, sticky="E")
displayLabel = ttk.Label(displayFrame, image=displayDefaultImage, text="", compound="bottom", style='MenuLabel.TLabel')
displayLabel.grid(row=0, column=0, padx=5, pady=5)
orderTransaction = ttk.Label(orderFrame, text="", style='orderTransaction.TLabel')
orderTransaction.grid(row=0, column=0, padx=5, pady=5, sticky="NSEW")
orderTotalLabel = ttk.Label(orderFrame, text="TOTAL : 0$", style='orderTotalLabel.TLabel')
orderTotalLabel.grid(row=1, column=0, padx=5, pady=5, sticky="SW")
orderIDLabel = ttk.Label(orderFrame, text="ORDER ID: " + ORDER_ID(), style='orderTotalLabel.TLabel')
orderIDLabel.grid(row=2, column=0, padx=5, pady=5, sticky="SW")

chopsButton = ttk.Button(chopsDishFrame, text="Chops - 12$", command=displayChops)
chopsButton.grid(row=0, column=0, padx=5, pady=5, sticky="NSEW")
sandwichButton = ttk.Button(sandwichDishFrame, text="Sandwich - 8$", command=displaySandwich)
sandwichButton.grid(row=0, column=0, padx=5, pady=5, sticky="NSEW")
fishButton = ttk.Button(fishDishFrame, text="Fish - 18$", command=displayFish)
fishButton.grid(row=0, column=0, padx=5, pady=5, sticky="NSEW")
shrimpsButton = ttk.Button(shrimpsDishFrame, text="Shrimps - 20$", command=displayShrimps)
shrimpsButton.grid(row=0, column=0, padx=5, pady=5, sticky="NSEW")

addButton = ttk.Button(displayFrame, text="ADD TO ORDER", command=add)
addButton.grid(row=1, column=0, padx=5, pady=5, sticky="NSEW")
removeButton = ttk.Button(displayFrame, text="REMOVE FROM ORDER", command=remove)
removeButton.grid(row=2, column=0, padx=5, pady=5, sticky="NSEW")
orderButton = ttk.Button(orderFrame, text="PLACE ORDER", command=order)
orderButton.grid(row=3, column=0, padx=5, pady=5, sticky="NSEW")

# Adjust column and row configurations
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
mainFrame.grid_rowconfigure(0, weight=1)
mainFrame.grid_rowconfigure(1, weight=10)
mainFrame.grid_columnconfigure(0, weight=1)
mainFrame.grid_columnconfigure(1, weight=1)
mainFrame.grid_columnconfigure(2, weight=1)
menuFrame.grid_rowconfigure(0, weight=1)
menuFrame.grid_rowconfigure(1, weight=1)
menuFrame.grid_rowconfigure(2, weight=1)
menuFrame.grid_rowconfigure(3, weight=1)
menuFrame.grid_rowconfigure(4, weight=1)
menuFrame.grid_columnconfigure(0, weight=1)
displayFrame.grid_rowconfigure(0, weight=8)
displayFrame.grid_rowconfigure(1, weight=1)
displayFrame.grid_rowconfigure(2, weight=1)
displayFrame.grid_columnconfigure(0, weight=1)
orderFrame.grid_rowconfigure(0, weight=8)
orderFrame.grid_rowconfigure(1, weight=1)
orderFrame.grid_rowconfigure(2, weight=1)
orderFrame.grid_rowconfigure(3, weight=1)
orderFrame.grid_columnconfigure(0, weight=1)

# Start the main loop
root.mainloop()
