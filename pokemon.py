from struct import pack
from tkinter import *
from turtle import bgcolor
from PIL import ImageTk,Image
import random as rm
from matplotlib.pyplot import text
from requests import delete
from sympy import ask

# Pokemo_game

class Pokemon_game:
  dano_base = 10

  def __init__(self,Pokemon,number):
    self.especie =Pokemon[number]['especie']
    self.stats = Pokemon[number]['stats']
    self.current_stats = self.stats.copy()
    self.tipo = Pokemon[number]['tipo']
    self.debilidades = Pokemon[number]['debilidades']
    self.fortalezas = Pokemon[number]['fortalezas']
    self.ataques_por_esc = Pokemon[number]['ataques_por_esc']

  def centro_pokemon(self):
    self.current_stats = self.stats

  def pelea(self, rival):
    text=""
 
    # Tu rival es furte o debil a ti?
    if self.tipo in rival.fortalezas:
      modificador_ataque = 1/2
    elif self.tipo in rival.debilidades:
      modificador_ataque = 2
    else:
      modificador_ataque = 1
    
    #eres fuerte o debil a tu rival?
    if rival.tipo in self.fortalezas:
      modificador_defensa = 1/2
    elif rival.tipo in self.debilidades:
      modificador_defensa = 2
    else:
      modificador_defensa = 1     
    
    # quien ataca primero
    if self.current_stats["velocidad"] >= rival.current_stats["velocidad"]:
      mi_turno = True
    else:
      mi_turno = False
    
    # combate por turnos
    if (self.current_stats["hp"] > 0) & (rival.current_stats["hp"] > 0):
      
      for i in range(2):
        
        
        if mi_turno:
          
          text+="\n"+"\n"+"\t"+"Tu ataque: "+ "\n"+"\n"

          escogido=r.get()
        
          dano = int(
            self.dano_base * 
            (self.current_stats["ataque"] / rival.current_stats["defensa"]) * modificador_ataque*
            self.ataques_por_esc[escogido-1][1]) 

          #Randomness 
          if escogido==1:
            suerte=rm.randrange(1,6,1)
          elif escogido==2:
            suerte=rm.randrange(1,11,1)
          elif escogido==3:
            suerte=rm.randrange(1,4,1)
          else:
            suerte=rm.randrange(1,3,1)
    
          if suerte != 1:
            dano = int(
                self.dano_base * 
                (self.current_stats["ataque"] / rival.current_stats["defensa"]) * modificador_ataque*
                self.ataques_por_esc[escogido-1][1]) 

          else:
            dano=0
            text+=(f"Diantres!! {self.especie} ha fallado")+"\n"


          rival.current_stats["hp"] -= dano
          text+=(f"{self.especie} hizo {dano} de daño a {rival.especie}")+"\n"
          text+=(f"A {rival.especie} le quedan {rival.current_stats['hp']} puntos de vida")+"\n"

          if  rival.current_stats["hp"]<=0:
            victoria(1)
            break

          mi_turno=not mi_turno

        else :
          # defendiendo

          text+="\n"+"\n"+"\t"+"Ataque del enemigo:"+"\n"+"\n"
          suerte_rival=rm.randrange(1,5,1)
          if suerte_rival != 1:
             enemy_label.config(image=image_attack[enemy_number][suerte_rival-2]) 
             dano = int(
             rival.dano_base *
            (rival.current_stats["ataque"] / self.current_stats["defensa"]) * 
          modificador_defensa)
          else:
              enemy_label.config(image=image_list[enemy_number]) 
              dano=0
              text+=(f"Genial!! {rival.especie} ha fallado")+"\n"
        
          self.current_stats["hp"] -= dano
          text+=(f"{rival.especie} hizo {dano} de daño a {self.especie}")+"\n"
          text+=(f"A {self.especie} le quedan {self.current_stats['hp']} puntos de vida")+"\n"

          if ( self.current_stats["hp"])<=0:
            victoria(0)
            break

          mi_turno = not mi_turno
        text_func(text)
    else:
      if self.current_stats["hp"] <= 0:
        button_fight.config( status=DISABLED)
      else:
        button_fight.config( status=DISABLED )

    

#Pokemons stats

