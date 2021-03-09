#!/usr/bin/env python

import sys, csv
import sploit
def show_help():
    print sys.argv[0] + " imput.csv"
    print "\tinput.csv - l'USER$ table dump un CSV en utilisant l'outil comme SQL Scratchpad"

def orjogn():
    try:
        with open(sys.argv[1], "rb") as csvfile:
            reader = csv.reader(csvfile, delimiter=",", quotechar="\"")
            try:
                for row in reader:
                    if len(str(row[3])) == 16:
                        print str(row[1]).lower() + ":0$" + row[1] + "#" + row [3]
            except IndexError:
                sploit.show_error("Le fichier d'entrée doit être un CSV valide pour pouvoir être utilisé, comme délimitateur \" comme guillemet ")
            except IQError:
                sploit.show_error("Tu as besoin de spécifié l'entrée du fichier CSV")
                
        if __name__ == "__main__":
            if len(sys.argv) != 2 or (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
                show_help()
        else:
              orjohn()
              