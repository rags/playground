package rps;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class GameRules {
    Map<String,Set<String>> domination;

    private GameRules() {
        this(new HashMap<String, Set<String>>());
    }

    private GameRules(Map<String, Set<String>> domination) {
        this.domination = domination;
    }

    public static GameRules rockPaperScissors(){

        return null;
    }

    public String [] validMoves(){

        return new String[0];
    }

    public boolean winner(String move1,String move2){

        return false;
    }

    public boolean winner
}
