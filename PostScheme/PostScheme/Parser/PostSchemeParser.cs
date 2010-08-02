// $ANTLR 3.2 Sep 23, 2009 12:02:23 PostScheme/Parser/PostSchemeParser.g 2009-10-12 18:28:05

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
public partial class PostSchemeParser : Parser
{
    public static readonly string[] tokenNames = new string[] 
	{
        "<invalid>", 
		"<EOR>", 
		"<DOWN>", 
		"<UP>", 
		"OPEN_PAREN", 
		"CLOSE_PAREN", 
		"DOT", 
		"COMMA", 
		"NEWLINE", 
		"WS", 
		"IDENTIFIER"
    };

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



        public PostSchemeParser(ITokenStream input)
    		: this(input, new RecognizerSharedState()) {
        }

        public PostSchemeParser(ITokenStream input, RecognizerSharedState state)
    		: base(input, state) {
            InitializeCyclicDFAs();

             
        }
        

    override public string[] TokenNames {
		get { return PostSchemeParser.tokenNames; }
    }

    override public string GrammarFileName {
		get { return "PostScheme/Parser/PostSchemeParser.g"; }
    }



    // $ANTLR start "statement"
    // PostScheme/Parser/PostSchemeParser.g:9:1: statement : OPEN_PAREN IDENTIFIER CLOSE_PAREN ;
    public void statement() // throws RecognitionException [1]
    {   
        try 
    	{
            // PostScheme/Parser/PostSchemeParser.g:9:10: ( OPEN_PAREN IDENTIFIER CLOSE_PAREN )
            // PostScheme/Parser/PostSchemeParser.g:9:12: OPEN_PAREN IDENTIFIER CLOSE_PAREN
            {
            	Match(input,OPEN_PAREN,FOLLOW_OPEN_PAREN_in_statement45); 
            	Match(input,IDENTIFIER,FOLLOW_IDENTIFIER_in_statement47); 
            	Match(input,CLOSE_PAREN,FOLLOW_CLOSE_PAREN_in_statement49); 

            }

        }
        catch (RecognitionException re) 
    	{
            ReportError(re);
            Recover(input,re);
        }
        finally 
    	{
        }
        return ;
    }
    // $ANTLR end "statement"

    // Delegated rules


	private void InitializeCyclicDFAs()
	{
	}

 

    public static readonly BitSet FOLLOW_OPEN_PAREN_in_statement45 = new BitSet(new ulong[]{0x0000000000000400UL});
    public static readonly BitSet FOLLOW_IDENTIFIER_in_statement47 = new BitSet(new ulong[]{0x0000000000000020UL});
    public static readonly BitSet FOLLOW_CLOSE_PAREN_in_statement49 = new BitSet(new ulong[]{0x0000000000000002UL});

}
}