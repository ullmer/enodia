% Entangler // Enodia Fargate tapestry
% By Brygg Ullmer, Clemson University
% Begun 2021-12-16

illuminated(CellCoord) :- 
  withinActiveSpread(Concept1), 
  cellRepresents(Cell, Concept1), 
  actionablyEntangled(Concept1, Concept2), 
  (valin(Concept2); valin(Concept1)).

valin(Concept) :- cellRepresents(Cell, Concept), cellSelected(CellCoord).

%rya(Concept) :- cellRepresents(Cell, Concept), selected(Cell).

withinActiveSpread(Concept) :- 
  ipanelWithinSpread(Ipanel), 
  conceptWithinIpanel(Concept, Ipanel).

% ipanels are interaction panels (both vertical/upon flying buttresses and 
%  upon varying-orientation ~hex-drums)

%%% end %%%
