/**
 * Created by IntelliJ IDEA.
 * User: rramakri
 * Date: Jun 21, 2006
 * Time: 3:50:42 PM
 * To change this template use File | Settings | File Templates.
 */
public class AuditorMailer extends Mailer implements INotifyOverDraw {
    String _email;

    public AuditorMailer(String email) {
        _email = email;
    }

    public void notifyOverDraw(Account account) {
        sendMail(_email,"blah");
    }

    protected void sendMailProxy(String email, String msg){

    }
}
