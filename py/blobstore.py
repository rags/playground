import uuid
import os
from threading import Thread, Lock, ThreadError
import hashlib

def hash(content):
    m = hashlib.md5()
    m.update(content)
#    print content, m.digest()
    return m.digest()

def _lock(map_, id_):
    if not id_ in map_:
        map_[id_] = Lock()
    map_[id_].acquire()

def _unlock(map_, id_, pop = False):
    if not id_ in map_:
        return
    try:
        if pop:
            map_.pop(id_).release()
        else:
            map_[id_].release()
    except ThreadError:
        pass
    
    
#A blob store
class BlobStore(object):
    def __init__(self, data_dir = './data'):
        self.cache = {}
        self.data_dir = data_dir
        self.locks = {}
        self.md5_locks = {}

    def lock(self, id_):
        _lock(self.locks, id_)

    def unlock(self, id_):
        _unlock(self.locks, id_)

    def lock_md5(self, id_):
        _lock(self.md5_locks, id_)

    def unlock_md5(self, id_):
        _unlock(self.md5_locks, id_)


    def evict_cache(self, id_):
        if id_ in self.cache:
            self.cache.pop(id_)
            
    '''
    use id as filename
    Assume *nix for now and hard-link duplicate blob.
    Hard linking should work even if original file is deleted

    correct solution - maintain a listing of id to file and delete file
    if no ids point to it

    TODO:
    # encode (huffman encoding?) blob to reduce disk space
    # evict cache after writing the file
    # create directory if it doesnt exist
    '''
    def store_to_disk(self, id_, blob):
        md5_digest = hash(blob)
        self.lock_md5(md5_digest)
        try:
            for dirname, dirnames, filenames in os.walk(self.data_dir):
                for filename in filenames:
                    file_path = os.path.join(dirname,  filename)
                    with open(file_path) as file:
                        if hash(file.read()) == md5_digest:
                            try:
                                self.lock(filename)
                                if os.path.exists(file_path):
                                    #todo: lock to ensure file is not delted by another thread
                                    os.link(os.path.abspath(file_path),
                                            os.path.join(dirname, id_))
                                    return self.evict_cache(id_)
                            finally: 
                                self.unlock(filename)
            
            with open(self.path(id_), 'w') as file:
                file.write(blob)
        finally: 
            self.unlock_md5(md5_digest)
        self.evict_cache(id_)
        
    def put(self, data):
        id_ = uuid.uuid4().hex
        self.cache[id_] = data
        self.store_async(id_, data) # store asynchronously
        return id_

    def store_async(self, id_, data):
        thread = Thread(target=self.__class__.store_to_disk, args = [self, id_, data])
        thread.start()
        return thread

    def path(self, id_):
        return os.path.join(self.data_dir, id_)
        
    def get(self, id_):
        if id_ in self.cache:
            return self.cache[id_]
        path = self.path(id_)
        if not os.path.exists(path):
            return None
        try:
            self.lock(id_)
            if not os.path.exists(path):
                return None
            with open(path) as file:
                return file.read()
        finally: 
            self.unlock(id_)

    #delete file, clear cache
    def delete(self, id_):
        try:
            self.lock(id_)
            path = self.path(id_)
            if os.path.exists(path):
                os.remove(path)
            self.evict_cache(id_)
        finally: 
            self.unlock(id_)

############################## TESTS ##############################
import time
from threading import Event, Semaphore

def should_delete():
    store = BlobStore()
    id0 = store.put('foo bar')
    id1 = store.put('foo bar')
    store.delete(id0)
    assert not store.get(id0)
    assert 'foo bar' == store.get(id1)
    while not os.path.exists(store.path(id1)):
        time.sleep(.1)
    store.cache.clear()
    assert 'foo bar' == store.get(id1)

    
def should_put():
    store = BlobStore()
    id0 = store.put('some text')
    id1 = store.put('some text')
    id2 = store.put('\n��s_��/�Y��<�%j5�)�.�[T���F��,�������,��x�[��]]')
    assert store.get(id0) == 'some text'
    assert store.get(id1) == 'some text'
    assert store.get(id2) == '\n��s_��/�Y��<�%j5�)�.�[T���F��,�������,��x�[��]]'

    
def should_read_from_files():
    store = BlobStore()
    id0 = store.put('some text')
    id1 = store.put('\n��s_��/�Y��<�%j5�)�.�[T���F��,�������,��x�[��]]]]')
    while not (os.path.exists(store.path(id0)) and os.path.exists(store.path(id1))):
        time.sleep(.1)
    store.cache.clear()
    assert store.get(id0) == 'some text'
    assert store.get(id1) == '\n��s_��/�Y��<�%j5�)�.�[T���F��,�������,��x�[��]]]]'
        

'''
Simultaneously put same content into blob store and ensure that
the files created in the process point to same inode.
i.e ensure only one physical file for duplicate content 
'''
def should_handle_simultaneous_put():
    random_text = 'foo bar %s' % uuid.uuid4().hex
    store = TestBlobStore()
    ids = store.put_concurrently(random_text)
    inodes = set()
    for id_ in ids:
        inodes.add(os.stat(store.path(id_)).st_ino)
    assert len(inodes) == 1


'''
This class overrides blob store to manipulate it in ways to make it convienient to test
for concurrency

put_concurrently artifically ensures that <no_of_threads> enter the critical section at
the same time.
Explantion:
To acheive this the main thread uses an Event and one semaphore per thread.
All threads wait for the event from main thread, while main thead waits for
all thread to reach the critical point and release one semaphore
'''
class TestBlobStore(BlobStore):
    no_of_threads = 3

    #block the current thread till every other thread has reached the contention point
    def block_till_all_threads_to_reach_this_point(self):
        print "debug: blocking"
        self.semaphore.release()
        self.all_threads_ready.wait(10.0)

    #block main thread till for all threads to reach the contention point
    def _block_till_all_threads_release(self):
        for i in range(TestBlobStore.no_of_threads):
            self.semaphore.acquire()

    def put_concurrently(self,  blob):
        self.semaphore =  Semaphore(TestBlobStore.no_of_threads)
        self.all_threads_ready =  Event()
        self.ids = []
        self.threads = []
        for i in range(TestBlobStore.no_of_threads):
            self.semaphore.acquire()
            self.ids.append(self.put(blob))
        self._block_till_all_threads_release()
        #release all the threads. They should now execute cricital section simultanously
        self.all_threads_ready.set()
        assert len(self.threads) == TestBlobStore.no_of_threads
        for thread in self.threads:
            thread.join()
        return self.ids

    
    def store_async(self, id_, blob):
        self.threads.append(super(TestBlobStore, self).store_async(id_, blob))

    def store_to_disk(self, id_, blob):
        #override store to disk to ensure all threads hit this point
        #and block till every other thread has reached this point
        self.block_till_all_threads_to_reach_this_point()
        super(TestBlobStore, self).store_to_disk(id_, blob)
        
    