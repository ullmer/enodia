% Family example: Molly of Denali family and friends
% Begun 2022-01-01 by Brygg Ullmer, Clemson University

%:- use_module(family).

girls([molly, trini, vera]).
boys([tooey, oscar]).

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

person(lf, molly,  [mabray, molly]).
person(lf, layla,  [mabray, layla]).
person(lf, walter, [mabray, walter]).

person(lf, trini,  [mumford, trini]).
person(lf, joy,    [mumford, joy]).
person(lf, daniel, [mumford, daniel]).

person(lfn, tooey, [ookami, tookkone, [tooey]]).
person(lf,  atsaq, [ookami, atsaq]).
person(lf,  kenji, [ookami, kenji]).

person(lfn, midge, [marsh, midge,  [auntie_midge, chief_midge]]).
person(lfn, nat,   [kon,   nehtan, [nat, grandpa_nat, lightning]]).

person(lfn, cbrown, [brown, charlie, [charles, chuck]]).



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
