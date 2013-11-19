#The number of ways a boolean exp can be bracketed to yield a overall True value

def _counts(lhs, rhs, dp_table):
    (i, j), (k, l) = lhs, rhs
    true_lhs, true_rhs, false_lhs, false_rhs = (
        dp_table[i][j], dp_table[k][l], dp_table[j][i], dp_table[l][k]
    )
    if i == j:
        exp = ['T' if true_lhs else 'F']
        true_lhs, false_lhs = (int(true_lhs), exp), (int(not true_lhs), exp)
    if k == l:
        exp = ['T' if true_rhs else 'F']
        true_rhs, false_rhs = (int(true_rhs), exp), (int(not true_rhs), exp)

    return true_lhs, true_rhs, false_lhs, false_rhs
    
#false_cnt = T*F + F*T + F*F
def and_(lhs, rhs, dp_table):
    ((true_cnt_lhs, true_exp_lhs),
     (true_cnt_rhs, true_exp_rhs),
     (false_cnt_lhs, false_exp_lhs),
     (false_cnt_rhs, false_exp_rhs)) = _counts(lhs, rhs, dp_table)

    tcnt = true_cnt_lhs * true_cnt_rhs
    fcnt = (false_cnt_lhs * false_cnt_rhs +
            false_cnt_lhs * true_cnt_rhs +
            true_cnt_lhs * false_cnt_rhs)
    true_exps = ['(%s&%s)' % (exp1, exp2)
                 for exp1 in true_exp_lhs
                 for exp2 in true_exp_rhs] if tcnt else []
    false_exps = (['(%s&%s)' % (exp1, exp2)
                   for exp1 in true_exp_lhs
                   for exp2 in false_exp_rhs] if true_cnt_lhs * false_cnt_rhs else []+
                  ['(%s&%s)' % (exp1, exp2)
                   for exp1 in false_exp_lhs
                   for exp2 in true_exp_rhs] if false_cnt_lhs * true_cnt_rhs else []+
                  ['(%s&%s)' % (exp1, exp2)
                   for exp1 in false_exp_lhs
                   for exp2 in false_exp_rhs] if false_cnt_lhs * false_cnt_rhs else []) 
    
    return ((tcnt, true_exps),
            (fcnt, false_exps))
    
def or_(lhs, rhs, dp_table):
    ((true_cnt_lhs, true_exp_lhs),
     (true_cnt_rhs, true_exp_rhs),
     (false_cnt_lhs, false_exp_lhs),
     (false_cnt_rhs, false_exp_rhs)) = _counts(lhs, rhs, dp_table)

    tcnt = (true_cnt_lhs * true_cnt_rhs +
            false_cnt_lhs * true_cnt_rhs +
            true_cnt_lhs * false_cnt_rhs)
    fcnt = false_cnt_lhs * false_cnt_rhs
    true_exps = (['(%s|%s)' % (exp1, exp2)
                   for exp1 in true_exp_lhs
                   for exp2 in false_exp_rhs] if true_cnt_lhs * false_cnt_rhs else []+
                  ['(%s|%s)' % (exp1, exp2)
                   for exp1 in false_exp_lhs
                   for exp2 in true_exp_rhs] if false_cnt_lhs * true_cnt_rhs else []+
                  ['(%s|%s)' % (exp1, exp2)
                   for exp1 in true_exp_lhs
                   for exp2 in true_exp_rhs] if true_cnt_lhs * true_cnt_rhs else [])
    false_exps = ['(%s|%s)' % (exp1, exp2)
                  for exp1 in false_exp_lhs
                  for exp2 in false_exp_rhs] if fcnt else []
    
    return ((tcnt, true_exps), 
            (fcnt, false_exps))

def xor_(lhs, rhs, dp_table):
    ((true_cnt_lhs, true_exp_lhs),
     (true_cnt_rhs, true_exp_rhs),
     (false_cnt_lhs, false_exp_lhs),
     (false_cnt_rhs, false_exp_rhs)) = _counts(lhs, rhs, dp_table)
    
    true_exps = (['(%s^%s)' % (exp1, exp2)
                   for exp1 in true_exp_lhs
                   for exp2 in false_exp_rhs] if true_cnt_lhs * false_cnt_rhs  else []+
                  ['(%s^%s)' % (exp1, exp2)
                   for exp1 in false_exp_lhs
                   for exp2 in true_exp_rhs] if false_cnt_lhs * true_cnt_rhs else [])
    false_exps = (['(%s^%s)' % (exp1, exp2)
                   for exp1 in false_exp_lhs
                   for exp2 in false_exp_rhs] if false_cnt_lhs * false_cnt_rhs else []+
                  ['(%s^%s)' % (exp1, exp2)
                   for exp1 in true_exp_lhs
                   for exp2 in true_exp_rhs] if true_cnt_lhs * true_cnt_rhs else [])
    
    return ((false_cnt_lhs * true_cnt_rhs +
            true_cnt_lhs * false_cnt_rhs, true_exps),
            (true_cnt_lhs * true_cnt_rhs +
            false_cnt_lhs * false_cnt_rhs, false_exps))


