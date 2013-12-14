package rps;

import java.util.Random;

public class RandomizedBot extends StrategicPlayer {
    private final Random random;
    private String[] choices;

    public RandomizedBot(GameRules rules) {
        super(new PlayerImpl("<random bot>"));
        this.choices = rules.validChoices().toArray(new String[0]);
        random = new Random();

    }

    @Override
    public String chooseImpl() {
        return choices[random.nextInt(choices.length)];
    }
}
