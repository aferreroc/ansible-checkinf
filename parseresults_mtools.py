#!/usr/bin/env python
import sys
import os, fnmatch
import re

import sys, getopt

def tail(f, n, offset=None):
    """Reads a n lines from f with an offset of offset lines.  The return
    value is a tuple in the form ``(lines, has_more)`` where `has_more` is
    an indicator that is `True` if there are more lines in the file.
    """
    avg_line_length = 74
    to_read = n + (offset or 0)

    while 1:
        try:
            f.seek(-(avg_line_length * to_read), 2)
        except IOError:
            # woops.  apparently file is smaller than what we want
            # to step back, go to the beginning instead
            f.seek(0)
        pos = f.tell()
        lines = f.read().splitlines()
        if len(lines) >= to_read or pos == 0:
            return lines[-to_read:offset and -offset or None], \
                   len(lines) > to_read or pos > 0
        avg_line_length *= 1.3


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

  # print("  %s\t\t  %s\t\t\t  %s\t\t%s" %
  #   ("Host", "Messages","Losts", "Result"))

  fout = open(outputfile, 'w')
  fout.write("  %s\t\t  %s\t\t\t  %s\t\t%s" %
        ("Host", "Messages","Losts", "Result"))

  for dirpath, dirs, files in os.walk(inputpath):
    for filename in fnmatch.filter(files, typefiles+"*"):
      #fout.write(filename+"\n")
      with open(os.path.join(dirpath, filename)) as f:
        # one file open, handle it, next loop will present you with a new file
        #fout.write(f.read())
        match1 = False
        for line in f:
          matchFile = re.match( r'imas_[a|b]_(.*)', filename, re.M|re.I)
          matchObj = re.match( r'(.*) msgs sent, (.*) received', line, re.M|re.I)
          matchObj2 = re.match( r'(.*)% loss', line, re.M|re.I)
          if matchFile and matchObj:
              linea1 = matchObj.group()
              match1 = True

          if match1 and matchObj2:
            linea2 = matchObj2.group()
            errores = float(matchObj2.group(1))
            hayErrores = "OK"
            if errores > 0:
              hayErrores = "ERROR !!!"

            # print("%s\t%s\t%s\t%s" %
            #   (matchFile.group(1),
            #   linea1,
            #   linea2,
            #   hayErrores))
            fout.write("%s\t%s\t%s\t%s" %
                  (matchFile.group(1),
                  linea1,
                  linea2,
                  hayErrores))

  fout.close()

if __name__ == "__main__":
   main(sys.argv[1:])
