package rps;

public class Game {
    protected StrategicPlayer player1;
    protected StrategicPlayer player2;
    protected GameRules rules;
    protected GameStrategy strategy;

    protected Game(StrategicPlayer player1, StrategicPlayer player2, GameRules rules, GameStrategy strategy) {
        this.player1 = player1;
        this.player2 = player2;
        this.rules = rules;
        this.strategy = strategy;
    }

    private void nextThrow(){
        player1.choose();
        player2.choose();
    }

    public Result play(){
        while(!strategy.gameOver()){
            nextThrow();
            strategy.updateStatus(this);
        }
        return calcWinner();
    }

    Result calcWinner() {
        return rules.winner(player1, player2);
    }

}
