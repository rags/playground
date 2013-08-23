#program that simulates "tail-n"
#todo: tail-f. logic make current eof (offset) as bof for next pass (i.e when the you detect file changes)
import os
import sys

def tail(fpath, n):
    fd = os.open(fpath, os.O_RDONLY)
    try:
        start_pos = end_pos = os.lseek(fd, 0, os.SEEK_END)#goto EOF
        new_line_cnt = 0
        os.lseek(fd, -1, os.SEEK_CUR)
        last_char = os.read(fd, 1)
        #move the file pointer backwards till you hit BOF or n newlines.
        while True: 
            if '\n' == os.read(fd, 1):
                new_line_cnt += 1
                if new_line_cnt == n:
                    start_pos += 1
                    break
            start_pos = os.lseek(fd, -2, os.SEEK_CUR)
            if start_pos == 0:
                break
        print os.read(fd,  end_pos - start_pos - (1 if last_char == '\n' else 0))
    finally:
        os.close(fd)

#usage: python tail.py <file> n        
if __name__ == '__main__':
    tail(sys.argv[1], int(sys.argv[2]))


############################## TESTS ##############################
import tempfile
if sys.version.startswith("3."):
    from io import StringIO as SOut
else:
    from StringIO import StringIO as SOut
import contextlib

@contextlib.contextmanager
def mock_stdout():
    oldout, olderr =  sys.stdout,  sys.stderr
    try:
        out = [SOut(),  SOut()]
        sys.stdout, sys.stderr =  out
        yield out
    finally:
        sys.stdout, sys.stderr =  oldout,  olderr
        out[0] =  out[0].getvalue()
        out[1] =  out[1].getvalue()

def assert_tail_out(file, n, expected):
    with mock_stdout() as out:
        tail(file, n)
    stdout = out[0]
    assert expected == stdout
    
def should_tail():
    foo, foo_path = tempfile.mkstemp("foo")
    bar, bar_path = tempfile.mkstemp("bar")

    os.write(foo, '0\n1\n2\n3\n4\n5\n6\n7\n8\n9')

    for i in range(1000):
        os.write(bar, 'Line %s\n' % i)
    os.close(foo)
    os.close(bar)
    assert_tail_out(foo_path, 3, '\n'.join(map(str, [7, 8, 9])) + '\n')
    assert_tail_out(foo_path, 5, '\n'.join(map(str, [5, 6, 7, 8, 9])) + '\n')
    assert_tail_out(foo_path, 20, '\n'.join(map(str, range(10))) + '\n')

    assert_tail_out(bar_path, 100, '\n'.join(map(lambda i: 'Line %s' %  i, range(900, 1000))) + '\n')
    assert_tail_out(bar_path, 20, '\n'.join(map(lambda i: 'Line %s' %  i, range(980, 1000))) + '\n')
    
    

    