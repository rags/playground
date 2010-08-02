// $ANTLR 3.2 Sep 23, 2009 12:02:23 PostScheme/Lexer/PostSchemeLexer.g 2009-10-12 18:28:04

// The variable 'variable' is assigned but its value is never used.
#pragma warning disable 168, 219
// Unreachable code detected.
#pragma warning disable 162


using System;
using Antlr.Runtime;
using IList 		= System.Collections.IList;
using ArrayList 	= System.Collections.ArrayList;
using Stack 		= Antlr.Runtime.Collections.StackList;


namespace  PostScheme 
{
public partial class PostSchemeLexer : Lexer {
    public const int WS = 9;
    public const int NEWLINE = 8;
    public const int COMMA = 7;
    public const int IDENTIFIER = 10;
    public const int OPEN_PAREN = 4;
    public const int CLOSE_PAREN = 5;
    public const int DOT = 6;
    public const int EOF = -1;

    // delegates
    // delegators

    public PostSchemeLexer() 
    {
		InitializeCyclicDFAs();
    }
    public PostSchemeLexer(ICharStream input)
		: this(input, null) {
    }
    public PostSchemeLexer(ICharStream input, RecognizerSharedState state)
		: base(input, state) {
		InitializeCyclicDFAs(); 

    }
    
    override public string GrammarFileName
    {
    	get { return "PostScheme/Lexer/PostSchemeLexer.g";} 
    }

    // $ANTLR start "OPEN_PAREN"
    public void mOPEN_PAREN() // throws RecognitionException [2]
    {
    		try
    		{
            int _type = OPEN_PAREN;
    	int _channel = DEFAULT_TOKEN_CHANNEL;
            // PostScheme/Lexer/PostSchemeLexer.g:10:11: ( '(' )
            // PostScheme/Lexer/PostSchemeLexer.g:10:15: '('
            {
            	Match('('); 

            }

            state.type = _type;
            state.channel = _channel;
        }
        finally 
    	{
        }
    }
    // $ANTLR end "OPEN_PAREN"

    // $ANTLR start "CLOSE_PAREN"
    public void mCLOSE_PAREN() // throws RecognitionException [2]
    {
    		try
    		{
            int _type = CLOSE_PAREN;
    	int _channel = DEFAULT_TOKEN_CHANNEL;
            // PostScheme/Lexer/PostSchemeLexer.g:11:12: ( ')' )
            // PostScheme/Lexer/PostSchemeLexer.g:11:16: ')'
            {
            	Match(')'); 

            }

            state.type = _type;
            state.channel = _channel;
        }
        finally 
    	{
        }
    }
    // $ANTLR end "CLOSE_PAREN"

    // $ANTLR start "DOT"
    public void mDOT() // throws RecognitionException [2]
    {
    		try
    		{
            int _type = DOT;
    	int _channel = DEFAULT_TOKEN_CHANNEL;
            // PostScheme/Lexer/PostSchemeLexer.g:12:4: ( '\\.' )
            // PostScheme/Lexer/PostSchemeLexer.g:12:6: '\\.'
            {
            	Match('.'); 

            }

            state.type = _type;
            state.channel = _channel;
        }
        finally 
    	{
        }
    }
    // $ANTLR end "DOT"

    // $ANTLR start "COMMA"
    public void mCOMMA() // throws RecognitionException [2]
    {
    		try
    		{
            int _type = COMMA;
    	int _channel = DEFAULT_TOKEN_CHANNEL;
            // PostScheme/Lexer/PostSchemeLexer.g:13:6: ( ',' )
            // PostScheme/Lexer/PostSchemeLexer.g:13:8: ','
            {
            	Match(','); 

            }

            state.type = _type;
            state.channel = _channel;
        }
        finally 
    	{
        }
    }
    // $ANTLR end "COMMA"

