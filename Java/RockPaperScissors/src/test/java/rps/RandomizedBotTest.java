package rps;

import com.google.common.collect.HashMultiset;
import org.junit.Test;

import static org.hamcrest.Matchers.*;
import static org.junit.Assert.assertThat;

public class RandomizedBotTest {
    @Test
    public void shouldRandomizeChoices() {
        GameRules rules = GamingInterface.rockPaperScissorsLizardSpock();
        RandomizedBot player = new RandomizedBot(rules);
        int N = 1000;
        for (int i = 0; i < N; i++) {
            player.choose();
        }

        HashMultiset<String> counts = HashMultiset.create();
        for (int i = 0; i < N; i++) {
            counts.add(player.choices(i));
        }
        for (String choice : rules.validChoices()) {
            assertThat(counts.count(choice), allOf(is(greaterThan(150)), is(lessThan(250))));
        }

    }
}
