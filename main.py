import hashlib
import requests
import re

def analyser_mot_de_passe():
    while True:
        password = input("Entrez un mot de passe : ")

        if password == "":
            print("\n Erreur : Vous n'avez rien entré  Veuillez réessayer")
            continue
        else:
            break

    print(f"\nMot de passe à analyser : **{password}**")    
#--> E(Vérification 1: Longueur);
    score_sec = 0
    len_pass = len(password)
    if len_pass >= 16:
        score_sec += 30
    elif len_pass >= 12:
        score_sec += 20
    elif len_pass >= 8:
        score_sec += 10
    else: 
        score_sec += 0
    
# --> F(Vérification 2: Complexité / Entropie);
    if re.search(r'[a-z]', password):
        score_sec += 10
    if re.search(r'[A-Z]', password):
        score_sec += 10
    if re.search(r'[0-9]', password):
        score_sec += 10
    if re.search(r'[!@#$%^&*()_+\-=\[\]{}|;:\'",.<>/?`~]', password):
        score_sec += 10

#--> G(Vérification 3: Liste de Mots de Passe Fuités);
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1_hash[:5]
    suffixe = sha1_hash[5:]
    
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    reponse = requests.get(url)

    if reponse.status_code == 200:
        hashes_retournes = (line.split(':') for line in reponse.text.splitlines())
        for h, count in hashes_retournes: 
            if h == suffixe:
                score_sec = 0
                print(f"Ce mot de passe a fuité {count} fois")

    if score_sec >= 70:
        print("EXCELLENT. Très sécurisé")
    elif score_sec >= 50:
        print("BON. Peut être utilisé, mais peut être amélioré")
    else:
        print("FAIBLE. A changer immédiatement")


    return password

if __name__ == "__main__":
    analyser_mot_de_passe()
