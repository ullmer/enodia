% Family example: Molly of Denali family and friends
% Begun 2022-01-01 by Brygg Ullmer, Clemson University
% https://en.wikipedia.org/wiki/Roosevelt_family

%:- use_module(family).

:- discontiguous(married/2).
:- discontiguous(parents/3).

girls([molly.mabray, trini.mumford, vera.malakas])

friends[molly.mabray, tookone.ookami, trini.mumford]).

dogs([suki]).

pets(molly.mabray,   [suki, bandifer]).
pets(tookone.ookami, [anka, luka, laika, tukoni, skippy, jax, 
                      rascal, kiwi, kobi, atsoo, sasha, mouse, bandifer]).

parents(layla.mabray, walter-mabray, [molly.mabray]). married(layla.mabray, walter.mabray).
parents(atsaq.ookami, kenji.ookami,  [tookone.ookami, jay.ookami, john.ookami]).
parents(nkw, nehtan.kon, [layla.mabray]).

person(molly.mabray, mabra, molly).

nicknames(tookkone.ookami, [tooey]).
nicknames(nehtan.kon, [nat, grandpa.nat, lightning]).

%nicknames(molly.mabray, [molly]).

%:s/.*/\L&/

%%% end %%%
