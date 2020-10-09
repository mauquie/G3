import classpoker as poker



def coup(p, co, cr):

    cr.distribuer(5)

    for i in range(len(p.joueurs_participants)):
        p.joueurs_participants[i].evaluer()
        print(f"\nVoici la main de {p.joueurs_participants[i].nom} : {p.joueurs_participants[i].main}, sa meilleur combinaison : {p.joueurs_participants[i].combinaison.name()} et ses jetons : {p.joueurs_participants[i].tapis}")

    co.abattre()

    print(f"\nLe gagnant de ce coup est : {co.gagnant}")

    for i in range(len(p.joueurs_participants)):
        p.joueurs_participants[i].nouvelle_main()


def main(p, co, cr):
    
    choix = input(
        "\n-Entrer 1 pour commencer une partie avec 3 joueurs prédéfinis\n-Entrer 2 pour commencer une partie avec des joueurs personnalisés\n-Entrer 3 pour terminer la partie en cours\n-Appuyer sur ENTRER pour faire un coup :\n "
    )

    if p == None:
        if choix == "":
            print("La partie n'a pas encore commencée, impossible de faire un coup...")
            main(p, co, cr)

        elif int(choix) == 1:
            choix2 = int(input("\nEntrer le tapis initial des joueurs : "))
            p=poker.Partie(choix2)
            p.ajouter("Alice")
            p.ajouter("Bob")
            p.ajouter("Carl")

        elif int(choix) == 2:            
            joueur = []
            nom = input("Entrer le nom de chaque joueur (ENTRER après le nom pour l'ajouter et ENTRER sans le nom pour stopper) : ")
            while nom != "":
                joueur.append(nom)
                nom = input("Entrer le nom de chaque joueur : ")

            choix2 = int(input("\nEntrer le tapis initial des joueurs : "))
            p=poker.Partie(choix2)

            for i in range(len(joueur)):
                p.ajouter(joueur[i])

        elif int(choix) == 3:
            print("La partie n'a pas encore commencée...")
            main(p, co, cr)
        
        else:
            print("Votre saisie n'est pas correcte...")
            main(p, co, cr)

    else:
        if choix == "":
            if len(cr.paquet) <= len(p.joueurs_participants)*5:
                tapis_joueurs = []
                for i in range(len(p.joueurs_participants)):
                    tapis_joueurs.append(p.joueurs_participants[i].tapis)
                tapis_max = max(tapis_joueurs)
                for i in range(len(tapis_joueurs)):
                    if tapis_max == p.joueurs_participants[i].tapis:
                        winner = p.joueurs_participants[i]
                print(f"\nIl n'y a plus assez de cartes dans le paquet, la partie s'est terminée en {co.nb} coup{'s.' if co.nb > 1 else '.'}\nLe gagnant de la partie est {winner.nom} avec {winner.tapis} jetons.")
                exit()
            else:
                coup(p, co, cr)
                main(p, co, cr)

        elif int(choix) == 1:
            print("La partie est déjà créée...")
            main(p, co, cr)

        elif int(choix) == 2:
            print("La partie est déjà créée...")
            main(p, co, cr)

        elif int(choix) == 3:
            confirm = input('Etes-vous sûr de vouloir arrêter la partie ? ("oui" ou "non")\n')
            if confirm == "oui":
                tapis_joueurs = []
                for i in range(len(p.joueurs_participants)):
                    tapis_joueurs.append(p.joueurs_participants[i].tapis)
                tapis_max = max(tapis_joueurs)
                for i in range(len(tapis_joueurs)):
                    if tapis_max == p.joueurs_participants[i].tapis:
                        winner = p.joueurs_participants[i]
                print(f"\nLa partie s'est terminée en {co.nb} coup{'s.' if co.nb > 1 else '.'}\nLe gagnant de la partie est {winner.nom} avec {winner.tapis} jetons.")
                exit()
            elif confirm == "non":
                main(p, co, cr)
            else:
                print("Votre saisie n'est pas correcte...")
                main(p, co, cr)
        
        else:
            print("Votre saisie n'est pas correcte...")
            main(p, co, cr)

    p.jouer()
    co=poker.Coup()
    cr=poker.Croupier()
    cr.nouvelle_donne()
    coup(p, co, cr)
    main(p, co, cr)



p = None
co = None
cr = None

main(p, co, cr)
