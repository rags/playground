package vehiclesurvey;

import vehiclesurvey.time.Time;

import java.util.ArrayList;
import java.util.Collection;

import static com.google.common.collect.Iterables.getLast;

public class DriveThruList extends ArrayList<DriveThru> {
    public DriveThruList(Collection<DriveThru> driveThrus) {
        super(driveThrus);
    }

    public DriveThruList() {
    }

    public int lastDay() {
        return getLast(this).day;
    }

    public double avgDistanceBetweenCars(){
        if (size()<2){
            return 0;
        }
        double distances = 0;
        for (int i = 1; i < this.size(); i++) {
            distances += get(i).timeDifference(get(i-1)).millis() * (avgSpeedFor(i) / Time.HOUR);
        }
        return distances/(size()-1);
    }

    private Double avgSpeedFor(int i) {
        return DriveThru.AVG_SPEED_KMPH; //60KMPH
        //return get(i).speed(); //actual recorded speed is more useful when intervals between cars are small
    }
}
