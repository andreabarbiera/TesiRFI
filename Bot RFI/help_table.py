help_table="""
<html>
    <head>
        <title>Guida all'uso - Chatbot RFI</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            .rules li{
                font-size: 10pt;
                font-family: courier;
            }
            .help_table{
                margin: 10px;
                border: 1px solid grey;
                border-collapse: collapse;
                color:black;
                background-color: white;
                font-family: courier;
                font-size: 14pt;
                text-align: center;
                width: 60%;
            }
            .privileges_table{
                margin: 10px;
                border: 1px solid grey;
                border-collapse: collapse;
                color:black;
                background-color: white;
                font-family: courier;
                font-size: 14pt;
                text-align: center;
                width: 60%;
            }
            .help_table td{
                border: 1px solid grey;
                color: black;
                text-align: center;
                font-family: courier;
                font-size: 10pt;
                padding: 10px;   
            }
            .privileges_table td{
                border: 1px solid grey;
                color: black;
                text-align: center;
                font-family: courier;
                font-size: 10pt;
                padding: 10px;  
            }
            thead{
                text-align: center;
                font-family: courier;
                font-size: 12pt;
                border: 1px solid grey;
                color: black;
                background-color: lightgray;
            }
            .privileges_table tr:hover {
                background-color: lightgrey;
            }
            ul.table {
                padding:0;
                list-style-position: inside;
                font-family: courier;
            }
            .asset_table{
                margin: 10px;
                border: 1px solid grey;
                border-collapse: collapse;
                color:black;
                background-color: white;
                font-family: courier;
                font-size: 14pt;
                text-align: center;
                width: 60%;
            }
            .asset_table td{
                border: 1px solid grey;
                color: black;
                text-align: center;
                font-family: courier;
                font-size: 10pt;
                padding: 10px;  
            }
            .asset_table thead{
                text-align: center;
                font-family: courier;
                font-size: 12pt;
                border: 1px solid grey;
                color: black;
                background-color: lightgray;
            }
            h1, h2 {
                width: 60%;
                font-family: courier;
                text-align: center;
            }
            .logo {
                width: 30%;
                margin-left: auto;
                margin-right: auto;
            }
            div.img_cont {
                width:60%;
                text-align: center;
            }
            div{
                width:60%;
                text-align: center;
                padding:2%                
            }
            li{
                width:auto;
                text-align: left;
                font-family: courier;
                padding-bottom:2%   
            }
        </style>
    </head>
    <h1>Guida all'uso - Chatbot RFI</h1>
    <h2>Regole generali</h2>
    <div>
        <ul class="rules">
            <li>Per usufruire del servizio &egrave necessario utilizzare una mail autorizzata.</li>
            <li>Indicare le istruzioni all'interno del corpo di un messaggio email, seguendo la sintassi indicata. Non &egrave necessario specificare l'oggetto del messaggio.</li>
            <li>Inserire soltanto testo nella mail, evitando allegati o contenuto in html.</li>
            <li>Ogni parola deve essere separata dalla successiva attraverso un singolo spazio, eccezion fatta per alcuni blocchi specifici che saranno analizzati in seguito, per i quali non è necessario lo spazio ma il simbolo di uguaglianza.</li>
            <li>La prima parola di ogni messaggio deve corrispondere al comando, che individua l'azione da svolgere.</li>
            <li>A seguire, indicare il target, ossia l'oggetto dell'azione.</li>
            <li>A seconda del comando, potrebbe essere necessario specificare ulteriori unità logiche.</li>
            <li>Inviare la mail all'indirizzo bot.areatecnica.DPA@rfi.it.</li>
        </ul>      
    </div>
    <h2>Tabella riassuntiva delle funzioni</h2>
    <table class="help_table">
        <thead> <!-- testata -->
            <th>Comando</th>
            <th>Target</th>
            <th>Specifiche</th>
            <th>Funzione</th>
            <th>Sintassi</th>
            <th>Esempi d'uso</th>
        </thead>
        <tbody>
            <tr>
                <td rowspan="6">Invia</td>
                <td>report</td>
                <td><ul><li>nome_asset</li><li>tipo_report</li><li>"modificabile"</li></ul></td>
                <td>Richiesta report impianti, server o telecamere</td>
                <td>Dopo aver digitato comando e target, inserire le specifiche <u>nell'ordine indicato</u> separate da uno spazio (l'ultima specifica è opzionale)</td>
                <td><ul class="table"><li>"invia report romatermini impianti"</li><li>"invia report firenzesmn telecamere modificabile"</li></ul></td>
            </tr>
            <tr>
                <td>note</td>
                <td>"oggetto=... mittente=... destinatario=... data=..."</td>
                <td>Richiesta note interne secondo differenti criteri</td>
                <td>Dopo aver digitato comando e target, inserire le specifiche desiderate digitando dopo il simbolo "=" il valore della specifica. Separare una specifica dalla successiva con un singolo spazio</td>
                <td><ul class="table"><li>"invia note mittente=m.rossi oggetto=polfer"</li><li>"invia note mittente=c.bianchi data=20201210</li></ul></td>
            </tr>
            <tr>
                <td>IP</td>
                <td>nome_asset</td>
                <td>Richiesta degli indirizzi IP (fisici e virtuali) e dello stato delle macchine di un dato sito</td>
                <td>Dopo aver digitato comando e target, digitare l'asset di interesse</td>
                <td>"invia ip genovapp"</td>
            </tr>
            <tr>
                <td>log</td>
                <td>Non richiesto</td>
                <td>Richiesta del file contenente il log degli eventi</td>
                <td>Indicare soltanto comando e target, separati da uno spazio</td>
                <td>"invia log"</td>
            </tr>
            <tr>
                <td>profilo</td>
                <td>Non richiesto</td>
                <td>Richiesta del proprio privilegio e delle autorizzazioni ad esso connesse</td>
                <td>Indicare soltanto comando e target, separati da uno spazio</td>
                <td>"invia profilo"</td>
            </tr>
            <tr>
                <td>guida</td>
                <td>Non richiesto</td>
                <td>Richiesta di una guida completa con esempi d'uso, in formato PDF</td>
                <td>Indicare soltanto comando e target, separati da uno spazio</td>
                <td>"invia guida"</td>
            </tr>
            <tr>
                <td>Aggiungi</td>
                <td>Non richiesto</td>
                <td><ul><li>mail_utente</li><li>privilegio</li></ul></td>
                <td>Aggiunta di account autorizzati</td>
                <td>Dopo aver digitato comando e target, inserire le specifiche <u>nell'ordine indicato</u> separate da uno spazio</td>
                <td>"aggiungi c.bianchi@rfi.it area_tecnica"</td>                
            </tr>
            <tr>
                <td>Rimuovi</td>
                <td>Non richiesto</td>
                <td>mail_utente</td>
                <td>Rimozione dagli account autorizzati</td>
                <td>Dopo aver digitato comando e target, inserire la specifica separata da uno spazio</td>
                <td>"rimuovi m.rossi@rfi.it"</td>  
            </tr>
            <tr>
                <td>Modifica</td>
                <td>Non richiesto</td>
                <td><ul><li>mail_utente</li><li>privilegio</li></ul></td>
                <td>Modifica dei privilegi degli account autorizzati</td>
                <td>Dopo aver digitato comando e target, inserire le specifiche <u>nell'ordine indicato</u> separate da uno spazio</td>
                <td>"modifica m.rossi@rfi.it stakeholder"</td>                
            </tr>
        </tbody>
    </table>
    <h2>Tabella riassuntiva delle autorizzazioni</h2>
    <table class="privileges_table">
        <thead> <!-- testata -->
            <th>Privilegio</th>
            <th>IP</th>
            <th>Note</th>
            <th>Modifica</th>
            <th>Aggiungi</th>
            <th>Rimuovi</th>
            <th>Modificabile</th>
            <th>Report</th>
            <th>Log</th>
            <th>Profilo</th>
            <th>Guida</th>
        </thead>
        <tbody>
            <tr>
                <td>admin</td>
                <td>✓</td>
                <td>✓</td>
                <td>✓</td>
                <td>✓</td>
                <td>✓</td>
                <td>✓</td>
                <td>✓</td>
                <td>✓</td>
                <td>✓</td>
                <td>✓</td>
            </tr>
            <tr>
                <td>user</td>
                <td>✓</td>
                <td>✓</td>
                <td>✗</td>
                <td>✗</td>
                <td>✗</td>
                <td>✗</td>
                <td>✓</td>
                <td>✗</td>
                <td>✓</td>
                <td>✓</td>
            </tr>
            <tr>
                <td>stakeholder</td>
                <td>✓</td>
                <td>✗</td>
                <td>✗</td>
                <td>✗</td>
                <td>✗</td>
                <td>✗</td>
                <td>✓</td>
                <td>✗</td>
                <td>✓</td>
                <td>✓</td>
            </tr>
            <tr>
                <td>area_tecnica</td>
                <td>✓</td>
                <td>✓</td>
                <td>✗</td>
                <td>✗</td>
                <td>✗</td>
                <td>✓</td>
                <td>✓</td>
                <td>✗</td>
                <td>✓</td>
                <td>✓</td>
            </tr>
        </tbody>
    </table>

    <table class="asset_table">
        <thead> <!-- testata -->
            <th colspan="3">Lista asset</th>
        </thead>
        <tbody>
            <tr>
                <td>baricentrale</td>
                <td>bolognacentrale</td>
                <td>firenzesmn</td>
            </tr>
            <tr>
                <td>genovabrignole</td>
                <td>genovapp</td>
                <td>milanocentrale</td>
            </tr>
            <tr>
                <td>napolicentrale</td>
                <td>palermocentrale</td>
                <td>romatermini</td>
            </tr>
            <tr>
                <td>romatiburtina</td>
                <td>torinopn</td>
                <td>veneziamestre</td>
            </tr>
            <tr>
                <td>veneziasl</td>
                <td>veronapn</td>
                <td></td>
            </tr>
        </tbody>
    </table>
</html>
"""