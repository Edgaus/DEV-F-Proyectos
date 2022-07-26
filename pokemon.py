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