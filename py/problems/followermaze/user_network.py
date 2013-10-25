from threading import Lock

#Think of this class as ConcurrentHashmap in java
class UserNetwork(object):
    def __init__(self):
        self.network = {}
        self.locks = {}
        self.locks_lock = Lock()

    def _user_lock(self, user):
        if not user in self.locks:
            with self.locks_lock: 
                if not user in self.locks: # double check lock
                    self.locks[user] = Lock()
        return self.locks[user]

    #Extension point for concurreny test. Not to be inlined
    def _in_network(self, user):
        return user in self.network
        
    def follow(self, user, follower):
        with self._user_lock(user): 
            if not self._in_network(user):
                self.network[user] = set()
            self.network[user].add(follower)
                
    def unfollow(self, user, follower):
        with self._user_lock(user):
            if self._in_network(user) and follower in self.network[user]:
                self.network[user].remove(follower)

    def __getitem__(self, user):
        if not user in self.network:
            return set()
        return self.network[user]