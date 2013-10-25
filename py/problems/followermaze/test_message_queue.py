from message_queue import MessageQueue
from threading import Thread, Semaphore

def should_handle_chunks_of_data_stream_sliced_randomly():
    stream = [bytes('7|U|46|17\n', 'UTF-8'), 
              b'6|U|46|68\n3|P|46|68\n4|F', 
              b'|4|68\n5|P|',
              b'5|68\n1',
              b'|F|46|49\n2|U|46|68\n']
    queue = MessageQueue()
    for chunk in stream:
        queue.push_data_stream(chunk)
    prev_seq = 0
    for expected in [b'1|F|46|49', b'2|U|46|68', b'3|P|46|68', 
                     b'4|F|4|68', b'5|P|5|68', b'6|U|46|68', 
                     b'7|U|46|17']:
        seq, data = queue.pop()
        assert expected == data
        assert seq >= prev_seq
    assert not queue.queue

def consume(queue, consumed, consume=1):
    for i in range(consume):
        consumed.append(queue.pop()[1])
    

def should_block_for_next_item():
    N = 5
    queue = MessageQueue()
    queue._push(N, 'data5')
    consumed = []
    consumer =  Thread(target=consume, args=[queue, consumed])
    consumer.start()
    queue._push(1, "data1")
    consumer.join()
    assert ['data1'] == consumed
    queue._push(4, 'data4')
    consumer =  Thread(target=consume, args=[queue, consumed])
    consumer.start()
    consumer.join(.3) #wait
    assert consumer.is_alive() #Thread is blocked
    queue._push(2, 'data2')
    consumer.join()
    assert ['data1', 'data2'] == consumed
    queue._push(3, 'data3')
    consumer =  Thread(target=consume, args=[queue, consumed, 3])
    consumer.start()
    consumer.join()
    assert consumed == ['data1', 'data2', 'data3', 'data4', 'data5']

    
        
if __name__ == '__main__':
    should_block_for_next_item()