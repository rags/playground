using System;
using System.Xml;

public class XmlStuff
{
	public static void Main()
	{
		var doc = new XmlDocument();
		doc.Load("xml.xml");
		Console.WriteLine(doc.OuterXml);
	}	
}