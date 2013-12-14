package rps;

//Allows game to continue as long as there is a tie. The first non-equal throw ends the game
public class TieBreakerStrategy implements GameStrategy {
    boolean gameOver;

    public TieBreakerStrategy() {
        gameOver = false;//being explicit
    }

    @Override
    public boolean gameOver() {
        return gameOver;
    }

    @Override
    public void updateStatus(Game game) {
        gameOver = !game.calcWinner().tie();
    }

}
