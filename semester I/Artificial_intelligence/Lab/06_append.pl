/*Question 6 - Write a program to append two lists and produce a single list containing the elements of both lists.*/
append([],L,L).
append([X|L1],L2,[X|L3]):-
    append(L1,L2,L3).