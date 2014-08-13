package exptree.tree.binary;

import exptree.Node;
import exptree.Visitor;

public class Mul extends BinaryOp{
    private Mul(Node left, Node right) {
        super(left, right);
    }

    public static Node mul(Node left, Node right){return new Mul(left, right);}

    @Override
    public char sign() {
        return '*';
    }

    @Override
    public void accept(Visitor visitor) {
        visitor.visit(this);
    }
}
