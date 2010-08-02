package foo;

import junit.framework.TestCase;

import java.util.List;
import java.util.ArrayList;

/**
 * job:explore thread local funtionality
 */
public class ThreadLocalTest extends TestCase {
    ThreadLocal<List<Integer>> localMember;
    ThreadLocal<List<Integer>> inheritedLocalMember;

    public void setUp() {
        localMember = new ThreadLocal<List<Integer>>(){
            protected List<Integer> initialValue() {
                return new ArrayList<Integer>();

            }
        };
        inheritedLocalMember = new InheritableThreadLocal<List<Integer>>(){
            protected List<Integer> initialValue() {
                return new ArrayList<Integer>();

            }
        };
    }


    public void testThreadLocal() throws InterruptedException {
        List<Integer> integers = localMember.get();
        integers.add(1);
        integers.add(2);
        integers.add(3);
        Thread thread = addInThread();
        thread.run();
        thread.join();
        assertEquals(3, integers.size());
    }

    private Thread addInThread() {
        return new Thread(){
            public void run() {
                List<Integer> integers = localMember.get();
                integers.add(4);
                integers.add(5);
                assertEquals(5, integers.size());
            }
        };
    }


}
