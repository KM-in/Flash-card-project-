from tkinter import  *
import pandas
import random




BACKGROUND_COLOR = "#B1DDC6"


# ---------flash cards words --------------------------
data =pandas.read_csv("data/french_words.csv")
data_dict =data.to_dict(orient="records")




def get_random_word():
    """Get a random French-English word pair"""
    return random.choice(data_dict)






def show_new_card():
    """Display a new random card"""
    global current_card,flip_timer 

    if flip_timer:
        window.after_cancel(flip_timer)
    current_card = get_random_word()
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")

    flip_timer =window.after(3000,show_meaning)
    

def show_meaning():
    """Will flip the card and show the meaning of the word """
    canvas.itemconfig(language_text,text = "English",fill = "black")
    canvas.itemconfig(word_text,text = current_card["English"],fill="black")














# ---------------------------UI SETUP -------------------------------
window = Tk()
window.title("flash cards ")
window.config(bg=BACKGROUND_COLOR,padx=70,pady=50)
window.minsize(1000,600)







background_image  = PhotoImage(file="images/background.png")


canvas = Canvas()
canvas.config(height=526,width=800,bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.create_image(400,263,image = background_image)
canvas.grid(row=1,column=1,columnspan=2)

language_text = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))


right_button_img = PhotoImage(file="images/right.png")
wrong_button_img = PhotoImage(file="images/wrong.png")




right_button = Button(image=right_button_img,width=50,height=50,command=show_new_card)
right_button.grid(column=2,row=2)




wrong_button = Button(image=wrong_button_img,width=50,height=50,command=show_new_card)
wrong_button.grid(column=1,row=2,)



current_card={}
flip_timer = 0
show_new_card()





window.mainloop()
