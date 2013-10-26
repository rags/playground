import heapq
from threading import Condition

class MessageQueue(object):

    def __init__(self):
        self.queue = []
        self.prev_truncated = b'' # holds truncated tail from previous chunk of data
        self.next_item = 1
        self.new_item_available = Condition()

    '''
    This function handles the fact that messages are just byte streams. So,
    message1\n
    message2\n
    message3\n
    The above 3 messages can come in as 3 chunks that look like this
    message1\nmess
    age2\nmess
    age3\n
    '''
    def push_data_stream(self, stream):
        *events, self.prev_truncated = (self.prev_truncated + stream).split(b'\n')
        for event in events:
            self._push(int(event[:event.index(b'|')]), event)

    def _push(self, id, event):
        with self.new_item_available: 
            heapq.heappush(self.queue, (id, event))
            if self.next_item == id:
                self.new_item_available.notify()
    
    #The call blocks till next item is available
    def pop(self):
        while True:
            with self.new_item_available:
                if self.queue and self.queue[0][0] == self.next_item:
                    self.next_item += 1
                    return heapq.heappop(self.queue)
                else:
                    self.new_item_available.wait()

        