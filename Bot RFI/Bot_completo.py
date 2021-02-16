#!/usr/bin/env python
# -*- coding: utf-8 -*-

########################### LEGGE IL MESSAGGIO E SE TROVA IL FILE LO MANDA.
########################### AGGIORNA IL DATALOG
########################### DA FARE: INVIA DATALOG CON 2 ARGOMENTI (METTO LA CARTELLA COL MESE DEL DATALOG O MODIFICO CON IF???)
########################### DA FARE: TABELLA HTML CON FUNZIONE HELP


import imaplib  # serve a ricevere messaggi, come smtplib serviva a inviarli
import email
import smtplib #serve per l'errore
import credentials  # credenziali accesso
from send_mail_attachment import send_mail_attachment
import os
import csv
from update_datalog import update_datalog
from add_user import add_user
from remove_user_duplicate import remove_user
from creadiz import msg_to_dict
from get_IP import get_IP
from notes_from_attribute import notes_from_attribute
from edit_user_duplicate import edit_user
from check_user import get_privilege, check_user
from privilege_exists import privilege_exists
from user_exists import user_exists
from privileges import priv_table
from help_table import help_table
from asset import asset_list
from welcome_message import welcome_message
from notes_param import notes_table


host = "imap.gmail.com"
username = credentials.username
password = credentials.password
this_file_path = os.path.abspath(__file__)  # Percorso assoluto di questo file
BASE_DIR = os.path.dirname(
    this_file_path
)  # Cartella che contiene questo file (Python_codes)


