package exptree.tree.binary;

import exptree.Node;
import exptree.Visitor;

public class Plus extends BinaryOp{
    private Plus(Node left, Node right) {
        super(left, right);
    }

    public static Node plus(Node left, Node right){return new Plus(left, right);}

    @Override
    public char sign() {
        return '+';
    }

    @Override
    public void accept(Visitor visitor) {
        visitor.visit(this);
    }
}
