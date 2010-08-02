using System.Xml;
class dom
{
public static void Main()
{
string xml = @"<GuidelineRoot>
<Guideline>
<Ruleset Id='29' Name='Test Ruleset 1' ExecuteType='1'>
<Rule id='1'></Rule>
</Ruleset>
<Ruleset Id='30' Name='Test Ruleset 1' ExecuteType='1'>
<Rule id='2'></Rule>
</Ruleset>
<Ruleset Id='31' Name='Test Ruleset 1' ExecuteType='1'/>
<Ruleset Id='32' Name='Test Ruleset 1' ExecuteType='1'/>
<Ruleset Id='33' Name='Test Ruleset 1' ExecuteType='1'>
<Rule id='3'></Rule>
</Ruleset>
<Ruleset Id='34' Name='Test Ruleset 1' ExecuteType='1'/>
<Ruleset Id='35' Name='Test Ruleset 1' ExecuteType='1'/>
</Guideline>
</GuidelineRoot>
";
XmlDocument doc = new XmlDocument();
doc.LoadXml(xml);
System.Console.WriteLine(doc.SelectNodes("/GuidelineRoot/Guideline/Ruleset[count(Rule)=0]").Count);
}
}
