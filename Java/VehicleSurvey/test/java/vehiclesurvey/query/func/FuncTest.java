package vehiclesurvey.query.func;

import com.google.common.base.Function;
import com.google.common.base.Functions;
import org.hamcrest.Matcher;
import org.hamcrest.Matchers;
import org.junit.Test;

import java.util.List;

import static java.util.Arrays.asList;
import static org.hamcrest.Matchers.*;
import static org.junit.Assert.assertThat;
import static vehiclesurvey.query.func.Func.*;

public class FuncTest {

    @Test
    public void shouldReturnMaxMinSimple() {
        assertThat(max(Functions.<Integer>identity(), asList(1, 5, 3, 4, 5)), is(5));
        assertThat(allMax(asList(1, 5, 3, 4, 5)), is(allOf(
                Matchers.<Integer>iterableWithSize(2),
                hasItems(5, 5))));
        assertThat(allMin(asList(1, 5, 3, 4, 5)), is(allOf(
                Matchers.<Integer>iterableWithSize(1),
                hasItems(1))));
    }

    @Test
    public void shouldReturnMinMaxWithComparators() {
        List<String> data = asList("one", "two", "three", "four", "five", "six", "seven");
        assertThat(min(stringLength(), data), is("one"));
        assertThat((List<String>)allMin(stringLength(), data),//Stupid compiler needs this cast. open jdk bug?
                is(allOf(Matchers.<String>iterableWithSize(3), hasItems("one", "two", "six"))));
        assertThat((List<String>)allMax(stringLength(), data),
                is(allOf(Matchers.<String>iterableWithSize(2), hasItems("three", "seven"))));
    }

    private Function<String, Comparable> stringLength() {
        return new Function<String, Comparable>() {
            @Override
            public Comparable apply(String input) {
                return input.length();
            }
        };
    }
}
