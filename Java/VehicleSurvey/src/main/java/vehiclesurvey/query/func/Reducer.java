package vehiclesurvey.query.func;

import java.util.Iterator;

public abstract class Reducer<A, B> {
    public abstract B apply(A item, B accumulator);

    //homogenous reduce where results and iterable type match. Ex: sum,min,max...
    public static <T> T reduce(Reducer<T, T> reducer, Iterable<T> items) {
        Iterator<T> iterator = items.iterator();
        if (!iterator.hasNext()) {
            throw new RuntimeException("Cant reduce on empty iterator. Use overload with initial value instead");
        }
        T next = iterator.next();
        return reduce(reducer, iterator, next);
    }

    public static <A, B> B reduce(Reducer<A, B> reducer, Iterable<A> items, B initialValue) {
        return reduce(reducer, items.iterator(), initialValue);
    }

    public static <A, B> B reduce(Reducer<A, B> reducer, Iterator<A> items, B initialValue) {
        while (items.hasNext()) {
            A next = items.next();
            initialValue = reducer.apply(next, initialValue);

        }
        return initialValue;
    }
}