Pokemon={
  0 : {
    'especie' : "Pikachu",
    'stats' : {
        "velocidad": 65,
        "hp": 39,
        "ataque": 52,
        "defensa": 43},
    'tipo' : "electrico",
    'fortalezas' : "planta",
    'debilidades' : "agua",
    'ataques_por_esc' : [[ "Impactrueno" ,1.0], ["Relampago",.7], ["Lightthunder" ,1.3],["Lightshockwave",1.6]]
  },  
  1 : {
    'especie' : "Charmander",
    'stats' : {
        "velocidad": 65,
        "hp": 39,
        "ataque": 52,
        "defensa": 43},
    'tipo' : "fuego",
    'fortalezas' : "planta",
    'debilidades' : "agua",
    'ataques_por_esc' : [[ "Gruñido Growl" ,1.0], ["Ascuas Ember",.7], ["Pantalla de Humo Smokescreen" ,1.3],["Furia Dragón Dragon Rage",1.6]]
  },
    
  2 : {
    'especie' : "Bulbasaur",
    'stats' : {
        "velocidad": 45,
        "hp": 45,
        "ataque": 49,
        "defensa": 49},
    'tipo' : "planta",
    'fortalezas' : "agua",
    'debilidades' : "fuego",
    'ataques_por_esc' : [["Latigazo", 1.0], ["Bomba lodo" ,.7], ["Bomba germen",1.],["Bomba enselada" ,1.6]]
  },
  3 : {
    'especie' : "Squirtle",
    'stats' : {
        "velocidad": 43,
        "hp": 44,
        "ataque": 48,
        "defensa": 65},
    'tipo' : "agua",
    'fortalezas' : "fuego",
    'debilidades' : "planta",
    'ataques_por_esc' :  [["Placaje Tackle",1.0],["Látigo Tail Whip",.7],["Burbuja Bubble",1.3],["Refugio Withdraw",1.6]]
  }

}

#Creating a label
root = Tk() 
root.title( "Pokemon")
root.config(bg="black")


#Your frame

global your_frame
your_frame= LabelFrame(root, text="You", padx=50, pady=20, font=("Terminal", 10), bg="black",fg="white" )
your_frame.grid(row=0, column=0)

#Your frame stats


r=IntVar()

global your_stats
your_stats= LabelFrame(root, text='Your stats', padx=50, pady=73, font=("Terminal", 10), bg="black",fg="white")
your_stats.grid(row=0, column=1)

def text_stats(img_number):

  text= "Especie: " + str(Pokemon[img_number]['especie']) + "\n""\n" + "Stats: "+ "\n"  "\t" +"velocidad:"+ str(Pokemon[img_number]["stats"]["velocidad"])  \
  +"\n"  "\t" + "hp:"+str(Pokemon[img_number]["stats"]["hp"]) + "\n"  "\t" + "Ataque:"+str(Pokemon[img_number]["stats"]["ataque"]) +"\n"  "\t" +"Defensa:"+ str(Pokemon[img_number]["stats"]['defensa'])  +"\n" \
  "\n" "Ataques por escoger:" +"\n" "\n" "\t" + str(Pokemon[img_number]["ataques_por_esc"][img_number][0])  +"\n"  "\t" + str(Pokemon[img_number]["ataques_por_esc"][1][0]) + "\n"  "\t" + \
  str(Pokemon[img_number]["ataques_por_esc"][2][0]) +"\n"  "\t" + str(Pokemon[img_number]["ataques_por_esc"][3][0])  + "\n""\n" "tipo: " + str(Pokemon[img_number]['tipo']) + "\n"+ \
  "\n" "Fortalezas: " + str(Pokemon[img_number]['fortalezas']) + "\n"+  "\n" "Debilidad: " + str(Pokemon[img_number]['debilidades']) 
  return(text)


text_box = Text( 
    your_stats,
    font=("Terminal", 10), bg="black",fg="white",
    height=20,
    width=40, 
    )

text_box.grid(row=0, column=0)
text_box.insert('end', text_stats(0))
text_box.config(state='disabled')

#Images to 

my_img_Pik=ImageTk.PhotoImage(Image.open("DEV-F-Proyectos/Images/Pikachu.png"))

