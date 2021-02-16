# Questa funzione prende in ingresso la lista dei parametri di specifica, precedentemente 
# estratti dal corpo del messaggio e-mail, e la trasforma in un dizionario mediante il quale
# avviene l'interazione con i file csv (le chiavi del dizionario corrispondono ai campi dei csv).

from syntax import syntax_table

def msg_to_dict(parameters, allowed_keys = ['OGGETTO', 'MITTENTE', 'DESTINATARIO', 'DATA']):
    parameters = [parameters[i].split('=') for i in range(len(parameters))]
    check = [(len(parameters[i]) == 2) for i in range(len(parameters))] 
    # Serve a controllare di avere tante liste di due elementi, che corrispondono
    # il primo alla chiave e il secondo al valore di ogni voce del dizionario 
    print(check)
    if False in check: # Se ho almeno un elemento diasccoppiato
        errore = 'Errore, inserire correttamente i parametri\n'+syntax_table
        return errore # L'uscita è una stringa di errore
    param_dict = {parameters[i][0].upper(): parameters[i][1] for i in range(len(parameters))}
    for key in param_dict.keys():
        if key not in allowed_keys: # Se inserisco una chiave non prevista
            errore = f'Spiacente, comando {key} non riconosciuto.\nScegliere tra:\n{allowed_keys}'
            return errore # L'uscita è una stringa di errore
    return param_dict

if __name__ == '__main__':
    lista =  ['oggetto=arg1', 'mittente=m.rossi@rfi.it']
    print(msg_to_dict(lista))