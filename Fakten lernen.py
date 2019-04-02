#Programm für den TMS-Teil "Fakten lernen"
import random

names = [ "Breidenbach", "Majewski", "Mang", "Ney", "Vollrath", "Willer", "Feldhaus", "Frech", "Klaiber", "Werle", "Heilig", "Brandner", "Engert", "Runkel", "Schurig", "Alex", "Kehrer", "Röser", "Schöner", "Benning", "Diefenbach", "Haberkorn", "Neef", "Häberle", "Kienzle", "Nolting", "Behrmann", "Breunig", "Blankenburg", "Fisch", "Saathoff", "Senft", "Stemmler", "Köcher", "Reber", "Steinkamp", "Dinter", "Genz", "Eichholz", "Hassel", "Dierkes", "Eckart", "Schlemmer", "Tolksdorf", "Bartmann", "Bethge", "Großkopf", "Limbach", "Reischl", "Kämpf", "Scheerer", "Thielemann", "Frühauf", "Schardt", "Stöckel", "Gruhn", "Liese", "Fast", "Finkbeiner", "Orlowski", "Ostendorf", "Messer", "Oßwald", "Schenke", "Emmert", "Greb", "Naß", "Prüfer", "Kolberg", "Seelig", "Siemens", "Coenen", "Moog", "Prill", "Weinreich", "Strauss", "Bunge", "Freiberg", "Huppertz", "Lex", "Matthiesen", "Tappe", "Fels", "Fick", "Fritzsch", "Niermann", "Peetz", "Schwanke", "Traut", "Topp", "Tremmel", "Hackmann", "Heppner", "Hotz", "Stöber", "Weyand", "Wolfrum", "Kruppa", "Lembke", "Ruge", "Sager", "Wöhrle", "Zach", "Stauch", "Blau", "Nadler", "Deininger", "Wisniewski", "Eifler", "Wenig", "Ziemer", "Herget", "Janson", "Neuberger", "Seyfarth", "Storck", "Geissler", "Heßler", "Hochmuth", "Heinig", "Irmer", "Milz", "Quade", "Schrade", "Giebel", "Heiser", "Rebmann", "Schmidl", "Beetz", "Dold", "Lieske", "Sieben", "Lührs", "Haus", "Rieke", "Scheler", "Seewald", "Kowalewski", "Meusel", "Rödiger", "Scheu", "Hengst", "Zipfel", "Böning", "Graß", "Teubner", "Wölfle", "Heinzel", "Erben", "Hausner", "Hennecke", "Pietzsch", "Rahm", "Russ", "Grabow", "Lay", "Pitz", "Spieker", "Wagenknecht", "Düring", "Gottschlich", "Gottschling", "Wesemann", "Hemmer", "Kliem", "Weniger", "Würfel", "Hessel", "Effenberger", "Markmann", "Stumm", "Weihrauch", "Häfele", "Strehl", "Graßl", "Hendricks", "Giesecke", "Woll", "Niggemann", "Staudinger", "Tauber", "Thielmann", "Hanf", "Liebert", "Karle", "Kügler", "Mittmann", "Stotz", "Wohlfarth", "Knüppel", "Kortmann", "Adolf", "Gäbler", "Sauermann", "Wachsmuth", "Nolden", "Hofstetter", "Jesse", "Pongratz", "Schroer", "Vögele", "Bröcker", "Hauk", "Brinker", "Herb", "Hüls", "Hund", "Voigtländer", "Ganter", "Pfitzner", "Till", "Bendel", "Plöger", "Flaig", "Hieber", "Husmann", "Knoth", "Rosendahl", "Schink", "Stevens", "Kissel", "Kolodziej", "Pausch", "Walch", "Feiler", "Fengler", "Hackbarth", "Rombach", "Worm", "Flügge", "Grätz", "Küsters", "Patzer", "Kohnen", "Kurt", "Weinberg", "Krauße", "Leinweber", "Lindenberg", "Schönborn", "Bohm", "Dost", "Fellner", "Glaß", "Haider", "Kallenbach", "Röhm", "Rick", "Behling", "Dieterich", "Hüther", "Laumann", "Schnitzer", "Winzer", "Dorner", "Moor", "Schurr", "Tiede", "Claußen", "Hauber", "Michler", "Middendorf", "Saller", "Hildenbrand", "Jänicke" ]
occupations = [ "Pilot", "Abgeordnete", "Geschäftsführer",
                "Unternehmensberaterin", "Maschinenbauingenieur",
                "Physikerin", "Mathematiker", "Elektroingenieurin",
                "Amtsleiter", "Verwaltungsfachfrau", "Richter",
                "Staatsanwältin", "Lehrer", "Informatikerin",
                "Meteorologe", "Bauingenieurin", "Pfarrer",
                "Industriemechanikerin", "Feuerwehrmann",
                "Übersetzering", "Werbefachmann", "Versicherungsfachmann",
                "Flugzeugmechanikerin", "Grafiker", "Bankfachfrau",
                "Fotografin", "Feinmechaniker", "Sozialarbeiterin",
                "Buchhalter", "Museumswärterin", "Busfahrer",
                "Maurer", "Krankenschwester", "Polizistin",
                "Dachdecker", "Kellnerin", "Klempner",
                "Lastwagenfahrerin" ]

