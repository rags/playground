import time
from datetime import datetime
MERSENNE = 2147483647 #2 ** 31 - 1
#MERSENNE61 = 2 ** 61 - 1


def random_generator():
    a = time.mktime(datetime.now().timetuple()) % MERSENNE
    b = (time.mktime(datetime.now().timetuple()) + a) % MERSENNE
    seed = [int(a), int(b)]

    def _rand():
        a, b = seed
        seed[0] = a = 23 * (a &  65535) + (a >>  16)
        seed[1] = b = 31 * (b &  65535) + (b >>  16)
        return a << 16 + b
    return _rand

gen = random_generator()

def rand(start=0, end=65535):
    x = gen()
    return (x % (end - start)) + start

class Hashtable(object):
    def __init__(self, capacity=16):
        self.a = rand(1)
        self.b = rand(1)
        self.capacity = capacity
        self.keys = []
        self.values = [None] * capacity

    @property
    def size(self):
        return len(self.keys)

    def shrink(self):
        self.resize(self.capacity // 2)
        
    def extend(self):
        self.resize(self.capacity * 2)
        
    def resize(self, capacity):
        keys = []
        values = [None] * capacity
        a, b = rand(), rand()
        for key in self.keys:
            value = self[key]
            self._add(a, b, keys, values, key, value, capacity)
        self.a, self.b = a, b
        self.keys, self.values = keys, values
        self.capacity = capacity

    def remove(self, key):
        if self.size < self.capacity // 2:
            self.shrink()
        i = self.idx(key)
        val_list = self.values[i]
        if not val_list:
            return None
        for k, v in val_list:
            if k == key:
                val_list.remove((k, v))
                self.keys.remove(key)
                return v
        return None
            
    def __getitem__(self, key):
        return self.get(key)
        
    def get(self, key):
        i = self.idx(key)
        if not self.values[i]:
            return None
        for k, v in self.values[i]:
            if key == k:
                return v
        return None
        
    def idx(self, key):
        return self._idx(key, self.a, self.b, self.capacity)
        
    def _idx(self, key, a, b, capacity):
        return (a *  hash(key) + b) % MERSENNE % capacity
        
    def _add(self, a, b, keys, values, key, value, capacity):
        i = self._idx(key, a, b, capacity)
        keys.append(key)
        if not values[i]:
            values[i] = []
        values[i].append((key, value))

    def add(self, key, value):
        if self.capacity <= self.size:
            self.extend()
        self._add(self.a, self.b, self.keys, self.values, key, value, self.capacity)

        



############################## TESTS ##############################

def should_generate_random_numbers():
    for i in range(1, 1000):
        assert i <= rand(i, i + 100) < i + 100
    rnd = random_generator()
    for i in range(1000):
        x, y = rnd(), rnd()
        assert x != y

        
        
def should_generate_random_numbers_uniformly():
    cnts = zip(range(1, 10), [0] * 9)
    for i in range(3):
        x = dict(cnts)
        for i in range(1000):
            x[rand(1, 10)] += 1
        print x
        for i in range(1, 10):
            assert x[i] > 50 and x[i] < 200
    

def should_insert_into_hash_table():
    h = Hashtable(3)
    h.add("hello", "world")
    h.add(5, "five")
    h.add('six', 666)
    assert 3 == h.size == h.capacity
    assert 'world' == h['hello']
    assert 'five' == h[5]
    assert 666 == h['six']
    h.add(666, 'The number of the beast')
    assert h.size == 4
    assert h.capacity == 6
    assert 'The number of the beast' == h[666]
    assert not h['invalid key']

def should_delete_from_hashtable():
    h = Hashtable()
    for i in range(20):
        h.add('key_%s' % i, 'val_%s' % i)
    assert h.size == 20
    assert h.capacity == 32
    for i in [1, 2, 3, 4, 5, 12, 13, 14, 15, 16]:
        assert 'val_%s' % i == h.remove('key_%s' % i)
    assert h.capacity == 16
    assert h.size == 10
    assert not h.remove('invalid key')
    assert 'val_10' == h['key_10']

def should_have_high_utilization():
    for i in range(3):
        h = Hashtable()
        for i in range(1000):
            h.add('key_%s' % rand(), 'val_%s' % i)
        assert h.size == 1000
        assert h.capacity == 1024
        util_cnt = 0
        for v in h.values:
            if v:
                util_cnt += 1
        assert util_cnt > 600 #60% utilization

