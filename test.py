import hashlib
import requests

def analyser_mot_de_passe():
    while True:
        password = input("Entrez un mot de passe : ")

        if password == "":
            print("\n Erreur : Vous n'avez rien entré ! Veuillez réessayer.")
            continue
        else:
            break

    print(f"\nMot de passe à analyser : **{password}**")
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
                print(f" AIE ! Ce mot de passe a fuité {count} fois.")
    print(prefix) 

    print(reponse)

    return password

if __name__ == "__main__":
    analyser_mot_de_passe()
