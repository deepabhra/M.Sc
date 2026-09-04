/*Question 12 - Find the reverse of the list.*/
rev([],[]).
rev([X],[X]).
rev([X|L], L1):- rev(L,L2), append(L2,[X], L1).

/*H.W:- Palindrome, odd or even of the list*/