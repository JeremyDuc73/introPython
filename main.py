import wordies


def verif_saisie():
    choose_number = input("Veuillez choisir un nombre entre 1 et " + str(len(wordies.words)) + " : ")
    try:
        val_check = int(choose_number)
        if val_check not in range(0, len(wordies.words) + 1):
            verif_saisie()
        else:
            return int(val_check)
    except ValueError:
        verif_saisie()


val = verif_saisie()
mot_choisi = wordies.words[val - 1]


def verif_mot():
    choose_word = input("Devine mon mot : ")
    if choose_word == mot_choisi:
        print("VICTOIRE")
    else:
        verif_mot()


verif_mot()
