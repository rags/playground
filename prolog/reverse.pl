reverse([],[]).
reverse([Head|Rest],Result):-reverse(Rest,TailResult),append(TailResult,Head,Result).
