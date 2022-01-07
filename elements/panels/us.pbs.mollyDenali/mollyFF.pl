% Family example: Molly of Denali family and friends
% Begun 2022-01-01 by Brygg Ullmer, Clemson University

%:- use_module(family).

:- discontiguous(married/2).
:- discontiguous(parents/3).

girls([molly_mabray, trini_mumford, vera_malakas]).
boys([tookkone_ookami, oscar_marsh]).

friends(molly_mabray, [tookkone_ookami, trini_mumford, oscar_marsh]).

dogs([suki]).

pets(molly,   [suki, bandifer]).
pets(tooey, [anka, luka, laika, tukoni, skippy, jax, 
                      rascal, kiwi, kobi, atsoo, sasha, mouse, bandifer]).

parents(layla, walter, [molly]).  married(layla, walter).
parents(atsaq, kenji,  [tooey, jay, john]).
parents(joy, daniel,   [trini]). married(joy, daniel).
parents(renate, omf,   [oscar]).   
parents(midge,  rmf,           [renate]).
parents(mmm, mmf,                    [midge_marsh, annie_marsh]).
parents(nkw, nehtan_kon, [layla_mabray]).

personMeta(flfn, [full, last, first, nickname]). %specify level of detail to describe people
personMeta(flf,  [full, last, first]).           %specify level of detail to describe people

person(lf, molly_mabray,  [mabray, molly]).
person(lf, layla_mabray,  [mabray, layla]).
person(lf, walter_mabray, [mabray, walter]).

person(lf, trini_mumford,  [mumford, trini]).
person(lf, joy_mumford,    [mumford, joy]).
person(lf, daniel_mumford, [mumford, daniel]).

person(lfn, tookone_ookami, [ookami, tookkone, [tooey]]).
person(lf,  atsaq_ookami,   [ookami, atsaq]).
person(lf,  kenji_ookami,   [ookami, kenji]).

person(lfn, midge_marsh, [marsh, midge,  [auntie_midge, chief_midge]]).
person(lfn, nehtan_kon,  [kon,   nehtan, [nat, grandpa_nat, lightning]]).

%:s/.*/\L&/

%%% end %%%
