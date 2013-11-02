package vehiclesurvey.query;

import org.junit.Test;
import vehiclesurvey.query.func.Reducer;

import static java.util.Arrays.asList;
import static org.hamcrest.CoreMatchers.containsString;
import static org.hamcrest.CoreMatchers.is;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.junit.Assert.fail;
import static vehiclesurvey.query.func.Reducer.reduce;

public class ReducerTest {
    @Test
    public void shouldSum() {
        assertThat(reduce(new Reducer<Integer, Integer>() {
            @Override
            public Integer apply(Integer item, Integer accumulator) {
                return item + accumulator;
            }
        }, asList(1, 2, 3, 4, 5)), is(15));
    }

    @Test
    public void shouldHandleEmptyIterables() {
        try {
            reduce(null, asList());
            fail("Should throw exception");
        } catch (Exception e) {
            assertThat(e.getMessage(), containsString("Use overload"));
        }
        assertThat(reduce(null, asList(), 23), is(23));
    }

    @Test
    public void shouldAccumulateStringsInABuffer() {
        assertThat(reduce(new Reducer<String, StringBuilder>() {
            @Override
            public StringBuilder apply(String item, StringBuilder accumulator) {
                accumulator.append(item);
                return accumulator;
            }
        }, asList("item1", "item2", "item3"), new StringBuilder()).toString(), is("item1item2item3"));
    }
}