    // $ANTLR start "NEWLINE"
    public void mNEWLINE() // throws RecognitionException [2]
    {
    		try
    		{
            int _type = NEWLINE;
    	int _channel = DEFAULT_TOKEN_CHANNEL;
            // PostScheme/Lexer/PostSchemeLexer.g:14:8: ( ( '\\r' )? '\\n' )
            // PostScheme/Lexer/PostSchemeLexer.g:14:9: ( '\\r' )? '\\n'
            {
            	// PostScheme/Lexer/PostSchemeLexer.g:14:9: ( '\\r' )?
            	int alt1 = 2;
            	int LA1_0 = input.LA(1);

            	if ( (LA1_0 == '\r') )
            	{
            	    alt1 = 1;
            	}
            	switch (alt1) 
            	{
            	    case 1 :
            	        // PostScheme/Lexer/PostSchemeLexer.g:14:9: '\\r'
            	        {
            	        	Match('\r'); 

            	        }
            	        break;

            	}

            	Match('\n'); 

            }

            state.type = _type;
            state.channel = _channel;
        }
        finally 
    	{
        }
    }
    // $ANTLR end "NEWLINE"

    // $ANTLR start "WS"
    public void mWS() // throws RecognitionException [2]
    {
    		try
    		{
            int _type = WS;
    	int _channel = DEFAULT_TOKEN_CHANNEL;
            // PostScheme/Lexer/PostSchemeLexer.g:15:5: ( ( ' ' | '\\t' )+ )
            // PostScheme/Lexer/PostSchemeLexer.g:15:9: ( ' ' | '\\t' )+
            {
            	// PostScheme/Lexer/PostSchemeLexer.g:15:9: ( ' ' | '\\t' )+
            	int cnt2 = 0;
            	do 
            	{
            	    int alt2 = 2;
            	    int LA2_0 = input.LA(1);

            	    if ( (LA2_0 == '\t' || LA2_0 == ' ') )
            	    {
            	        alt2 = 1;
            	    }


            	    switch (alt2) 
            		{
            			case 1 :
            			    // PostScheme/Lexer/PostSchemeLexer.g:
            			    {
            			    	if ( input.LA(1) == '\t' || input.LA(1) == ' ' ) 
            			    	{
            			    	    input.Consume();

            			    	}
            			    	else 
            			    	{
            			    	    MismatchedSetException mse = new MismatchedSetException(null,input);
            			    	    Recover(mse);
            			    	    throw mse;}


            			    }
            			    break;

            			default:
            			    if ( cnt2 >= 1 ) goto loop2;
            		            EarlyExitException eee2 =
            		                new EarlyExitException(2, input);
            		            throw eee2;
            	    }
            	    cnt2++;
            	} while (true);

            	loop2:
            		;	// Stops C# compiler whining that label 'loop2' has no statements

            	 Skip(); 

            }

            state.type = _type;
            state.channel = _channel;
        }
        finally 
    	{
        }
    }
    // $ANTLR end "WS"

    // $ANTLR start "IDENTIFIER"
    public void mIDENTIFIER() // throws RecognitionException [2]
    {
    		try
    		{
            int _type = IDENTIFIER;
    	int _channel = DEFAULT_TOKEN_CHANNEL;
            // PostScheme/Lexer/PostSchemeLexer.g:16:11: ( (~ ( OPEN_PAREN | CLOSE_PAREN | DOT | COMMA ) )+ )
            // PostScheme/Lexer/PostSchemeLexer.g:16:13: (~ ( OPEN_PAREN | CLOSE_PAREN | DOT | COMMA ) )+
            {
            	// PostScheme/Lexer/PostSchemeLexer.g:16:13: (~ ( OPEN_PAREN | CLOSE_PAREN | DOT | COMMA ) )+
            	int cnt3 = 0;
            	do 
            	{
            	    int alt3 = 2;
            	    int LA3_0 = input.LA(1);

            	    if ( ((LA3_0 >= '\u0000' && LA3_0 <= '\'') || (LA3_0 >= '*' && LA3_0 <= '+') || LA3_0 == '-' || (LA3_0 >= '/' && LA3_0 <= '\uFFFF')) )
            	    {
            	        alt3 = 1;
            	    }


            	    switch (alt3) 
            		{
            			case 1 :
            			    // PostScheme/Lexer/PostSchemeLexer.g:16:13: ~ ( OPEN_PAREN | CLOSE_PAREN | DOT | COMMA )
            			    {
            			    	if ( (input.LA(1) >= '\u0000' && input.LA(1) <= '\'') || (input.LA(1) >= '*' && input.LA(1) <= '+') || input.LA(1) == '-' || (input.LA(1) >= '/' && input.LA(1) <= '\uFFFF') ) 
            			    	{
            			    	    input.Consume();

            			    	}
            			    	else 
            			    	{
            			    	    MismatchedSetException mse = new MismatchedSetException(null,input);
            			    	    Recover(mse);
            			    	    throw mse;}


            			    }
            			    break;

            			default:
            			    if ( cnt3 >= 1 ) goto loop3;
            		            EarlyExitException eee3 =
            		                new EarlyExitException(3, input);
            		            throw eee3;
            	    }
            	    cnt3++;
            	} while (true);

            	loop3:
            		;	// Stops C# compiler whining that label 'loop3' has no statements


            }

            state.type = _type;
            state.channel = _channel;
        }
        finally 
    	{
        }
    }
    // $ANTLR end "IDENTIFIER"

