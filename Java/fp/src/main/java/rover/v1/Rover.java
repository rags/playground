package rover.v1;

enum Direction{North,South,East,West}

public class Rover {
    int x;
    int y;
    Direction direction;

    public void left(){
        switch (direction){
            case North:
                direction=Direction.West;
                break;
            case West:
                direction=Direction.South;
                break;
            case South:
                direction=Direction.East;
                break;
            case East:
                direction=Direction.North;
        }

    }

    public void right(){
        switch (direction){
            case North:
                direction=Direction.East;
                break;
            case West:
                direction=Direction.North;
                break;
            case South:
                direction=Direction.West;
                break;
            case East:
                direction=Direction.South;
        }

    }

    public void move(){
        switch (direction){
            case North:
                y++;
                break;
            case West:
                x--;
                break;
            case South:
                y--;
                break;
            case East:
                x++;
        }

    }


}
