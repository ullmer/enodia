% Entangler // Enodia Fargate tapestry
% By Brygg Ullmer, Clemson University
% Begun 2021-12-16

illuminated(CurrentSpread, IPanel, CellCoord) :- 
  iPanelActive(IPanel, CurrentSpread),
  withinActiveSpread(CurrentSpread, Concept1), 
  cellRepresents(CellCoord, Concept1), 
  actionablyEntangled(Concept1, Concept2), 
  (chosen(Concept2); chosen(Concept1)).  
   %considered rya, valin, picked, pinched, selected as alternatives

withinActiveSpread(Concept) :- 
  ipanelWithinSpread(Ipanel), 
  conceptWithinIpanel(Concept, Ipanel).

screenDynamicsPossible(Ipanel, CodeName, ScreenAddr) :-
  proximal(Ipanel, Screen),
  panelCode(Ipanel, CodeName).

screenDynamicsSelected(Ipanel, CodeNameSelected, ScreenAddr) :-
  findall([Ipanel, CodeName, ScreenAddr], 
          screenDynamicsPossible(Ipanel, CodeName, ScreenAddr), L),
  selectBestCodeFit(L, CodeNameSelected).

% ipanels are interaction panels (both vertical/upon flying buttresses and 
%  upon varying-orientation ~hex-drums)

%%% end %%%
