# $ANTLR 3.0.1 Exp.g 2008-11-10 00:44:26

from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



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



class ExpParser(Parser):
    grammarFileName = "Exp.g"
    tokenNames = tokenNames

    def __init__(self, input):
        Parser.__init__(self, input)



                
        self.adaptor = CommonTreeAdaptor()




    class low_prededence_op_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start low_prededence_op
    # Exp.g:20:1: low_prededence_op : ( OP_PLUS | OP_MINUS );
    def low_prededence_op(self, ):

        retval = self.low_prededence_op_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set1 = None

        set1_tree = None

        try:
            try:
                # Exp.g:20:18: ( OP_PLUS | OP_MINUS )
                # Exp.g:
                root_0 = self.adaptor.nil()

                set1 = self.input.LT(1)
                if (OP_PLUS <= self.input.LA(1) <= OP_MINUS):
                    self.input.consume();
                    self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set1))
                    self.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_low_prededence_op0
                        )
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self.adaptor.rulePostProcessing(root_0)
                self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end low_prededence_op

    class high_prededence_op_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start high_prededence_op
    # Exp.g:21:1: high_prededence_op : ( OP_MULT | OP_DIV );
    def high_prededence_op(self, ):

        retval = self.high_prededence_op_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set2 = None

        set2_tree = None

        try:
            try:
                # Exp.g:21:19: ( OP_MULT | OP_DIV )
                # Exp.g:
                root_0 = self.adaptor.nil()

                set2 = self.input.LT(1)
                if (OP_MULT <= self.input.LA(1) <= OP_DIV):
                    self.input.consume();
                    self.adaptor.addChild(root_0, self.adaptor.createWithPayload(set2))
                    self.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recoverFromMismatchedSet(
                        self.input, mse, self.FOLLOW_set_in_high_prededence_op0
                        )
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self.adaptor.rulePostProcessing(root_0)
                self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end high_prededence_op

    class low_precedence_exp_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start low_precedence_exp
    # Exp.g:23:1: low_precedence_exp : high_precedence_exp ( low_prededence_op high_precedence_exp )* ;
    def low_precedence_exp(self, ):

        retval = self.low_precedence_exp_return()
        retval.start = self.input.LT(1)

        root_0 = None

        high_precedence_exp3 = None

        low_prededence_op4 = None

        high_precedence_exp5 = None



        try:
            try:
                # Exp.g:23:19: ( high_precedence_exp ( low_prededence_op high_precedence_exp )* )
                # Exp.g:23:21: high_precedence_exp ( low_prededence_op high_precedence_exp )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_high_precedence_exp_in_low_precedence_exp126)
                high_precedence_exp3 = self.high_precedence_exp()
                self.following.pop()

                self.adaptor.addChild(root_0, high_precedence_exp3.tree)
                # Exp.g:23:41: ( low_prededence_op high_precedence_exp )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((OP_PLUS <= LA1_0 <= OP_MINUS)) :
                        alt1 = 1


                    if alt1 == 1:
                        # Exp.g:23:42: low_prededence_op high_precedence_exp
                        self.following.append(self.FOLLOW_low_prededence_op_in_low_precedence_exp129)
                        low_prededence_op4 = self.low_prededence_op()
                        self.following.pop()

                        root_0 = self.adaptor.becomeRoot(low_prededence_op4.tree, root_0)
                        self.following.append(self.FOLLOW_high_precedence_exp_in_low_precedence_exp132)
                        high_precedence_exp5 = self.high_precedence_exp()
                        self.following.pop()

                        self.adaptor.addChild(root_0, high_precedence_exp5.tree)


                    else:
                        break #loop1





                retval.stop = self.input.LT(-1)


                retval.tree = self.adaptor.rulePostProcessing(root_0)
                self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end low_precedence_exp

    class high_precedence_exp_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start high_precedence_exp
    # Exp.g:24:1: high_precedence_exp : atom ( high_prededence_op atom )* ;
    def high_precedence_exp(self, ):

        retval = self.high_precedence_exp_return()
        retval.start = self.input.LT(1)

        root_0 = None

        atom6 = None

        high_prededence_op7 = None

        atom8 = None



        try:
            try:
                # Exp.g:24:20: ( atom ( high_prededence_op atom )* )
                # Exp.g:24:22: atom ( high_prededence_op atom )*
                root_0 = self.adaptor.nil()

                self.following.append(self.FOLLOW_atom_in_high_precedence_exp140)
                atom6 = self.atom()
                self.following.pop()

                self.adaptor.addChild(root_0, atom6.tree)
                # Exp.g:24:27: ( high_prededence_op atom )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if ((OP_MULT <= LA2_0 <= OP_DIV)) :
                        alt2 = 1


                    if alt2 == 1:
                        # Exp.g:24:28: high_prededence_op atom
                        self.following.append(self.FOLLOW_high_prededence_op_in_high_precedence_exp143)
                        high_prededence_op7 = self.high_prededence_op()
                        self.following.pop()

                        root_0 = self.adaptor.becomeRoot(high_prededence_op7.tree, root_0)
                        self.following.append(self.FOLLOW_atom_in_high_precedence_exp146)
                        atom8 = self.atom()
                        self.following.pop()

                        self.adaptor.addChild(root_0, atom8.tree)


                    else:
                        break #loop2





                retval.stop = self.input.LT(-1)


                retval.tree = self.adaptor.rulePostProcessing(root_0)
                self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end high_precedence_exp

    class atom_return(object):
        def __init__(self):
            self.start = None
            self.stop = None

            self.tree = None


    # $ANTLR start atom
    # Exp.g:25:1: atom : ( OPERAND | LEFT_PAREN low_precedence_exp RIGHT_PAREN );
    def atom(self, ):

        retval = self.atom_return()
        retval.start = self.input.LT(1)

        root_0 = None

        OPERAND9 = None
        LEFT_PAREN10 = None
        RIGHT_PAREN12 = None
        low_precedence_exp11 = None


        OPERAND9_tree = None
        LEFT_PAREN10_tree = None
        RIGHT_PAREN12_tree = None

        try:
            try:
                # Exp.g:25:5: ( OPERAND | LEFT_PAREN low_precedence_exp RIGHT_PAREN )
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == OPERAND) :
                    alt3 = 1
                elif (LA3_0 == LEFT_PAREN) :
                    alt3 = 2
                else:
                    nvae = NoViableAltException("25:1: atom : ( OPERAND | LEFT_PAREN low_precedence_exp RIGHT_PAREN );", 3, 0, self.input)

                    raise nvae

                if alt3 == 1:
                    # Exp.g:25:7: OPERAND
                    root_0 = self.adaptor.nil()

                    OPERAND9 = self.input.LT(1)
                    self.match(self.input, OPERAND, self.FOLLOW_OPERAND_in_atom154)


                    OPERAND9_tree = self.adaptor.createWithPayload(OPERAND9)
                    self.adaptor.addChild(root_0, OPERAND9_tree)



                elif alt3 == 2:
                    # Exp.g:25:16: LEFT_PAREN low_precedence_exp RIGHT_PAREN
                    root_0 = self.adaptor.nil()

                    LEFT_PAREN10 = self.input.LT(1)
                    self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_atom157)

                    self.following.append(self.FOLLOW_low_precedence_exp_in_atom160)
                    low_precedence_exp11 = self.low_precedence_exp()
                    self.following.pop()

                    self.adaptor.addChild(root_0, low_precedence_exp11.tree)
                    RIGHT_PAREN12 = self.input.LT(1)
                    self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_atom162)



                retval.stop = self.input.LT(-1)


                retval.tree = self.adaptor.rulePostProcessing(root_0)
                self.adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return retval

    # $ANTLR end atom


 

    FOLLOW_set_in_low_prededence_op0 = frozenset([1])
    FOLLOW_set_in_high_prededence_op0 = frozenset([1])
    FOLLOW_high_precedence_exp_in_low_precedence_exp126 = frozenset([1, 7, 8])
    FOLLOW_low_prededence_op_in_low_precedence_exp129 = frozenset([4, 5])
    FOLLOW_high_precedence_exp_in_low_precedence_exp132 = frozenset([1, 7, 8])
    FOLLOW_atom_in_high_precedence_exp140 = frozenset([1, 9, 10])
    FOLLOW_high_prededence_op_in_high_precedence_exp143 = frozenset([4, 5])
    FOLLOW_atom_in_high_precedence_exp146 = frozenset([1, 9, 10])
    FOLLOW_OPERAND_in_atom154 = frozenset([1])
    FOLLOW_LEFT_PAREN_in_atom157 = frozenset([4, 5])
    FOLLOW_low_precedence_exp_in_atom160 = frozenset([6])
    FOLLOW_RIGHT_PAREN_in_atom162 = frozenset([1])

