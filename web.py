import webbrowser, math

# in.txt
numbers = []
try:
    file = open("in.txt", "r")
    for line in file.readlines():
        try:
            numbers.append(float(line))
        except ValueError:
            numbers.append(1)
    file.close()
    try:
        x1 = numbers[0]
    except IndexError:
        x1 = 1
    try:
        i1 = numbers[1]
    except IndexError:
        i1 = 1
    try:
        x2 = numbers[2]
    except IndexError:
        x2 = 1
    try:
        i2 = numbers[3]
    except IndexError:
        i2 = 1
    try:
        n = numbers[4]
    except IndexError:
        n = 1
except IOError:
    print("Blad otwierania pliku")

#out.txt
results = []
try:
    file = open("out.txt", "r")
    for line in file.readlines():
        try:
            results.append(float(line))
        except ValueError:
            results.append(0)
    file.close()
except IOError:
    print("Blad otwierania pliku")

if len(results) < 9:
    results = [0, 0, 0, 0, 0, 0, 0, 0, 0]

def plusorminus(number):
    if number >= 0:
        return " + " + str(number)
    else:
        return " " + str(number)

try:
    file = open("index.html", "w", encoding="utf-8")
    content = """
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Liczby zespolone</title>
    <style>
        *, body {
            margin: 0;
            padding: 0;
            color: rgb(255, 255, 255);
            font-size: 24px;
        }
        table {
            width: 50vw;
            height: 50vh;
            margin-top: 10vh;
        }
        table,
        td {
            border: 3px solid #333;
            text-align: center;
        }
        table, th {
            background: rgb(114, 114, 245);
        }

        thead,
        tfoot {
            background-color: #333;
            color: #fff;
        }
        .center {
            margin-left: auto;
            margin-right: auto;
        }
    </style>
</head>
<body>
    <table class="center">
        <thead>
            <tr>
                <th colspan="4">Działania na liczbach zespolonych</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Dodawanie</td>
                <td>""" + str(x1) + plusorminus(i1) + """i</td>
                <td>""" + str(x2) + plusorminus(i2) + """i</td>
                <td>""" + str(round(results[0])) + " " + plusorminus(round(results[1])) + """i</td>
            </tr>
            <tr>
                <td>Odejmowanie</td>
                <td>""" + str(x1) + plusorminus(i1) + """i</td>
                <td>""" + str(x2) + plusorminus(i2) + """i</td>
                <td>""" + str(round(results[2])) + " " + plusorminus(round(results[3])) + """i</td>
            </tr>
            <tr>
                <td>Mnozenie</td>
                <td>""" + str(x1) + plusorminus(i1) + """i</td>
                <td>""" + str(x2) + plusorminus(i2) + """i</td>
                <td>""" + str(round(results[4])) + " " + plusorminus(round(results[5])) + """i</td>
            </tr>
            <tr>
                <td>Dzielenie</td>
                <td>""" + str(x1) + plusorminus(i1) + """i</td>
                <td>""" + str(x2) + plusorminus(i2) + """i</td>
                <td>""" + str(round(results[6])) + " " + plusorminus(round(results[7])) + """i</td>
            </tr>
            <tr>
                <td>Potegowanie</td>
                <td>""" + str(x1) + plusorminus(i1) + """i</td>
                <td> </td>
                <td>""" + str(round(results[8])) + " " + plusorminus(round(results[9])) + """i</td>
            </tr>
        </tbody>
    </table>
</body>
</html>
    """
    file.write(content)
    file.close()
    webbrowser.open_new_tab('index.html')

except IOError:
    print("Blad otwierania pliku")