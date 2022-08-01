from struct import pack
from tkinter import *
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
            (self.current_stats["ataque"] / rival.current_stats["defensa"]) * 
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
                (self.current_stats["ataque"] / rival.current_stats["defensa"]) * 
                self.ataques_por_esc[escogido-1][1]) 

          else:
            dano=0
            text+=(f"Diantres!! {self.especie} ha fallado")+"\n"


          rival.current_stats["hp"] -= dano
          text+=(f"{self.especie} hizo {dano} de daño a {rival.especie}")+"\n"
          text+=(f"A {rival.especie} le quedan {rival.current_stats['hp']} puntos de vida")+"\n"

          print( rival.current_stats["hp"])
            #button_fight.config( text="Se acabo", command=text_func("Has ganado") )
            #continue

          mi_turno=not mi_turno






        else :
          # defendiendo

          text+="\n"+"\n"+"\t"+"Ataque del enemigo:"+"\n"+"\n"
          suerte_rival=rm.randrange(1,5,1)
          if suerte_rival != 1:
             dano = int(
             rival.dano_base *
            (rival.current_stats["ataque"] / self.current_stats["defensa"]) * 
          1)
          else:
              dano=0
              text+=(f"Genial!! {rival.especie} ha fallado")+"\n"
        
          self.current_stats["hp"] -= dano
          text+=(f"{rival.especie} hizo {dano} de daño a {self.especie}")+"\n"
          text+=(f"A {self.especie} le quedan {self.current_stats['hp']} puntos de vida")+"\n"

          print( self.current_stats["hp"])
          #button_fight.config( text="Se acabo", command=text_func("Has perdido") )
           # continue

          mi_turno = not mi_turno

    else:
      if self.current_stats["hp"] <= 0:
        button_fight.config( text="Se acabo", command=text_func("Has perdido") )
      else:
        button_fight.config( text="Se acabo", command=text_func("Has ganado") )

    text_func(text)

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

#Your frame

global your_frame
your_frame= LabelFrame(root, text="You", padx=50, pady=20 )
your_frame.grid(row=0, column=0)

#Your frame stats


r=IntVar()

global your_stats
your_stats= LabelFrame(root, text='Your stats', padx=50, pady=73)
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
    height=20,
    width=40
    )

text_box.grid(row=0, column=0)
text_box.insert('end', text_stats(0))
text_box.config(state='disabled')

#Images to 

my_img_Pik=ImageTk.PhotoImage(Image.open("DEV-F-Proyectos/Images/Pikachu.png"))
my_img_Char=ImageTk.PhotoImage(Image.open("DEV-F-Proyectos/Images/Charmander.png"))
my_img_Bul=ImageTk.PhotoImage(Image.open("DEV-F-Proyectos/Images/bulbasaur.png"))
my_img_Squ=ImageTk.PhotoImage(Image.open("DEV-F-Proyectos/Images/Squirtle.png"))

image_list= [my_img_Pik, my_img_Char, my_img_Bul, my_img_Squ]

