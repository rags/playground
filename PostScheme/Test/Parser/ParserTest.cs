using System;
using NUnit.Framework;
using PostScheme;
using Antlr.Runtime;

namespace PostSchemeTest
{
	
	[TestFixture]
	public class ParserTest
	{
	
		[Test]
		public void Test()
		{			
			Parser("(fn)");
		}
		
		[Test]
		public void Test1()
		{			
			throw new Exception();
		}
		
		private PostSchemeParser Parser(string input)
		{
			return new PostSchemeParser(new CommonTokenStream(new PostSchemeLexer(new ANTLRStringStream(input))));
		}
	}
}
