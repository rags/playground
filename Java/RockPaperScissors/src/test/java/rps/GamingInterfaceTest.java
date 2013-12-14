package rps;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.io.InputStream;

import static junit.framework.Assert.fail;
import static org.hamcrest.Matchers.containsString;
import static org.junit.Assert.assertThat;
import static rps.GamingInterface.*;

public class GamingInterfaceTest {

    @Test
    public void shouldBuildOnlyWhenAllParamsPresent() {
        try {
            aGame().withPlayers(aRandomBot(), aRandomBot()).play();
            fail("Should throw exception");
        } catch (PreconditionFailure e) {
            assertThat(e.getMessage(), containsString("Make sure withRules and one of bestOf/tillSomeoneWins is called before play"));
        }

        try {
            aGame().withPlayers(aRandomBot(), aRandomBot()).tillSomeoneWins().play();
            fail("Should throw exception");
        } catch (PreconditionFailure e) {
            assertThat(e.getMessage(), containsString("Make sure withRules and one of bestOf/tillSomeoneWins is called before play"));
        }

        try {
            aGame().tillSomeoneWins().withRules(rockPaperScissors()).play();
            fail("Should throw exception");
        } catch (PreconditionFailure e) {
            assertThat(e.getMessage(), containsString("Make sure withPlayers is called before play"));
        }

    }


}
