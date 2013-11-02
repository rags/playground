package vehiclesurvey.query;

import com.google.common.base.Function;
import com.google.common.base.Predicate;
import com.google.common.collect.Collections2;
import com.google.common.collect.Iterables;
import vehiclesurvey.query.func.Reducer;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.Iterator;

import static com.google.common.collect.Collections2.filter;
import static com.google.common.collect.Iterables.addAll;
import static com.google.common.collect.Iterables.getFirst;

class GroupOfGroups extends Group<Group>{
    public GroupOfGroups(Collection<Group> items, String tag) {
        super(items, tag);
    }

    public GroupOfGroups(Iterable<Group> items, String tag) {
        super(items, tag);
    }

    @Override
    protected boolean isComposite() {
        return true;
    }
}

public class Group<T> implements Iterable<T>{
    private Collection<T> items;
    private final String tag;//Meant for identifying a group (Optional)

    public Group(Collection<T> items, String tag) {
        this.items = items;
        this.tag = tag;
    }

    public Group(Iterable<T> items, String tag) {
        this(new ArrayList<T>(), tag);
        addAll(this.items, items);
    }

    public String tag() {
        return tag;
    }

    private Collection<T> items() {
        return items;
    }

    public <K> Group group(final Predicates<K> predicates) {
        if (isComposite()) { //composition. i.e, group of groups
            return handleComposite(new Function<T, Group>() {
                @Override
                public Group apply(T input) {
                    return ((Group) input).group(predicates);
                }
            });
        }

        return new GroupOfGroups(Iterables.transform(predicates, new Function<Predicate<K>, Group>() {
            @Override
            public Group apply(Predicate predicate) {
                return new Group<T>(filter(items, predicate), predicate.toString());
            }
        }), tag);
    }

    public <A,B> Group aggregate(final Function<A,B> function){
        if (isComposite()) { //composition. i.e, group of groups
            return handleComposite(new Function<T, Group>() {
                @Override
                public Group apply(T input) {
                    return ((Group) input).aggregate(function);
                }
            });
        }

        return new Group(Collections.singleton(function.apply((A)items())),tag);

    }

    public Group count() {
        return aggregate(new Function<Collection, Integer>() {
            @Override
            public Integer apply(Collection c) {
                return c.size();
            }
        });
    }

    public <A, B> Group reduce(final Reducer<A, B> reducer, final B initialValue) {
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

    private Group<Group> handleComposite(Function<T, Group> function) {
        return new GroupOfGroups(Collections2.transform(items, function), tag);
    }

    @Override
    public Iterator<T> iterator() {
        return items().iterator();
    }

    public T scalarResult(){
        return getFirst(items,null);
    }
}

