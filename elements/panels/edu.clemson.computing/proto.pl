
% domain categories 

metaCat(hn,       [handle, name]).
metaCat(hnflfl,   [handle, name, firstname, lastname, firstnameStr, lastnameStr]).
metaCat(hncp,     [handle, name, category, people]).
metaCat(hdncpsci, [handle, domain, name, category, people, sab, cab, ia3]). 
  %sab, cab, ia3: state, city, country abbrevs

doCat(research, ai,   hn,   ['ai',   'Artificial Intelligence']).     %handle, name
doCat(research, aie,  hncp, ['aie',  ai, 'AI Education', [kc, bk]]).  %handle, name, category, people
docat(research, dmml, hncp, ['dmml', ai, 'Data Mining & Machine Learning', 
                                   [bcd, ah, nh, sj, sj, ik, kl, fl, ep, jw, yy, ar, nl]]).
docat(research, haii, hncp, ['haii', ai, 'Human-AI Interaction', [kc, bk, nm]]).

doCat(division, cs,  hncp, ['cs',  soc, 'Computer Science',
  [bcd, nh, kl, fl, jw, yy, wg, sh, ps, ms, jm, js, mw, dd, pr, ms, aa, rg, lc, ar, zz, nl]]).

doCat(division, hcc,  hncp, ['hcc', soc, 'Human-Centered Computing']).

doCat(acadRank, asst, hncp,  ['asst', acadRank, 'Assistant Professor', 
                             [jb, lc...]]).

doCat(person, bcd, hnflfl, ['bcd', 'Brian C. Dean', brian, dean, 'Brian', 'Dean']).

doCat(inst, brown, hdncpsci, ['brown', 'brown.edu', 'Brown University', [jt], ri, pvd, usa]).

Artificial Intelligence:
  AI Education: [Kelly Caine, Bart Knijnenburg]
  Data Mining & Machine Learning: [Brian C. Dean, Alexander Herzog, 
    Nina Hubig, Shuangshuang Jin, Sophie Joerg, Ioannis Karamouzas, 
    Kai Liu, Feng Luo, Eric Patterson, James Wang, Yin Yang, 
    Abolfazl Razi, Nianyi Li]
  Human-AI Interaction: [Kelly Caine, Bart Knijnenburg, Nathan McNeese]


divisions:
  CS:  [Brian C. Dean, Nina Hubig, Kai Liu, Feng Luo, James Wang, Yin Yang,
        Wayne Goddard, Sandra Hedetniemi, Pradip Srimani, Mark Smotherman,
        Jim Martin, Jacob Sorber, Mike Westall, David Donar, Paige Rodeghero,
        Murali Sitaraman, Amy Apon, Rong Ge, Long Cheng, Abolfazl Razi,
        Zhenkai Zhang, Nianyi Li]

  HCC: [Kelly Caine, Bart Knijnenburg, Nathan McNeese, Sabarish Babu,
        Andrew Robb, Brygg Ullmer, Eileen Kraemer, Guo Freeman, Julian Brinkley]

  VC:  [Shuangshuang Jin, Sophie Joerg, Ioannis Karamouzas, Eric Patterson,
        Federico Iuricich, Jerry Tessendorf, Victor Zordan,
        Daljit Singh Dhillon, Andrew Duchowski, Insun Kwon]

  FOI: [Svetlana Drachova, Yvon Feaster, Alexander Herzog,
        Catherine Kittelstad, Christopher Plaue, Carrie Russell, Mitch Shue,
        Yu-Shan Sun, Connie Taylor, Roger Van Scoy, Nicolas Widman]

rank:
  asst:      [Brinkley, Cheng, Singh Dhillon, Freeman, Hubig, Iuricich,
              Karamouzas, Li, Liu, McNeese, Robb, Rodeghero, Zhang]
  assoc:     [Babu, Caine, Donar, Ge, Jin, Joerg, Knijnenburg, Patterson,
              Razi, Smotherman, Sorber, Yang]
  full:      [Apon, Dean, Duchowski, Goddard, Hedetniemi, Kraemer, Luo, Martin,
              Sitaraman, Srimani, Tessendorf, Ullmer, Wang, Zordan]
  lecturer:  [Drachova, Sun, Widman]
  slecturer: [Feaster, Kittelstad, Plaue]
  pop:       [Kwon, Russell, Shue, Taylor, Van Scoy]

institutions: #ftd: Faculty w/ Terminal Degrees; sab, cab: State, City Abbrv
  brown.edu:      {ftd: [Tessendorf],             sab: RI, cab: PVD, ia3: USA}
  clemson.edu:    {ftd: [Patterson, Drachova, Feaster, Kittelstad, Russell, Sun],
                                                  sab: SC, cab: CEU, ia3: USA}
  mines.edu:      {ftd: [Liu],                    sab: CO, cab: DEN, ia3: USA}
  udel.edu:       {ftd: [Li],                     sab: DE, cab: ILG, ia3: USA}
  gmu.edu:        {ftd: [Shue],                   sab: VA, cab: DCA, ia3: USA}

