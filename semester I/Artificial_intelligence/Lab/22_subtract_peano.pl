/*Question 22 - Write a predicate to find the difference of two Peano numbers.
  Three alternative implementations are shown (diff1, diff2, diff3).
  (plus/3 is repeated here as a helper for diff3, so this file runs standalone.)*/
plus(0,Y,Y).
plus(s(X), Y, s(Z)) :- plus(X,Y,Z).

diff1(X,0,X).
diff1(s(X), s(Y), Z) :- diff1(X,Y,Z).

diff2(X,0,X).
diff2(X, s(Y), Z) :- diff1(X,Y,s(Z)).

diff3(X,Y,Z) :- plus(Y,Z,X).
