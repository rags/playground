edge(a,b).
edge(a,e).
edge(b,d).
edge(b,c).
edge(c,a).
edge(e,b).
edge(a,f).

route?(N1,N2):-edge(N1,N2).
route?(N1,N2):-edge(N1,X),route?(X,N2).

route(N1,N2,[N1,N2]):-edge(N1,N2).
route(N1,N2,[N1|Y]):-edge(N1,X),route(X,N2,Y).


son_of(ramakrishna,raghu).
son_of(chandramouli,deepthi).
son_of(srinivas,chandramouli).

grand_dad(X,Y):- son_of(X,A),son_of(A,Y).
