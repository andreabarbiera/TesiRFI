# Questa funzione serve a modificare il profilo di un utente. Essa prende in 
# ingresso il dizionario contenente l'indirizzo e-mail ed i nuovi privilegi
# dell'utente, e li sostituisce all'interno del file csv degli utenti. 

import csv
import os


def edit_user(param_dict):
    this_file_path = os.path.abspath(__file__) # Percorso assoluto di questo file
    BASE_DIR = os.path.dirname(this_file_path) # Directory che contiene questo file 
    filepath = os.path.join(BASE_DIR, 'users.csv')

    with open(filepath, 'r') as csv_file: 
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        new_filepath = os.path.join(BASE_DIR, 'temporary.csv')

        with open(new_filepath, 'w', newline = '') as csv_temp:
            fieldnames = ['MAIL','PRIVILEGI']
            csv_writer = csv.DictWriter(csv_temp, fieldnames = fieldnames, delimiter = ',') 
            csv_writer.writeheader() 
            for user in csv_reader:
                if user['MAIL'] == param_dict['MAIL']: # Sostituisco solo i privilegi corrispondenti all'utente
                    user['PRIVILEGI'] = param_dict['PRIVILEGI']              
                csv_writer.writerow(user) # Scrivo su un nuovo file 'temporary.csv'

    os.remove(filepath) # Elimino il vecchio file utenti
    os.rename(new_filepath, filepath) # Rinomino il nuovo file come il vecchio
            
    return 


if __name__ == "__main__":
    edit_user({'MAIL':'m.rossi@rfi.it','PRIVILEGI':'stakeholder'})