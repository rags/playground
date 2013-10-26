def send(socket, data):
    try:
        socket.send(data + b'\n')
    except:
        'Silently ignore exceptions'
    
class EventHandler(object):
    def __init__(self, users, user_network):
        self.users = users
        self.network = user_network
        self.handlers = {
            b'F': self.follow,
            b'U': self.unfollow,
            b'B': self.broadcast,
            b'P': self.private_message,
            b'S': self.status_update
        }
        
    def follow(self, event):
        follower, user = event[2:4]
        self.network.follow(user, follower)
        return [user]

    def unfollow(self, event):
        follower, user = event[2:4]
        self.network.unfollow(user, follower)
        return []

    def broadcast(self, event):
        return self.users.keys()

    def private_message(self, event):
        return [event[3]]

    def status_update(self, event):
        return self.network[event[2]]

    def handle(self, data):
        print("Handling: ", data)
        parts = data.split(b'|')
        receivers = self.handlers[parts[1]](parts)
        for receiver in receivers:
            if receiver in self.users:
                send(self.users[receiver], data)
