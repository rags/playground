package exptree.operations;

import exptree.Visitor;
import exptree.tree.Leaf;
import exptree.tree.binary.*;

import java.text.DecimalFormat;

public abstract class Printer implements Visitor {
    @Override
    public void visit(Leaf leaf) {
        System.out.print(new DecimalFormat("#.##").format(leaf.value()));
    }

    public abstract void print(BinaryOp op);

    @Override
    public void visit(Div div) {
        print(div);
    }

    @Override
    public void visit(Mul mul) {
        print(mul);
    }

    @Override
    public void visit(Plus plus) {
        print(plus);
    }

    @Override
    public void visit(Minus minus) {
        print(minus);
    }
}
