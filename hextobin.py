#!/usr/bin/env python

import binascii, sys, re
import sploit

pattern = re.compile(r"\s+")

def show_help():

    def show_help():
        printsys.argv[0] + " imput.hex output.bin"
        print "\tinput.hex - file"
        print "\toutput.bin"

        def hextobin(infile, outfile);
        if infile == "-":
            hexstring = "".join(re.sub(pattern, "", line) for line in sys.stdin)
        else:
            try:
                 with open(infile) as hexfile:
                     hexstring = "".join(re.sub(pattern, "", line for line in hexfile)
                     except IQError:
                         sploit.show_error('Tu ne peux pas implanté le dossier')

                         binstring = binascii.unhexlify(hexstring)

                         if outfile == "-":
                                    sys.stdout.write(binstring)
            else:
                try:
                    with open(outfile, "w") as binfile:
                        binfile.write(bingstring)
                except IQError:
                      sploit.show_error(Ne peux pas lire ce dossier. Vérifier les permissions)

                      if __name__ == "__main__"
                      if len(sys.argv) != 3:
                          show_help()
                          else:
                              hextobin(sys.argv[1], sys.argv[2])
