/*Question 11 - Delete all occurrences of X from the list.*/
del_all(_,[],[]).
del_all(X,[X|L],L1):-
    del_all(X,L,L1).
del_all(X,[Y|L],L1):-
    del_all(X,L,L2), append([Y],L2,L1).