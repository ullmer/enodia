% Family example: Molly of Denali family and friends
% Begun 2022-01-01 by Brygg Ullmer, Clemson University

%:- use_module(family).


friends(molly, [tooey, trini, oscar]).

dogs([suki]).

residents(alaska, qyah, [molly, trini, tooey, oscar,
                         layla, walter, daniel, midge, nat]).

pets(molly, [suki, bandifer]).
pets(tooey, [anka, luka, laika, tukoni, skippy, jax, 
                      rascal, kiwi, kobi, atsoo, sasha, mouse, bandifer]).

parents(layla, walter, [molly]).            married(layla, walter).
parents(atsaq, kenji,  [tooey, jay, john]). married(atsaq, kenji).
parents(joy, daniel,   [trini]).            married(joy, daniel).
parents(renate, omf,   [oscar]).   
parents(midge,  rmf,           [renate]).
parents(mmm, mmf,                    [midge_marsh, annie_marsh]).
parents(nkw, nat, [layla_mabray]).

personMeta(flfn, [full, last, first, nickname]). %specify level of detail to describe people
personMeta(flf,  [full, last, first]).           %specify level of detail to describe people

boys( [cbrown, franklin, linus, shroeder, pigpen]).
girls([eudora, frieda, lucy, marcie, patty, peggy, sally, violet]).

person(lfn, cbrown, [brown, charlie, [charles, chuck]]).
person(fn,  patty,  [patty, [peppermint]]).
person(lf,  lucy,   [vanpelt, lucy]]).
person(lf,  linus,  [vanpelt, linus]]).

dog(snoopy).
bird(woodstock).

"Pig-Pen"
Charlie Brown
Eudora
Franklin
Frieda
Linus van Pelt
Lucy van Pelt
Marcie
Patty
Peggy Jean
Peppermint Patty
Rerun van Pelt
Sally Brown
Schroeder
Shermy
Snoopy
Violet Gray
Woodstock

%%% end %%%
