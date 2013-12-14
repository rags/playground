package rps;

import com.google.common.base.Function;
import com.google.common.base.Predicate;
import com.google.common.collect.HashMultiset;
import com.google.common.collect.Multiset;
import com.google.common.collect.Ordering;
import com.google.common.collect.Sets;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Random;
import java.util.Set;

import static com.google.common.collect.Collections2.transform;
import static com.google.common.collect.Iterables.getLast;
import static com.google.common.collect.Iterables.getOnlyElement;
import static com.google.common.collect.Lists.newArrayList;

/*
 Looks at opponents move history to decide on next throw.
 There is no proof that this is the best strategy it is more
 of a demonstration of the kind of things that can be done and
 also first step towards creating a BOT with some intelligence

 Logic: 1. Get opponent's prev moves sorted by counts (descending)
        2. Find a move that can beat maximum number of top favorite moves
        3. Repeat 2 till you have narrowed down to one best choice.
*/
public class SmartBot extends StrategicPlayer {
    private final GameRules rules;
    private Player opponent;
    Multiset<String> opponentMoves;
    private boolean aggresive;//Take more risk to win.

    public SmartBot(Player opponent, GameRules rules, boolean aggresive) {
        super(new PlayerImpl("<smart bot>"));
        this.opponent = opponent;
        this.rules = rules;
        opponentMoves = HashMultiset.create(opponent.choices());
        this.aggresive = aggresive;
    }

    public SmartBot(Player opponent, GameRules rules) {
        this(opponent, rules, false);
    }

    @Override
    protected String chooseImpl() {
        if (rounds() > 0) {
            opponentMoves.add(opponent.choices(rounds() - 1));
        }
        Set<String> candidates = rules.validChoices();
        for (final Count mostLikelyMove : prevThrowsByCountDesc()) {
            Predicate[] filters = aggresive ?
                    new Predicate[]{winOrDraw(mostLikelyMove), winOnly(mostLikelyMove)} :
                    new Predicate[]{winOrDraw(mostLikelyMove)};

            for (Predicate<String> predicate : filters) {
                Set<String> newCandidates = Sets.filter(candidates, predicate);
                if (newCandidates.isEmpty()) {
                    return selectRandom(candidates);
                }
                if (newCandidates.size() == 1) {
                    return getOnlyElement(newCandidates);
                }
                candidates = newCandidates;
            }
        }
        return selectRandom(candidates);
    }

    private String selectRandom(Set<String> candidates) {
        System.out.println("pick randomly from " + candidates);
        ArrayList<String> list = newArrayList(candidates);
        return list.get(new Random().nextInt(list.size()));
    }

    private Predicate<String> winOrDraw(final Count mostLikelyMove) {
        return new Predicate<String>() {
            @Override
            public boolean apply(String candidate) {
                return rules.dominationFor(candidate, mostLikelyMove.choice).winner().equals(candidate);
            }
        };
    }

    private Predicate<String> winOnly(final Count mostLikelyMove) {
        return new Predicate<String>() {
            @Override
            public boolean apply(String candidate) {
                return !candidate.equals(mostLikelyMove.choice);
            }
        };
    }

    private Collection<Count> prevThrowsByCountDesc() {
        return Ordering.natural().reverse().sortedCopy(transform(rules.validChoices(), new Function<String, Count>() {
            @Override
            public Count apply(String choice) {
                return new Count(opponentMoves.count(choice), choice);
            }
        }));
    }

    class Count implements Comparable<Count> {
        int cnt;
        String choice;

        Count(int cnt, String choice) {
            this.cnt = cnt;
            this.choice = choice;
        }

        @Override
        public int compareTo(Count o) {
            return Integer.compare(cnt, o.cnt);
        }

        @Override
        public String toString() {
            return "Count{" +
                    cnt + ", " +
                    choice +
                    '}';
        }
    }
}
