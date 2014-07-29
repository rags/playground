package rover;

public class Position {
    private int x;
    private int y;

    public Position(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public Position delta(int x,int y){
        return new Position(x+this.x,y+this.y);
    }

    public Position incX(){
        return delta(1,0);
    }

    public Position decX(){
        return delta(-1,0);
    }

    public Position incY(){
        return delta(0,1);
    }

    public Position decY(){
        return delta(0,-1);
    }
}
