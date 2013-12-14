package rps;


import com.google.common.base.Function;

import static com.google.common.collect.ObjectArrays.concat;

public class GamingInterface<T extends Game> {
    public static final String ROCK = "Rock";
    public static final String PAPER = "Paper";
    public static final String SCISSORS = "Scissors";
    public static final String LIZARD = "Lizard";
    public static final String SPOCK = "Spock";
    public static final String BEAR = "Bear";
    public static final String HUNTER = "Hunter";
    public static final String NINJA = "Ninja";

    //alias to avoid ugly < > and code more readable
    public interface PlayerBuilder extends Function<GamingInterface, StrategicPlayer> {
    }

    private GameRules rules;

    private GameStrategy strategy;
    private StrategicPlayer player2;
    private StrategicPlayer player1;
    private PlayerBuilder player1Builder;
    private PlayerBuilder player2Builder;
    private Class<T> gameClass;

    public GamingInterface(Class<T> gameClass) {
        this.gameClass = gameClass;
    }

    public GameRules rules() {
        return rules;
    }

    public static GamingInterface aGame() {
        return new GamingInterface(Game.class);
    }


    public GamingInterface withRules(GameRules rules) {
        this.rules = rules;
        return this;
    }

    public GamingInterface tillSomeoneWins() {
        this.strategy = new TieBreakerStrategy();
        return this;
    }

    public GamingInterface bestOf(int nthrows) {
        this.strategy = new BestOfStrategy(nthrows);
        return this;
    }

    public GamingInterface withPlayers(PlayerBuilder player1, PlayerBuilder player2) {
        this.player1Builder = player1;
        this.player2Builder = player2;
        return this;
    }

    public GamingInterface withPlayers(StrategicPlayer player1, StrategicPlayer player2) {
        this.player1 = player1;
        this.player2 = player2;
        return this;
    }

    public Result play() {
        //invariant/precondition for the method
        if (gameClass == null ||  rules == null || strategy == null) {
            throw new PreconditionFailure("Make sure withRules and one of bestOf/tillSomeoneWins is called before play");
        }
        if((player1Builder == null || player2Builder == null) && (player1==null || player1==null)){
            throw new PreconditionFailure("Make sure withPlayers is called before play");
        }
        try {
            StrategicPlayer p1 = null, p2 = null;
            if (player1 != null && player2 != null) {
                p1 = player1;
                p2 = player2;
            } else {
                p1 = player1Builder.apply(this);
                p2 = player2Builder.apply(this);

            }

            return ((T) gameClass.getDeclaredConstructors()[0]
                    .newInstance(p1, p2, this.rules, this.strategy)).play();

        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }


    public static PlayerBuilder aPlayer(final StrategicPlayer player) {
        return new PlayerBuilder() {
            @Override
            public StrategicPlayer apply(GamingInterface input) {
                return player;
            }
        };
    }

    public static PlayerBuilder aRandomBot() {
        return new PlayerBuilder() {
            @Override
            public StrategicPlayer apply(GamingInterface input) {
                return new RandomizedBot(input.rules);
            }
        };
    }

    public static GameRules rockPaperScissors() {
        return new GameRules(rsp());
    }

    public static GameRules bearHunterNinja() {
        return new GameRules(
                new Domination(BEAR, NINJA, "eats"),
                new Domination(NINJA, HUNTER, "kills"),
                new Domination(HUNTER, BEAR, "shoots"));
    }

    public static GameRules rockPaperScissorsLizardSpock() {
        return new GameRules(concat(rsp(), new Domination[]{
                new Domination(ROCK, LIZARD, "crushes"),
                new Domination(LIZARD, SPOCK, "poisons"),
                new Domination(SPOCK, SCISSORS, "smashes"),
                new Domination(SCISSORS, LIZARD, "decapitates"),
                new Domination(LIZARD, PAPER, "eats"),
                new Domination(PAPER, SPOCK, "disproves"),
                new Domination(SPOCK, ROCK, "vaporizes"),
        }, Domination.class));
    }

    private static Domination[] rsp() {
        return new Domination[]{
                new Domination(SCISSORS, PAPER, "cuts"),
                new Domination(ROCK, SCISSORS, "breaks"),
                new Domination(PAPER, ROCK, "covers")};
    }


}
