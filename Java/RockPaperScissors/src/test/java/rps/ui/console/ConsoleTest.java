package rps.ui.console;

import org.junit.After;
import org.junit.Before;

import java.io.InputStream;
import java.io.PrintStream;

public class ConsoleTest {
    private InputStream inbackup;
    private PrintStream outbackup;

    @Before
    public void setUp() throws Exception {
        this.inbackup = System.in;
        this.outbackup = System.out;
        IO.reset();
    }

    @After
    public void tearDown() throws Exception {
        System.setIn(inbackup);
        System.setOut(outbackup);
    }
}
