# $ANTLR 3.0.1 ExpTreeParser.g 2008-11-10 00:44:27

from antlr3 import *
from antlr3.tree import *
from antlr3.compat import set, frozenset
        
from common.nodes import *
from common.post_order_visitor import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
RIGHT_PAREN=6
WS=11
OP_MINUS=8
OP_PLUS=7
OPERAND=4
LEFT_PAREN=5
OP_DIV=10
OP_MULT=9
EOF=-1

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "OPERAND", "LEFT_PAREN", "RIGHT_PAREN", "OP_PLUS", "OP_MINUS", "OP_MULT", 
    "OP_DIV", "WS"
]



class ExpTreeParser(TreeParser):
    grammarFileName = "ExpTreeParser.g"
    tokenNames = tokenNames

    def __init__(self, input):
        TreeParser.__init__(self, input)



                




    # $ANTLR start exp
    # ExpTreeParser.g:11:1: exp returns [node] : (theNode= plus | theNode= minus | theNode= div | theNode= mult | theNode= leaf ) ;
    def exp(self, ):

        node = None

        theNode = None


        try:
            try:
                # ExpTreeParser.g:11:19: ( (theNode= plus | theNode= minus | theNode= div | theNode= mult | theNode= leaf ) )
                # ExpTreeParser.g:11:20: (theNode= plus | theNode= minus | theNode= div | theNode= mult | theNode= leaf )
                # ExpTreeParser.g:11:20: (theNode= plus | theNode= minus | theNode= div | theNode= mult | theNode= leaf )
                alt1 = 5
                LA1 = self.input.LA(1)
                if LA1 == OP_PLUS:
                    alt1 = 1
                elif LA1 == OP_MINUS:
                    alt1 = 2
                elif LA1 == OP_DIV:
                    alt1 = 3
                elif LA1 == OP_MULT:
                    alt1 = 4
                elif LA1 == OPERAND:
                    alt1 = 5
                else:
                    nvae = NoViableAltException("11:20: (theNode= plus | theNode= minus | theNode= div | theNode= mult | theNode= leaf )", 1, 0, self.input)

                    raise nvae

                if alt1 == 1:
                    # ExpTreeParser.g:11:21: theNode= plus
                    self.following.append(self.FOLLOW_plus_in_exp45)
                    theNode = self.plus()
                    self.following.pop()



                elif alt1 == 2:
                    # ExpTreeParser.g:11:34: theNode= minus
                    self.following.append(self.FOLLOW_minus_in_exp49)
                    theNode = self.minus()
                    self.following.pop()



                elif alt1 == 3:
                    # ExpTreeParser.g:11:48: theNode= div
                    self.following.append(self.FOLLOW_div_in_exp53)
                    theNode = self.div()
                    self.following.pop()



                elif alt1 == 4:
                    # ExpTreeParser.g:11:60: theNode= mult
                    self.following.append(self.FOLLOW_mult_in_exp57)
                    theNode = self.mult()
                    self.following.pop()



                elif alt1 == 5:
                    # ExpTreeParser.g:11:73: theNode= leaf
                    self.following.append(self.FOLLOW_leaf_in_exp61)
                    theNode = self.leaf()
                    self.following.pop()




                #action start
                                                                                                      
                node=theNode

                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return node

    # $ANTLR end exp


    # $ANTLR start plus
    # ExpTreeParser.g:15:1: plus returns [node] : ^( OP_PLUS lhs= exp rhs= exp ) ;
    def plus(self, ):

        node = None

        lhs = None

        rhs = None


        try:
            try:
                # ExpTreeParser.g:15:20: ( ^( OP_PLUS lhs= exp rhs= exp ) )
                # ExpTreeParser.g:15:21: ^( OP_PLUS lhs= exp rhs= exp )
                self.match(self.input, OP_PLUS, self.FOLLOW_OP_PLUS_in_plus74)


                self.match(self.input, DOWN, None)
                self.following.append(self.FOLLOW_exp_in_plus78)
                lhs = self.exp()
                self.following.pop()

                self.following.append(self.FOLLOW_exp_in_plus82)
                rhs = self.exp()
                self.following.pop()


                self.match(self.input, UP, None)

                #action start
                                                               
                node = AddOperator(lhs,rhs)

                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return node

    # $ANTLR end plus


    # $ANTLR start minus
    # ExpTreeParser.g:19:1: minus returns [node] : ^( OP_MINUS lhs= exp rhs= exp ) ;
    def minus(self, ):

        node = None

        lhs = None

        rhs = None


        try:
            try:
                # ExpTreeParser.g:19:21: ( ^( OP_MINUS lhs= exp rhs= exp ) )
                # ExpTreeParser.g:19:23: ^( OP_MINUS lhs= exp rhs= exp )
                self.match(self.input, OP_MINUS, self.FOLLOW_OP_MINUS_in_minus96)


                self.match(self.input, DOWN, None)
                self.following.append(self.FOLLOW_exp_in_minus100)
                lhs = self.exp()
                self.following.pop()

                self.following.append(self.FOLLOW_exp_in_minus104)
                rhs = self.exp()
                self.following.pop()


                self.match(self.input, UP, None)

                #action start
                                                                  
                node = SubstractOperator(lhs,rhs)

                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return node

    # $ANTLR end minus


    # $ANTLR start mult
    # ExpTreeParser.g:23:1: mult returns [node] : ^( OP_MULT lhs= exp rhs= exp ) ;
    def mult(self, ):

        node = None

        lhs = None

        rhs = None


        try:
            try:
                # ExpTreeParser.g:23:20: ( ^( OP_MULT lhs= exp rhs= exp ) )
                # ExpTreeParser.g:23:22: ^( OP_MULT lhs= exp rhs= exp )
                self.match(self.input, OP_MULT, self.FOLLOW_OP_MULT_in_mult118)


                self.match(self.input, DOWN, None)
                self.following.append(self.FOLLOW_exp_in_mult122)
                lhs = self.exp()
                self.following.pop()

                self.following.append(self.FOLLOW_exp_in_mult126)
                rhs = self.exp()
                self.following.pop()


                self.match(self.input, UP, None)

                #action start
                                                                
                node = MultiplyOperator(lhs,rhs)

                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return node

    # $ANTLR end mult


    # $ANTLR start div
    # ExpTreeParser.g:27:1: div returns [node] : ^( OP_DIV lhs= exp rhs= exp ) ;
    def div(self, ):

        node = None

        lhs = None

        rhs = None


        try:
            try:
                # ExpTreeParser.g:27:19: ( ^( OP_DIV lhs= exp rhs= exp ) )
                # ExpTreeParser.g:27:21: ^( OP_DIV lhs= exp rhs= exp )
                self.match(self.input, OP_DIV, self.FOLLOW_OP_DIV_in_div140)


                self.match(self.input, DOWN, None)
                self.following.append(self.FOLLOW_exp_in_div144)
                lhs = self.exp()
                self.following.pop()

                self.following.append(self.FOLLOW_exp_in_div148)
                rhs = self.exp()
                self.following.pop()


                self.match(self.input, UP, None)

                #action start
                                                              
                node = DivideOperator(lhs,rhs)

                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return node

    # $ANTLR end div


    # $ANTLR start leaf
    # ExpTreeParser.g:31:1: leaf returns [node] : OPERAND ;
    def leaf(self, ):

        node = None

        OPERAND1 = None

        try:
            try:
                # ExpTreeParser.g:31:20: ( OPERAND )
                # ExpTreeParser.g:31:22: OPERAND
                OPERAND1 = self.input.LT(1)
                self.match(self.input, OPERAND, self.FOLLOW_OPERAND_in_leaf161)

                #action start
                                             
                node = Operand(OPERAND1.getText())

                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return node

    # $ANTLR end leaf


 

    FOLLOW_plus_in_exp45 = frozenset([1])
    FOLLOW_minus_in_exp49 = frozenset([1])
    FOLLOW_div_in_exp53 = frozenset([1])
    FOLLOW_mult_in_exp57 = frozenset([1])
    FOLLOW_leaf_in_exp61 = frozenset([1])
    FOLLOW_OP_PLUS_in_plus74 = frozenset([2])
    FOLLOW_exp_in_plus78 = frozenset([4, 7, 8, 9, 10])
    FOLLOW_exp_in_plus82 = frozenset([3])
    FOLLOW_OP_MINUS_in_minus96 = frozenset([2])
    FOLLOW_exp_in_minus100 = frozenset([4, 7, 8, 9, 10])
    FOLLOW_exp_in_minus104 = frozenset([3])
    FOLLOW_OP_MULT_in_mult118 = frozenset([2])
    FOLLOW_exp_in_mult122 = frozenset([4, 7, 8, 9, 10])
    FOLLOW_exp_in_mult126 = frozenset([3])
    FOLLOW_OP_DIV_in_div140 = frozenset([2])
    FOLLOW_exp_in_div144 = frozenset([4, 7, 8, 9, 10])
    FOLLOW_exp_in_div148 = frozenset([3])
    FOLLOW_OPERAND_in_leaf161 = frozenset([1])

