package rps;

import com.google.common.collect.Sets;
import org.junit.Test;

import java.util.Set;

import static org.hamcrest.Matchers.is;
import static org.junit.Assert.*;
import static rps.GamingInterface.*;

public class GameRulesTest {
    @Test
    public void shouldFindWinningMove() {
        GameRules gameRules = rockPaperScissors();
        assertThat(gameRules.winningChoice(ROCK, PAPER), is(PAPER));
        assertThat(gameRules.winningChoice(SCISSORS, PAPER), is(SCISSORS));
        assertThat(gameRules.winningChoice(SCISSORS, ROCK), is(ROCK));
    }

    @Test
    public void shouldProvideValidMoves() {
        assertThat(bearHunterNinja().validChoices(), is((Set<String>) Sets.newHashSet(BEAR, HUNTER, NINJA)));
    }


    @Test
    public void shouldAllowOnlyValidMoves() {
        try {
            bearHunterNinja().winningChoice(PAPER, HUNTER);
            fail("Should be an assertion error: Invalid choice Paper");
        } catch (PreconditionFailure e) {

        }
        try {
            bearHunterNinja().winningChoice(ROCK, SCISSORS);
            fail("Should be an assertion error: Invalid choice Rock,Scissors");
        } catch (PreconditionFailure e) {

        }
    }


    @Test
    public void shouldDecideWinnerInAMultiRoundGame() {
        GameRules gameRules = rockPaperScissorsLizardSpock();
        assertTrue(gameRules.winner(new PlayerImpl("foo"), new PlayerImpl("bar")).tie());
        assertTrue(gameRules.winner(new PlayerImpl("foo", LIZARD, SPOCK, SPOCK), new PlayerImpl("bar", LIZARD, SPOCK, SPOCK)).tie());

    }

}
