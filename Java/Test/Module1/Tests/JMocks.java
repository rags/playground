import org.junit.Test;
import org.junit.Assert;
import org.jmock.Mock;
import org.jmock.MockObjectTestCase;
import org.jmock.core.DynamicMock;
import org.jmock.core.Stub;
import org.jmock.core.Invokable;
import org.jmock.core.matcher.InvokeOnceMatcher;
import org.jmock.core.matcher.InvokeCountMatcher;
import junit.framework.TestCase;

/**
 * Created by IntelliJ IDEA.
 * User: rramakri
 * Date: Jun 14, 2006
 * Time: 5:09:09 PM
 * To change this template use File | Settings | File Templates.
 */
public class JMocks //extends TestCase
{
    static class ClassToTest
    {
        public ClassToTest(Runnable runnable)
        {
            runnable.run();
        }
    }
    /*public void testAddition()
    {
        assertEquals(2,1+1+0);
    }*/

    @Test public void mockTest()
    {
        Mock mockRunnable = new Mock(Runnable.class);
        mockRunnable.expects(new InvokeCountMatcher(1)).method("run");
        new ClassToTest((Runnable) mockRunnable.proxy());
        mockRunnable.verify();
    }

}
