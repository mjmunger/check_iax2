#!/usr/bin/env python3
"""
Usage: check_iax2 [-vdh] <peer>

Where:
  peer        Name of the peer / trunk to check. Use "all" for all peers.
Options:
  -h         Help
  -d         Debug mode
  -v         Be verbose
"""
import subprocess
import sys
from docopt import docopt
from check_iax2.iax_status_parser import IaxParser

args = docopt(__doc__)
cmd = "asterisk -rx".split(' ')
cmd.append('iax2 show peers')

proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
outs, errs = proc.communicate()

Iax = IaxParser(args['<peer>'], outs)
Iax.set_debug_mode(args['-d'])
# print(Iax)
Iax.parse()
Iax.exit()