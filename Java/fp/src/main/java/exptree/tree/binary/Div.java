package exptree.tree.binary;

import exptree.Node;
import exptree.Visitor;

public class Div extends BinaryOp{
    private Div(Node left, Node right) {
        super(left, right);
    }

    public static Node div(Node left, Node right){return new Div(left, right);}

    @Override
    public char sign() {
        return '/';
    }

    @Override
    public void accept(Visitor visitor) {
        visitor.visit(this);
    }
}
