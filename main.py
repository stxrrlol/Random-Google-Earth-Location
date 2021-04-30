import webbrowser
import random
import xlrd
coorddes = ['1', '1', '1', '1', '1', '1', '2', '1']
des = random.choice(coorddes)
urllist = 'https://earth.google.com/web/search/'
if des == "1":
    randint1 = random.randint(1, 28560)
    loc = "worldcities.xls"
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    city = sheet.cell_value(randint1, 1)
    city = city.replace(" ", "+")
    url = urllist + city + "/"
    webbrowser.open_new_tab(url)
if des == "2":
    intager1 = "50.6071"
    intager2 = "165.9729"
    valtype = "S"
    valtype2 = "E"
    intbase1 = intager1 + valtype
    intbase2 = intager2 + valtype2
    search = intbase1 + "+" + intbase2
    url = urllist + search
    url = str(url)
    webbrowser.open_new_tab(url)
