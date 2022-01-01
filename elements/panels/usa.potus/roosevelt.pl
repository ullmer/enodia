% Family example: Roosevelt family
% Begun 2022-01-01 by Brygg Ullmer, Clemson University
% https://en.wikipedia.org/wiki/Roosevelt_family

%:- use_module(family).

:- discontiguous(married/2).
:- discontiguous(parents/3).

parents(j.s.thomas, c.m.v.rosenvelt, [e.roosevelt, a.m.roosevelt, n.roosevelt]).
parents(h.j.kunst, n.roosevelt, [n.roosevelt2, jo.roosevelt, ja.roosevelt]).
parents(

parents(r.howland,  j.roosevelt, [j.r.roosevelt]).
parents(s.a.delano, j.roosevelt, [f.d.roosevelt]).

parents(a.e.roosevelt, f.d.roosevelt, 
  [a.e.roosevelt2, j.roosevelt2, f.d.roosevelt2, e.roosevelt, 
   f.d.rosevelt3, j.a.roosevelt2]).

married(a.e.roosevelt, f.d.roosevelt).

potus(f.d.roosevelt, 32, 1933, 1945).

person(f.d.roosevelt, roosevelt, franklin, d, 1882, hydepark, ny, 1945, warmsprings, ga).

nicknames(f.d.roosevelt, [fdr]).
nicknames(t.roosevelt, [teddy]).

%:s/.*/\L&/

%%% end %%%
