# Questa funzione prende in ingresso la stringa contenente il sito (o gruppo di siti)
# di interesse, e restituisce una stringa formattata contenente gli indirizzi IP e 
# lo stato dei server di interesse, ricercata all'interno del file IP.csv.

import csv
from asset import asset_list


def get_IP(criterion, filepath = 'IP.csv'):

    with open(filepath, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        # Creo una lista di tuple, ogni tupla è relativa ad un sito
        results = [(record['ASSET'],record['IP_FIS'],record['IP_VIR1'],record['IP_VIR2']) for record in csv_reader 
                    if record['ASSET']==criterion]
        text = ''
        if len(results) == 0: # Se il sito non viene trovato restituisce  una stringa di errore
            text = 'Spiacente, non ho trovato nulla riguardante'+' '+criterion+'\n\n'+asset_list
        else:
            for i in range(len(results)): # Converto ogni tupla in una unica stringa
                row = ' '.join(results[i]) + '\n'
                text+=row # Accodo le stringhe
    return text


if __name__ == "__main__":
    print(get_IP('genovabrignole'))
