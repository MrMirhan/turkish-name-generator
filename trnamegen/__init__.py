import random, os
import pandas as pd

path = os.path.dirname(__file__)

def firstName(ntype=0):
    df = pd.read_csv(path + "/data/isimler.csv")
    if ntype == 0:
        adflist = df['isimler'].tolist()
        return random.choice(adflist)
    elif ntype == 1:
        edf = df[df.cinsiyet == "E"]
        udf = df[df.cinsiyet == "U"]
        edflist = edf['isimler'].tolist()
        udflist = udf['isimler'].tolist()
        edflist.append(udflist)
        return random.choice(edflist)
    elif ntype == 2:
        kdf = df[df.cinsiyet == "K"]
        udf = df[df.cinsiyet == "U"]
        kdflist = kdf['isimler'].tolist()
        udflist = udf['isimler'].tolist()
        kdflist.append(udflist)
        return random.choice(kdflist)

def lastName():
    stripped_linefile = open(path + "/data/soyisimler.txt", "r", encoding="utf-8")
    slines = []
    def manual_replace(s, char, index):
        return s[:index] + char + s[index +1:]
    for line in stripped_linefile:
        stripped_line = line
        if "İ" in stripped_line:
            stripped_line = stripped_line.replace("İ", "i")
        if "I" in stripped_line:
            stripped_line = stripped_line.replace("I", "ı")
        if "Ö" in stripped_line:
            stripped_line = stripped_line.replace("Ö", "ö")
        if "Ş" in stripped_line:
            stripped_line = stripped_line.replace("Ş", "ş")
        if "Ç" in stripped_line:
            stripped_line = stripped_line.replace("Ç", "ç")
        if "Ü" in stripped_line:
            stripped_line = stripped_line.replace("Ü", "ü")
        stripped_line = stripped_line.lower()
        if "i" == stripped_line[0]:
            stripped_line = manual_replace(stripped_line, "İ", 0)
        elif "ı" == stripped_line[0]:
            stripped_line = manual_replace(stripped_line, "I", 0)
        elif "ö" == stripped_line[0]:
            stripped_line =  manual_replace(stripped_line, "Ö", 0)
        elif "ş" == stripped_line[0]:
            stripped_line =  manual_replace(stripped_line, "Ş", 0)
        elif "ç" == stripped_line[0]:
            stripped_line =  manual_replace(stripped_line, "Ç", 0)
        elif "ü" == stripped_line[0]:
            stripped_line =  manual_replace(stripped_line, "Ü", 0)
        else:
            stripped_line =  stripped_line.title()
        stripped_line = stripped_line.strip()
        slines.append(stripped_line)
    return random.choice(slines)

def randomName(gender=0):
    if gender == 0:
        name = firstName(0)
    elif gender == 1:
        name = firstName(1)
    elif gender == 2:
        name = firstName(2)
    surname = lastName()
    return name + " " + surname