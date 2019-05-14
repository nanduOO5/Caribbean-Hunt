import tkinter as tk
from functools import partial # a quick way to make a callback function

class Situation(tk.Frame):
    def __init__(self, master=None, story='', buttons=[], **kwargs):
        tk.Frame.__init__(self, master, **kwargs)

        story_lbl = tk.Label(self, text=story, justify=tk.LEFT, anchor=tk.NW, font=("Play", 10))
        story_lbl.pack()

        for btn_text, new_situation in buttons:
            btn = tk.Button(self, text=btn_text, command=partial(self.quit_, new_situation))
            btn.pack()

    def quit_(self, new_situation):
        self.destroy()
        load(new_situation)

def load(situation='intro'):
    frame = Situation(root, **SITUATIONS.get(situation))
    frame.pack()

SITUATIONS = {
    'intro': {
        'story':
"""
    We, the PIRATES OF CARIBBEAN are on a treasure hunt.
We have finally reached the end of our voyage as we have found the island
where the secret treasure is hiding. You, our captain must go and retrive
the LOST TREASURE OF THE SEVEN SEAS with the help your golden compass.
You have entered the island by following the map and you have entered a huge
cave.Now, you have 3 tunnels infront of you...

What will you do?
""",
        'buttons': [
            ('LEFT', 'yourDemise'),
            ('MIDDLE', 'thisTooYourDemise'),
            ('RIGHT','alwaysRight'),
        ]
        },

    'yourDemise': {
        'story':
"""
    In the depths of the lake in the cave you see a monster staring at you.
You have realized it is none other than the fabled KRAKEN of the legend.

Will you flee or face the KRAKEN...? 
""",
        'buttons': [
            ('FLEE','intro' ),
            ('FACE', 'gameOver'),
        ]
        },

    'thisTooYourDemise': {
        'story':
"""
    You fell into an under water volcano and died
""",
        'buttons': [
            ('Restart','intro'),
            ('Quit','gameOver'),
        ]
        },

    'alwaysRight': {
        'story':
"""
    Here you find two doors. You are forced to choose one as the path behind has
    been closed

Which way will you go?
""",
        'buttons': [
            ('RED', 'treasureFinally'),
            ('BLUE', 'someonesWaiting'),
        ]
        },


    'treasureFinally': {
        'story':
"""
Congratulations!!! You have found the treasure and are teleported to your ship.
""",
        'buttons': [
            ('Play Again', 'intro'),
            ('Quit', 'gameOver'),
        ]
        },

    'someonesWaiting': {
        'story':
"""You have entered Medusas' Lair and have been turned into a stone for eternity
""",
        'buttons': [
            ('Play Again','intro'),
            ('Quit','gameOver'),
            ]
        },

    'gameOver': {
        'story':
"""
    You have played well.
""",
        
        },

    

    }

def beginning():
    start_button.destroy()
    load() # load the first story

#WINDOW
root = tk.Tk()
root.geometry('500x500-500-300')
root.title('Caribbean Hunt')

#START
start_button = tk.Button(root, text="START", command=beginning)
start_button.place(relx=.5, rely=.5, anchor='c')

#THE LOOP
root.mainloop()
