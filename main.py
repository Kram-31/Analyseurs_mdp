def analyse_len():
	score_sec = 0
	len_pass = len(password)
	print(len_pass)
	if len_pass >= 20:
		score_sec += 4 
	elif len_pass >= 16:
		score_sec += 3
	elif len_pass >= 12:
		score_sec += 2
	elif len_pass >= 8:
		score_sec += 1
	else: 
		score_sec += 0
	return score_sec
def analyser_mot_de_passe():
	while True:
		password = input("Entrez un mot de passe : ")

		if password == "":
			print("\n❌ Erreur : Vous n'avez rien entré ! Veuillez réessayer.")
			continue
		else:
			break

	print(f"\nMot de passe à analyser : **{password}**")	
	score_sec = 0
	len_pass = len(password)
	print(len_pass)
	if len_pass >= 20:
		score_sec += 4 
	elif len_pass >= 16:
		score_sec += 3
	elif len_pass >= 12:
		score_sec += 2
	elif len_pass >= 8:
		score_sec += 1
	else: 
		score_sec += 0
	print(f"Votre score est de ",score_sec)
	if passw
	
	return password

if __name__ == "__main__":
	analyser_mot_de_passe()
