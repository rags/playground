package exptree.tree;

import exptree.Node;
import exptree.Visitor;

public class Leaf implements Node {
    private double value;

    private Leaf(double value) {
        this.value = value;
    }

    public static Leaf leaf(double value) {
        return new Leaf(value);
    }

    @Override
    public void accept(Visitor visitor) {
        visitor.visit(this);
    }

    public double value() {
        return value;
    }
}
