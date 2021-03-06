#!/usr/bin/env python

import csv

reader = csv.reader(open("adressen.csv"))

# Ueber den Reader kann man direkt iterieren:
#
# We can directly iterate over the reader:
for row in reader:
    print "=" * 20
    for item in row:
        print repr(item)


# Das csv-Modul kommt offensichtlich auch damit klar, wenn innerhalb
# eines Strings Spalten-Delimiter, Zeilen-Delimiter (Zeilenumbrueche)
# und sogar String-Quotes (Anfuehrungszeichen) vorkommen. Soetwas ist
# nicht so einfach selbst zu parsen.
#
# Obviously, the reader can handle column delimiters, row delimiters
# (line breaks) and quitation marks inside of a string. Such a thing
# is not easy to parse manually.
