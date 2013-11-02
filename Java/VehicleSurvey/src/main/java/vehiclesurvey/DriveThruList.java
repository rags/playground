package vehiclesurvey;

import com.google.common.base.Function;
import vehiclesurvey.query.func.Reducer;

import java.util.ArrayList;

import static com.google.common.collect.Iterables.getLast;
import static vehiclesurvey.query.func.Reducer.reduce;

public class DriveThruList extends ArrayList<DriveThru> {
    public int lastDay() {
        return getLast(this).day;
    }

    public Double min(final Function<DriveThru, Double> f) {
        return reduce(new Reducer<DriveThru, Double>() {
            @Override
            public Double apply(DriveThru item, Double accumulator) {

                return Math.min(accumulator, f.apply(item));
            }
        }, this, Double.MAX_VALUE);
    }

    public Double max(final Function<DriveThru, Double> f) {
        return reduce(new Reducer<DriveThru, Double>() {
            @Override
            public Double apply(DriveThru item, Double accumulator) {

                return Math.max(accumulator, f.apply(item));
            }
        }, this, Double.MIN_VALUE);
    }



}
