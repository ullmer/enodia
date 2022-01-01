% Family example: Roosevelt family
% Begun 2022-01-01 by Brygg Ullmer, Clemson University
% https://en.wikipedia.org/wiki/Roosevelt_family

%:- use_module(family).

:- discontiguous(married/2).
:- discontiguous(parents/3).

parents(j.s.thomas, c.m.v.rosenvelt, [e.roosevelt, a.m.roosevelt, n.roosevelt]).
parents(h.j.kunst, n.roosevelt, [n.roosevelt2, jo.roosevelt, ja.roosevelt]).

parents(m.s.bulloch, t.roosevelt1, [t.roosevelt2, e.b.roosevelt]).
parents(a.h.lee,     t.roosevelt2, [a.l.roosevelt]).
parents(e.k.carow,   t.roosevelt2, [t.roosevelt3, k.roosevelt, et.roosevelt, 
                                    a.roosevelt, q.roosevelt]).

parents(r.howland,  j.roosevelt, [j.r.roosevelt]).
parents(s.a.delano, j.roosevelt, [f.d.roosevelt]).

parents(a.e.roosevelt, f.d.roosevelt, 
  [a.e.roosevelt2, j.roosevelt2, f.d.roosevelt2, e.roosevelt, 
   f.d.rosevelt3, j.a.roosevelt2]).

married(a.e.roosevelt, f.d.roosevelt).

potus(t.roosevelt2,  26, 1901, 1909).
potus(f.d.roosevelt, 32, 1933, 1945).

person(t.roosevelt2,  roosevelt, theodore, -, 1858, newyorkcity, ny, 1919, oysterbay, ny).
person(f.d.roosevelt, roosevelt, franklin, d, 1882, hydepark,    ny, 1945, warmsprings, ga).

nicknames(t.roosevelt2, [teddy, tr]).
nicknames(f.d.roosevelt, [fdr]).

%:s/.*/\L&/

%%% end %%%
