package vehiclesurvey;

import com.google.common.base.Predicate;

public interface ScopedPredicate<T> extends Predicate<T> {
    Object scope();
}
