from gtts import gTTS
from tkinter import *
from playsound import playsound

# og window #
window = Tk()
window.geometry("350x300")
window.resizable(0,0)
window.config(bg="ghost white")
window.title("TTS in python")
# og window close #

# heading fam #
tts = Label(window, text="TTS - Text To Speech", font='ariel 20 bold', bg="white smoke")
tts.pack()
# heading fam close #

# button label #
txt = Label(window, text="Enter text please :)", font='ariel 20 bold', bg="white smoke")
txt.pack(padx=20, pady=40)
# button label close #

# txt #
msg = StringVar()
# txt close #

# entry #
entry = Entry(window, textvariable=msg, width="50")
entry.place(x=20, y=120)
# entry close #

# main stuff #
def tts():
    info = entry.get()
    speech = gTTS(text=info)
    speech.save("Your request.mp3")
    playsound("Your request.mp3")

def exit():
    window.destroy()

def reset():
    msg.set("")

play = Button(window, text="play :)", font='arial 15 bold', command=tts, width=5)
play.place(x=20, y=140)

_exit_ = Button(window, text="Exit :(", font="arial 15 bold", command=exit, bg="OrangeRed1")
_exit_.place(x=130, y=140)

_reset_ = Button(window, text="reset :|", font="arial 15 bold", command=reset)
_reset_.place(x=240, y=140)

window.mainloop()