    override public void mTokens() // throws RecognitionException 
    {
        // PostScheme/Lexer/PostSchemeLexer.g:1:8: ( OPEN_PAREN | CLOSE_PAREN | DOT | COMMA | NEWLINE | WS | IDENTIFIER )
        int alt4 = 7;
        alt4 = dfa4.Predict(input);
        switch (alt4) 
        {
            case 1 :
                // PostScheme/Lexer/PostSchemeLexer.g:1:10: OPEN_PAREN
                {
                	mOPEN_PAREN(); 

                }
                break;
            case 2 :
                // PostScheme/Lexer/PostSchemeLexer.g:1:21: CLOSE_PAREN
                {
                	mCLOSE_PAREN(); 

                }
                break;
            case 3 :
                // PostScheme/Lexer/PostSchemeLexer.g:1:33: DOT
                {
                	mDOT(); 

                }
                break;
            case 4 :
                // PostScheme/Lexer/PostSchemeLexer.g:1:37: COMMA
                {
                	mCOMMA(); 

                }
                break;
            case 5 :
                // PostScheme/Lexer/PostSchemeLexer.g:1:43: NEWLINE
                {
                	mNEWLINE(); 

                }
                break;
            case 6 :
                // PostScheme/Lexer/PostSchemeLexer.g:1:51: WS
                {
                	mWS(); 

                }
                break;
            case 7 :
                // PostScheme/Lexer/PostSchemeLexer.g:1:54: IDENTIFIER
                {
                	mIDENTIFIER(); 

                }
                break;

        }

    }


    protected DFA4 dfa4;
	private void InitializeCyclicDFAs()
	{
	    this.dfa4 = new DFA4(this);
	    this.dfa4.specialStateTransitionHandler = new DFA.SpecialStateTransitionHandler(DFA4_SpecialStateTransition);
	}

    const string DFA4_eotS =
        "\x05\uffff\x01\x08\x01\x09\x01\x0a\x03\uffff";
    const string DFA4_eofS =
        "\x0b\uffff";
    const string DFA4_minS =
        "\x01\x00\x04\uffff\x01\x0a\x02\x00\x03\uffff";
    const string DFA4_maxS =
        "\x01\uffff\x04\uffff\x01\x0a\x02\uffff\x03\uffff";
    const string DFA4_acceptS =
        "\x01\uffff\x01\x01\x01\x02\x01\x03\x01\x04\x03\uffff\x01\x07\x01"+
        "\x05\x01\x06";
    const string DFA4_specialS =
        "\x01\x00\x05\uffff\x01\x01\x01\x02\x03\uffff}>";
    static readonly string[] DFA4_transitionS = {
            "\x09\x08\x01\x07\x01\x06\x02\x08\x01\x05\x12\x08\x01\x07\x07"+
            "\x08\x01\x01\x01\x02\x02\x08\x01\x04\x01\x08\x01\x03\uffd1\x08",
            "",
            "",
            "",
            "",
            "\x01\x06",
            "\x28\x08\x02\uffff\x02\x08\x01\uffff\x01\x08\x01\uffff\uffd1"+
            "\x08",
            "\x09\x08\x01\x07\x16\x08\x01\x07\x07\x08\x02\uffff\x02\x08"+
            "\x01\uffff\x01\x08\x01\uffff\uffd1\x08",
            "",
            "",
            ""
    };

