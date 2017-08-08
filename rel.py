#!/usr/bin/env python
#https://github.com/maxwedge/relativity-clock/rel.py
import sys,os,math,time,getopt
from decimal import *
getcontext()
Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999999, Emax=999999999,
    capitals=1, flags=[], traps=[Overflow, DivisionByZero,
    InvalidOperation])
getcontext().prec = 99
Decimal('3.14159265358979323846264338327950288419716939937510')
# pi to 50 places

class colors :
# Because why not?
  RED = '\033[91m'
  GREEN = '\033[92m'
  END = '\033[0m'

def speeder():
# Catch speeders
  print colors.RED + "Officer Einstein says, \"Where's the fire, Bub?\""
  print "You cannot exceed the speed of light. Keep it under 100%.\n" + colors.END
  usage()

def usage():
  print "usage: " + sys.argv[0] + " -v <velocity> -s <seconds>"
  print sys.argv[0] + " -h for help"
  sys.exit()

def help():
    print "Relativistic Time Dilation Clock\n"
    print "Demonstrates relativistic time dilation of Earth-bound clocks as observed by"
    print "     someone traveling near the speed of light, C (Celeritas).\n"
    print "Enter a velocity as a percentage of C, e.g. 90 for 90% of the speed of light."
    print "     You cannot go faster than light; keep it under 100%."
    print "     Values less than .4 will be boring to watch; values above .999 or so"
    print "     will show much time dilation. It's not a linear curve.\n"
    print "Enter a number of seconds to run the clock. Note that traveling very near"
    print "     the speed of light for a long period will likely dilate the Earth clock"
    print "     (your computer) beyond its limit and eventually throw an error.\n"
    print "See: https://en.wikipedia.org/wiki/Twin_paradox\n"
    print "Example: " + sys.argv[0] + " -v 99.9999999999 -s 120\n"
    sys.exit()

def main():
  seconds = 0 
  velocity = 0
# Get options
  try:
    opts, args = getopt.getopt(sys.argv[1:], "hv:s:", ["velocity=", "seconds=", "help"])
  except getopt.GetoptError as err: # print help information and exit
      print str(err) # will print something like "option -a not recognized"
      usage()
# If an option is required (condradiction, I know), add boolean tests:
  reqd_v = False
  reqd_s = False
  reqd_missing = False
  for o, a in opts:
    if o in ("-v", "--velocity"):
      velocity  = Decimal(a)
      reqd_v = True
    elif o in ("-s", "--seconds"):
      seconds = int(a)
      reqd_s = True
    elif o in ("-h", "--help"):
      help()
    else:
      assert False, "unhandled option"
  if not reqd_v:
    print "-v is required"
    reqd_missing = True
  if not reqd_s:
    print "-s is required"
    reqd_missing = True
  if reqd_missing:
    usage()
# Start the plug & chug
  velocity = Decimal(velocity/100)
  if velocity >= 1:
    speeder()
  pc = (velocity*100)
  kps = Decimal(299792.458)
  speedometer = int(kps*velocity)
# Reduction of the Einstein-Lorentz Transformation
  transform = (1/(math.sqrt(1-(velocity**2))))
  startepoch = time.time();
  starttime = time.asctime(time.localtime(startepoch));
  count = 0
# Grab epoch time and loop through
  while (count <= seconds) :
    currentepoch = time.time()
    currenttime = time.asctime(time.localtime(currentepoch))
    deltaepoch = currentepoch - startepoch
    dilate = ((deltaepoch*transform)+startepoch)
    dilatedtime = time.asctime(time.localtime(dilate))
    os.system('clear') # I don't care for this workaround...
    print "You left Earth \t\t" + str(starttime)
    print colors.GREEN + "Your clock:\t\t" + str(currenttime) + colors.END
    print colors.RED + "Earth clock:\t\t" + str(dilatedtime) + colors.END
    print "You are traveling at " + str(speedometer) + " km/sec. (" + str(pc) + "% C)"
    count = count + 1
    time.sleep(1)

if __name__ == "__main__":
   main()

