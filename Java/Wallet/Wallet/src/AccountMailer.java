/**
 * Created by IntelliJ IDEA.
 * User: rramakri
 * Date: Jun 21, 2006
 * Time: 3:09:15 PM
 * To change this template use File | Settings | File Templates.
 */

public class AccountMailer extends Mailer implements INotifyOverDraw {

   public void notifyOverDraw(Account account) {
             sendMail(account.getEmail(),"some message");
    }
}
