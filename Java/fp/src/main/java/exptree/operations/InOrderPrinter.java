package exptree.operations;

import exptree.tree.binary.BinaryOp;

import java.text.DecimalFormat;

public class InOrderPrinter extends Printer {

    @Override
    public void print(BinaryOp op){
        System.out.print("(");
        op.left().accept(this);
        System.out.print(" " + op.sign() + " ");
        op.right().accept(this);
        System.out.print(")");
    }
}
