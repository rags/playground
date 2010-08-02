import org.jmock.Mock;
import org.jmock.MockObjectTestCase;


/**
 * Created by IntelliJ IDEA.
 * User: rramakri
 * Date: Jun 21, 2006
 * Time: 2:17:18 PM
 * To change this template use File | Settings | File Templates.
 */
public class AccountTest extends MockObjectTestCase {
    private Account _account;
    private String _email;

    protected void setUp() throws Exception {
        _email = "foo@mailinator.com";
        _account = new Account(_email);
    }


    public void testThatMoneyCanBePutIntoAccount() {

        _account.putMoney(100);
        assertTrue(_account.hasGotMoney());
    }
    public void testGetMoney() {
        _account.putMoney(34);
        assertEquals(34, _account.getMoney());
    }

    public void testAssertThatMoneyPutInAddsUp() {
        _account.putMoney(14);
        _account.putMoney(6);
        assertEquals(20, _account.getMoney());
    }

    public void testThatOwnerCanTakeMoneyOut() {
        _account.putMoney(50);
        _account.withdraw(20);
        assertEquals(30, _account.getMoney());
    }

    public void testThatOwnerCanTNotTakeOutNegativeMoney() {
        try {
            _account.withdraw(-34);
            fail("no exception thrown");
        }
        catch (RuntimeException ex) {
            assertEquals("Cant put -ve money", ex.getMessage());
        }
    }

    public void testassertThatOwnersCanOverdraw() {
         _account.putMoney(50);
         _account.withdraw(70);
         assertEquals(-20, _account.getMoney());
    }

    public void testEmailNotificationonOverDraw()
    {
        Mock auditorMock = mock(INotifyOverDraw.class);
        Mock accountMock = mock(INotifyOverDraw.class);
        Account acct = new Account(_email);
        auditorMock.expects(once()).method("notifyOverDraw").with(eq(acct));
        accountMock.expects(once()).method("notifyOverDraw").with(eq(acct));
        acct.subscribeNofity((INotifyOverDraw) accountMock.proxy());
        acct.subscribeNofity((INotifyOverDraw) auditorMock.proxy());
         acct.putMoney(50);
         acct.withdraw(70);
        auditorMock.verify();
    }
}
