package vehiclesurvey.query;

import com.google.common.base.Function;
import com.google.common.base.Predicate;
import com.google.common.collect.Collections2;
import com.google.common.collect.ImmutableList;
import com.google.common.collect.Iterables;
import vehiclesurvey.ScopedPredicate;
import vehiclesurvey.query.func.Reducer;

import java.util.*;

import static com.google.common.collect.Collections2.filter;
import static com.google.common.collect.Collections2.transform;
import static com.google.common.collect.Iterables.addAll;
import static com.google.common.collect.Iterables.getFirst;
import static vehiclesurvey.query.func.Func.allMax;

class GroupOfQueryProcessors extends QueryProcessor<QueryProcessor> {
    public GroupOfQueryProcessors(Collection<QueryProcessor> items, Object tag) {
        super(items, tag);
    }

    public GroupOfQueryProcessors(Iterable<QueryProcessor> items, Object tag) {
        super(items, tag);
    }

    @Override
    protected boolean isCompositeOfComposites() {
        return isComposite() && (hasResult() && getFirst(results(),null).isComposite());
    }

    @Override
    protected boolean isComposite() {
        return true;
    }
}

public class QueryProcessor<T> implements Iterable<T>{
    private final static QueryProcessor NULL = new QueryProcessor(ImmutableList.of(),new Object());
    private Collection<T> items;
    private final Object scope;//Meant for identifying a group or data associated with it

    public QueryProcessor(Collection<T> items, Object scope) {
        this.items = items;
        this.scope = scope;
    }

    public QueryProcessor(Iterable<T> items, Object scope) {
        this(new ArrayList<T>(), scope);
        addAll(this.items, items);
    }

    public <T> T scope() {
        return (T)scope;
    }

    public <A,B> QueryProcessor map(final Function<A,B> mapper){
        if (isComposite()) { //composition. i.e, groupBy of groups
            return handleComposite(new Function<T, QueryProcessor>() {
                @Override
                public QueryProcessor apply(T input) {
                    return ((QueryProcessor) input).map(mapper);
                }
            });
        }
        return new QueryProcessor<B>(transform((Collection<A>) items, mapper), scope);
    }

    public <K> QueryProcessor where(final Predicate<K> predicate) {
        if (isComposite()) { //composition. i.e, groupBy of groups
            return handleComposite(new Function<T, QueryProcessor>() {
                @Override
                public QueryProcessor apply(T input) {
                    return ((QueryProcessor) input).where(predicate);
                }
            });
        }
        return new QueryProcessor<T>(filter(items, (Predicate<? super T>) predicate), scope);
    }

    public <K> QueryProcessor groupBy(final Predicates<K> predicates) {
        if (isComposite()) { //composition. i.e, groupBy of groups
            return handleComposite(new Function<T, QueryProcessor>() {
                @Override
                public QueryProcessor apply(T input) {
                    return ((QueryProcessor) input).groupBy(predicates);
                }
            });
        }

        return new GroupOfQueryProcessors(Iterables.transform(predicates, new Function<ScopedPredicate<K>, QueryProcessor>() {
            @Override
            public QueryProcessor apply(ScopedPredicate predicate) {
                return new QueryProcessor<T>(filter(items, predicate), predicate.scope());
            }
        }), scope);
    }

    public <A,B> QueryProcessor aggregate(final Function<A,B> function){
        if (isComposite()) { //composition. i.e, groupBy of groups
            return handleComposite(new Function<T, QueryProcessor>() {
                @Override
                public QueryProcessor apply(T input) {
                    return ((QueryProcessor) input).aggregate(function);
                }
            });
        }

        return new QueryProcessor(Collections.singleton(function.apply((A) results())), scope);
    }

    public <B> QueryProcessor aggregateAggregates(final Function<Iterable<QueryProcessor>,B> function){
        if (isCompositeOfComposites()) { //composition. i.e, groupBy of groups
            return handleComposite(new Function<T, QueryProcessor>() {
                @Override
                public QueryProcessor apply(T input) {
                    return ((QueryProcessor) input).aggregateAggregates(function);
                }
            });
        }

        return new QueryProcessor(Collections.singleton(function.apply((GroupOfQueryProcessors) this)), scope);
    }

    public QueryProcessor filterAggregates(final Function<Iterable<QueryProcessor>,Iterable<QueryProcessor>> function){
        if (isCompositeOfComposites()) { //composition. i.e, groupBy of groups
            return handleComposite(new Function<T, QueryProcessor>() {
                @Override
                public QueryProcessor apply(T input) {
                    return ((QueryProcessor) input).filterAggregates(function);
                }
            });
        }

        Iterable<QueryProcessor> apply = function.apply((GroupOfQueryProcessors) this);
        return new GroupOfQueryProcessors(apply, scope);

    }

    public QueryProcessor count() {
        return aggregate(new Function<Collection, Integer>() {
            @Override
            public Integer apply(Collection c) {
                return c.size();
            }
        });
    }


    public <A, B> QueryProcessor reduce(final Reducer<A, B> reducer, final B initialValue) {
        return aggregate(new Function<Collection<A>, B>() {
            @Override
            public B apply(Collection<A> c) {
                return Reducer.reduce(reducer, c, initialValue);
            }
        });
    }

    protected boolean isComposite() {
        return false;
    }

    protected boolean isCompositeOfComposites() {
        return false;
    }

    private QueryProcessor<QueryProcessor> handleComposite(Function<T, QueryProcessor> function) {
        return new GroupOfQueryProcessors(Collections2.transform(items, function), scope);
    }

    @Override
    public Iterator<T> iterator() {
        return results().iterator();
    }

    public Collection<T> results() {
        return items;
    }

    public boolean hasResult() {
        return !items.isEmpty();
    }

    public QueryProcessor resultFor(Object scope) {
        if(!isComposite()){
            return NULL;
        }
        for (T item : items) {
            QueryProcessor queryProcessor = (QueryProcessor) item;
            if(queryProcessor.scope().equals(scope)){
                return queryProcessor;
            }
        }
        return NULL;
    }

    public T scalarResult(){
        return getFirst(items,null);
    }
}

