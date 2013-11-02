package vehiclesurvey;

import com.google.common.io.Files;
import org.junit.Before;
import org.junit.Test;

import java.io.File;
import java.io.IOException;
import java.nio.charset.Charset;

import static org.hamcrest.collection.IsCollectionWithSize.hasSize;
import static org.hamcrest.core.IsCollectionContaining.hasItem;
import static org.hamcrest.core.IsCollectionContaining.hasItems;
import static org.junit.Assert.assertThat;
import static vehiclesurvey.DriveThruMatcher.someDriveThru;

public class DriveThroughScannerTest {

    private File tempDir;
    private DriveThroughScanner driveThroughScanner;

    @Before
    public void setUp() throws Exception {
        tempDir = Files.createTempDir();
        driveThroughScanner = new DriveThroughScanner();
    }

    @Test
    public void shouldCreateDriveThroughsFromLog() {
        DriveThruList driveThrus = sampleLog();
        assertThat(driveThrus, hasSize(3));
        assertThat(driveThrus, hasItems(someDriveThru().atTime(268981), someDriveThru().atTime(604957), someDriveThru().atTime(1089807)));

    }

    @Test
    public void shouldIncrementDays() {
        DriveThruList driveThrus = sampleLogAcrossDays();
        assertThat(driveThrus, hasSize(2));
        assertThat(driveThrus, hasItems(someDriveThru().onDay(1).atTime(86328771), someDriveThru().onDay(2)));
    }

    @Test
    public void shouldCalulateCorrectSpeed() {
        DriveThruList driveThrus = sampleLog();
        assertThat(driveThrus, hasItem(someDriveThru().atTime(268981).withSpeed(speedFor(269123, 268981))));
        assertThat(driveThrus, hasItems(
                someDriveThru().withSpeed(avg(speedFor(605128, 604957), speedFor(605132, 604960))),
                someDriveThru().withSpeed(avg(speedFor(1089948, 1089807), speedFor(1089951, 1089810)))));
    }

    private double avg(double val1, double val2) {
        return (val1 + val2) / 2;
    }

    private double speedFor(int time2, int time1) { //independently recalculate speed in tests
        return 2.5 / (time2 - time1) * 1000 * 60 * 60 / 1000;
    }

    private DriveThruList sampleLog() {
        return getDriveThrusFor("A268981\n" +
                "A269123\n" +
                "A604957\n" +
                "B604960\n" +
                "A605128\n" +
                "B605132\n" +
                "A1089807\n" +
                "B1089810\n" +
                "A1089948\n" +
                "B1089951\n");
    }

    private DriveThruList sampleLogAcrossDays() {
        return getDriveThrusFor("A86328771\n" +
                "B86328774\n" +
                "A86328899\n" +
                "B86328902\n" +
                "A582668\n" +
                "B582671\n" +
                "A582787\n" +
                "B582789");
    }

    private DriveThruList getDriveThrusFor(String input) {
        try {
            File file = new File(tempDir, "log1");
            Files.write(input, file, Charset.defaultCharset());
            return driveThroughScanner.scan(new File(file.getAbsolutePath()));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }


}
