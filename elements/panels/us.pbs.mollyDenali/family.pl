% Family example: Brygg, Miriam, and Lilleken
% Begun 2022-01-01

% borrows from https://raw.githubusercontent.com/Anniepoo/prolog-examples/master/familytree.pl

%:- module(family, []).

fullFirst(Fullname, Firstname) :- person(flf,  [Fullname, Firstname, _]).
fullNick(Fullname, Nickname)   :- 
  person(flfn, [Fullname, _, N]), member(Nickname, N).

male(P)    :- parents(_, P, _).
male(P)    :- boys(B), member(P, B).

female(P)  :- parents(P, _, _).
female(P)  :- girls(G), member(P, G).

friend(P1, P2) :- (friends(P1, F), member(P2, F));
                  (friends(P2, G), member(P1, G)).

%male(X)    :- males(Y),   member(X, Y).
%female(X)  :- females(Y), member(X, Y).

father(F, C)   :- parents(_, F, L), member(C, L).
mother(M, C)   :- parents(M, _, L), member(C, L).
parent(P, C)   :- mother(P,C); father(P,C).

partners(X, Y) :- married(X, Y); parents(X, Y, _).
wife(X, Y)     :- married(X, Y), female(X).
husband(X, Y)  :- married(X, Y), husband(X).

relation(father, X, Y)   :- father(X, Y).
relation(mother, X, Y)   :- mother(X, Y).
relation(sister, X, Y)   :- sister(X, Y).
relation(brother, X, Y)  :- brother(X, Y).
relation(daughter, X, Y) :- daughter(X, Y).
relation(siblings, X, Y) :- siblings(X, Y).
relation(cousin, X, Y)   :- cousin(X, Y).
relation(son, X, Y)      :- son(X, Y).
relation(aunt, X, Y)     :- aunt(X, Y).
relation(uncle, X, Y)    :- uncle(X, Y).
relation(niece, X, Y)    :- niece(X, Y).
relation(nephew, X, Y)   :- nephew(X, Y).
relation(nephew, X, Y)   :- nephew(X, Y).
relation(married, X, Y)  :- married(X, Y); married(Y, X).
relation(partners, X, Y) :- partners(X, Y).
relation(parents, X, Y)  :- parents(X, Y, _); parents(Y, X, _).
relation(grandfather, X, Y)  :- grandfather(X, Y).
relation(grandmother, X, Y)  :- grandmother(X, Y).

relation(X,Y) :- ancestor(A,X), ancestor(A,Y).
nickname(P, N) :- nicknames(P, Nnames), member(N, Nnames).

son(Child,Parent)      :- male(Child),   parent(Parent,Child).
daughter(Child,Parent) :- female(Child), parent(Parent,Child).

grandfather(GF,GC) :- male(GF),   parent(GF,Somebody),parent(Somebody,GC).
grandmother(GM,GC) :- female(GM), parent(GM,Somebody),parent(Somebody,GC).

uncle(X,Y)    :- brother(Par, X), parent(Par,Y).
aunt(X,Y)     :- sister(Par, X),  parent(Par,Y).

nephew(X,Y)   :- male(Y),   (aunt(Y, X); uncle(Y, X)).
niece(X,Y)    :- female(Y), (aunt(Y, X); uncle(Y, X)).

%sister(X,Y)   :- female(X), parent(Par,X), parent(Par,Y), X \= Y.
%brother(X,Y)      :- male(X),   parent(Par,X), parent(Par,Y), X \= Y.

brother(B, P) :- male(B),   B \= P, siblings(Sib, P), member(B, Sib).
brother(B, P1) :- married(P1, P2), brother(B, P2).

sister(S, P)  :- female(S), S \= P, siblings(Sib, P), member(S, Sib).
sister(S, P1)  :- married(P1, P2), sister(S, P2).

siblings(Siblings, Person) :- parents(_, _, Siblings), member(Person, Siblings).
%brother(X,Y)  :- male(X), parents(_, _, Children), 
%                 member(X, Children), member(Y, Children), X \= Y.

cousin(X,Y)   :- uncle(Unc, X), father(Unc,Y).
cousin(X,Y)   :- aunt(Unc, X),  mother(Unc,Y).
ancestor(X,Y) :- parent(X,Y).
ancestor(X,Y) :- parent(X,Somebody),ancestor(Somebody,Y).

enby(X)        :- enbies(Y),    member(X, Y).

%%% end %%%
