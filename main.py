from Personnage import Personnage
from Arme import Arme

epee_legendaire = Arme("Épée légendaire", 10)
joueur1 = Personnage("Wise", "Mage", 55, 75, 3, 10, epee_legendaire)
joueur2 = Personnage("Belle", "Berserker", 55, 110, 15, 7)

joueur1.afficher_info()
joueur2.afficher_info()

joueur1.attaquer(joueur2)
joueur2.afficher_info()