my_label = Label(your_frame,image=my_img_Pik)
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

    my_label=Label(your_frame,image=image_list[img_number-1])
    button_forward = Button(your_frame, text=">>", command=lambda: forward(img_number+1))
    button_back = Button(your_frame, text="<<", command=lambda : back(img_number-1 ))
    my_label.grid( row=0, column=0, columnspan=3 )
    button_name=Button(your_frame, text="Choose",command=enemy_image)

    if img_number==len(image_list):
        button_forward=Button(your_frame, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_name.grid(row=1, column=1,columnspan=1)
    button_forward.grid(row=1, column=2,)
    
    text_box = Text(
    your_stats,
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

    my_label=Label(your_frame,image=image_list[img_number-1])
    button_forward = Button(your_frame, text=">>", command=lambda: forward(img_number+1))
    button_back = Button(your_frame, text="<<", command=lambda : back(img_number-1 ))
    my_label.grid( row=0, column=0, columnspan=3 )
    button_name=Button(your_frame, text="Choose", command=enemy_image)
    
    if img_number==1:
        button_back=Button(your_frame, text="<<", state=DISABLED)


    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_name.grid(row=1, column=1,columnspan=1)
    button_forward.grid(row=1, column=2,)

    text_box = Text(
    your_stats,
    height=20,
    width=40
    )
    text_box.grid(row=0, column=0)
    text_box.insert('end', text_stats(img_number-1))
    text_box.config(state='disabled')

#Images from the enemy

my_ask=ImageTk.PhotoImage(Image.open("DEV-F-Proyectos/Images/question.png"))

enemy_frame= LabelFrame(root, text="Enemy", padx=50, pady=33 )
enemy_frame.grid(row=0, column=3)

global enemy_label

enemy_label = Label(enemy_frame, image=my_ask)
enemy_label.grid( row=0, column=3 )
  
def enemy_image():

    global enemy_number
    while True:
      enemy_number=rm.randrange(0,len(image_list))
      if enemy_number!=your_number-1:
        break
    enemy_label.config(image=image_list[enemy_number]) 


    button_back = Button(your_frame, text="<<", command=back, state=DISABLED)
    button_forward = Button(your_frame, text=">>", command=back, state=DISABLED)
    button_fight.config( text="Let´s fight",command=activate_fight, state=NORMAL)
    button_name.config(state=DISABLED)

    button_back.grid(row=1, column=0)
    button_name.grid(row=1, column=1)
    button_forward.grid(row=1, column=2)
    button_fight.grid(row=5,column=1)


#Botones iniciales

button_back = Button(your_frame, text="<<", command=back, state=DISABLED)
button_name=Button(your_frame, text="Choose", command=enemy_image)
button_forward = Button(your_frame, text=">>", command= lambda: forward(2))

button_back.grid(row=1, column=0)
button_name.grid(row=1, column=1)
button_forward.grid(row=1, column=2)


button_fight=Button(root, text="Lets fight",state=DISABLED)
button_fight.grid(row=5,column=1)



Pikachu=Pokemon_game(Pokemon,0)
charmander=Pokemon_game(Pokemon,1)
Bulbasuar=Pokemon_game(Pokemon,2)
Squirtle=Pokemon_game(Pokemon,3)

Peleadores=[Pikachu,charmander, Bulbasuar,Squirtle ]

def text_func(text):
  text_box = Text(
    your_stats,
    height=20,
    width=40
    )
  text_box.grid(row=0, column=0)
  text_box.insert('end', text)
  text_box.config(state='disabled')

  button_fight.config( text="Siguiente turno: ",command=activate_fight)

  if text=="Has ganado" or text=="Has perdido":
    button_fight.config( text="Salir ",command=root.quit)

  


def delscreen():
  for child in your_stats.winfo_children():
    child.destroy() 



def fight():
  for child in your_stats.winfo_children():
    child.destroy()
  Peleadores[your_number-1].pelea(Peleadores[enemy_number])
  
def botton():
  a=r.get()
  button_fight.config(text="Confirmar ataque: "+str(a),command=fight)

  


def activate_fight():

  for child in your_stats.winfo_children():
    child.destroy()
      
   
  your_stats.config( text='Lets fight')
      
  Radiobutton(your_stats, text=" 80% de exito: "+Pokemon[your_number-1]["ataques_por_esc"][0][0], variable=r, value=1, command=botton).grid(row=3, column=0)
  Radiobutton(your_stats, text=" 90% de exito: "+Pokemon[your_number-1]["ataques_por_esc"][1][0], variable=r, value=2, command=botton).grid(row=4, column=0)
  Radiobutton(your_stats, text=" 67% de exito: "+Pokemon[your_number-1]["ataques_por_esc"][2][0], variable=r, value=3, command=botton).grid(row=5, column=0)
  Radiobutton(your_stats, text=" 50% de exito: "+Pokemon[your_number-1]["ataques_por_esc"][3][0], variable=r, value=4, command=botton).grid(row=6, column=0)  

  button_fight.config( text="Escoger ataque")
  







root.mainloop()



























































from tkinter import *

#Creating a label
root = Tk() 
root.title( "Pokemon")

#myLabel1 = Label(root, text="Hello World!")
#myLabel2 = Label(root, text="My name is Edgar Agustin")
#myLabel3 = Label(root, text="Physics")

#Shoving it onto the screen
#myLabel1.grid(row=0,column=0)
#myLabel2.grid(row=1,column=5)
#myLabel3.grid(row=2,column=1)



e= Entry(root, width=35 ,borderwidth=5, bg="white", fg="black")
e.grid(row=0,column=0, columnspan=3, padx=10, pady=10)



#def myCLick():
 # myLabel = Label(root, text="Hello "+e.get())
 # myLabel.pack()

def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
    
def button_clear():
    e.delete(0,END)

def button_add():
    first_number = e.get()
    global f_number
    f_number=int(first_number)
    e.delete(0,END)

def button_equal():
    second_number=e.get()
    e.delete(0, END)
    e.insert(0, f_number+int(second_number))




button_1= Button( root, text="1", padx=40, pady=20, command=lambda:  button_click(1))
button_2= Button( root, text="2", padx=40, pady=20, command=lambda:  button_click(2))
button_3= Button( root, text="3", padx=40, pady=20, command=lambda:  button_click(3))
button_4= Button( root, text="4", padx=40, pady=20, command=lambda:  button_click(4))
button_5= Button( root, text="5", padx=40, pady=20, command=lambda:  button_click(5))
button_6= Button( root, text="6", padx=40, pady=20, command=lambda:  button_click(6))
button_7= Button( root, text="7", padx=40, pady=20, command=lambda:  button_click(7))
button_8= Button( root, text="8", padx=40, pady=20, command=lambda:  button_click(8))
button_9= Button( root, text="9", padx=40, pady=20, command=lambda:  button_click(9))
button_0= Button( root, text="0", padx=40, pady=20, command=lambda:  button_click(0))
button_add= Button( root, text="+", padx=39, pady=20, command=button_add)
button_equal= Button( root, text="=", padx=91, pady=20, command=button_equal)
button_clear= Button( root, text="Clear", padx=79, pady=20, command=button_clear)

button_subtract= Button( root, text="-", padx=39, pady=20, command=button_add)
button_multiply= Button( root, text="*", padx=39, pady=20, command=button_add)
button_divide= Button( root, text="/", padx=39, pady=20, command=button_add)

#Put the button in the screen

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)


#myButton= Button (root, text="Enter", command=myCLick, fg="black"  )





root.mainloop()










import random as rm

class Pokemon:
  dano_base = 10

  def __init__(self, especie, stats, tipo, fortalezas, debilidades, ataques_por_esc):
    self.especie = especie
    self.stats = stats
    self.current_stats = self.stats.copy()
    self.tipo = tipo
    self.debilidades = debilidades
    self.fortalezas = fortalezas
    self.ataques_por_esc = ataques_por_esc

  def centro_pokemon(self):
    self.current_stats = self.stats

  def pelea(self, rival):
    
    # Tu rival es furte o debil a ti?
    if self.tipo in rival.fortalezas:
      modificador_ataque = 1/2
      print(f"{rival.especie} es fuerte a los ataques de {self.especie} \n")
    elif self.tipo in rival.debilidades:
      modificador_ataque = 2
      print(f"{rival.especie} es debil a los ataques de {self.especie} \n")
    else:
      modificador_ataque = 1
    
    #eres fuerte o debil a tu rival?
    if rival.tipo in self.fortalezas:
      modificador_defensa = 1/2
      print(f"{self.especie} es fuerte a los ataques de {rival.especie} \n")
    elif rival.tipo in self.debilidades:
      modificador_defensa = 2
      print(f"{self.especie} es debil a los ataques de {rival.especie} ")
    else:
      modificador_defensa = 1

    # quien ataca primero
    if self.current_stats["velocidad"] >= rival.current_stats["velocidad"]:
      mi_turno = True
    else:
      mi_turno = False
    
    # combate por turnos
    while (self.current_stats["hp"] > 0) & (rival.current_stats["hp"] > 0):
      if mi_turno:
        # atacando

        print( " Escoger ataque " )
        print( f""" 
        1. {self.ataques_por_esc[0][0]}/ Daño: {int(self.ataques_por_esc[0][1]*self.current_stats["ataque"])}
        2. {self.ataques_por_esc[1][0]}/ Daño: {int(self.ataques_por_esc[1][1]*self.current_stats["ataque"])}
        3. {self.ataques_por_esc[2][0]}/ Daño: {int(self.ataques_por_esc[2][1]*self.current_stats["ataque"])}
        4. {self.ataques_por_esc[3][0]}/ Daño: {int(self.ataques_por_esc[3][1]*self.current_stats["ataque"])}
        """ )

        while True:
            try:
                escogido = int(input("Escribir el numero asociado al ataque a escoger: "))
                if escogido in [1,2,3,4]:
                    print(f"{self.especie} utliza {self.ataques_por_esc[escogido-1][0]} ")
                    break
                else:
                    print("Numero debe estar entre 0 y 4")
                    continue
            except:
                print("No valido, ingresar un numero")
        
        dano = int(
            self.dano_base * 
            (self.current_stats["ataque"] / rival.current_stats["defensa"]) * 
            modificador_ataque*self.ataques_por_esc[escogido-1][1]) 

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
                (self.current_stats["ataque"] / rival.current_stats["defensa"]) * 
                modificador_ataque*self.ataques_por_esc[escogido-1][1]) 

        else:
            dano=0
            print(f"Diantres!! {self.especie} ha fallado")


        rival.current_stats["hp"] -= dano
        print(f"{self.especie} hizo {dano} de daño a {rival.especie}")
        print(f"A {rival.especie} le quedan {rival.current_stats['hp']} puntos de vida")
      else:
        # defendiendo
        suerte_rival=rm.randrange(1,5,1)
        if suerte_rival != 1:
            dano = int(
            rival.dano_base *
            (rival.current_stats["ataque"] / self.current_stats["defensa"]) * 
            modificador_defensa)
        else:
            dano=0
            print(f"Genial!! {rival.especie4} ha fallado")
        
        self.current_stats["hp"] -= dano
        print(f"{rival.especie} hizo {dano} de daño a {self.especie}")
        print(f"A {self.especie} le quedan {self.current_stats['hp']} puntos de vida")
      mi_turno = not mi_turno
    else:
      if self.current_stats["hp"] <= 0:
        print(f'{rival.especie} ha ganado la pelea \n')
      else:
        print(f'{self.especie} ha ganado la pelea \n')

