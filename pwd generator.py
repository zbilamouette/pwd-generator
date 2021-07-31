#bibliothèques requises
import tkinter
import random
import string
import pyperclip

#spec fenetre
screen = tkinter.Tk()
screen.title("MDP Generator")
screen.geometry('436x202')
screen.resizable(False, False)

# FONCTION CALCUL MDP
def mdp():
    size=value.get()
    entropi=valeur.get()
    mdp = []
    for i in range(size):
        for k in range(size):
            if entropi>=1:
                letter_down = random.choice(string.ascii_lowercase)
                mdp.append(letter_down)
            if entropi>=2:
                letter_up = random.choice(string.ascii_uppercase)
                mdp.append(letter_up)
        if entropi>=3:
            punctuation = random.choice(string.punctuation)
            mdp.append(punctuation)
    txt=''.join(mdp)
    pyperclip.copy(txt)
    #print(''.join(mdp))


# 1ERE CELLULE
ZoneOptions = tkinter.LabelFrame(screen, borderwidth = 2, text = 'Options', labelanchor = 'n', relief = tkinter.RIDGE,width = 200, height = 200)
ZoneOptions.grid(row = 0, column = 0)
ZoneOptions.grid_propagate(0)
# 2EME CELLULE
ZoneOptions1 = tkinter.LabelFrame(screen, borderwidth = 2, text = '', labelanchor = 'n', relief = tkinter.RIDGE, width = 200, height = 200)
ZoneOptions1.grid(row=0, column=1)
ZoneOptions1.grid_propagate(0)
mess= tkinter.Label(ZoneOptions1, text="Le MDP sera automatiquement copié dans\nvotre presse papier !", background='yellow')
mess.pack()


# CURSEUR ENTROPIE
valeur = tkinter.IntVar(ZoneOptions)
valeur.set(1)
EchelleRayon = tkinter.Scale(ZoneOptions, orient='horizontal', from_=1, to=3, resolution=1, tickinterval=1, length=190, label='Entropie du MDP', variable=valeur)
EchelleRayon.grid(row=40, columnspan=2)
entropie=valeur.get()


# CURSEUR TAILLE
value = tkinter.IntVar(ZoneOptions)
value.set(1)
EchelleRayon1 = tkinter.Scale(ZoneOptions, orient='horizontal', from_=1, to=5, resolution=1, tickinterval=1, length=190, label='Taille du MDP', variable=value)
EchelleRayon1.grid(row=100, columnspan=2)
size_mdp=value.get()


# GENERATOR BUTTON
Button_generator = tkinter.Button(ZoneOptions1, text='Générer un MDP', command=mdp,  activebackground='yellow', height=3, width=25)
Button_generator.grid(row=30, pady=20, columnspan=2)
Button_generator.pack()


#loop script
screen.mainloop()