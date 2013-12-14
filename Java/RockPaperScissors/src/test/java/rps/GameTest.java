package rps;

import com.google.common.base.Joiner;
import org.junit.Test;
import rps.ui.console.ConsolePlayer;
import rps.ui.console.ConsoleTest;
import rps.ui.console.IO;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.util.Scanner;

import static org.hamcrest.Matchers.*;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertThat;
import static org.junit.Assert.assertTrue;
import static rps.GamingInterface.*;

public class GameTest extends ConsoleTest{
    GameRules rockPaperScissorsLizardSpock = rockPaperScissorsLizardSpock();

    @Test
    public void shouldPlayBestOf3() throws IOException {
        ConsolePlayer player1 = consolePlayer("blahName1", ROCK, ROCK, ROCK);
        Result result = aGame().withPlayers(
                aPlayer(player1),
                aPlayer(consolePlayer("blahName1",ROCK,PAPER,SCISSORS))).bestOf(3).withRules(rockPaperScissors()).play();
        assertTrue(result.tie());
        assertThat(player1.rounds(),is(3));
    }

    @Test
    public void shouldContinueTillTiesAreBroken() throws IOException {
        ConsolePlayer player1 = consolePlayer("blahName1", ROCK, ROCK, ROCK);
        ConsolePlayer player2 = consolePlayer("blahName2", ROCK, PAPER, SCISSORS);
        Result result = aGame().withPlayers(aPlayer(player1), aPlayer(player2)).withRules(rockPaperScissors()).tillSomeoneWins().play();
        assertThat(result.winner(), is((Player) player2));
        assertThat(2, allOf(is(player1.rounds()),is(player2.rounds())));
    }

    @Test
    public void shouldPlayTillSomebotWins(){
        for (int i = 0; i < 3; i++) {
            Result result = aGame().withRules(rockPaperScissorsLizardSpock).withPlayers(aRandomBot(), aRandomBot()).tillSomeoneWins().play();
            assertFalse(result.tie());
            assertThat(result.winner().rounds(),is(greaterThanOrEqualTo(1)));
        }
    }

    public ConsolePlayer consolePlayer(String name,String... choices) throws IOException {
        return new ConsolePlayer(new PlayerImpl(name), rockPaperScissorsLizardSpock, new Scanner(Joiner.on("\n").join(choices)));
    }
}


