from __future__ import print_function, division
import random

class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next or []
        
class SkipList(object):
    def __init__(self, values=None):
        self.head = None
        for val in (values or []):
            self.add(val)
        
    def find_with_hop_cnt(self, value):
        cnt = 0
        if not self.head:
            return None, cnt
        node = self.head
        i = max(len(self.head.next) - 1, 0)
        while node.value <= value and i > -1:
            if node.value == value:
                return node, cnt
            while i < len(node.next) and  node.next[i].value <= value:
                node = node.next[i]
                cnt += 1
            i -= 1
        return node if node.value == value else None, cnt
        

    def find(self, value):
        prevs = self._find(value)
        if not prevs:
            return
        node = prevs.pop()
        if node.value == value:
            return node
        
    def _find(self, value):
        if not self.head:
            return
        node = self.head
        i = max(len(self.head.next) - 1, 0)
        prev = []
        while node.value <= value and i > -1:
            while i < len(node.next) and  node.next[i].value <= value:
                node = node.next[i]
            prev.append(node)
            i -= 1
        return prev
        
    def delete(self, value):
        if not self.head:
            raise Exception("Empty list")
        node = self.find(value)
        if not node:
            raise Exception("Node not found")
        if node == self.head:
            if not self.head.next:
                self.head = None
                return node
            next = node.next[0]
            for nxt in node.next[len(next.next):]:
                if nxt != next:
                    next.next.append(nxt)
            node.next = None
            self.head = next
            return node
        n = len(self.head.next)
        i = n - 1
        prev = None
        prevs = []
        while i > -1:
            node_ = (prev or self.head)
            while node_ and node_ != node:
                assert isinstance(node_.next, list), (node_.value,
                                                     prev.value if prev else None, i)
                node_, prev= node_.next[i] if i < len(node_.next) else None, node_
            #print(value, node.value if node else None, prev.value if prev else None)
            if node_ and node_ == node:
                prevs.append(prev)
            else:
                prev = prevs[-1] if prevs else None
            i -= 1
        if not prevs:
            raise Exception("%s should have a prev node" %  node.value)
        while prevs:
            i = len(prevs) - 1
            prev = prevs.pop(0)
            if i < len(node.next):
                prev.next[i] = node.next[i]
            else:
                if i == len(prev.next) - 1:
                    prev.next.pop()
                else:
                    prev.next[i] = prev.next[i + 1]
        node.next = None
        return node

    def add(self, value):
        if not self.head:
            self.head = Node(value)
            return
        prev = self._find(value)
        i = 0
        new_node = Node(value)
        if not prev:
            new_node.next = [self.head] + self.head.next[1:]
            self.head.next = self.head.next[:1]
            node, self.head = self.head, new_node
            i = 1
            while random.randint(0, 1):
                if i < len(self.head.next):
                    node.next.append(self.head.next[i])
                    self.head.next[i] = node
                else:
                    self.head.next.append(node)
                i += 1
            return
        while True:
            prev_node = prev.pop() if prev else self.head
            assert prev_node.value <= value
            if i < len(prev_node.next):
                 new_node.next.append(prev_node.next[i])
                 prev_node.next[i] = new_node
            else:
                assert i == len(prev_node.next)
                prev_node.next.append(new_node)
            if not random.randint(0, 1):
                break
            i += 1

    @property
    def values(self):
        values = []
        node = self.head
        while node:
            values.append(node.value)
            node = node.next[0] if node.next else None
        return values
            
    
############################## TESTS ##############################

import sys
import math
import pytest
from numpy import random as nprand
def print_list(lst, max=None):
    if not lst.head:
        return
    i = 0
    while True:
        print('-' * 40)
        node = lst.head
        cnt = 0
        prev = None
        while node:
            print(node.value, end = ' ')
            sys.stdout.flush()
            assert isinstance(node.next, list), (node.value,
                                                 prev.value if prev else None, i)

            node, prev= node.next[i] if i < len(node.next) else None, node
            cnt += 1
            if cnt > 25:
                print("inf loop")
                return
        
        i += 1
        print()
        if not i < len(lst.head.next):
            break
        print('~' * 40)
def should_insert_bug():
    nums = [20, 1, 11, 18, 25, 16, 20, 15, 7, 9, 14, 7, 5, 11, 25, 2,
                     25, 16, 17, 23, 9, 1, 12, 4, 11]
    sorted_nums = sorted(nums)
    for i in range(5):
        list = SkipList(nums)
        assert sorted_nums == list.values

    
@pytest.mark.parametrize('_', range(5))
def should_insert(_):
    list = SkipList()
    N = 1000
    for i in range(N):
        num = random.randint(1, N)
#        print(num, end=' ')
#        sys.stdout.flush()
        list.add(num)
    values = list.values
    assert N == len(values)
    assert values == sorted(values)
#    print_list(list)
#    assert 0

def shuffle(list):
    l = list[:]
    random.shuffle(l)
    return l

@pytest.mark.parametrize('nums', [range(1024), reversed(range(2048)),
                                  nprand.random_integers(1, 25, size=25),
                                  nprand.random_integers(1, 10, size=10),
                                  nprand.random_integers(1, 15, size=15),
                                  nprand.random_integers(1, 100, size=128),
                                  nprand.random_integers(1, 2048, size=2048),
                                  nprand.random_integers(1, 1024, size=1024)
                              ])
def should_delete(nums):
    nums = list(nums)
    list_ = SkipList(nums)
    #print_list(list_, len(nums))
    cnt = len(nums)
    for num in nums:
        list_.delete(num)
        print("del %s" % num)
        #sys.stdout.flush()
        #print_list(list_, len(nums))
        cnt -= 1
        if cnt % 50 == 0:
            vals = list_.values
            assert cnt == len(vals)
            assert sorted(vals) == vals
    assert not list_.head

@pytest.mark.parametrize('N', [1024, 512, 2048, 128, 128, 1024, 1024])
def should_find_in_logn(N):
    logn = math.log(N, 2)
    nums = range(1, N + 1)
    deviations = []
    for modifier in [reversed, lambda l:l, shuffle]:
        list = SkipList(modifier(nums))
        assert nums == list.values
        for i in range(30):
            num = random.randint(1, N)
            node, cnt = list.find_with_hop_cnt(num)
            assert node, "%s not found" % num
            assert num == node.value, num
            deviations.append(logn - cnt)
    assert logn >= math.fabs(sum(deviations) / len(deviations))

    
if __name__ == '__main__':
    should_insert_bug()