my_img_Pik_atacando1=ImageTk.PhotoImage(Image.open("DEV-F-Proyectos/Images/ataque1_pikachu.png"))
my_img_Pik_atacando2=ImageTk.PhotoImage(Image.open("DEV-F-Proyectos/Images/ataque2_pikachu.png"))
my_img_Pik_atacando3=ImageTk.PhotoImage(Image.open("DEV-F-Proyectos/Images/ataque3_pikachu.png"))
my_img_Pik_atacando4=ImageTk.PhotoImage(Image.open("DEV-F-Proyectos/Images/ataque4_pikachu.png"))

my_win_Pik=ImageTk.PhotoImage(Image.open("DEV-F-Proyectos/Images/Pikachu-wins.png"))
my_sad_Pik=ImageTk.PhotoImage(Image.open("DEV-F-Proyectos/Images/Pikachu_sad.png"))


my_img_Char=ImageTk.PhotoImage(Image.open("DEV-F-Proyectos/Images/Charmander.png"))

my_img_Char_atacando1=ImageTk.PhotoImage(Image.open("DEV-F-Proyectos/Images/ataque1_charmander.png"))
my_img_Char_atacando2=ImageTk.PhotoImage(Image.open("DEV-F-Proyectos/Images/ataque2_charmander.png"))
my_img_Char_atacando3=ImageTk.PhotoImage(Image.open("DEV-F-Proyectos/Images/ataque3_charmander.png"))
my_img_Char_atacando4=ImageTk.PhotoImage(Image.open("DEV-F-Proyectos/Images/ataque4_charmander.png"))

my_win_Char=ImageTk.PhotoImage(Image.open("DEV-F-Proyectos/Images/charmander_wins.png"))
my_sad_Char=ImageTk.PhotoImage(Image.open("DEV-F-Proyectos/Images/charmander_sad.png"))


my_img_Bul=ImageTk.PhotoImage(Image.open("DEV-F-Proyectos/Images/bulbasaur.png"))

my_img_Bul_atacando1=ImageTk.PhotoImage(Image.open("DEV-F-Proyectos/Images/ataque1_bulbasaur.png"))
my_img_Bul_atacando2=ImageTk.PhotoImage(Image.open("DEV-F-Proyectos/Images/ataque2_bulbasaur.png"))
my_img_Bul_atacando3=ImageTk.PhotoImage(Image.open("DEV-F-Proyectos/Images/ataque3_bulbasaur.png"))
my_img_Bul_atacando4=ImageTk.PhotoImage(Image.open("DEV-F-Proyectos/Images/ataque4_bulbasaur.png"))

my_win_Bul=ImageTk.PhotoImage(Image.open("DEV-F-Proyectos/Images/bulbasuar_win.png"))
my_sad_Bul=ImageTk.PhotoImage(Image.open("DEV-F-Proyectos/Images/bulbasaur_sad.png"))

my_img_Squ=ImageTk.PhotoImage(Image.open("DEV-F-Proyectos/Images/Squirtle.png"))

my_img_Squ_atacando1=ImageTk.PhotoImage(Image.open("DEV-F-Proyectos/Images/ataque1_squirtle.png"))
my_img_Squ_atacando2=ImageTk.PhotoImage(Image.open("DEV-F-Proyectos/Images/ataque2_squirtle.png"))
my_img_Squ_atacando3=ImageTk.PhotoImage(Image.open("DEV-F-Proyectos/Images/ataque3_squirtle.png"))
my_img_Squ_atacando4=ImageTk.PhotoImage(Image.open("DEV-F-Proyectos/Images/ataque4_squirtle.png"))

my_win_Squ=ImageTk.PhotoImage(Image.open("DEV-F-Proyectos/Images/squirtle_wins.png"))
my_sad_Squ=ImageTk.PhotoImage(Image.open("DEV-F-Proyectos/Images/squirtle_sad.png"))



image_list= [my_img_Pik, my_img_Char, my_img_Bul, my_img_Squ]

image_attack=[ [my_img_Pik_atacando1, my_img_Pik_atacando2,my_img_Pik_atacando3, my_img_Pik_atacando4],
               [my_img_Char_atacando1, my_img_Char_atacando2,my_img_Char_atacando3, my_img_Char_atacando4],
               [my_img_Bul_atacando1, my_img_Bul_atacando2,my_img_Bul_atacando3, my_img_Bul_atacando4],
               [my_img_Squ_atacando1, my_img_Squ_atacando2,my_img_Squ_atacando3, my_img_Squ_atacando4]
]

