% Family example: Molly of Denali family and friends
% Begun 2022-01-01 by Brygg Ullmer, Clemson University
% https://en.wikipedia.org/wiki/Roosevelt_family

%:- use_module(family).

:- discontiguous(married/2).
:- discontiguous(parents/3).

parents(layla.mabray, walter-mabray, [molly.mabray]). married(layla.mabray, walter.mabray).

person(molly.mabray, mabra, molly).
%nicknames(molly.mabray, [molly]).

%:s/.*/\L&/

%%% end %%%
