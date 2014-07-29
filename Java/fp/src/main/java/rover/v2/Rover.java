package rover.v2;

import rover.Position;

public class Rover {
    Direction direction;
    Position position;

    public void left(){
        direction=direction.left();
    }

    public void right(){
        direction=direction.right();
    }

    public void move(){
        position=direction.move(position);
    }

}
