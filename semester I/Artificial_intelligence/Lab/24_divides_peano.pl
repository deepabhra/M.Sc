/*Question 24 - Write a predicate to check whether one Peano number divides another.
  Two alternative implementations are shown (divides1, divides2).
  (plus/3 and times/3 are repeated here as helpers so this file runs standalone.)*/
plus(0,Y,Y).
plus(s(X), Y, s(Z)) :- plus(X,Y,Z).

times(0, _, 0).
times(s(X), Y, Z) :- times(X,Y,Z1), plus(Z1, Y, Z).

divides1(X, Y) :- times(Y, _, X).

divides2(0,_).
divides2(X,X).
divides2(X,Y):- plus(Y, U, X), divides2(U, Y).
