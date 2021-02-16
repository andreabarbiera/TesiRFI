asset_list = """<!DOCTYPE html> <!-- convenzione -->
<html>
    <head>
        <style>
            .asset_table{
                margin: 10px;
                border: 1px solid grey;
                border-collapse: collapse;
                color:black;
                background-color: white;
                font-family: courier;
                font-size: 14pt;
                text-align: center;
                width: 50%;
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
                width: 50%;
                font-family: courier;
                text-align: center;
            }
            div{
                width:50%;
                text-align: center;
                padding:2%                
            }
        </style>
    </head>
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