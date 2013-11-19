package rps;

public interface GameStrategy {
    boolean gameOver();
    void nextMove(String player1Move,String player2Move);
}
