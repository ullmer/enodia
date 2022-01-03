% Initial ensemble of interaction panels
% Brygg Ullmer, Clemson University
% Begun 2022-01-03

commonDenominators([people, places, times, unsdg, researchInterests]).

defaultDescr('panel.pl') %e.g., "elements/panels/unsdg/panel.pl"

panelDescr(hd, [handleStr, denominators]).

qualRelation(people, strong,   El1, El2) :- %qualitative relation
  associatedPerson(El1, P1), associatedPerson(El2, P2), samePerson(P1, P2).
  
qualRelation(people, strong,   El1, El2) :- %qualitative relation
  associatedPerson(El1, P1), associatedPerson(El2, P2), samePerson(P1, P2).
  
qualRelation(places, moderate, El1, El2) :- %qualitative relation
  presentLocation(El1, P1), presentLocation(El2, P2), samePlace(P1, P2).
  
qualRelation(places, weak, El1, El2) :- %qualitative relation
  presentLocation(El1, P1n), presentLocation(El2, P2n), %n: now
  pastLocation(El1, P1t), pastLocation(El2, P2t),       %t: then
  (samePlace(P1n, P2t); samePlace(P1p, P2p); samePlace(P1p, P2n)).

panel(edu.clemson.computing, ['edu.clemson.computing', 
                              [people, researchInterests]]).

panel(edu.clemson.arch,      ['edu.clemson.arch',      [people, 

globe.qantipode
unsdg
us.pbs.mollyDenali
usa.interstate
usa.potus
usa.sc
usa.sc.parks

%%% end %%%
