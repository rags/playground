# y combinator allows for definition of recursive function with just lambda and variable assignment (note that 'def' is not used)
Y = lambda f: (lambda fn: f(lambda arg: (fn(fn))(arg)))((lambda fn: f(lambda arg: (fn(fn))(arg))))


#equivalent code using def. Note that in this case the assumption still is that a function cannot be refered to (recursively) inside its body. A function can only be used after it is defined.
def Y1(f):
    def recur(fn):
        def recur2(arg):
            return (fn(fn))(arg)
        return f(recur2)
    return recur(recur)

fact_lambda = lambda fn: (lambda n: 1 if n == 0 else n * fn(n - 1))

#equivalent code using def. The above fact assumes there is no 'def' available in the language
def fact(fn):
    def fact_step(n):
        return 1 if n == 0 else n * fn(n - 1)
    return fact_step

############################## TESTS ##############################
import pytest

@pytest.mark.parametrize('algorithm', [Y1, Y])
@pytest.mark.parametrize(('tester', 'input',  'result'),
                         [(fact, 5, 120),
                          (fact_lambda, 4, 24)])
def should_recur(algorithm, tester,  input, result):
    assert algorithm(tester)(input) == result
