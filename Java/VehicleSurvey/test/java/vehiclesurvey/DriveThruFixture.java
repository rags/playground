package vehiclesurvey;

import vehiclesurvey.time.Time;

import static vehiclesurvey.time.Time.time;

//Build DriveThru by only configuring fields (like speed,time) you care about and ignoring the rest (defaults are used for rest)
public class DriveThruFixture {
    int day = 1;
    Time time = time().hours(12);
    double speed = 60;
    Direction direction = Direction.North;

    private DriveThruFixture() {
    }

    public static DriveThruFixture aDriveThru() {
        return new DriveThruFixture();
    }

    public DriveThru build() {
        return new DriveThru(day, time, speed, direction);
    }

    public DriveThruFixture onDay(int day) {
        this.day = day;
        return this;
    }

    public DriveThruFixture atTime(int timeStamp) {
        return atTime(time(timeStamp));
    }

    public DriveThruFixture atTime(Time time) {
        this.time = time;
        return this;
    }

    public DriveThruFixture driveAt(double speed) {
        this.speed = speed;
        return this;
    }

    public DriveThruFixture heading(Direction direction) {
        this.direction = direction;
        return this;
    }


}
