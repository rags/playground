import javax.xml.parsers.*;
import org.w3c.dom.*;
import java.io.*;
import javax.xml.transform.dom.*;
import javax.xml.transform.*;
import javax.xml.transform.stream.*;

class Xml{
    public static void main(String [] a) throws Exception{
	Document doc = DocumentBuilderFactory.newInstance().
	    newDocumentBuilder().parse("xml.xml");
	Transformer transformer = TransformerFactory.newInstance().newTransformer();
	StreamResult result = new StreamResult(new StringWriter());
	DOMSource source = new DOMSource(doc);
	transformer.transform(source, result);
	System.out.println(result.getWriter().toString());

    }
}
