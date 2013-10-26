SoundCloud Data Challenge
=========================

Given a set **S** of pairs of usernames corresponding to mutual friendships in
a social network, write a program to output each user’s **i**-th degree friends,
for every positive **i** less than or equal to **N**, for a fixed **N**. A
successful solution can be scaled to very large **S**, using parallel and
distributed computing techniques.


Input:
------

Input is a text file, where each line contains a tab-separated pair of user
names:

```
davidbowie  omid
davidbowie  kim
kim         torsten
torsten	    omid
brendan	    torsten
ziggy       davidbowie
mick        ziggy
```

The input file is not sorted. Each pair of usernames appears only once, in unspecified order, eg. the relationship between `mick` and `ziggy` might appear as `mick ziggy` **or** `ziggy mick`, but not both.


Output:
------

For **N** = 2, the output should look like:

```
brendan    kim        omid       torsten
davidbowie kim        mick       omid    torsten ziggy
kim        brendan    davidbowie omid    torsten ziggy
mick       davidbowie ziggy
omid       brendan    davidbowie kim     torsten ziggy
torsten    brendan    davidbowie kim     omid
ziggy      davidbowie kim        mick    omid
```

where each line begins with a username and is followed by all 1st and 2nd degree
friends of that user, separated by tabs and sorted lexicographically. The lines
are as well sorted by the first username on each line.


Implementation Notes:
---------------------

- Solutions can be implemented in any programming language
- Try to keep the external dependencies of your implementation to a minimum
- Assume that the target system has a compiler / interpreter for your language
  of choice, as well as a standard build / dependency management tool installed,
  but nothing more. Ie. your project should have a self-contained build.
- One possibility to achieve a scalable implementation is to use the MapReduce
  programming model
  - should you choose do implement your solution using MapReduce, use Hadoop's
    Streaming API [1], so that the program can be easily tested locally using a
    chain of UNIX pipes, like so:

      `cat input_file | mapper_executable | sort -k1,1 | reducer_executable`

      (your solution may require multiple map and reduce steps, however)
  - should you prefer a different model than MapReduce, make sure it is
    similarly easy for the reviewer to build and run your program on a single
    machine, with no additional software installed. We are also interested in
    your reasoning about your choice.
- Bonus points if you discuss time and space complexity of your solution
- Extra bonus points if you discuss correctness of your solution



[1] if you're not familiar with the Hadoop Streaming API, see here for an
introductory example: http://bit.ly/PYsjwD
