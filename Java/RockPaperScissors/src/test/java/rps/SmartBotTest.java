package rps;

import com.google.common.base.Joiner;
import org.junit.Test;
import rps.ui.console.ConsolePlayer;

import java.io.IOException;
import java.util.Scanner;

import static junit.framework.Assert.assertFalse;
import static junit.framework.Assert.assertTrue;
import static org.hamcrest.Matchers.is;
import static org.hamcrest.Matchers.isOneOf;
import static org.junit.Assert.assertThat;
import static rps.GamingInterface.*;


public class SmartBotTest {
    @Test
    public void shouldFindTheBestMove() {
        SmartBot smartBot = new SmartBot(new PlayerImpl("blahOpponent", BEAR, HUNTER, BEAR, BEAR, NINJA, NINJA), bearHunterNinja());
        assertThat(smartBot.chooseImpl(), is(BEAR)); //bear draws with bear (highest count) and kills ninja (2nd highest count)
    }

    @Test
    public void shouldFindBestMoveForMultipleBestMoves() {
        /*
        opponent counts: 4 = Spock
                         2 = Lizard
                         1 = Paper
                         1 = Rock
                         1 = Scissors
                         best throw is Lizard -> poison Spock, ties with Lizard, eats Paper
        */
        assertThat(new SmartBot(new PlayerImpl("blahOpponent", ROCK, PAPER, SCISSORS, SPOCK, SPOCK, LIZARD, SPOCK, SPOCK, LIZARD), rockPaperScissorsLizardSpock()).chooseImpl(), is(LIZARD));


        /*
        opponent counts: 4 = Spock
                         2 = Lizard
                         2 = Rock
                         1 = Paper
                         1 = Scissors
                         best throws are
                                 Spock -> ties with Spock, vaporizes rock
                                 Paper -> disproves Spock, covers rock
                         non agressive picks one at random
                         for aggresive startegy best throw is Paper
        */
        PlayerImpl blahOpponent = new PlayerImpl("blahOpponent", ROCK, PAPER, SCISSORS, SPOCK, SPOCK, LIZARD, SPOCK, SPOCK, LIZARD, ROCK);
        assertThat(new SmartBot(blahOpponent, rockPaperScissorsLizardSpock()).chooseImpl(), isOneOf(SPOCK, PAPER));
        assertThat(new SmartBot(blahOpponent, rockPaperScissorsLizardSpock(), true).chooseImpl(), is(PAPER));
    }


    @Test
    public void aggresiveSmartBotShouldWinAgainstPredicatablePlayer() throws IOException {
        String[] preditablePlayerInputs = {ROCK, PAPER, SCISSORS};
        for (int i = 0; i < preditablePlayerInputs.length; i++) {
            ConsolePlayer naivePlayer = consolePlayer("foo", preditablePlayerInputs[i], preditablePlayerInputs[i], preditablePlayerInputs[i], preditablePlayerInputs[i], preditablePlayerInputs[i]);
            Result result = aGame().withRules(rockPaperScissors()).withPlayers(naivePlayer, new SmartBot(naivePlayer, rockPaperScissors(), true)).bestOf(5).play();
            assertFalse(result.tie());
            assertTrue(result.winner() instanceof SmartBot);
        }
    }

    @Test
    public void shouldFairWellAgainstPavlov() throws IOException {
        for (int i = 0; i < 3; i++) {
            int N = 5 * (i + 1);
            ConsolePlayer naivePlayer = consolePlayer("foo", rockPaper(N));
            SmartBot smartBot = new SmartBot(naivePlayer, rockPaperScissors());
            Result result = aGame().withRules(rockPaperScissors()).withPlayers(naivePlayer, smartBot).bestOf(N).play();
            assertFalse(result.tie());
            assertTrue(result.winner() instanceof SmartBot);
        }
    }

    private String[] rockPaper(int n) {
        String[] list = new String[n];
        String[] choices = {ROCK, PAPER};
        for (int i = 0; i < list.length; i++) {
            list[i] = choices[i % 2];
        }
        return list;
    }

    public ConsolePlayer consolePlayer(String name, String... choices) throws IOException {
        return new ConsolePlayer(new PlayerImpl(name), rockPaperScissors(), new Scanner(Joiner.on("\n").join(choices)));
    }
}

