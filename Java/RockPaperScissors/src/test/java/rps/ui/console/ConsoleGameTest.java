package rps.ui.console;

import com.google.common.base.Joiner;
import org.junit.Test;
import rps.Result;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.PrintStream;

import static org.hamcrest.Matchers.allOf;
import static org.hamcrest.Matchers.containsString;
import static org.hamcrest.Matchers.is;
import static org.junit.Assert.assertThat;
import static rps.GamingInterface.*;
import static rps.ui.console.ConsoleGame.aConsoleGame;
import static rps.ui.console.ConsolePlayerBuilder.namedConsolePlayer;

public class ConsoleGameTest extends ConsoleTest {


    @Test
    public void shouldConstructConsoleGame() throws IOException {
        ByteArrayInputStream in = new ByteArrayInputStream(Joiner.on('\n').join(
                "Foo", "Bar", BEAR, BEAR, HUNTER, BEAR
        ).getBytes());
        System.setIn(in);

        Result result = aConsoleGame().withPlayers(namedConsolePlayer(), namedConsolePlayer()).tillSomeoneWins().withRules(bearHunterNinja()).play();
        assertThat(result.winner().name(), is("Foo"));
        assertThat(result.winner().rounds(), is(2));
    }

    @Test
    public void shouldPlayBestOf5ConsoleGame_EndtoEndTest() throws IOException {
        ByteArrayInputStream in = new ByteArrayInputStream(Joiner.on('\n').join(
                "2\n1\n3","Foo", "Bar", ROCK,SPOCK,SCISSORS,LIZARD,SPOCK,PAPER,SPOCK,SPOCK,LIZARD,ROCK,"Exit"
        ).getBytes());
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        System.setIn(in);
        System.setOut(new PrintStream(out));//comment this line to view output for debugging
        ConsoleGame.main();
        assertThat(out.toString(), allOf(
                containsString("The winner is: Bar"),
                containsString("Foo vs Bar [ 5 round(s) ]"),
                containsString("1. Spock vaporizes Rock"),
                containsString("2. Scissors decapitates Lizard"),
                containsString("3. Paper disproves Spock"),
                containsString("4. Spock <ties with> Spock"),
                containsString("5. Rock crushes Lizard")
                )
        );
    }

}
