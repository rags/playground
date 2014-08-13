package exptree.tree.binary;

import exptree.Node;

public abstract class BinaryOp implements Node{
    private Node left;
    private Node right;

    protected BinaryOp(Node left, Node right) {
        this.left = left;
        this.right = right;
    }

    public abstract char sign();

    public Node left() {
        return left;
    }

    public Node right() {
        return right;
    }
}

