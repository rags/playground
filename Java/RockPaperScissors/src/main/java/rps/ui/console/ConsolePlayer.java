package rps.ui.console;

import com.google.common.base.Joiner;
import rps.GameRules;
import rps.PlayerImpl;
import rps.StrategicPlayer;

import java.util.Scanner;

import static rps.ui.console.IO.in;
import static rps.ui.console.IO.prompt;

public class ConsolePlayer extends StrategicPlayer {

    public static final String SINGLE_PLAYER = "<you>";
    private GameRules rules;
    private final Scanner in;

    public ConsolePlayer(PlayerImpl playerImpl, GameRules rules, Scanner in) {
        super(playerImpl);
        this.rules = rules;
        this.in = in;
    }

    public ConsolePlayer(String name, GameRules rules) {
        this(new PlayerImpl(name), rules,in());
    }

    @Override
    public String chooseImpl() {
        prompt((singlePlayer() ? "": (name() + "'s turn, ")) +"enter one of [ " + Joiner.on(", ").join(rules.validChoices()) + " ]");
        return in.nextLine();
    }

    private boolean singlePlayer() {
        return SINGLE_PLAYER.equals(name());
    }

}
