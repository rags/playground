package rps.ui.console;

import java.io.PrintStream;
import java.util.Scanner;

public class IO {

    private static Scanner in;
    private static PrintStream out;

    public static Scanner in() {
        if (in == null) {
            in = new Scanner(System.in);
        }
        return in;
    }

    public static PrintStream out() {
        if (out == null) {
            out = System.out;
        }
        return out;
    }

    public static void reset() {
        in = null;
        out = null;
    }

    public static Scanner prompt(String prompt){
        out().print(prompt + "\n> ");
        return in();
    }

}
