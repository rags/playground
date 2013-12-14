package rps.ui.console;

import rps.GameRules;
import rps.GamingInterface;
import rps.StrategicPlayer;

import static rps.ui.console.IO.prompt;

public class ConsolePlayerBuilder{

    public static GamingInterface.PlayerBuilder namedConsolePlayer() {
        return new GamingInterface.PlayerBuilder(){
            @Override
            public StrategicPlayer apply(rps.GamingInterface input) {
                return new ConsolePlayer(prompt("Enter player's name").nextLine(), input.rules());
            }
        };
    }

    public static GamingInterface.PlayerBuilder aConsolePlayer() {
        return new GamingInterface.PlayerBuilder(){
            @Override
            public StrategicPlayer apply(rps.GamingInterface input) {
                return aConsolePlayer(input.rules());
            }
        };
    }

    public static ConsolePlayer aConsolePlayer(GameRules rules) {
        return new ConsolePlayer(ConsolePlayer.SINGLE_PLAYER, rules);
    }
}
