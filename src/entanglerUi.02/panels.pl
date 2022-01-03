% Initial ensemble of interaction panels
% Brygg Ullmer, Clemson University
% Begun 2022-01-03

commonDenominators([people, places, times, unsdg]).

defaultDescr('panel.pl') %e.g., "elements/panels/unsdg/panel.pl"

panelDescr(hd, [handleStr, denominators]).

qualRelation(people, strong,   El1, El2) :- %qualitative relation
  associatedPerson(El1, P1), associatedPerson(El2, P1), P1=P2.
  
qualRelation(places, moderate, El1, El2) :- %qualitative relation
  presentLocation(El1, Place1), presentLocation(El2, Place2), Place1=Place2.
  
qualRelation(places, weak, El1, El2) :- %qualitative relation
  presentLocation(El1, Place1n), presentLocation(El2, Place2n), %n: now
  pastLocation(El1, Place1t), pastLocation(El2, Place2t),       %t: then
  (Place1n = Place2t; Place1p = Place2p; Place1p = Place2n).

Place1=Place2.
  

edu.clemson.computing
panel(edu.clemson.arch, ['edu.clemson.arch', [people

globe.qantipode
unsdg
us.pbs.mollyDenali
usa.interstate
usa.potus
usa.sc
usa.sc.parks

%%% end %%%
