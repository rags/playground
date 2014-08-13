package exptree.tree.binary;

import exptree.Node;
import exptree.Visitor;

public class Minus extends BinaryOp{
    private Minus(Node left, Node right) {
        super(left, right);
    }

    public static Node minus(Node left, Node right){return new Minus(left, right);}

    @Override
    public char sign() {
        return '-';
    }

    @Override
    public void accept(Visitor visitor) {
        visitor.visit(this);
    }
}
