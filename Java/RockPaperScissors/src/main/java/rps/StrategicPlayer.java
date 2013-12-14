package rps;

import java.util.List;

public abstract class StrategicPlayer implements Player {
    private PlayerImpl playerImpl;

    protected StrategicPlayer(PlayerImpl playerImpl) {
        this.playerImpl = playerImpl;
    }

    protected abstract String chooseImpl();

    public void choose(){
      playerImpl.addChoice(chooseImpl());
    }

    @Override
    public String name() {
        return playerImpl.name();
    }

    @Override
    public int rounds() {
        return playerImpl.rounds();
    }

    @Override
    public String choices(int i) {
        return playerImpl.choices(i);
    }


    @Override
    public List<String> choices() {
        return playerImpl.choices();
    }

}