    static readonly short[] DFA4_eot = DFA.UnpackEncodedString(DFA4_eotS);
    static readonly short[] DFA4_eof = DFA.UnpackEncodedString(DFA4_eofS);
    static readonly char[] DFA4_min = DFA.UnpackEncodedStringToUnsignedChars(DFA4_minS);
    static readonly char[] DFA4_max = DFA.UnpackEncodedStringToUnsignedChars(DFA4_maxS);
    static readonly short[] DFA4_accept = DFA.UnpackEncodedString(DFA4_acceptS);
    static readonly short[] DFA4_special = DFA.UnpackEncodedString(DFA4_specialS);
    static readonly short[][] DFA4_transition = DFA.UnpackEncodedStringArray(DFA4_transitionS);

    protected class DFA4 : DFA
    {
        public DFA4(BaseRecognizer recognizer)
        {
            this.recognizer = recognizer;
            this.decisionNumber = 4;
            this.eot = DFA4_eot;
            this.eof = DFA4_eof;
            this.min = DFA4_min;
            this.max = DFA4_max;
            this.accept = DFA4_accept;
            this.special = DFA4_special;
            this.transition = DFA4_transition;

        }

        override public string Description
        {
            get { return "1:1: Tokens : ( OPEN_PAREN | CLOSE_PAREN | DOT | COMMA | NEWLINE | WS | IDENTIFIER );"; }
        }

    }


    protected internal int DFA4_SpecialStateTransition(DFA dfa, int s, IIntStream _input) //throws NoViableAltException
    {
            IIntStream input = _input;
    	int _s = s;
        switch ( s )
        {
               	case 0 : 
                   	int LA4_0 = input.LA(1);

                   	s = -1;
                   	if ( (LA4_0 == '(') ) { s = 1; }

                   	else if ( (LA4_0 == ')') ) { s = 2; }

                   	else if ( (LA4_0 == '.') ) { s = 3; }

                   	else if ( (LA4_0 == ',') ) { s = 4; }

                   	else if ( (LA4_0 == '\r') ) { s = 5; }

                   	else if ( (LA4_0 == '\n') ) { s = 6; }

                   	else if ( (LA4_0 == '\t' || LA4_0 == ' ') ) { s = 7; }

                   	else if ( ((LA4_0 >= '\u0000' && LA4_0 <= '\b') || (LA4_0 >= '\u000B' && LA4_0 <= '\f') || (LA4_0 >= '\u000E' && LA4_0 <= '\u001F') || (LA4_0 >= '!' && LA4_0 <= '\'') || (LA4_0 >= '*' && LA4_0 <= '+') || LA4_0 == '-' || (LA4_0 >= '/' && LA4_0 <= '\uFFFF')) ) { s = 8; }

                   	if ( s >= 0 ) return s;
                   	break;
               	case 1 : 
                   	int LA4_6 = input.LA(1);

                   	s = -1;
                   	if ( ((LA4_6 >= '\u0000' && LA4_6 <= '\'') || (LA4_6 >= '*' && LA4_6 <= '+') || LA4_6 == '-' || (LA4_6 >= '/' && LA4_6 <= '\uFFFF')) ) { s = 8; }

                   	else s = 9;

                   	if ( s >= 0 ) return s;
                   	break;
               	case 2 : 
                   	int LA4_7 = input.LA(1);

                   	s = -1;
                   	if ( (LA4_7 == '\t' || LA4_7 == ' ') ) { s = 7; }

                   	else if ( ((LA4_7 >= '\u0000' && LA4_7 <= '\b') || (LA4_7 >= '\n' && LA4_7 <= '\u001F') || (LA4_7 >= '!' && LA4_7 <= '\'') || (LA4_7 >= '*' && LA4_7 <= '+') || LA4_7 == '-' || (LA4_7 >= '/' && LA4_7 <= '\uFFFF')) ) { s = 8; }

                   	else s = 10;

                   	if ( s >= 0 ) return s;
                   	break;
        }
        NoViableAltException nvae4 =
            new NoViableAltException(dfa.Description, 4, _s, input);
        dfa.Error(nvae4);
        throw nvae4;
    }
 
    
}
}