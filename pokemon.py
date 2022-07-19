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
      print(f"{self.especie} es debil a los ataques de {rival.especie} \n")
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
        print( " Escribir el numero asociado al ataque a escoger " )
        escogido = input( f""" 
        1. {self.ataques_por_esc["Normal"][0]}
        2. {self.ataques_por_esc["Normal"][1]}
        3. {self.ataques_por_esc["Normal"][2]}
        4. {self.ataques_por_esc["Normal"][3]}
        """ )

        dano = int(
            self.dano_base * 
            (self.current_stats["ataque"] / rival.current_stats["defensa"]) * 
            modificador_ataque) 
        rival.current_stats["hp"] -= dano
        print(f"{self.especie} hizo {dano} de daño a {rival.especie}")
        print(f"A {rival.especie} le quedan {rival.current_stats['hp']} puntos de vida")
      else:
        # defendiendo
        dano = int(
            rival.dano_base *
            (rival.current_stats["ataque"] / self.current_stats["defensa"]) * 
            modificador_defensa)
        self.current_stats["hp"] -= dano
        print(f"{rival.especie} hizo {dano} de daño a {self.especie}")
        print(f"A {self.especie} le quedan {self.current_stats['hp']} puntos de vida")
      mi_turno = not mi_turno
    else:
      if self.current_stats["hp"] <= 0:
        print(f'{rival.especie} ha ganado la pelea \n')
      else:
        print(f'{self.especie} ha ganado la pelea \n')



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
    ataques_por_esc = {
        "Normal" : [["Placaje Tackle",35],["Látigo Tail Whip",35],["Burbuja Bubble",35],["Refugio Withdraw",35]]
    })

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
    ataques_por_esc = {
        "Gruñido Growl" : ["normal",35],
        "Ascuas Ember" : ["normal",35],
        "Pantalla de Humo Smokescreen" : ["normal",35],
        "Furia Dragón Dragon Rage" : ["normal",35]
    })

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
    ataques_por_esc = {
        "Latigazo" : ["normal",35],
        "Bomba lodo" : ["normal",35],
        "Bomba germen" : ["normal",35],
        "Furia Dragón Dragon Rage" : ["normal",35]
    })


squirtle.pelea(charmander)
squirtle.centro_pokemon()
charmander.centro_pokemon()