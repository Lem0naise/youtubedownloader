import urllib.request as ur     
import json
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk 

#setting up window and canvas
root = tk.Tk()
root.resizable(0,0)
root.title("Kahoot Answers")
root.configure(bg= "pale turquoise")

leftFrame = Frame(root, bg = "pale turquoise")

#importing image
load = Image.open("assets/find_answers_button.png")
load = load.resize((100, 33), Image.ANTIALIAS)
find_answers_button = ImageTk.PhotoImage(load)


#inputting gameid
gameid = StringVar()

temp = Label(text="Game ID (End Of Link):", bg="pale turquoise", fg = "SteelBlue4")
temp2 =Label(text=" Eg : 'f954d734-7b26-4519-ba99-4134b3416be1'", bg="pale turquoise", fg = "SteelBlue4")


temp.grid(row=1, column=1, padx=10, pady=2)
temp2.grid(row=2, column=1, padx=10, pady=2)

gameurl = Entry(textvariable = gameid, borderwidth = 0, width = 70)
leftFrame.grid(row=3, column=1, padx=10, pady=2)

#function when you click the go button
def getkahoot():
    number = 0
    numbercolumn = 1
    url = str("https://play.kahoot.it/rest/kahoots/" + str(gameid.get()))
    print(url)
    q = json.loads(ur.urlopen(url).read())["questions"]
    colours_list = ["red", "blue", "yellow", "green"]
    for index, slide in enumerate(q):
        if slide.get("type") == "quiz":
            for i in range(len(slide.get("choices"))):
                if slide["choices"][i]["correct"] == True:
                    right_answer = slide["choices"][i].get("answer")
                    right_colour = colours_list[i]
                    if right_answer.endswith("&nbsp;"):
                        right_answer = right_answer[:-6]
                        if right_answer.endswith("</i>"):
                            right_answer = right_answer[:-4]
                            right_answer = right_answer[3:]

                    if right_colour == "red":
                        nicer_colour = "red3"
                    if right_colour == "blue":
                        nicer_colour = "DodgerBlue3"
                    if right_colour == "yellow":
                        nicer_colour = "gold3"
                    if right_colour == "green":
                        nicer_colour = "forest green"

                    answer = Label(leftFrame, text = right_answer, bg= nicer_colour, fg ="snow")
                    answer.config(font=("Ariel", 10))


                    qn = "Q." + str(index + 1)

                    qnumber = Label(leftFrame, text = qn, bg = "pale turquoise", font=("Ariel", 12), fg = "SteelBlue4")
                    if number>10:
                        number = 0
                        numbercolumn+=1
                    #the fill makes it take up the whole space (on the x axis)
                    qnumber.grid(row=number, column=numbercolumn, padx=10, pady=2)
                    answer.grid(row=number+1, column=numbercolumn, padx=10, pady=2)
                    number+=2



#button to go              
gobutton = Button(image = find_answers_button, command = getkahoot, bg = "pale turquoise", borderwidth = 0, activebackground = "pale turquoise")
gameurl.grid(row=4, column=1, padx=10, pady=2)
gobutton.grid(row=5, column=1, padx=10, pady=2)

root.mainloop()