details = [ "belastbar", "durchsetzungsfähig", "ehrlich", 
            "empathisch", "fair", "flexibel", "geduldig", 
            "gewissenhaft", "hilfsbereit", "innovativ", 
            "kommunikativ", "konfliktfähig", "kreativ", 
            "leistungsbereit", "lernbereit", "loyal", 
            "mobil", "motiviert", "offen", "optimistisch", 
            "organisiert", "proaktiv", "widerstandsfähig", 
            "selbstbewusst", "selbstständig", "sorgfältig", 
            "sozial", "sportlich", "stabil", "teamfähig", 
            "unternehmerisch", "verantwortungsbewusst", 
            "zuverlässig", "zuversichtlich", "vier Kinder",
            "alleinerziehend", "ledig", "verheiratet", 
            "Notfall", "Normalstation", "Intensivstation", 
            "überwiesen", "Krankmeldung", "kinderlos" ]

diagnoses = [ "Erkältung", "Fieber", "Viruserkrankung",
              "Otitis media", "Mandelentzündung", "Fehlsichtigkeit",
              "Schielen", "Sehstörung", "Netzhauterkrankung",
              "Glaukom", "Muttermal", "Dermatitis",
              "Neurodermitis", "Pilzinfektion", "Akne",
              "Ohrerkrankung", "Hörvlerlust", "Gehörgangentzündung",
              "Nasennebenhöhlenentzündung", "Laryngitis", "Bauchschmerzen",
              "Harnwegsinfekt", "Harnblasenentzündung", "Nierensteine",
              "Rückenschmerzen", "Hämorrhoiden", "Kniegelenkarthrose",
              "Sehnenentzündung", "Bandscheibenvorfall", "Plattfuß",
              "Depressionen", "Epilepsie", "Angststörungen",
              "Schizophrenie", "Durchfall", "Husten" ]

ages = [25, 26, 27, 28, 29, 30, 35, 40, 45, 50, 60]

random.shuffle(names)
random.shuffle(occupations)
random.shuffle(details)
random.shuffle(diagnoses)
random.shuffle(ages)

persons = []
age = ages[0]
for i in range(0, 15):
    if i > 0 and i % 3 == 0:
        age = ages[int(i/3)]
    persons.append([names[i], age, occupations[i], details[i], diagnoses[i]])

def sortFunc(array):
    return array[1]

persons = sorted(persons, key=sortFunc)
file = open("Fakten lernen Infos.txt", "w")
for person in persons:
    file.write(person[0] + ":")
    for i in range(0, 15-len(person[0])):
        file.write(" ")
    file.write("ca. " + str(person[1]) + " Jahre, \t" +
          person[2] + ", " + person[3] + " - " + person[4] + "\n")

file.close()

file = open("Fakten lernen Fragen.txt", "w")
random.shuffle(persons)

def generateIndex(forbiddenIndex, r=[0, 4]):
    index = forbiddenIndex
    while index == forbiddenIndex:
        index = random.randint(r[0], r[1])
    return index

keywords = ["Name", "Alter", "Beruf", "Detail", "Diagnose"]

def adjust(index, m=14):
    if index > m:
        index -= m
    return index

solutions = []
questionnumber = 0

for i in range(0, 20):
    i = adjust(i)
    questionIndex = generateIndex(forbiddenIndex=1)
    answerIndex = generateIndex(forbiddenIndex=questionIndex)
    possibleAnswers = [ persons[i][answerIndex] ]
    for j in range(0, 4):
        personIndex = adjust(i + j)
        while persons[personIndex][answerIndex] in possibleAnswers:
            personIndex = adjust(personIndex+1)
        possibleAnswers.append(persons[personIndex][answerIndex])
    questionnumber += 1
    file.write(str(questionnumber) + ".  " + keywords[questionIndex] + ": " + persons[i][questionIndex] +
          ", Frage: " + keywords[answerIndex] + "\n")
    random.shuffle(possibleAnswers)
    solutionIndex = 0
    while possibleAnswers[solutionIndex] != persons[i][answerIndex]:
        solutionIndex += 1
    solutions.append(solutionIndex)
    for j in range(0, 5):
        file.write("(" + str(chr(65+j)) + ")  " + str(possibleAnswers[j]) + "\n")
    file.write("\n\n")

file.write("\n"*10)
for i in range(0, 20):
    file.write(str(i+1)+".: " + str(chr(65+solutions[i])) + " ")

file.close()
