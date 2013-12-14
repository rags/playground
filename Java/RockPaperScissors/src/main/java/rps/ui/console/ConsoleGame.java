package rps.ui.console;

import com.google.common.collect.ImmutableMap;
import rps.*;

import java.util.Map;

import static com.google.common.base.Strings.repeat;
import static rps.GamingInterface.*;
import static rps.ui.console.ConsolePlayerBuilder.aConsolePlayer;
import static rps.ui.console.ConsolePlayerBuilder.namedConsolePlayer;
import static rps.ui.console.IO.*;

public class ConsoleGame extends Game {
    public ConsoleGame(StrategicPlayer player1, StrategicPlayer player2, GameRules rules, GameStrategy strategy) {
        super(player1, player2, rules, strategy);
    }

    @Override
    public Result play() {
        Result result = super.play();
        out().println("\n"+player1.name() + " vs " + player2.name() + " [ " + player1.rounds() + " round(s) ]");
        for (int i = 0; i < player1.rounds(); i++) {
            out().println((i + 1) + ". " + rules.dominationFor(player1.choices(i), player2.choices(i)).toString());
        }
        out().println(repeat("-", 40));
        if (result.tie()) {
            out().println("Its a TIE");
        } else {
            out().println("The winner is: " + result.winner().name());
        }
        out().println("\n-- End of game --\n");
        return result;
    }

    public static GamingInterface aConsoleGame() {
        return new GamingInterface(ConsoleGame.class);
    }


    static final Map<Integer, GameRules> RULES = ImmutableMap.of(1, rockPaperScissors(), 2, rockPaperScissorsLizardSpock(), 3, bearHunterNinja());

    public static void main(String... args) {
        //Runtime.getRuntime().addShutdownHook(Thread.currentThread());
        for (; ; ) {
            out().println("\n-- New game --\n");
            GamingInterface gamingInterface = aConsoleGame();
            if(!prompt("1. Rock-Paper-Scissors 2. Rock-Paper-Scissors-Lizard-Spock 3. Bear-Hunter-Ninja <Any other Key>. Exit. Enter[ 1/2/3/... ]").hasNextInt()){
                out().println("DONE");
                return;
            }
            gamingInterface.withRules(RULES.get(in().nextInt()));
            if(!prompt("1. Multiplayer 2. You vs Random Bot 3. You vs Smart Bot. Enter [ 1/2/3 ]").hasNextInt()){
                out().println("Need input [ 1/2 ]");
                return;
            }
            switch (in().nextInt()) {
                case 1:
                    gamingInterface.withPlayers(namedConsolePlayer(), namedConsolePlayer());
                    break;
                case 2:
                    gamingInterface.withPlayers(aConsolePlayer(), aRandomBot());
                    break;
                case 3:
                    StrategicPlayer player1 = aConsolePlayer(gamingInterface.rules());
                    gamingInterface.withPlayers(player1, new SmartBot(player1, gamingInterface.rules()));
                    break;
                default:
                    out().println("Need input [ 1/2 ]");
                    return;
            }
            if(!prompt("Enter: 1. To play till someone wins 2. Best of three 3. Best of five. Enter [ 1/2/3 ]").hasNextInt()){
                out().println("Need input [ 1/2/3 ]");
                return;
            }
            switch (in().nextInt()) {
                case 1:
                    gamingInterface.tillSomeoneWins();
                    break;
                case 2:
                    gamingInterface.bestOf(3);
                    break;
                case 3:
                    gamingInterface.bestOf(5);
                    break;
                default:

                    out().println("Need input [ 1/2/3 ]");
                    return;
            }
            in().nextLine();
            out().println("Note that all inputs are case sensitive");
            gamingInterface.play();
            out().println("[At any point press CTRL-C to exit]\n");
        }
    }

}