image_result=[ 
              [my_win_Pik, my_win_Char, my_win_Bul, my_win_Squ],
              [my_sad_Pik, my_sad_Char, my_sad_Bul, my_sad_Squ]
 ]

my_label = Label(your_frame,image=my_img_Pik, font=("Terminal", 10), bg="black",fg="white")
my_label.grid( row=0, column=0, columnspan=3 )
your_number=1

#Selecionador de jugadores hacia adelante

def forward(img_number):
    global my_label
    global button_forward
    global button_back
    global button_name
    global your_number
    global text_box
  
    my_label.grid_forget()
    your_number=img_number

    my_label=Label(your_frame,image=image_list[img_number-1],bg="black",fg="white")
    button_forward = Button(your_frame, text=">>", command=lambda: forward(img_number+1), font=("Terminal", 10), bg="black",fg="white")
    button_back = Button(your_frame, text="<<", command=lambda : back(img_number-1 ), font=("Terminal", 10), bg="black",fg="white")
    my_label.grid( row=0, column=0, columnspan=3 )
    button_name=Button(your_frame, text="Choose",command=enemy_image, font=("Terminal", 10), bg="black",fg="white")

    if img_number==len(image_list):
        button_forward=Button(your_frame, text=">>", state=DISABLED, font=("Terminal", 10), bg="black",fg="white")

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_name.grid(row=1, column=1,columnspan=1)
    button_forward.grid(row=1, column=2,)
    
    text_box = Text(
    your_stats,
    font=("Terminal", 10), bg="black",fg="white",
    height=20,
    width=40
    )
    text_box.grid(row=0, column=0)
    text_box.insert('end', text_stats(img_number-1))
    text_box.config(state='disabled')

#Selecionador de jugadores hacia atras

def back(img_number):
    global my_label
    global button_forward
    global button_back
    global button_name
    global your_number
    global text_box
  
    my_label.grid_forget()
    your_number=img_number

    my_label=Label(your_frame,image=image_list[img_number-1],bg="black",fg="white")
    button_forward = Button(your_frame, text=">>", command=lambda: forward(img_number+1), font=("Terminal", 10), bg="black",fg="white")
    button_back = Button(your_frame, text="<<", command=lambda : back(img_number-1 ), font=("Terminal", 10), bg="black",fg="white")
    my_label.grid( row=0, column=0, columnspan=3 )
    button_name=Button(your_frame, text="Choose", command=enemy_image, font=("Terminal", 10), bg="black",fg="white")
    
    if img_number==1:
        button_back=Button(your_frame, text="<<", state=DISABLED, font=("Terminal", 10), bg="black",fg="white")


    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_name.grid(row=1, column=1,columnspan=1)
    button_forward.grid(row=1, column=2,)

    text_box = Text(
    your_stats,
    font=("Terminal", 10), bg="black",fg="white",
    height=20,
    width=40
    )
    text_box.grid(row=0, column=0)
    text_box.insert('end', text_stats(img_number-1))
    text_box.config(state='disabled')

#Images from the enemy

my_ask=ImageTk.PhotoImage(Image.open("DEV-F-Proyectos/Images/question.png"))
 
enemy_frame= LabelFrame(root, text="Enemy", padx=50, pady=33, font=("Terminal", 10), bg="black",fg="white")
enemy_frame.grid(row=0, column=3)

global enemy_label

enemy_label = Label(enemy_frame, image=my_ask, font=("Terminal", 10), bg="black",fg="white")
enemy_label.grid( row=0, column=3 )
  
def enemy_image():

    global enemy_number
    while True:
      enemy_number=rm.randrange(0,len(image_list))
      if enemy_number!=your_number-1:
        break
    enemy_label.config(image=image_list[enemy_number], bg="black") 


    button_back = Button(your_frame, text="<<", command=back, state=DISABLED,font=("Terminal", 10), bg="black",fg="white")
    button_forward = Button(your_frame, text=">>", command=back, state=DISABLED,font=("Terminal", 10), bg="black",fg="white")
    button_fight.config( text="Let´s fight",command=activate_fight, state=NORMAL,font=("Terminal", 10), bg="black",fg="white")
    button_name.config(state=DISABLED)

    button_back.grid(row=1, column=0)
    button_name.grid(row=1, column=1)
    button_forward.grid(row=1, column=2)
    button_fight.grid(row=5,column=1)


