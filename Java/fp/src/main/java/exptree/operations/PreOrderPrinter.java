package exptree.operations;

import exptree.tree.binary.BinaryOp;

public class PreOrderPrinter extends Printer {

    @Override
    public void print(BinaryOp op){
        System.out.print("(");
        System.out.print(op.sign());
        System.out.print(" ");
        op.left().accept(this);
        System.out.print(" ");
        op.right().accept(this);
        System.out.print(")");
    }

}
