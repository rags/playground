package rover.v2;

import rover.Position;

public enum Direction {

    North{
        @Override
        public Direction left() {
            return West;
        }

        @Override
        public Direction right() {
            return East;
        }

        @Override
        public Position move(Position position) {
            return position.incY();
        }
    },
    South{
        @Override
        public Direction left() {
            return East;
        }

        @Override
        public Direction right() {
            return West;
        }

        @Override
        public Position move(Position position) {
            return position.decY();
        }
    },
    East{
        @Override
        public Direction left() {
            return North;
        }

        @Override
        public Direction right() {
            return South;
        }

        @Override
        public Position move(Position position) {
            return position.incX();
        }
    },
    West{
        @Override
        public Direction left() {
            return South;
        }

        @Override
        public Direction right() {
            return North;
        }

        @Override
        public Position move(Position position) {
            return position.decX();
        }
    };
    public abstract Direction left();
    public abstract Direction right();
    public abstract Position move(Position position);
    
}
