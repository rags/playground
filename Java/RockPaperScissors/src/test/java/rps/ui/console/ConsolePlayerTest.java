package rps.ui.console;

import org.junit.Test;
import rps.GamingInterface;
import rps.PlayerImpl;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static org.hamcrest.Matchers.*;
import static org.junit.Assert.assertThat;
import static rps.GamingInterface.*;
import static rps.ui.console.IO.in;

public class ConsolePlayerTest extends ConsoleTest{
    @Test
    public void shouldIO() throws Exception {
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        System.setOut(new PrintStream(out));
        System.setIn(new ByteArrayInputStream((ROCK + "\n").getBytes()));
        ConsolePlayer player1 = new ConsolePlayer(new PlayerImpl("player1"),
                GamingInterface.rockPaperScissors(), in());
        player1.choose();
        assertThat(player1.rounds(), is(1));
        assertThat(player1.choices(0), is(ROCK));
        assertThat(out.toString(), allOf(containsString("player1"), containsString(ROCK), containsString(PAPER), containsString(SCISSORS)));

    }
}
