X, Y = '[',  ']'

SCORE = {X: 1, Y: -1}

def make_dyck_words(n):
    assert n > 0
    XY = X + Y
    if n == 1:
        return [XY]

    words = make_dyck_words(n - 1)
    return ([X + word +  Y for word in words] +
            [XY + word for word in words] + [(word + XY) for word in words])

def _count(cnt, c):
    return cnt + SCORE[c]
    
def is_valid(word):
    return 0 == reduce(_count, word, 0)

#delete a char and maintain balance
def delete(word, i):
    lst =  list(word)
    assert i < len(lst) and is_valid(lst)
    step = cnt = SCORE[lst[i]]
    j = i
    while(cnt != 0):
        j += step
        cnt += SCORE[lst[j]]
    lst.pop(max(i, j))
    lst.pop(min(i, j))
    return ''.join(lst)
    
def should_delete():
    assert '' == delete('[]', 0)== delete('[]', 1)
    assert delete('[][[]][]', 2) == '[][][]'
    assert delete('[][[]][]', 7) == '[][[]]'
    for i in range(8):
        assert delete('[[[[]]]]', i) == '[[[]]]'
    
def should_vaidate():
    assert is_valid('[]')
    assert is_valid('[][[]][]')
    assert not is_valid('[][[]][]]')
    
def should_generate_dyck_words():
    assert make_dyck_words(1) == ['[]']
    assert make_dyck_words(2) == ['[[]]', '[][]', '[][]']
    four_word_combs = set(make_dyck_words(4))
    assert all(map(is_valid, four_word_combs))
    assert four_word_combs == {'[[[[]]]]', '[[[][]]]',  '[[][[]]]',
                                       '[[[]][]]', '[[][][]]', '[][[[]]]',
                                       '[][[][]]', '[][[][]]', '[][][[]]',
                                       '[[]][][]', '[][][][]', '[[][]][]', 
                                       '[[[]]][]', '[][[]][]'}
    
    