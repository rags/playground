package rps;

import java.util.List;

import static com.google.common.collect.Lists.newArrayList;

public class PlayerImpl implements Player {
    private String name;
    private List<String> choices;

    public PlayerImpl(String name, List<String> choices) {
        this.name = name;
        this.choices = choices;
    }

    public PlayerImpl(String name, String... choices) {
        this(name, newArrayList(choices));
    }

    public void addChoice(String move){
        choices.add(move);
    }

    @Override
    public String name() {
        return name;
    }

    @Override
    public int rounds() {
        return choices.size();
    }

    @Override
    public String choices(int i) {
        return choices.get(i);
    }

    @Override
    public List<String> choices() {
        return choices;
    }
}
