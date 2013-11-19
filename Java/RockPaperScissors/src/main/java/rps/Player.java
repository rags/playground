package rps;

import java.util.ArrayList;
import java.util.List;

public class Player {
    List<String> moves;
    String name;
     public Player(String name) {
        this.name = name;
        moves = new ArrayList<String>();
    }
}
