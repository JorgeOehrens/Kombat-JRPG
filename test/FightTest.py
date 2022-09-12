from models.characters.Tonynstallone import TonynStallone
from models.characters.Character import Character
from models.movements.BasicAttack import Puño
from models.characters.ArnaldorShuatseneguer import ArnoldShuatseneguer


def RecibeDanage(playerAttack: 'Character' ):

    player2= TonynStallone()

    lifeNow= player2.energyNow

    player2.eventNow.subscribe(
        lambda event: print(event)
    )

    for a in range(7):
        playerAttack.attack(player2, Puño())
        print('Life player 2;', player2.energyNow)

    assert player2.energyNow < lifeNow




def tests():
    RecibeDanage(ArnoldShuatseneguer())