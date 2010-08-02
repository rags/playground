from __future__ import with_statement
from itertools import *

MIN_COMP_SIZE = 3
class CompositeCounter:
    def __init__(self,words,min_comp_count):
        self.all_words = words
        self.min_comp_count = min_comp_count
 

    def count(self):
        composite_cnt = 0
        for word in ifilter(lambda wrd: len(wrd)>=self.min_comp_count*MIN_COMP_SIZE, self.all_words):
            if self.count_comp(word) >= self.min_comp_count:
                composite_cnt += 1
        return composite_cnt        
                

    def count_comp(self,word):
        sub_word_cnt = 0
        for sub_word in ifilter(lambda wrd: len(wrd)>=MIN_COMP_SIZE and len(wrd)<=len(word), self.all_words):
            if sub_word==word:
                sub_word_cnt = max(sub_word_cnt,1)
                continue            
            if self.contains_sub_word_in_right_place(word,sub_word): 
                continue
            parts = word.rsplit(sub_word,1)
            if len(parts)>1:
                sub_word_cnt = max(sub_word_cnt,self.count_comp_parts(parts))
            if sub_word_cnt >= self.min_comp_count:
                return sub_word_cnt
        return sub_word_cnt
                
    def contains_sub_word_in_right_place(self,word,sub_word):
        index = word.find(sub_word)
        return index==-1 or index>0 and index<MIN_COMP_SIZE or index>len(word)-1-MIN_COMP_SIZE

    def count_comp_parts(self,parts):
        cnt = 0
        for part in parts:
            if len(part)==0:
                continue
            part_cnt = self.count_comp(part)
            if part_cnt==0:
                return 0
            cnt += part_cnt            
        return part_cnt + len(parts) - 1

def count_composites(args):
    return CompositeCounter(read1(args[0]),int(args[1])).count()

def read1(file_name):
    with open(file_name) as file:                    
        return map(lambda line: line.rstrip(),file.readlines())

if __name__ == "__main__":
    print count_composites(raw_input().rsplit(' ',1))
