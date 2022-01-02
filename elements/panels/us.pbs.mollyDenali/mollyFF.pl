% Family example: Molly of Denali family and friends
% Begun 2022-01-01 by Brygg Ullmer, Clemson University
% https://en.wikipedia.org/wiki/Roosevelt_family

%:- use_module(family).

:- discontiguous(married/2).
:- discontiguous(parents/3).

girls([molly_mabray, trini_mumford, vera_malakas]).
boys([tookkone_ookami, oscar_marsh]).

friends(molly_mabray, [tookkone_ookami, trini_mumford, oscar_marsh]).

dogs([suki]).

pets(molly_mabray,   [suki, bandifer]).
pets(tookone_ookami, [anka, luka, laika, tukoni, skippy, jax, 
                      rascal, kiwi, kobi, atsoo, sasha, mouse, bandifer]).

parents(layla_mabray, walter_mabray, [molly_mabray]).  married(layla_mabray, walter_mabray).
parents(atsaq_ookami, kenji_ookami,  [tookkone_ookami, jay_ookami, john_ookami]).
parents(joy_mumford, daniel_mumford, [trini_mumford]). married(joy_mumford, daniel_mumford).
parents(renate_marsh, omf,           [oscar_marsh]).   
parents(midge_marsh,  rmf,           [renate_marsh]).
parents(mmm, mmf,                    [midge_marsh, annie_marsh]).
parents(nkw, nehtan_kon, [layla_mabray]).

personMeta(flf, [full, last, first]). %specify level of detail to describe people

person(flf, [molly_mabray,  mabray, molly]).
person(flf, [layla_mabray,  mabray, layla]).
person(flf, [walter_mabray, mabray, walter]).
person(flf, [trini_mumford, mumford, trini]).
person(flf, [tookone_ookami, ookami, tookkone]).
person(flf, [atsaq_ookami,   ookami, atsaq]).
person(flf, [kenji_ookami,   ookami, kenji]).

nicknames(tookkone_ookami, [tooey]).
nicknames(midge_marsh, [auntie_midge]).
nicknames(nehtan_kon, [nat, grandpa_nat, lightning]).

%:s/.*/\L&/

%%% end %%%
