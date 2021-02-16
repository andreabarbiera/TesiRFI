# Questa funzione prende in ingresso il dizionario dei parametri che identificano un
# nuovo utente, e aggiungono un nuovo record al file csv degli utenti se non esiste
# già un utente con l'indirizzo e-mail passato in ingresso.

import csv
import os


def add_user (param_dict): # Dizionario di parametri in ingresso
    fieldnames = ['MAIL','PRIVILEGI'] # Campi del file csv   
    this_file_path = os.path.abspath(__file__) # Percorso assoluto di questo file
    BASE_DIR = os.path.dirname(this_file_path) # Directory che contiene questo file 
    filepath = os.path.join(BASE_DIR, 'users.csv') # Percorso del file da leggere 
    exists = False # True se esiste già un record con la e-mail in ingresso
    with open(filepath, 'r+', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter = ',') # Leggo i record come un dizionario
        for user in csv_reader:
            if user['MAIL'] == param_dict['MAIL']:
                exists = True
                break
        if not exists: # Se non esiste ancora l'utente, lo aggiungo
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames, delimiter = ',') 
            csv_writer.writerow(param_dict)
    return

if __name__ == "__main__":
    add_user({'MAIL':'m.rossi@rfi.it', 'PRIVILEGI':'user'})