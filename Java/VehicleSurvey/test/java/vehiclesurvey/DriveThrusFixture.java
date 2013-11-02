package vehiclesurvey;

import static java.util.Arrays.asList;

public class DriveThrusFixture {
    public static DriveThruList driveThrus(final DriveThru... driveThrus) {
        return new DriveThruList() {{
            addAll(asList(driveThrus));
        }};
    }
}
