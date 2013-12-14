package rps;

public interface GameStrategy {
    boolean gameOver();

    void updateStatus(Game game);
}

