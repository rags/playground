package vehiclesurvey.query.func;

import com.google.common.base.Function;
import vehiclesurvey.DriveThru;

import java.util.Collection;

import static com.google.common.collect.Iterables.size;
import static vehiclesurvey.query.func.Reducer.reduce;

public class Func {
    public static <T> Double sum(final Function<T, Double> f, Iterable<T> iterable) {
        return reduce(new Reducer<T, Double>() {
            @Override
            public Double apply(T item, Double accumulator) {

                return accumulator + f.apply(item);
            }
        }, iterable, 0d);
    }

    public static <T> Double avg(final Function<T, Double> f, Iterable<T> iterable) {
        int size = size(iterable);
        return size==0? 0 : sum(f, iterable) / size;
    }
}
