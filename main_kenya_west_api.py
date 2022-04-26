"""
    Example code to get Kenya West Quotes API
    https://api.kanye.rest/
"""
from tkinter import *
import requests

kenya_west_api_url = "https://api.kanye.rest/"


def get_quote():
    kenya_quotes_response = requests.get(url=kenya_west_api_url)
    kenya_quotes = kenya_quotes_response.json()
    print(kenya_quotes)
    canvas.itemconfig(quote_text, text=kenya_quotes["quote"])


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Click on My Head to get My Quotes", width=250, font=("Arial", 18, "bold"),
                                fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
