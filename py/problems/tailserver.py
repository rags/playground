import os
import BaseHTTPServer
import SocketServer
import time

'''
Usage:

http://server:port/filepath

Example:

**Server**
python tailserver.py # start the server

**Client**
curl http://localhost:8000/tmp/foo # Equivalent to - "tail -f /tmp/foo"

'''

class Handler(BaseHTTPServer.BaseHTTPRequestHandler):
    def write_chunk(self, content,  ignore_empty = True):
        if not content and ignore_empty:
            return
        self.wfile.write(hex(len(content))[2:] + "\r\n")
        self.wfile.write(content + "\r\n")
        self.wfile.flush()
        
        
    def do_GET(self):
        try:
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.send_header("Transfer-Encoding", "chunked")
            self.end_headers()
            content, last_pos = tailf(self.path)
            self.write_chunk(content)
            stat = os.lstat(self.path)
            while(True): 
                time.sleep(5)
                cur_stat = os.lstat(self.path)
                if cur_stat == stat:
                    continue
                stat = cur_stat
                content, last_pos = tailf(self.path, last_pos)
                self.write_chunk(content)
        except:
            return

'''
usage: 
content, lst_pos = tailf(file)
to get newer changes...
content, lst_post = tailf(file,lst_pos)
'''
#tail -f
def tailf(fpath, startpos=None):
    if startpos is None:
        return tail(fpath, 10)
    fd = os.open(fpath, os.O_RDONLY)
    try:
        end_pos = os.lseek(fd, 0, os.SEEK_END)#goto EOF
        os.lseek(fd, startpos, os.SEEK_SET)
        if end_pos > startpos:
            return os.read(fd,  end_pos - startpos), end_pos
        else:
            return "", startpos
    finally:
        os.close(fd)

#tail -number
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
        return os.read(fd,  end_pos - start_pos - (1 if last_char == '\n' else 0)), end_pos
    finally:
        os.close(fd)



'''
NonChunked handler for browser based ajax apps...
The resposibility of maintaining the cursor is on the client
Usage:
  server:port/path/to/file to get <pos>&<last_10_lines>
  server:port/path/to/file?pos=last_seen to get <pos>&<delta>
'''
class NonChunkHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        parts = self.path.split("?")
        file_path = parts[0]
        pos = None
        if len(parts) > 1:
            _, pos_str = parts[1].split("=")
            pos = int(pos_str)
        content, last_pos = tailf(file_path, pos)
        out = str(last_pos) + "&" + content
        self.send_header("Content-Length", len(out))
        self.end_headers()
        self.wfile.write(out)


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass
    
def main(handler=Handler):
    PORT = 8000
    httpd = ThreadedTCPServer(("", PORT), handler)
    print "serving at port %s\nCTRL+C to stop" % PORT
    httpd.serve_forever()

if __name__ == '__main__':
    main()
    #main(NonChunkHandler)
