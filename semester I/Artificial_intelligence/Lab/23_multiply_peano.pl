/*Question 23 - Write a predicate to multiply two Peano numbers.
  (plus/3 is repeated here as a helper so this file runs standalone.)*/
plus(0,Y,Y).
plus(s(X), Y, s(Z)) :- plus(X,Y,Z).

times(0, _, 0).
times(s(X), Y, Z) :- times(X,Y,Z1), plus(Z1, Y, Z).
