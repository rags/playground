package exptree;

import exptree.tree.Leaf;
import exptree.tree.binary.Div;
import exptree.tree.binary.Minus;
import exptree.tree.binary.Mul;
import exptree.tree.binary.Plus;

public interface Visitor {
    void visit(Leaf leaf);
    void visit(Div div);
    void visit(Mul mul);
    void visit(Plus plus);
    void visit(Minus minus);
}
