package vehiclesurvey.query;

import java.util.Collection;

public interface Query<T> {
    public QueryProcessor execute(Collection<T> data);
}
