/*Question 2 - Write a program to check whether two lists have the same length or not.*/
same_length([],[]).
samelength([_|R1],[_|R2]):-
    samelength(R1,R2).