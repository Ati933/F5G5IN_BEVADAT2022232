"""
1. Értelmezd az adatokat!!!

2. Írj egy osztályt a következő feladatokra:  
     - Neve legyen NJCleaner és mentsd el a NJCleaner.py-ba. Ebben a fájlban csak ez az osztály legyen.
     - Konsturktorban kapja meg a csv elérési útvonalát és olvassa be pandas segítségével és mentsük el a data (self.data) osztályszintű változóba 
     - Írj egy függvényt ami sorbarendezi a dataframe-et 'scheduled_time' szerint növekvőbe és visszatér a sorbarendezett df-el, a függvény neve legyen 'order_by_scheduled_time' és térjen vissza a df-el  
     - Dobjuk el a from és a to oszlopokat, illetve a nan-okat és adjuk vissza a df-et. A függvény neve legyen 'drop_columns_and_nan' és térjen vissza a df-el  
     - A date-et alakítsd át napokra, pl.: 2018-03-01 --> Thursday, ennek az oszlopnak legyen neve a 'day'. Ezután dobd el a 'date' oszlopot és térjen vissza a df-el. A függvény neve legyen 'convert_date_to_day' és térjen vissza a df-el   
     - Hozz létre egy új oszlopot 'part_of_the_day' névvel. A 'scheduled_time' oszlopból számítsd ki az alábbi értékeit. A 'scheduled_time'-ot dobd el. A függvény neve legyen 'convert_scheduled_time_to_part_of_the_day' és térjen vissza a df-el  
         4:00-7:59 -- early_morning  
         8:00-11:59 -- morning  
         12:00-15:59 -- afternoon  
         16:00-19:59 -- evening  
         20:00-23:59 -- night  
         0:00-3:59 -- late_night  
    - A késéeket jelöld az alábbiak szerint. Az új osztlop neve legyen 'delay'. A függvény neve legyen pedig 'convert_delay' és térjen vissza a df-el
         0 <= x < 5  --> 0  
         5 <= x    --> 1  
    - Dobd el a felesleges oszlopokat 'train_id' 'scheduled_time' 'actual_time' 'delay_minutes'. A függvény neve legyen 'drop_unnecessary_columns' és térjen vissza a df-el
    - Írj egy olyan metódust, ami elmenti a dataframe első 60 000 sorát. A függvénynek egy string paramétere legyen, az pedig az, hogy hova mentse el a csv-t (pl.: 'data/NJ.csv'). A függvény neve legyen 'save_first_60k'. 
    - Írj egy függvényt ami a fenti függvényeket összefogja és megvalósítja (sorbarendezés --> drop_columns_and_nan --> ... --> save_first_60k), a függvény neve legyen 'prep_df'. Egy paramnétert várjon, az pedig a csv-nek a mentési útvonala legyen. Ha default value-ja legyen 'data/NJ.csv'

3.  A feladatot a HAZI06.py-ban old meg.
    Az órán megírt DecisionTreeClassifier-t fit-eld fel az első feladatban lementett csv-re. 
    A feladat célja az, hogy határozzuk meg azt, hogy a vonatok késnek-e vagy sem. 0p <= x < 5p --> nem késik, ha 5 < x --> késik.
    Az adatoknak a 20% legyen test és a splitelés random_state-je pedig 41 (mint órán)
    A testset-en 80% kell elérni. Ha megvan a minimum százalék, akkor azzal paraméterezd fel a decisiontree-t és azt kell leadni.

    A leadásnál csak egy fit kell, ezt azzal a paraméterre paraméterezd fel, amivel a legjobb accuracy-t elérted.

    A helyes paraméter megtalálásához használhatsz grid_search-öt.
    https://www.w3schools.com/python/python_ml_grid_search.asp 

4.  A tanításodat foglald össze 4-5 mondatban a HAZI06.py-ban a fájl legalján kommentben. Írd le a nehézségeket, mivel próbálkoztál, mi vált be és mi nem. Ezen kívül írd le 10 fitelésed eredményét is, hogy milyen paraméterekkel probáltad és milyen accuracy-t értél el. 
Ha ezt feladatot hiányzik, akkor nem fogadjuk el a házit!

HAZI06-
    -NJCleaner.py
    -HAZI06.py

##################################################################
##                                                              ##
## A feladatok közül csak a NJCleaner javítom unit test-el      ##
## A decision tree-t majd manuálisan fogom lefuttatni           ##
## NJCleaner - 10p, Tanítás - acc-nál 10%-ként egy pont         ##
## Ha a 4. feladat hiányzik, akkor nem tudjuk elfogadni a házit ##
##                                                              ##
##################################################################
"""

classifier = DecisionTreeClassifier(min_samples_split=30, max_depth=10)
classifier.fit(X_train, Y_train)

#Nekem ezzel sikerült elérnem a 80,075%-ot. Kezdetben azzal próbálkoztam, hogy egyesével növeltem a max_depth értéket 3-tól kezdve, 
#ez túl nagy sikert nem hozott önmagában, nagyjából olyan 0,001-et hozhatott minden egyes max_depth növelés. Nem tudtam viszont ezt csak
#önmagában tovább növelni egy bizonyos értéktől kezdve (6 volt a max), mivel exceptiont kaptam. Ezt az oldotta meg, hogy elkezdtem a
#min_samples_split értékét is növelni, azt vettem észre, hogy ezt viszont a max_depth növelésével együtt egyre nagyobb értékkel kell növelni,
#hogy ne kapjak egyáltalán exceptiont. Végül a min_samples_split=30, max_depth=10 paraméterek hoztak megváltást magukkal.

#Próba 1: min_samples_split=3, max_depth=3
#Próba 2: min_samples_split=3, max_depth=4
#Próba 3: min_samples_split=3, max_depth=5
#Próba 4: min_samples_split=3, max_depth=6
#Próba 5: min_samples_split=3, max_depth=9 (exception)
#Próba 6: min_samples_split=3, max_depth=8 (exception)
#Próba 7: min_samples_split=3, max_depth=7 (exception)
#Próba 8: min_samples_split=4, max_depth=7 (exception)
#Próba 9: min_samples_split=9, max_depth=7 
#Próba 10: min_samples_split=15, max_depth=10 (exception)
#Próba 11: min_samples_split=30, max_depth=10 -> accuracy 0,80075

#Mindegyikhez nem mentettem le az accuracy értékét, sorry, ezt csak később vettem észre hogy kell, újra már nem futtatnám őket,
#de a lényeg, hogy 0,788x és 0,79xx között ingadozott valahol, nem túl nagy lépcsőfokokkal egymás között.