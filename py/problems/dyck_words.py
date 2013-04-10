def make_dyck_words(n, X='[', Y = ']'):
    XY = X + Y
    if n == 1:
        return [XY]

    words = make_dyck_words(n - 1)
    return ([X + word +  Y for word in words] +
            [XY + word for word in words] + [(word + XY) for word in words])


def should_generate_dyck_words():
    assert make_dyck_words(1) == ['[]']
    assert make_dyck_words(2) == ['[[]]', '[][]', '[][]']
    assert set(make_dyck_words(4)) == {'[[[[]]]]', '[[[][]]]',  '[[][[]]]',
                                       '[[[]][]]', '[[][][]]', '[][[[]]]',
                                       '[][[][]]', '[][[][]]', '[][][[]]',
                                       '[[]][][]', '[][][][]', '[[][]][]', 
                                       '[[[]]][]', '[][[]][]'}
    
    