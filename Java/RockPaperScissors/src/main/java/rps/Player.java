package rps;

import java.util.List;

public interface Player {
    String name();

    int rounds();

    String choices(int i);

    List<String> choices();
}
