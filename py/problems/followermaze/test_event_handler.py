from unittest.mock import Mock
from pytest import fixture
from event_handler import EventHandler
from user_network import UserNetwork

@fixture
def event_handler():
    user_network = UserNetwork()
    user_network.follow(b'1', b'2')
    user_network.follow(b'1', b'4')
    return EventHandler({b'1': Mock(), b'2': Mock(), b'3': Mock()}, user_network)
    
def should_follow(event_handler):
    event_handler.handle(b'payload|F|3|1')
    assert event_handler.network[b'1'] == {b'2', b'3', b'4'}
    event_handler.users[b'1'].send.assert_called_once_with(bytes('payload|F|3|1\n', 'UTF-8'))

def should_follow_and_not_notify_user(event_handler):
    event_handler.handle(b'payload|F|3|4')
    assert event_handler.network[b'4'] == {b'3'}

def should_unfollow(event_handler):
    event_handler.handle(b'payload|U|2|1')
    assert event_handler.network[b'1'] == {b'4'}
    assert 0 == event_handler.users[b'1'].send.call_count

def should_broadcast(event_handler):
    event_handler.handle(b'payload|B|blah|blah')
    for socket in event_handler.users.values():
        socket.send.assert_called_once_with(bytes('payload|B|blah|blah\n', 'UTF-8'))

def should_send_private_message(event_handler):
    event_handler.handle(b'payload|P|4|1')
    event_handler.users[b'1'].send.assert_called_once_with(bytes('payload|P|4|1\n', 'UTF-8'))


def should_update_status(event_handler):
    event_handler.handle(b'payload|F|3|1')
    event_handler.handle(b'payload|S|1')
    for user in event_handler.network[b'1']:
        if user in event_handler.users:
            event_handler.users[user].send.assert_called_once_with(bytes('payload|S|1\n', 'UTF-8'))
                                                                   
