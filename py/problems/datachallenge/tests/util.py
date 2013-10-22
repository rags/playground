import sys
import contextlib
#comment this like uncomment next for python 2.7.x
from io import StringIO as SOut #3.x
#from StringIO import StringIO as SOut #2.7.x 
from collections import Iterable
import re

@contextlib.contextmanager
def mock_console_io(input_str):
    oldout, oldin =  sys.stdout,  sys.stdin
    try:
        (sys.stdout, sys.stdin) =  out = [SOut(),  SOut(input_str)]
        yield out
    finally:
        sys.stdout, sys.stdin =  oldout,  oldin
        out[0] =  out[0].getvalue()
        out[1] =  out[1].getvalue()

def replace(txt, frm, to):
    def rep(s):
        return re.sub(frm, to, s)
    if isinstance(txt, str):
        return rep(txt)
    elif isinstance(txt, Iterable):
        return list(map(rep, txt))
    
def tabify(txt):
    return replace(txt, ' +',  '\t')


def untabify(txt):
    return replace(txt, '\t',  ' ')


