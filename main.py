import webbrowser
import random
nstypelist = ["N", "S"]
ewtypelist = ["E", "W"]
coorddes = ['1', '1', '1', '1', '1', '1', '2', '1']
des = random.choice(coorddes)
urllist = 'https://earth.google.com/web/search/'
if des == "1":
    valtype = random.choice(nstypelist)
    valtype2 = random.choice(ewtypelist)
    intager1 = random.randint(0,180)
    intager2 = random.randint(0,180)
    intager1 = str(intager1)
    intager2 = str(intager2)
    intbase1 = intager1 + valtype
    intbase2 = intager2 + valtype2
    search = intbase1 + "+" + intbase2
    url = urllist + search
    url = str(url)
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
