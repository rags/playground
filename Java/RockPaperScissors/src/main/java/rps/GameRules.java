package rps;

import com.google.common.base.Function;
import com.google.common.collect.Maps;
import com.google.common.collect.Sets;

import java.util.Map;
import java.util.Set;

import static com.google.common.collect.Collections2.transform;
import static java.util.Arrays.asList;

public class GameRules {
    private Map<Integer, Domination> dominations; //For O(1) lookup
    private Set<String> validChoices;

    GameRules(Domination... dominations) {
        this.dominations = Maps.uniqueIndex(asList(dominations), new Function<Domination, Integer>() {
            @Override
            public Integer apply(Domination input) {
                return input.hashCode();
            }
        });
    }

    public Set<String> validChoices() {
        if (validChoices == null) {
            validChoices = Sets.newHashSet(transform(dominations.values(), new Function<Domination, String>() {
                @Override
                public String apply(Domination input) {
                    return input.winner();
                }
            }));
        }
        return validChoices;
    }

    public Domination dominationFor(String choice1, String choice2) {
        if(!(validChoices().contains(choice1) && validChoices().contains(choice2))){
            throw new PreconditionFailure("invalid choices");
        }
        if(choice1.equals(choice2)){
            return new Domination(choice1,choice2,"<ties with>");
        }
        return firstAvailable(Domination.hashCode(choice1, choice2), Domination.hashCode(choice2, choice1));
    }

    private Domination firstAvailable(int key1, int key2) {
        return dominations.containsKey(key1) ? dominations.get(key1) : dominations.get(key2);
    }

    String winningChoice(String choice1, String choice2) {
        return dominationFor(choice1, choice2).winner();
    }

    public Result winner(Player player1, Player player2) {
        int player1Score = 0;
        int player2Score = 0;
        for (int i = 0; i < player1.rounds(); i++) {
            String winningChoice = winningChoice(player1.choices(i), player2.choices(i));
            if (player1.choices(i).equals(winningChoice)) {
                player1Score += 1;
            }
            if (player2.choices(i).equals(winningChoice)) {
                player2Score += 1;
            }
        }
        if (player1Score > player2Score) return new Result(player1);
        if (player2Score > player1Score) return new Result(player2);
        return new Result(player1, player2);//tie
    }

}

