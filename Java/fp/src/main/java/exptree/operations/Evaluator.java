package exptree.operations;

import com.google.common.base.Preconditions;
import exptree.Node;
import exptree.Visitor;
import exptree.tree.Leaf;
import exptree.tree.binary.*;

import java.util.Stack;

public class Evaluator implements Visitor {

    Stack<Double> stack;

    public Evaluator() {
        stack = new Stack<>();
    }

    public double eval(Node tree){
        tree.accept(this);
        Preconditions.checkState(stack.size()==1, "Meh! Something's wrong");
        return stack.pop();
    }

    @Override
    public void visit(Leaf leaf) {
        stack.push(leaf.value());
    }

    @Override
    public void visit(Div div) {
        visitOperands(div);
        stack.push(stack.pop()/stack.pop());
    }

    private void visitOperands(BinaryOp binOp) {
        binOp.right().accept(this);
        binOp.left().accept(this);
    }

    @Override
    public void visit(Mul mul) {
        visitOperands(mul);
        stack.push(stack.pop() * stack.pop());
    }

    @Override
    public void visit(Plus plus) {
        visitOperands(plus);
        stack.push(stack.pop() + stack.pop());

    }

    @Override
    public void visit(Minus minus) {
        visitOperands(minus);
        stack.push(stack.pop() - stack.pop());
    }
}
