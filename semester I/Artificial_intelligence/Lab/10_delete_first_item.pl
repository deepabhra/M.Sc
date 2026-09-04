/*Question 10 - Delete the first item from the list.*/
del_first(X,[X|L],L).
del_first(X,[Y|L],[Y|L1]):-
    del_first(X,L,L1).