#Botones iniciales

button_back = Button(your_frame, text="<<", command=back, state=DISABLED, font=("Terminal", 10), bg="black",fg="white")
button_name=Button(your_frame, text="Choose", command=enemy_image, font=("Terminal", 10), bg="black",fg="white")
button_forward = Button(your_frame, text=">>", command= lambda: forward(2), font=("Terminal", 10), bg="black",fg="white")

button_back.grid(row=1, column=0)
button_name.grid(row=1, column=1)
button_forward.grid(row=1, column=2)


button_fight=Button(root, text="Lets fight",state=DISABLED, font=("Terminal", 10), bg="black",fg="white")
button_fight.grid(row=5,column=1)



Pikachu=Pokemon_game(Pokemon,0)
charmander=Pokemon_game(Pokemon,1)
Bulbasuar=Pokemon_game(Pokemon,2)
Squirtle=Pokemon_game(Pokemon,3)

Peleadores=[Pikachu,charmander, Bulbasuar,Squirtle ]

def text_func(text):
  text_box = Text(
    your_stats,
    font=("Terminal", 10), bg="black",fg="white",
    height=20,
    width=40
    )
  text_box.grid(row=0, column=0)
  text_box.insert('end', text)
  text_box.config(state='disabled')

  button_fight.config( text="Siguiente turno: ",command=activate_fight, font=("Terminal", 10), bg="black",fg="white")

def delscreen():
  for child in your_stats.winfo_children():
    child.destroy() 

def delscreenf(number):
  for child in your_stats.winfo_children():
    child.destroy()
  if number==1:
    textf="Has ganado"
  else:
    textf="Has perdido"
  text_func(textf)
  
  button_fight.config(state=DISABLED,font=("Terminal", 10), bg="black",fg="white")
  
  final()

def fight():
  for child in your_stats.winfo_children():
    child.destroy()
  Peleadores[your_number-1].pelea(Peleadores[enemy_number])
  
def botton():
  a=r.get()
  my_label.config(image=image_attack[your_number-1][r.get()-1])
  button_fight.config(text="Confirmar ataque: "+str(a),command=fight, font=("Terminal", 10), bg="black",fg="white")

  
def final():
  Termina=Button(root,text="Terminar" ,command=root.quit, font=("Terminal", 10), bg="black",fg="white").grid(row=3, column=1)

def activate_fight():

  for child in your_stats.winfo_children():
    child.destroy()
      
   
  your_stats.config( text='Lets fight')
      
  Radiobutton(your_stats, text=" 80% de exito: "+Pokemon[your_number-1]["ataques_por_esc"][0][0], variable=r, value=1, command=botton, font=("Terminal", 10), bg="black",fg="white").grid(row=3, column=0)
  Radiobutton(your_stats, text=" 90% de exito: "+Pokemon[your_number-1]["ataques_por_esc"][1][0], variable=r, value=2, command=botton, font=("Terminal", 10), bg="black",fg="white").grid(row=4, column=0)
  Radiobutton(your_stats, text=" 67% de exito: "+Pokemon[your_number-1]["ataques_por_esc"][2][0], variable=r, value=3, command=botton, font=("Terminal", 10), bg="black",fg="white").grid(row=5, column=0)
  Radiobutton(your_stats, text=" 50% de exito: "+Pokemon[your_number-1]["ataques_por_esc"][3][0], variable=r, value=4, command=botton, font=("Terminal", 10), bg="black",fg="white",).grid(row=6, column=0)  

  button_fight.config( text="Escoger ataque") 

def victoria(number):
  button_fight.config(text="Se acabo", command=delscreenf(number))
  if number==1:
    my_label.config(image=image_result[0][your_number-1])
    enemy_label.config(image=image_result[1][enemy_number]) 
  else:
    my_label.config(image=image_result[1][your_number-1])
    enemy_label.config(image=image_result[0][enemy_number]) 

root.mainloop()
