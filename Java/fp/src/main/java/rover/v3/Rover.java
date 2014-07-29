package rover.v3;

import java.util.function.Function;

interface F<A, B, C, D> {
    public D apply(A a, B b, C c);
}

interface F1<A, B, C, D,E> {
    public E apply(A a, B b, C c, D d);
}

public class Rover {

    public static void main(String[] args) {
        print(rover(1, 1, north()));
        System.out.println("------left--------");
        print(left(rover(1, 1, north())));
        print(left(rover(1, 1, south())));
        print(left(rover(1, 1, east())));
        print(left(rover(1, 1, west())));

        System.out.println("------right--------");
        print(right(rover(1, 1, north())));
        print(right(rover(1, 1, south())));
        print(right(rover(1, 1, east())));
        print(right(rover(1, 1, west())));

        System.out.println("------move--------");
        print(move(rover(1, 1, north())));
        print(move(rover(1, 1, south())));
        print(move(rover(1, 1, east())));
        print(move(rover(1, 1, west())));

        /*
                  1 2 N
          left -> 1 2 W
          move -> 0 2 W
          left -> 0 2 S
          move -> 0 1 S
          left -> 0 1 E
          move -> 1 1 E
          left -> 1 1 N
          move -> 1 2 N #back to origin
          move -> 1 3 N
        * */
        print(move(move(left(move(left(move(left(move(left(rover(1, 2, north())))))))))));
    }

    public static Function left(Function rover){
        return execute(rover, (F1) (_left, right, move, print) -> ((Function) _left).apply(rover));
    }

    public static Function right(Function rover){
        return execute(rover, (F1) (left, _right, move,print) -> ((Function) _right).apply(rover));
    }

    public static Function move(Function rover){
        return execute(rover, (F1) (left, right, _move, print) -> ((Function) _move).apply(rover));
    }

    public static Function print(Function r){
        return execute(r, (F1) (left, right, move, _print) -> ((Function) _print).apply(r));
    }

    private static Function execute(Function rover, F1 f) {
        return (Function)dir(rover).apply(f);
    }

    public static Function<F1<Function,Function,Function,Function,Function>,Function> north() {
        return (F1<Function,Function,Function,Function, Function> fn) -> fn.apply(
                (Function) (r -> rover((Function) r, west())),
                (Function) (r -> rover((Function) r, east())),
                (Function) (r ->  rover(x(((Function) r)), y(((Function) r)) + 1, north())),
                print("N")

        );
    }

    public static Function south() {
        return fn -> ((F1) fn).apply(
                (Function) (r -> rover((Function) r, east())),
                (Function) (r -> rover((Function) r, west())),
                (Function) (r -> rover(x(((Function) r)), y(((Function) r)) - 1, south())),
                print("S")
        );
    }

    private static Function print(String direction) {
        return r -> {
            System.out.println(x(((Function) r)) + " " + y(((Function) r)) + " " + direction);
            return r;
        };
    }

    public static Function east() {
        return fn -> ((F1) fn).apply(
                (Function) (r -> rover((Function) r, north())),
                (Function) (r -> rover((Function) r, south())),
                (Function) (r -> rover(x(((Function) r))+1, y(((Function) r)), east())),
                print("E")
        );
    }

    public static Function west() {
        return fn -> ((F1) fn).apply(
                (Function) (r -> rover((Function) r, south())),
                (Function) (r -> rover((Function) r, north())),
                (Function) (r -> rover(x(((Function) r))-1, y(((Function) r)), west())),
                print("W")
        );
    }

    public static Function rover(final int x, final int y, final Function direction) {
        return (f) -> ((F) f).apply(x, y, direction);
    }

    public static Function rover(Function rover, Function direction) {
        return rover(x(rover), y(rover), direction);
    }

    public static int x(Function rover) {
        return (int) rover.apply((F) (x, y, dir) -> x);
    }

    public static int y(Function rover) {
        return (int) rover.apply((F) (x, y, dir) -> y);
    }

    public static Function dir(Function rover) {
        return (Function) rover.apply((F) (x, y, dir) -> dir);
    }


}
