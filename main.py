import pandas

# Créé par moret, le 15/03/2025 en Python 3.7
print("Give two criteria for us to generate a ranking for the best food to eat")

var1 = "Protein"
quest1 = "maximum"
var2 = "Carbs"
quest2 = "maximum"

var1 = input("criteria 1")
quest1 = input("want the 'maximum' or the 'mininimum' ? ")
var2 = input("criteria 2")
quest2 = input("want the 'maximum' or the 'mininimum' ? ")

monfichier = pandas.read_csv("modified_file.csv")
monfichier = monfichier.loc[monfichier["Category"]=="Dairy products"]

print(monfichier)


if quest1== "maximum":
    print("hi")
    monclassement1= monfichier.sort_values (by= [var1], ascending= False)
else: monclassement1= monfichier.sort_values (by= [var1], ascending= True)

print(monclassement1)

if quest1== "maximum":
    print("hi")
    monclassement2= monfichier.sort_values (by= [var2], ascending= False)
else: monclassement2= monfichier.sort_values (by= [var2], ascending= True)

print(monclassement2)

rank1 = monclassement1["Food"].tolist()
rank2 = monclassement2["Food"].tolist()

newdic = {}
for i in range(len(rank1)):
    newpos = int((i + rank2.index(rank1[i]))/2)
    newdic[rank1[i]] = newpos

print(newdic)

sorted = []

k = 0
while len(sorted) < 7:
    for cle, valeur in newdic.items():
        if valeur == k and len(sorted) < 7:
            print(valeur)
            if cle not in sorted:
                sorted.append(cle)
    k += 1

print(sorted)