#Stats

squirtle = Pokemon(
    especie = "Squirtle",
    stats = {
        "velocidad": 43,
        "hp": 44,
        "ataque": 48,
        "defensa": 65},
    tipo = "agua",
    fortalezas = ["fuego"],
    debilidades = ["planta"],
    ataques_por_esc =  [["Placaje Tackle",1.0],["Látigo Tail Whip",.7],["Burbuja Bubble",1.3],["Refugio Withdraw",1.6]]
    )

charmander = Pokemon(
    especie = "Charmander",
    stats = {
        "velocidad": 65,
        "hp": 39,
        "ataque": 52,
        "defensa": 43},
    tipo = "fuego",
    fortalezas = ["planta"],
    debilidades = ["agua"],
    ataques_por_esc = [[ "Gruñido Growl" ,1.0], ["Ascuas Ember",.7], ["Pantalla de Humo Smokescreen" ,1.3],["Furia Dragón Dragon Rage",1.6]]
    )

bulbasaur = Pokemon(
    especie = "Bulbasaur",
    stats = {
        "velocidad": 45,
        "hp": 45,
        "ataque": 49,
        "defensa": 49},
    tipo = "planta",
    fortalezas = ["agua"],
    debilidades = ["fuego"],
    ataques_por_esc = [["Latigazo", 1.0], ["Bomba lodo" ,.7], ["Bomba germen",1.],["Bomba enselada" ,1.6]]
    )


squirtle.pelea(charmander)
squirtle.centro_pokemon()
charmander.centro_pokemon()
