# $ANTLR 3.0.1 Exp.g 2008-11-10 00:44:26

from antlr3 import *
from antlr3.compat import set, frozenset


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
Tokens=12
EOF=-1

class ExpLexer(Lexer):

    grammarFileName = "Exp.g"

    def __init__(self, input=None):
        Lexer.__init__(self, input)





    # $ANTLR start OPERAND
    def mOPERAND(self, ):

        try:
            self.type = OPERAND

            # Exp.g:9:8: ( ( '0' .. '9' )+ )
            # Exp.g:9:10: ( '0' .. '9' )+
            # Exp.g:9:10: ( '0' .. '9' )+
            cnt1 = 0
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((u'0' <= LA1_0 <= u'9')) :
                    alt1 = 1


                if alt1 == 1:
                    # Exp.g:9:10: '0' .. '9'
                    self.matchRange(u'0', u'9')



                else:
                    if cnt1 >= 1:
                        break #loop1

                    eee = EarlyExitException(1, self.input)
                    raise eee

                cnt1 += 1






        finally:

            pass

    # $ANTLR end OPERAND



    # $ANTLR start LEFT_PAREN
    def mLEFT_PAREN(self, ):

        try:
            self.type = LEFT_PAREN

            # Exp.g:11:11: ( '(' )
            # Exp.g:11:13: '('
            self.match(u'(')





        finally:

            pass

    # $ANTLR end LEFT_PAREN



    # $ANTLR start RIGHT_PAREN
    def mRIGHT_PAREN(self, ):

        try:
            self.type = RIGHT_PAREN

            # Exp.g:12:12: ( ')' )
            # Exp.g:12:14: ')'
            self.match(u')')





        finally:

            pass

    # $ANTLR end RIGHT_PAREN



    # $ANTLR start OP_PLUS
    def mOP_PLUS(self, ):

        try:
            self.type = OP_PLUS

            # Exp.g:13:8: ( '+' )
            # Exp.g:13:10: '+'
            self.match(u'+')





        finally:

            pass

    # $ANTLR end OP_PLUS



    # $ANTLR start OP_MINUS
    def mOP_MINUS(self, ):

        try:
            self.type = OP_MINUS

            # Exp.g:14:9: ( '-' )
            # Exp.g:14:11: '-'
            self.match(u'-')





        finally:

            pass

    # $ANTLR end OP_MINUS



    # $ANTLR start OP_MULT
    def mOP_MULT(self, ):

        try:
            self.type = OP_MULT

            # Exp.g:15:8: ( '*' )
            # Exp.g:15:10: '*'
            self.match(u'*')





        finally:

            pass

    # $ANTLR end OP_MULT



    # $ANTLR start OP_DIV
    def mOP_DIV(self, ):

        try:
            self.type = OP_DIV

            # Exp.g:16:7: ( '/' )
            # Exp.g:16:9: '/'
            self.match(u'/')





        finally:

            pass

    # $ANTLR end OP_DIV



    # $ANTLR start WS
    def mWS(self, ):

        try:
            self.type = WS

            # Exp.g:18:4: ( ( ' ' | '\\t' | '\\n' | '\\r' )+ )
            # Exp.g:18:6: ( ' ' | '\\t' | '\\n' | '\\r' )+
            # Exp.g:18:6: ( ' ' | '\\t' | '\\n' | '\\r' )+
            cnt2 = 0
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if ((u'\t' <= LA2_0 <= u'\n') or LA2_0 == u'\r' or LA2_0 == u' ') :
                    alt2 = 1


                if alt2 == 1:
                    # Exp.g:
                    if (u'\t' <= self.input.LA(1) <= u'\n') or self.input.LA(1) == u'\r' or self.input.LA(1) == u' ':
                        self.input.consume();

                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt2 >= 1:
                        break #loop2

                    eee = EarlyExitException(2, self.input)
                    raise eee

                cnt2 += 1


            #action start
            self.skip()
            #action end




        finally:

            pass

    # $ANTLR end WS



    def mTokens(self):
        # Exp.g:1:8: ( OPERAND | LEFT_PAREN | RIGHT_PAREN | OP_PLUS | OP_MINUS | OP_MULT | OP_DIV | WS )
        alt3 = 8
        LA3 = self.input.LA(1)
        if LA3 == u'0' or LA3 == u'1' or LA3 == u'2' or LA3 == u'3' or LA3 == u'4' or LA3 == u'5' or LA3 == u'6' or LA3 == u'7' or LA3 == u'8' or LA3 == u'9':
            alt3 = 1
        elif LA3 == u'(':
            alt3 = 2
        elif LA3 == u')':
            alt3 = 3
        elif LA3 == u'+':
            alt3 = 4
        elif LA3 == u'-':
            alt3 = 5
        elif LA3 == u'*':
            alt3 = 6
        elif LA3 == u'/':
            alt3 = 7
        elif LA3 == u'\t' or LA3 == u'\n' or LA3 == u'\r' or LA3 == u' ':
            alt3 = 8
        else:
            nvae = NoViableAltException("1:1: Tokens : ( OPERAND | LEFT_PAREN | RIGHT_PAREN | OP_PLUS | OP_MINUS | OP_MULT | OP_DIV | WS );", 3, 0, self.input)

            raise nvae

        if alt3 == 1:
            # Exp.g:1:10: OPERAND
            self.mOPERAND()



        elif alt3 == 2:
            # Exp.g:1:18: LEFT_PAREN
            self.mLEFT_PAREN()



        elif alt3 == 3:
            # Exp.g:1:29: RIGHT_PAREN
            self.mRIGHT_PAREN()



        elif alt3 == 4:
            # Exp.g:1:41: OP_PLUS
            self.mOP_PLUS()



        elif alt3 == 5:
            # Exp.g:1:49: OP_MINUS
            self.mOP_MINUS()



        elif alt3 == 6:
            # Exp.g:1:58: OP_MULT
            self.mOP_MULT()



        elif alt3 == 7:
            # Exp.g:1:66: OP_DIV
            self.mOP_DIV()



        elif alt3 == 8:
            # Exp.g:1:73: WS
            self.mWS()








 

