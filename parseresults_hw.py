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


  fout = open(outputfile, 'w')
  fout.write("%-15s %10s %15s %15s %15s %15s %15s %15s %15s\n" %
        ("Host", "RX Ring Buff","driver", "driver-ver", "firmware-ver", "bus-info", "Coalescing RX", "RX disc", "RX fw disc"))

  for dirpath, dirs, files in os.walk(inputpath):
    for filename in fnmatch.filter(files, "*_" + typefiles):
      #fout.write(filename+"\n")
      with open(os.path.join(dirpath, filename)) as f:
        # one file open, handle it, next loop will present you with a new file
        #fout.write(f.read())
        match1 = False
        for line in f:

          match = re.match("host=(.*) RX=(.*) driver=(.*) version=(.*) firmware-version=(.*) bus-info=(.*) rx-usecs=(.*) rx_discards=(.*) rx_fw_discards=(.*) pci_nomsi=(.*) pcie_aspm_policy=(.*)",
                  line)

          hayErrores = "OK"

          if match:
            fout.write("%-15s %10s %15s %15s %15s %15s %15s %15s %15s %15s %25s\n" %
                (match.group(1) if match.group(1).strip() else "-----",
                match.group(2) if match.group(2).strip() else "-----",
                match.group(3) if match.group(3).strip() else "-----",
                match.group(4) if match.group(4).strip() else "-----",
                match.group(5) if match.group(5).strip() else "-----",
                match.group(6) if match.group(6).strip() else "-----",
                match.group(7) if match.group(7).strip() else "-----",
                match.group(8) if match.group(8).strip() else "-----",
                match.group(9) if match.group(9).strip() else "-----",
                match.group(10) if match.group(10).strip() else "-----",
                match.group(11) if match.group(11).strip() else "-----"))
          else:
            nada = "-----"
            fout.write("%-15s %10s %15s %15s %15s %15s %15s %15s %15s %15s %25s\n" %
                (nada,
                nada,
                nada,
                nada,
                nada,
                nada,
                nada,
                nada,
                nada,
                nada,
                nada))

  fout.close()

if __name__ == "__main__":
   main(sys.argv[1:])
