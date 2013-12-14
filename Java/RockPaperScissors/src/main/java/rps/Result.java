package rps;

public class Result{
    private Player[] winners;

    public Result(Player... winners) {
        this.winners = winners;
    }

    public boolean tie(){
        return winners.length!=1;
    }

    public Player winner() {
        if(tie()){
            throw new PreconditionFailure("No single winner. Its a TIE");
        }
        return winners[0];
    }
}
