# Huffman encoding is a compression algorithm that ensures that the no of bits used
# for char is indirectly proportional to the total times the char appears in a piece
# of text. http://en.wikipedia.org/wiki/Huffman_coding

from contextlib import nested
import sys

class Node(object):
    def __init__(self, weight, value=None, left=None, right=None):
        self.weight = weight
        self.value = value
        self.left = left
        self.right = right
    def __cmp__(self, other):
        return cmp(self.weight, other.weight)
        
    def __str__(self):
        ret_val = '(%s,%s)' %  (self.value, self.weight) if self.value else str(self.weight)
        if not (self.left or self.right):
            return ret_val
        return '[%s%s%s]' % (ret_val, (", left=" + str(self.left)) if self.left else '',
                             (", right=" + str(self.right)) if self.right else '')
        
        
def queue(vals):
    for i in range(len(vals) // 2 - 1, -1, -1):
        siftdown(vals, i)
    return vals
def pop(q):
    if not q:
        return None
        
    q[0], q[-1] = q[-1], q[0]
    ret = q.pop()
    if q:
        siftdown(q, 0)
    return ret

def push(q, val):
    q.append(val)
    siftup(q, len(q) - 1)

def siftup(q, i):
    parent = (i - 1)// 2
    while i and q[parent] > q[i]:
        q[parent], q[i] = q[i], q[parent]
        i, parent = parent, (parent - 1) // 2
        
def siftdown(vals, i):
    min = i
    left, right = 2 * i + 1, 2 * i + 2
    n = len(vals)
    if left < n and vals[left] < vals[min]:
        min = left
    if right < n and vals[right] < vals[min]:
        min = right
    if i != min:
        vals[i], vals[min] = vals[min], vals[i]
        if min < len(vals) // 2:
            siftdown(vals, min)
    
    
    
def char_counts(text):
    counts = {}
    for c in text:
        counts[c] = counts.get(c, 0) + 1
    return counts

def find(node, c):
    if node.value == c:
        return True, ''
    if node.left:
        found,encodings = find(node.left, c)
        if found:
            return found, '0' + encodings
    if node.right:
        found, encodings = find(node.right, c)
        if found:
            return found, '1' + encodings
    return False, ''
    
        

def huffman_decode(in_file_path,  out_file_path, encodings):
    with nested(open(in_file_path, 'r'), open(out_file_path, 'w')) as (file, out):
        out.write(_huffman_decode(file.read(), encodings))

def bit_stream(bytes):
    last_bits = bytes[0]
    for byte in bytes[1:-1]:
        for bit in bin(byte)[2:].zfill(8):
            yield bit
    last_byte = bin(bytes[-1])[2:].zfill(8)
    for bit in (last_byte[-last_bits:] if last_bits else last_byte):
        yield bit
    
def _huffman_decode(text, encodings):
    code_to_char = dict(zip(encodings.values(), encodings.keys()))
    key = ''
    ret_val = ''
    bytes =  bytearray(text)
    for bit in bit_stream(bytes):
        key += bit
        if key in code_to_char:
            ret_val += code_to_char[key]
            key = ''
    return ret_val
        
def huffman_encode(in_file_path,  out_file_path):
    with nested(open(in_file_path, 'r'), open(out_file_path, 'w')) as (file, out): 
        text = file.read()
        encoded_text, encodings = _huffman_encode(text, char_counts(text))
        out.write(encoded_text)
    return encodings
    
def _huffman_encode(text, weights):
    sorted_weights = sorted(zip(weights.values(), weights.keys()), reverse = True)
    nodes_q = queue(map(lambda (weight, c): Node(weight, c), sorted_weights))
    while len(nodes_q) > 1:
        smaller = pop(nodes_q)
        small = pop(nodes_q)
        push(nodes_q, Node(small.weight + smaller.weight, left = smaller, right = small))

    assert len(nodes_q) == 1
    encodings = {}
    for c in weights:
        found, encodings[c] = find(nodes_q[0], c)
        #assert found
    byte_arr = bytearray()
    bit_buffer = ''
    for c in text:
        bit_buffer += encodings[c]
        while len(bit_buffer) >= 8:
            byte_arr.append(int(bit_buffer[:8], 2))
            bit_buffer = bit_buffer[8:]
    assert len(bit_buffer) < 8
    byte_arr.insert(0, len(bit_buffer))
    if bit_buffer:
        byte_arr.append(int(bit_buffer, 2))
    return str(byte_arr), encodings

    
if __name__ == '__main__':
    huffman_encode(sys.argv[1], sys.argv[2])
        
############################## TESTS ##############################

import pytest
import tempfile

def should_return_char_weights():
    assert ({'H': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1, ' ': 1} ==
            char_counts('Hello world'))
    assert char_counts('''First line: foo bar
    Second line is blah blah
    ''') == {'a': 3, ' ': 15, 'c': 1, 'b': 3, 'e': 3, 'd': 1, 'F': 1, 'i': 4,
             'h': 2, 'f': 1, 'l': 4, 'o': 3, 'n': 3, 's': 2, 'r': 2, 't': 1,
             ':': 1, '\n': 2, 'S': 1}
    
@pytest.mark.parametrize('text', ['Hello world', 'aa bbbb cccc ddddd ee',
                              '''First line: foo bar
    Second line is blah blah
    '''])
def should_encode(text):
    counts = char_counts(text)
    encoded, encodings = _huffman_encode(text, counts)
    sorted_counts = sorted(zip(counts.values(), counts.keys()))
    for i in range(1, len(counts)):
        if sorted_counts[i - 1][0] < sorted_counts[i][0]:
            assert len(encodings[sorted_counts[i - 1][1]]) >= len(encodings[sorted_counts[i][1]])
    bits = text
    for c in text:
        bits = bits.replace(c, encodings[c])
    expected = [chr(len(bits) % 8)]
    while bits:
        expected.append(chr(int(bits[:8], 2)))
        bits = bits[8:]
    assert ''.join(expected) == encoded

@pytest.mark.parametrize('text', ['ab', '1234','Hello world',
                                  'aa bbbb cccc ddddd ee',
                                  '''First line: foo bar
                                  Second line is blah blah
                                  '''])
def should_encode_decode_text(text):
    encoded, encodings = _huffman_encode(text, char_counts(text))
    print encoded, encodings
    assert text == _huffman_decode(encoded, encodings)


def should_encode_decode_file():
    handle, file_path_encoded = tempfile.mkstemp()
    handle, file_path_decoded = tempfile.mkstemp()
    encodings = huffman_encode('article.txt', file_path_encoded)
    huffman_decode(file_path_encoded, file_path_decoded, encodings)
    with nested(open('article.txt'), open(file_path_decoded)) as (original, decoded):
        assert original.read() == decoded.read()
    
    

