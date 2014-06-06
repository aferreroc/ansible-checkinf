#!/usr/bin/env python
import sys
import os, fnmatch
import re

import sys, getopt


def main(argv):
  inputpath = ''
  outputfile = ''
  typefiles = ''
  try:
    myopts, args = getopt.getopt(sys.argv[1:],"i:o:t:")
  except getopt.GetoptError as e:
    print (str(e))
    print ("Usage %s -t <interface> -i <inputpath> -o <outputfile>" %  sys.argv[0])
    sys.exit(2)
  for opt, arg in myopts:
    if opt == '-h':
       print ("Usage %s -t <interface> -i <inputpath> -o <outputfile>" % sys.argv[0])
       sys.exit()
    elif opt in ("-i", "--ipath"):
       inputpath = arg
    elif opt in ("-o", "--ofile"):
       outputfile = arg
    elif opt in ("-t", "--ttype"):
       typefiles = arg

  #print 'Input path is "', inputpath
  #print 'Output file is "', outputfile
  #print 'Type is "', typefiles

  #Desired output
  #<nombre_maquina>        <errores_paquetes_UDP>(primer punto)    <errores RX>(punto 2)   <paquetes dropped>(punto 2)             <paquetes_descartados>(punto 3)


  fout = open(outputfile, 'w')
  fout.write("%-15s %10s %10s %10s %15s\n" %
        ("Host", "UDP rcv err","RX err", "RX drp", "Result"))

  for dirpath, dirs, files in os.walk(inputpath):
    for filename in fnmatch.filter(files, "*_" + typefiles):
      #fout.write(filename+"\n")
      with open(os.path.join(dirpath, filename)) as f:
        # one file open, handle it, next loop will present you with a new file
        #fout.write(f.read())
        match1 = False
        for line in f:

          match = re.match("host=(.*) udp_errors=(.*) RX-ERR=(.*) RX-DRP=(.*)", line)

          hayErrores = "OK"

          if match:
            fout.write("%-15s %10s %10s %10s %15s\n" %
                (match.group(1) if match.group(1).strip() else "-----",
                match.group(2) if match.group(2).strip() else "not in driver",
                match.group(3) if match.group(3).strip() else "not in driver",
                match.group(4) if match.group(4).strip() else "not in driver",
                hayErrores))
          else:
            nada = "-----"
            fout.write("%-15s %10s %10s %10s %15s\n" %
                (nada,
                nada,
                nada,
                nada,
                nada))

  fout.close()

if __name__ == "__main__":
   main(sys.argv[1:])
