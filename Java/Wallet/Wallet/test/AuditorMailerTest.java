import org.jmock.MockObjectTestCase;

/**
 * Created by IntelliJ IDEA.
 * User: rramakri
 * Date: Jun 21, 2006
 * Time: 4:05:40 PM
 * To change this template use File | Settings | File Templates.
 */
public class AuditorMailerTest extends MockObjectTestCase {

    public void testAuditorMailer(){
        INotifyOverDraw auditorMailer = new AuditorMailerStub("some@some.com");
        auditorMailer.notifyOverDraw(new Account("someaccount@jhgj.com"));
    }
}
