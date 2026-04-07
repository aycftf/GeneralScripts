##Helper script

import argparse
import os
import sys
#Change cur directory of abs path of script
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.system("python3 rawTCPdump.py")
os.system("python3 rawDNSdump.py")


