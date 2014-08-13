package exptree;

import exptree.operations.Evaluator;
import exptree.operations.InOrderPrinter;
import exptree.operations.PostOrderPrinter;
import exptree.operations.PreOrderPrinter;


import static exptree.tree.Leaf.leaf;
import static exptree.tree.binary.Div.div;
import static exptree.tree.binary.Minus.minus;
import static exptree.tree.binary.Mul.mul;
import static exptree.tree.binary.Plus.plus;

public class Main {
    public static void main(String[] args) {
        //(1 + 2 * 3) * 8/(3-2)
        Node tree = mul(
                plus(leaf(1), mul(leaf(2), leaf(3))),
                div(leaf(8),minus(leaf(3), leaf(2))));
        tree.accept(new InOrderPrinter());
        System.out.println();
        tree.accept(new PreOrderPrinter());
        System.out.println();
        tree.accept(new PostOrderPrinter());
        System.out.println();
        System.out.println("Result of eval " + new Evaluator().eval(tree));
    }
}
