package rps;

//A triplet of <winner dominates loser>
public class Domination {
    private String winner;
    private String loser;
    private String reason;

    public Domination(String winner, String loser, String reason) {
        this.winner = winner;
        this.loser = loser;
        this.reason = reason;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Domination)) return false;

        Domination that = (Domination) o;

        if (!loser.equals(that.loser)) return false;
        if (!winner.equals(that.winner)) return false;

        return true;
    }

    public static int hashCode(String theDominator, String theDominated){
        int result = theDominator.hashCode();
        result = 31 * result + theDominated.hashCode();
        return result;
    }

    @Override
    public int hashCode() {
      return hashCode(winner, loser);
    }

    public String winner() {
        return winner;
    }

    @Override
    public String toString() {
        return winner() + " " + reason + " " + loser;
    }
}
