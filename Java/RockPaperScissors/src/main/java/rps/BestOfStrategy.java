package rps;

//Best of N throws.
public class BestOfStrategy implements GameStrategy {
    private int counter;
    private int count;

    public BestOfStrategy(int count) {
        this.count = count;
        this.counter = 0;
    }

    @Override
    public boolean gameOver() {
        return counter>=count;
    }

    @Override
    public void updateStatus(Game game) {
        counter++;
    }

}
