% Friends example: Charlie Brown friends and family
% Begun 2022-01-13 by Brygg Ullmer, Clemson University

%:- use_module(family).

boys( [cbrown, franklin, linus, shroeder, pigpen]).
girls([eudora, frieda,   lucy,  marcie,   patty, peggyjean, sally, violet, littleRedHairedGirl]).

siblings([cbrown, sally]).
siblings([lucy, linus]).

pets(cbrown, [snoopy]).

friends(cbrown, [linus, lucy, frieda, violet, eudora, snoopy, schroeder, 
                 franklin, patty, marcie, peggyjean]).

person(lfn, cbrown, [brown, charlie, [charles, chuck]]).
person(fn,  patty,  [patty, [peppermint]]).
person(lf,  lucy,   [vanpelt, lucy]]).
person(lf,  linus,  [vanpelt, linus]]).

dog(snoopy).
bird(woodstock).


%%% end %%%