def get_inbox():

    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)
    mail.select("inbox")
    _, search_data = mail.search(None, "UNSEEN")  # _ è un placeholder per una variabile, spacchetto (unpacking) la tupla ignorando il primo elemento
    my_message = []
    for num in search_data[0].split():  # search data è una lista con un elemento. Con split separo gli elementi del primo elemento secondo gli spazi. In uscita ho una lista di stringhe
        email_data = {}
        _, data = mail.fetch(num, "(RFC822)")
        _, b = data[0]
        email_message = email.message_from_bytes(b)

        for header in ["subject", "to", "from", "date"]:
            print("{}: {}".format(header, email_message[header]))
            email_data[header] = email_message[header]

        for part in email_message.walk():

            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                email_data["body"] = body.decode()
                instruction = email_data["body"].strip().lower()
                try:
                    instruction = instruction.split("\n",1)[0]
                    instruction = instruction.split()
                    sender = email_data["from"].split()[-1].strip("<>")
                    privilege = get_privilege(sender)
                    command = instruction[0].lower()

                    if command.lower() == "aggiungi":
                        if check_user(privilege, command.upper()):
                            try: #se ho inserito il numero giusto di parametri
                                user = instruction[1].lower()  # Indirizzo e-mail
                                privilegio = instruction[2].lower()  # .lower() dovrebbe essere inutile 
                                param_dict = {"MAIL": user, "PRIVILEGI": privilegio}
                                if privilege_exists(privilegio):
                                    if not user_exists(user):                                  
                                        try:
                                            send_mail_attachment(
                                                text="",
                                                subject="Utente Aggiunto",
                                                from_email="Bot DPA - RFI",
                                                to_emails=[user],
                                                html="Sei stato aggiunto come {}".format(privilegio) +"\n\n"+welcome_message,
                                                filepath=None,
                                                filename=None,
                                            )
                                            text="MAIL: {}\nPRIVILEGI: {}".format(user, privilegio)
                                            send_mail_attachment(
                                                text=text,
                                                subject="Utente Aggiunto",
                                                from_email="Bot DPA - RFI",
                                                to_emails=[email_data["from"]],
                                                html=None,
                                                filepath=None,
                                                filename=None,
                                            )
                                            add_user(param_dict)
                                        except smtplib.SMTPRecipientsRefused:
                                            text="Spiacente, indirizzo {} non valido".format(user)
                                            send_mail_attachment(
                                                text=text,
                                                subject="Errore",
                                                from_email="Bot DPA - RFI",
                                                to_emails=[email_data["from"]],
                                                html=None,
                                                filepath=None,
                                                filename=None,
                                            )
                                    else:
                                        text="Spiacente, utente {} già esistente".format(user)
                                        send_mail_attachment(
                                            text=text,
                                            subject="Errore",
                                            from_email="Bot DPA - RFI",
                                            to_emails=[email_data["from"]],
                                            html=None,
                                            filepath=None,
                                            filename=None,
                                        )
                                else:
                                    text="Spiacente, privilegio {} inesistente".format(privilegio)
                                    send_mail_attachment(
                                        text=text,
                                        subject="Errore",
                                        from_email="Bot DPA - RFI",
                                        to_emails=[email_data["from"]],
                                        html=None,
                                        filepath=None,
                                        filename=None,
                                    )
                            except IndexError:
                                text = "Inserire un numero adeguato di parametri (prima la mail e poi i privilegi)"
                                send_mail_attachment(
                                    text=text,
                                    subject="Errore",
                                    from_email="Bot DPA - RFI",
                                    to_emails=[email_data["from"]],
                                    html=None,
                                    filepath=None,
                                    filename=None,
                                )
                        else:
                            send_mail_attachment(
                                text="Spiacente, non godi dei privilegi necessari",
                                subject="Errore",
                                from_email="Bot DPA - RFI",
                                to_emails=[email_data["from"]],
                                html="Spiacente, non godi dei privilegi necessari\n\n"+priv_table,
                                filepath=None,
                                filename=None,
                            )

                    elif command.lower() == "rimuovi":
                        if check_user(privilege, command.upper()):
                            try:
                                user = instruction[1]
                                param_dict = {"MAIL": user}
                                if user_exists(user):
                                    text="MAIL: {}".format(user)
                                    remove_user(param_dict)
                                    send_mail_attachment(
                                        text=text,
                                        subject="Utente Rimosso",
                                        from_email="Bot DPA - RFI",
                                        to_emails=[email_data["from"]],
                                        html=None,
                                        filepath=None,
                                        filename=None,
                                    )
                                else:
                                    text="Spiacente, utente {} inesistente".format(user)
                                    send_mail_attachment(
                                        text=text,
                                        subject="Errore",
                                        from_email="Bot DPA - RFI",
                                        to_emails=[email_data["from"]],
                                        html=None,
                                        filepath=None,
                                        filename=None,
                                    )
                            except IndexError:
                                text = "Inserire un numero adeguato di parametri (prima la mail e poi i privilegi)"
                                send_mail_attachment(
                                    text=text,
                                    subject="Errore",
                                    from_email="Bot DPA - RFI",
                                    to_emails=[email_data["from"]],
                                    html=None,
                                    filepath=None,
                                    filename=None,
                                )
                        else:
                            send_mail_attachment(
                                text="Spiacente, non godi dei privilegi necessari",
                                subject="Errore",
                                from_email="Bot DPA - RFI",
                                to_emails=[email_data["from"]],
                                html="Spiacente, non godi dei privilegi necessari\n\n"+priv_table,
                                filepath=None,
                                filename=None,
                            )


                    elif command.lower() == "modifica":
                        if check_user(privilege, command.upper()):
                            try:  # Se ho inserito il numero giusto di parametri
                                user = instruction[1].lower()
                                privilegio = instruction[2].lower()
                                param_dict = {"MAIL": user, "PRIVILEGI": privilegio}
                                if privilege_exists(privilegio):
                                    if user_exists(user):
                                        try:
                                            send_mail_attachment(
                                                text="",
                                                subject="Utente Modificato - Bot RFI",
                                                from_email="Bot DPA - RFI",
                                                to_emails=[user],
                                                html="Sei stato modificato come {}".format(privilegio) +"\n\n"+priv_table,
                                                filepath=None,
                                                filename=None,
                                            )                                                                                
                                            text="MAIL: {}\nPRIVILEGI: {}".format(user, privilegio)
                                            send_mail_attachment(
                                                text=text,
                                                subject="Utente Modificato",
                                                from_email="Bot DPA - RFI",
                                                to_emails=[email_data["from"]],
                                                html=None,
                                                filepath=None,
                                                filename=None,
                                            )
                                            edit_user(param_dict)
                                        except smtplib.SMTPRecipientsRefused:
                                            text="Spiacente, indirizzo {} non valido".format(user)
                                            send_mail_attachment(
                                                text=text,
                                                subject="Errore",
                                                from_email="Bot DPA - RFI",
                                                to_emails=[email_data["from"]],
                                                html=None,
                                                filepath=None,
                                                filename=None,
                                            ) 
                                    else:
                                        text="Spiacente, utente {} inesistente".format(user)
                                        send_mail_attachment(
                                            text=text,
                                            subject="Errore",
                                            from_email="Bot DPA - RFI",
                                            to_emails=[email_data["from"]],
                                            html=None,
                                            filepath=None,
                                            filename=None,
                                        )
                                else:
                                    text="Spiacente, privilegio {} inesistente".format(privilegio)
                                    send_mail_attachment(
                                        text=text,
                                        subject="Errore",
                                        from_email="Bot DPA - RFI",
                                        to_emails=[email_data["from"]],
                                        html=None,
                                        filepath=None,
                                        filename=None,
                                    )
                            except IndexError:
                                text = "Inserire un numero adeguato di parametri (prima la mail e poi i privilegi)"
                                send_mail_attachment(
                                    text=text,
                                    subject="Errore",
                                    from_email="Bot DPA - RFI",
                                    to_emails=[email_data["from"]],
                                    html=None,
                                    filepath=None,
                                    filename=None,
                                )
                        else:
                            send_mail_attachment(
                                text="Spiacente, non godi dei privilegi necessari",
                                subject="Errore",
                                from_email="Bot DPA - RFI",
                                to_emails=[email_data["from"]],
                                html="Spiacente, non godi dei privilegi necessari\n\n"+priv_table,
                                filepath=None,
                                filename=None,
                            )



                    elif command.lower() == "invia":

                        target = instruction[1]

                        if (target.lower() == "ip"):  # problema: se IP non è maiuscolo non me lo trova dentro il file IP.csv
                            if check_user(privilege, "IP"):
                                try:
                                    criterion = instruction[2].lower()
                                    text = get_IP(criterion=criterion)  # text già include il messaggio di errore se non trova nulla
                                    send_mail_attachment(
                                        text=text,
                                        subject="Risposta",
                                        from_email="Bot DPA - RFI",
                                        to_emails=[email_data["from"]],
                                        html=text,
                                        filepath=None,
                                        filename=None,
                                    )
                                except IndexError:
                                    text = "Inserire un numero adeguato di parametri (inserire l'asset di interesse)"
                                    send_mail_attachment(
                                        text=text,
                                        subject="Errore",
                                        from_email="Bot DPA - RFI",
                                        to_emails=[email_data["from"]],
                                        html=None,
                                        filepath=None,
                                        filename=None,
                                    )

                            else:
                                send_mail_attachment(
                                    text="Spiacente, non godi dei privilegi necessari",
                                    subject="Errore",
                                    from_email="Bot DPA - RFI",
                                    to_emails=[email_data["from"]],
                                    html="Spiacente, non godi dei privilegi necessari\n\n"+priv_table,
                                    filepath=None,
                                    filename=None,
                                )

                        elif target.lower() == "note":
                            if check_user(privilege, target.upper()):
                                try:
                                    filepath = []
                                    criteria = instruction[2:]
                                    criteria = [criteria[i].lower() for i in range(len(criteria))]
                                    param_dict = msg_to_dict(criteria)
                                    if (type(param_dict) == str):  # se non riconosce una chiave inserita
                                        send_mail_attachment(
                                            text=param_dict,
                                            subject="Errore",
                                            from_email="Bot DPA - RFI",
                                            to_emails=[email_data["from"]],
                                            html=param_dict,
                                            filepath=None,
                                            filename=None,
                                        )
                                    else:
                                        file_list = notes_from_attribute(param_dict)  # qui dovrei provare a vedere quale parametro non è stato riconosciuto
                                        for i in range(len(file_list)):
                                            filepath.append(
                                                os.path.join(BASE_DIR, "note", file_list[i])
                                            )
                                        try:
                                            send_mail_attachment(
                                                text="Allego il file",
                                                subject="Risposta",
                                                from_email="Bot DPA - RFI",
                                                to_emails=[email_data["from"]],
                                                html=None,
                                                filepath=filepath,
                                                filename=file_list,
                                            )
                                        except:  # Se file_list è una stringa
                                            send_mail_attachment(
                                                text=file_list,
                                                subject="Errore",
                                                from_email="Bot DPA - RFI",
                                                to_emails=[email_data["from"]],
                                                html=file_list,
                                                filepath=None,
                                                filename=None,
                                            )
                                except IndexError: 
                                    text = "Inserire i parametri per la ricerca delle note"
                                    send_mail_attachment(
                                        text=text,
                                        subject="Errore",
                                        from_email="Bot DPA - RFI",
                                        to_emails=[email_data["from"]],
                                        html=text+"\n\n"+notes_table,
                                        filepath=None,
                                        filename=None,
                                    )

                            else:
                                send_mail_attachment(
                                    text="Spiacente, non godi dei privilegi necessari",
                                    subject="Errore",
                                    from_email="Bot DPA - RFI",
                                    to_emails=[email_data["from"]],
                                    html="Spiacente, non godi dei privilegi necessari\n\n"+priv_table,
                                    filepath=None,
                                    filename=None,
                                )

                        elif target.lower() == "report":
                            if check_user(privilege, target.upper()):
                                try:
                                    site = instruction[2].lower()  # questo rimane misto maiuscole-minuscole (es.RomaTermini) altrimenti non trova il file
                                    folder = instruction[3].lower()
                                    try:
                                        editable = instruction[4].lower()
                                        if editable == "modificabile": 
                                            if check_user(privilege, editable.upper()):
                                                ext = ".txt"
                                                text = ""
                                            else:  # per non lasciar scoperto ext nel caso in cui l'utente sbagli a scrivere 'modificabile'
                                                ext = ".pdf"
                                                text = "Non godi dei privilegi necessari a ricevere la versione modificabile. "
                                        else:
                                            ext = ".pdf"
                                            text = "Specifica '{}' non riconosciuta. Invio la versione non modificabile. ".format(editable)                                        
                                    except:  # se non viene inserita la specifica "modificabile" non incorro in errori
                                        ext = ".pdf" 
                                        text = ""
                                    try:
                                        folder_dict={"impianti":["impianti"], 
                                                    "telecamere":["telecamere"], 
                                                    "server":["server"], 
                                                    "completo":["server","impianti","telecamere"]}
                                        filename = []
                                        filepath = []
                                        for cartella in folder_dict[folder]:
                                            filename.append(site+cartella+ext)
                                            filepath.append(os.path.join(BASE_DIR, "report", cartella, site+ext))
                                        print(filepath)
                                        try:
                                            send_mail_attachment(
                                                text=text+"Allego il file",
                                                subject="Risposta",
                                                from_email="Bot DPA - RFI",
                                                to_emails=[email_data["from"]],
                                                html=None,
                                                filepath=filepath,
                                                filename=filename,
                                            )
                                        except:
                                            send_mail_attachment(
                                                text="Spiacente, file non trovato",
                                                subject="Errore",
                                                from_email="Bot DPA - RFI",
                                                to_emails=[email_data["from"]],
                                                html="Spiacente, file non trovato\n\n"+asset_list,
                                                filepath=None,
                                                filename=None,
                                            )
                                    except KeyError:
                                            send_mail_attachment(
                                                text="Inserire un tipo valido di report, tra 'server', 'impianti', 'telecamere', 'completo'",
                                                subject="Errore",
                                                from_email="Bot DPA - RFI",
                                                to_emails=[email_data["from"]],
                                                html=None,
                                                filepath=filepath,
                                                filename=filename,
                                            )                                              
                                except IndexError:
                                    send_mail_attachment(
                                        text="Inserire un numero adeguato di parametri",
                                        subject="Errore",
                                        from_email="Bot DPA - RFI",
                                        to_emails=[email_data["from"]],
                                        html="Inserire un numero adeguato di parametri\n\n"+help_table,
                                        filepath=None,
                                        filename=None,
                                    )                                                              

                            else:
                                send_mail_attachment(
                                    text="Spiacente, non godi dei privilegi necessari",
                                    subject="Errore",
                                    from_email="Bot DPA - RFI",
                                    to_emails=[email_data["from"]],
                                    html="Spiacente, non godi dei privilegi necessari\n\n"+priv_table,
                                    filepath=None,
                                    filename=None,
                                )


                        elif target.lower() == "guida":
                            if user_exists(sender):
                                filename=[]
                                filename.append("guida.pdf")
                                filepath=[]
                                filepath.append(os.path.join(BASE_DIR, "guida.pdf"))
                                print(filepath)
                                send_mail_attachment(
                                    text="Allego la guida",
                                    subject="Guida all'uso",
                                    from_email="Bot DPA - RFI",
                                    to_emails=[email_data["from"]],
                                    html=None,
                                    filepath=filepath,
                                    filename=filename,
                                )


                        elif target.lower() == "log":
                            if check_user(privilege, target.upper()):
                                filepath=[]
                                filename=[]
                                filename.append("datalog.csv")
                                filepath.append(os.path.join(BASE_DIR, filename[0]))
                                send_mail_attachment(
                                    text="Allego il log eventi",
                                    subject="Log RFI",
                                    from_email="Bot DPA - RFI",
                                    to_emails=[email_data["from"]],
                                    html=None,
                                    filepath=filepath,
                                    filename=filename,
                                )
                            else:
                                send_mail_attachment(
                                    text="Spiacente, non godi dei privilegi necessari",
                                    subject="Errore",
                                    from_email="Bot DPA - RFI",
                                    to_emails=[email_data["from"]],
                                    html="Spiacente, non godi dei privilegi necessari\n\n"+priv_table,
                                    filepath=None,
                                    filename=None,
                                )

    ##########################################################################################################à

                        elif target.lower() == "profilo":
                            if check_user(privilege, target.upper()):
                                text="I privilegi associati a questo profilo sono quelli di {}\n".format(privilege)
                                send_mail_attachment(
                                    text="",
                                    subject="Info profilo",
                                    from_email="Bot DPA - RFI",
                                    to_emails=[email_data["from"]],
                                    html=text+priv_table,
                                    filepath=None,
                                    filename=None,
                                )
                            else:
                                send_mail_attachment(
                                    text="Spiacente, non godi dei privilegi necessari",
                                    subject="Errore",
                                    from_email="Bot DPA - RFI",
                                    to_emails=[email_data["from"]],
                                    html="Spiacente, non godi dei privilegi necessari\n\n"+priv_table,
                                    filepath=None,
                                    filename=None,
                                )


                    else:
                        send_mail_attachment(
                            text="Spiacente, comando non riconosciuto",
                            subject="Errore",
                            from_email="Bot DPA - RFI",
                            to_emails=[email_data["from"]],
                            html="Spiacente, comando non riconosciuto\n\n"+help_table,
                            filepath=None,
                            filename=None,
                        )

                except IndexError:
                    text = "Inserire un numero adeguato di parametri"
                    send_mail_attachment(
                        text=text,
                        subject="Errore",
                        from_email="Bot DPA - RFI",
                        to_emails=[email_data["from"]],
                        html=text+"\n\n"+help_table,
                        filepath=None,
                        filename=None,
                    )                    



                update_datalog(
                    username=email_data["from"], message=email_data["body"].strip()
                )

            elif part.get_content_type() == "text/html":
                pass

        my_message.append(email_data)

    return my_message


if __name__ == "__main__":
    while True:
        my_inbox = get_inbox()
    # print(my_inbox)
# print(search_data)
