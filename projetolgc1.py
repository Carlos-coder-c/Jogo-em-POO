import sys

class Jogo:

 def __init__(self, pular, abaixar, atirar,  defender, correr, jogar_fogo, congelar, tacar_pedra):
        self.pular = pular
        self.abaixar = abaixar
        self.atirar = atirar
        self.defender = defender
        self.correr = correr
        self.jogar_fogo = jogar_fogo
        self.congelar = congelar
        self.tacar_pedra = tacar_pedra

 def pular_abaixar(self, pular, abaixar):
  print('Você está em uma situação perigosa uma bala gigante está vindo em sua direção, escolha sua ação')
  ação = str(input("Qual ação tu escolhe?:"))

  if ação == pular:
   print("Você conseguiu sobreviveu com sucesso!")

  elif ação == abaixar:
    print("Você foi de vasco da gama!")
    sys.exit()  


 def atirar_defender_correr(self, atirar, defender, correr):
     print("Bom  você encontrou o monstro gigante qual sua proxima ação?")
     ação = str(input("Escolha sua ação (atirar), (defender) ou (correr)?"))

     if ação == atirar:
      print("Você derrotou o monstro com sua IPER MEGA BLASTE BAZUCA")

     elif ação == defender:
      print("Você defendeu defendeu e defendeu o monstro cansou fujaaa!")

     elif ação == correr:
      print("Sua escolha foi correr o monstro era mais rapido você foi derrotado")
      sys.exit()  # encerra o programa


 def boss(self, jogar_fogo, congelar, tacar_pedra):
      print("Você está de cara com o bosso apenas 1 ataque necessita sua vitoria escolha a sua ação (jogar_fogo), (tacar_pedras), (congelar)")
      
      ação = str(input("Escolha sua ação: "))

      if ação == jogar_fogo:
        print("O monstro foi queimado em pedacinhos, Parabens você completou o game!")
      elif ação == congelar:
        print("Monstro congelado com sucesso você escapou!")
      elif ação == tacar_pedra:
        print("VOCÊ PERDEU O GAME!")
        sys.exit()  


jogo_rpg = Jogo("pular", "abaixar", "atirar", "defender", "correr", "jogar_fogo", "congelar", "tacar_pedra")
jogo_rpg.pular_abaixar("pular", "abaixar")
jogo_rpg.atirar_defender_correr("atirar", "defender", "correr")
jogo_rpg.boss("jogar_fogo", "congelar", "tacar_pedra")
