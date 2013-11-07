package vehiclesurvey.query.func;

import com.google.common.base.Function;
import com.google.common.base.Functions;

import java.util.ArrayList;
import java.util.List;

import static com.google.common.collect.Iterables.getFirst;
import static com.google.common.collect.Iterables.size;
import static vehiclesurvey.query.func.Reducer.reduce;

public class Func {
    //mutable version of asList()
    public static <T> List<T> mutableList(final T... items){
        return new ArrayList<T>(){{
            for (T item : items) {
                add(item);
            }
        }};
    }

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

    public static <T,K extends Comparable<K>> T min(final Function<T, K> f, Iterable<T> collection) {
        return getFirst(allMin(f, collection),null);
    }

    public static  <T,K extends Comparable<K>> T max(final Function<T, K> f, Iterable<T> collection) {
        return getFirst(allMax(f, collection), null);
    }

    public static <T extends Comparable<T>> List<T> allMin(Iterable<T> collection) {
        return allMin(Functions.<T>identity(), collection);
    }

    public static <T extends Comparable<T>> List<T> allMax(Iterable<T> collection) {
        return allMax(Functions.<T>identity(), collection);
    }
    //collect all item where the value of item = MIN
    public static <T,K extends Comparable<K>> List<T> allMin(final Function<T, K> f, Iterable<T> collection) {
        return reduce(new Reducer<T, List<T>>() {
            @Override
            public List<T> apply(T item, List<T> accumulator) {
                if (accumulator == null) {
                    return mutableList(item);
                }
                return accumulate(item, accumulator, f.apply(accumulator.get(0)).compareTo(f.apply(item)));
            }
        }, collection, null);
    }

    public static  <T,K extends Comparable<K>> List<T> allMax(final Function<T, K> f, Iterable<T> collection) {
        return reduce(new Reducer<T, List<T>>() {
            @Override
            public List<T> apply(T item, List<T> accumulator) {
                if (accumulator==null){
                    return mutableList(item);
                }
                return accumulate(item, accumulator, f.apply(item).compareTo(f.apply(accumulator.get(0))));
            }
        }, collection, null);
    }

    private static <T> List<T> accumulate(T item, List<T> accumulator, int cmp) {
        if(cmp>0){
            return mutableList(item);
        }
        if(0 == cmp){
            accumulator.add(item);
        }
        return accumulator;
    }

}
