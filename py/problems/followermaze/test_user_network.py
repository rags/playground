from user_network import UserNetwork
from threading import Thread, Event, Semaphore

def should_follow_unfollow():
    network =  UserNetwork()
    network.follow(1, 2)
    network.follow(1, 3)
    network.follow(2, 3)
    assert network[1] == {2, 3}
    assert network[3] == set()
    assert network[2] == {3}
    network.unfollow(1, 3)
    network.unfollow(1, 3) # no error
    assert network[1] == {2}

#comment out "with self._user_lock(user)" line to fail the test
def should_handle_concurrent_updates():
    network = TestNetwork()
    network.network = {1: {2, 3}} #direcly modify private member
    network.do_concurrent(
        lambda: network.follow(2, 3), 
        lambda: network.follow(2, 1), 
        lambda: network.unfollow(1, 3), 
        lambda: network.unfollow(1, 2)
    )
    assert network[1] == set()
    assert network[2] == {1, 3}

class TestNetwork(UserNetwork):

    #block the current thread till every other thread has
    # reached the contention point
    def block_till_all_threads_reach_contention_point(self):
        print("debug: release")
        self.semaphore.release()
        print("debug: and block")
        self.all_threads_ready.wait(1)

    def _acquire_all(self):
        for i in range(self.no_of_threads):
            self.semaphore.acquire()

    #override to force contention
    def _in_network(self, user):
        res = super(TestNetwork, self)._in_network(user)
        self.block_till_all_threads_reach_contention_point()
        return res

    def do_concurrent(self, *operations):
        self.no_of_threads = len(operations)
        self.semaphore =  Semaphore(self.no_of_threads)
        self.all_threads_ready =  Event()
        threads = []
        self._acquire_all()
        for i in range(self.no_of_threads):
            t = Thread(target = operations[i])
            t.start()
            threads.append(t)
        #block main thread till for all threads to reach the contention point
        self._acquire_all()
        #release all the threads. They should now execute cricital section simultanously
        self.all_threads_ready.set()
        for t in threads: t.join()
            

