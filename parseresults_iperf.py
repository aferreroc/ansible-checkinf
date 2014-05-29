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
    print ("Usage %s -t [imas_a | imas_b] -i <inputpath> -o <outputfile>" %  sys.argv[0])
    sys.exit(2)
  for opt, arg in myopts:
    if opt == '-h':
       print ("Usage %s -t [imas_a | imas_b] -i <inputpath> -o <outputfile>" % sys.argv[0])
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

  # print("%s\t   %s\t   %s\t   %s\t%s" %
  #   ("HOST","Transfer","Bandwith","Jitter","Losts / Total"))

  fout = open(outputfile, 'w')
  fout.write("%s\t   %s\t   %s\t  %s\t%s\t%s\n" %
      ("Host","Transfer","Bandwith","Jitter","Losts / Total", "Result"))

  for dirpath, dirs, files in os.walk(inputpath):
    for filename in fnmatch.filter(files, typefiles+"*"):
      #fout.write(filename+"\n")
      with open(os.path.join(dirpath, filename)) as f:
        # one file open, handle it, next loop will present you with a new file
        #fout.write(f.read())
        for line in f:
          matchFile = re.match( r'imas_[a|b]_(.*)', filename, re.M|re.I)
          #[  3]  0.0-30.0 sec  2.78 GBytes    797 Mbits/sec  0.034 ms  241/58595 (0.41%)
          matchObj = re.match( r'.* sec (.*ytes) (.*its/sec) (.*ms) (.*) \((.*)%\)', line, re.M|re.I)
          if matchFile and matchObj:
            errores = float(matchObj.group(5))
            hayErrores = "OK"
            if errores > 0:
              hayErrores = "ERROR !!!"

            # print("%s %s %s\t%s %s  (%s%s)\t%s" %
            #   (matchFile.group(1),
            #   matchObj.group(1),
            #   matchObj.group(2),
            #   matchObj.group(3),
            #   matchObj.group(4),
            #   matchObj.group(5),
            #   "%",
            #   hayErrores))
            fout.write("%s %s %s\t%s %s  (%s%s)\t%s\n" %
                (matchFile.group(1),
                matchObj.group(1),
                matchObj.group(2),
                matchObj.group(3),
                matchObj.group(4),
                matchObj.group(5),
                "%",
                hayErrores))

  fout.close()

if __name__ == "__main__":
   main(sys.argv[1:])
