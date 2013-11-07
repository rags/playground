package vehiclesurvey.query;

import com.google.common.base.Function;
import com.google.common.base.Predicate;
import vehiclesurvey.ScopedPredicate;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.concurrent.Executor;

import static vehiclesurvey.query.func.Func.avg;

public class QueryImpl<T> implements Query<T> {
    private List<Predicates<T>> groupByList;
    private List<Predicate<T>> whereList;

    public QueryImpl() {
        groupByList = new ArrayList<Predicates<T>>();
        whereList = new ArrayList<Predicate<T>>();
    }

    public static <T> QueryImpl<T> select(Class<T> _) {
        return select();
    }

    public static <T> QueryImpl<T> select() {
        return new QueryImpl<T>();
    }

    public QueryImpl<T> groupBy(Predicates<T> predicates) {
        return addToList(groupByList, predicates);
    }

    public QueryImpl<T> where(Predicate<T> predicate) {
        return addToList(whereList, predicate);
    }

    private <K> QueryImpl addToList(List<K> list, K item) {
        list.add(item);
        return this;
    }

    public Query<T> count() {
        return new Query<T>() {
            @Override
            public QueryProcessor execute(Collection<T> data) {
                return QueryImpl.this.execute(data).count();
            }
        };
    }

    public Query<T> countAvg() {
        return new Query<T>() {
            @Override
            public QueryProcessor execute(Collection<T> data) {
                return QueryImpl.this.execute(data).count().aggregateAggregates(aggregateAvg());
            }
        };
    }

    public static Function<Iterable<QueryProcessor<Number>>, Double> aggregateAvg() {
        return new Function<Iterable<QueryProcessor<Number>>, Double>() {
            @Override
            public Double apply(Iterable<QueryProcessor<Number>> input) {
                return avg(new Function<QueryProcessor<Number>, Double>() {

                    @Override
                    public Double apply(QueryProcessor<Number> queryProcessor) {
                        return queryProcessor.scalarResult().doubleValue();
                    }
                }, input);
            }
        };
    }

    @Override
    public QueryProcessor execute(Collection<T> data) {
        QueryProcessor queryProcessor = new QueryProcessor(data, "Count query");
        for (Predicate<T> where : whereList) {
            queryProcessor = queryProcessor.where(where);
        }
        for (Predicates<T> predicates : groupByList) {
            queryProcessor = queryProcessor.groupBy(predicates);
        }
        return queryProcessor;
    }

    public Query<T> aggregate(final Function function) {
        return new Query<T>() {
            @Override
            public QueryProcessor execute(Collection<T> data) {
                return QueryImpl.this.execute(data).aggregate(function);
            }
        };
    }
}











