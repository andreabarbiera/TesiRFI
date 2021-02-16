# Questa funuzione prende in ingresso la stringa contenente l'indirizzo e-mail
# dell'utente e la richiesta effettuata, e fornisce in  uscita la stringa privilege 
# che contiene le autorizzazioni associate all'utente.

import csv
import os


def get_privilege(email):
    privilege = None
    this_file_path = os.path.abspath(__file__) # Percorso assoluto di questo file
    BASE_DIR = os.path.dirname(this_file_path) # Directory che contiene questo file
    filepath = os.path.join(BASE_DIR, 'users.csv')
    with open(filepath, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for user in csv_reader:
            if user['MAIL'] == email:
                privilege = user['PRIVILEGI']
                break # Utente già trovato: interrompo la ricerca nel file
    return privilege

# Questa funuzione prende in ingresso la stringa contenente l'indirizzo e-mail
# dell'utente e la richiesta effettuata, e fornisce in  uscita la variabile booleana
# authorized, che assume valore True se l'utente è autorizzato, False altrimenti.


def check_user(privilege, request):
    this_file_path = os.path.abspath(__file__) # Percorso assoluto di questo file
    BASE_DIR = os.path.dirname(this_file_path) # Directory che contiene questo file
    filepath = os.path.join(BASE_DIR, 'privileges.csv')
    with open(filepath, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        authorized = False
        for row in csv_reader:
            if row['PRIVILEGIO'] == privilege:
                if row[request] == 'True': 
                    authorized = True
                break # Privilegio già trovato: interrompo la ricerca nel file
    return authorized


if __name__ == "__main__":
    privilege = get_privilege('m.rossi@rfi.it')
    request = 'invia'
    authorized = check_user(privilege, request)
    print(authorized)

