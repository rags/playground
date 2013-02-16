def match(_str, pattern):
    tokens = tokenize(pattern)
    return _match(_str, tokens)

def _match(_str, tokens):
    print _str, tokens
    if not(_str or tokens):
        return True
    if not tokens and _str:
        return False
    match, number = tokens[0]
    if number == '*':
        if not _str:
            return _match(_str, tokens[1:])
        if match == _str[0] or match == '.':
            return _match(_str[1:], tokens) or _match(_str, tokens[1:])
        return _match(_str, tokens[1:])
    else:
        if not _str:
            return False
        return (match == _str[0] or match == '.') and _match(_str[1:], tokens[1:])
    
def tokenize(pattern):
    tokens = []
    for i, c in enumerate(pattern):
        if c == '*':
            continue
        if i + 1 < len(pattern) and pattern[i + 1] == '*':
            tokens.append((c, '*'))
        else:
            tokens.append((c, 1))
    return tokens
############################ TEST ############################
            
def should_match():
    assert match('ab', 'ab')
    assert not match('aba', 'ab')
    assert match('aaa', 'a*b*')
    assert match('aaa', 'a*')
    assert match('aaa', 'a*a')
    assert match('aaa', 'a*aa')
    assert match('aaa', 'a*aaa')
    assert match('aaa', 'b*a*aaaa*.*')
    assert match('aaa', 'a*aa*aa*.*')
    assert match('aaab', 'a*aa*aa*.*')
    assert match('aaa', 'a*aa*a.*a')
    assert match('aaa', 'a*aa*a.*.')
    assert not match('aaab', 'a*aa*a.*a')
    assert match('aaab', '.*')
    assert match('aaab', '.*a*b*....*b')
    assert not match('aaab', '.*a*b*....*ab')
    