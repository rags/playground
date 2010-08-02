import java.util.List;
import java.util.ArrayList;

/**
 * Created by IntelliJ IDEA.
 * User: rramakri
 * Date: Jun 21, 2006
 * Time: 2:16:38 PM
 * To change this template use File | Settings | File Templates.
 */
public class Account {
    private int _money;
    private String _email;
    private List<INotifyOverDraw> _allSubscribers;

    public Account(String email) {
        this._email = email;
        _allSubscribers = new ArrayList<INotifyOverDraw>();
    }

    public void putMoney(int money) {
        _money += money;
    }

    public boolean hasGotMoney() {
        return _money>0;
    }

    public int getMoney() {
       return _money;
    }

    public void withdraw(int money) {
        if(money<0) throw new RuntimeException("Cant put -ve money");
        if(money>_money) {
            notifyOverDraw();
        }
        _money -= money;
    }

    private void notifyOverDraw() {
        for(int i=0; i<_allSubscribers.size();i++){
            _allSubscribers.get(i).notifyOverDraw(this);
        }
    }

    public String getEmail() {
        return _email;
    }

    public void subscribeNofity(INotifyOverDraw notify) {
        _allSubscribers.add(notify);
    }
}