def add(result1, result2):
    (cnt1, exps1), (cnt2, exps2) = result1, result2
    return (cnt1 + cnt2, set(exps1) | set(exps2))

OPS = {'&': and_, '|': or_, '^': xor_}
BASIC_OPS = {'&': bool.__and__, '|': bool.__or__, '^': bool.__xor__}

#O(n^3)
def total_ways_to_true(exp):
    tokens = exp.replace(' ','')
    operands = [tokens[i] for i in range(len(tokens)) if i % 2 == 0]
    ops = [tokens[i] for i in range(len(tokens)) if i % 2 == 1]
    basic_operators = [BASIC_OPS[op] for op in ops]
    operators = [OPS[op] for op in ops]
    n = len(operands)

    #upper traingle (elements above pricipal diag) holds True counts
    #lower traingle holds false counts
    #for i,j dp[i,j] holds true counts and dp[j,i] holds false counts
    dp_table = [[(0, []) for i in range(n)] for j in range(n)]
    for i in range(n):
        dp_table[i][i] = operands[i] == 'T'
    for k in range(n - 1):
        for i in range(n - k - 1):
            j = i + k + 1
            m = k + 2
            for l in range(1, m):
                if k == 0:
                    res = basic_operators[j - 1](dp_table[i][j - 1], dp_table[i + 1][j])
                    exp = ['(' +  operands[i] + ops[j - 1] + operands[j] + ')']
                    dp_table[i][j] = int(res), exp if res else []
                    dp_table[j][i] = int(not res), exp if not res else []
                    continue
                lhs = (i, j - l)
                rhs = (i + m - l, j)
                tc, fc= operators[j - l](lhs, rhs, dp_table)
                dp_table[i][j] = add(dp_table[i][j], tc)
                dp_table[j][i] = add(dp_table[j][i], fc)
    #print([ [c[0] if isinstance(c, tuple) else (c, r) for c in r] for r in dp_table])
    #print(dp_table)
    return dp_table[0][n - 1]

def total_ways_to_true_recur(exp):
    tokens = exp.replace(' ','')
    texps, fexps = _total_ways_to_true_recur(tokens)
    return len(texps), texps
    
def  _total_ways_to_true_recur(tokens):
    if len(tokens) == 1:
        return ([tokens], []) if tokens == 'T' else ([], [tokens])
    texps, fexps = set(), set()
    for i in range(len(tokens) // 2):
        lhs, op, rhs = tokens[:i * 2 + 1], tokens[i * 2 + 1], tokens[i * 2 + 2:]
        ltexps, lfexps = _total_ways_to_true_recur(lhs)
        rtexps, rfexps = _total_ways_to_true_recur(rhs)
        tt = set('(%s%s%s)' % (l, op, r) for l in ltexps for r in rtexps)
        tf = set('(%s%s%s)' % (l, op, r) for l in ltexps for r in rfexps)
        ft = set('(%s%s%s)' % (l, op, r) for l in lfexps for r in rtexps)
        ff = set('(%s%s%s)' % (l, op, r) for l in lfexps for r in rfexps)
        #print op, tt, tf, ft, ff
        if op == '|':
            texps |= tt | tf | ft
            fexps |= ff
        elif op == '^':
            texps |= tf | ft
            fexps |= tt | ff
        elif op == '&':
            texps |= tt
            fexps |= tf | ft | ff
    return texps, fexps

############################## TESTS ##############################
import pytest

@pytest.mark.parametrize('algorithm', [total_ways_to_true_recur, total_ways_to_true])
def should_counts_brackets_for_true_eval(algorithm):
    assert (1, {'(T^(T&F))'})== algorithm('T^T&F')
    assert (2, {'((F|T)&T)', '(F|(T&T))'}) == algorithm('F|T&T')
    assert (5, {'(T|((F|T)|F))', '(((T|F)|T)|F)', '((T|F)|(T|F))',
                '((T|(F|T))|F)', '(T|(F|(T|F)))'}) == algorithm('T|F|T|F')
    assert (5, {'(T|(F&(T^F)))', '(T|((F&T)^F))', '((T|F)&(T^F))',
                '(((T|F)&T)^F)', '((T|(F&T))^F)'}) == algorithm('T|F&T^F')
    assert (2, {'(T|((F&T)&F))', '(T|(F&(T&F)))'}) == algorithm('T|F&T&F')
    
    cnt, exps = algorithm('F&T|F^F^T&T|F')
    assert cnt == len(exps)
    assert cnt == 66
    assert cnt == sum(map(lambda exp: eval(exp,{'F':0,'T':1}),exps))
    #assert 0
