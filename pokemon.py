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
