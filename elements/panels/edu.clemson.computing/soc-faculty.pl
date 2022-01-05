
doCat(acadRank, asst, hncp,  [acadRank, 'Assistant Professor',
        [brinkley, lc]]).

doCat(division, cs,  hncp, [soc, 'Computer Science',
  [apon, dean, hubig, liu, luo, wang, yang, goddard, hedetniemi, srimani, smotherman,
   martin, sorber, westall, donar, rodeghero, sitaraman, ge, cheng, razi, zhang, li]]).

doCat(inst, brown, dncpsci, ['brown.edu', 'Brown University', [tessendorf], ri, pvd, usa]).

doCat(person, apon,       fl,  ['Amy', 'Apon']).
doCat(person, dean,       fml, ['Brian', 'C.', 'Dean']).
doCat(person, hubig,      fl,  ['Nina', 'Hubig']).
doCat(person, liu,        fl,  ['Kai', 'Liu']).
doCat(person, luo,        fl,  ['Feng', 'Luo']).
doCat(person, wang,       fl,  ['James', 'Wang']).
doCat(person, yang,       fl,  ['Yin', 'Yang']).
doCat(person, goddard,    fl,  ['Wayne', 'Goddard']).
doCat(person, hedetniemi, fl,  ['Sandra', 'Hedetniemi']).
doCat(person, srimani,    fl,  ['Pradip', 'Srimani']).
doCat(person, smotherman, fl,  ['Mark', 'Smotherman']).
doCat(person, martin,     fl,  ['Jim', 'Martin']).
doCat(person, sorber,     fl,  ['Jacob', 'Sorber']).
doCat(person, westall,    fl,  ['Mike', 'Westall']).
doCat(person, donar,      fl,  ['David', 'Donar']).
doCat(person, rodeghero,  fl,  ['Paige, 'Rodeghero']).
doCat(person, sitaraman,  fl,  ['Murali', 'Sitaraman']).
doCat(person, ge,         fl,  ['Rong', 'Ge']).
doCat(person, cheng,      fl,  ['Long', 'Cheng']).
doCat(person, razi,       fl,  ['Abolfazi', 'Razi']).
doCat(person, zhang,      fl,  ['Zhenkai', 'Zhang']).
doCat(person, li,         fl,  ['Nianyi', 'Li']).


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
  gatech.edu:     {ftd: [Caine, Kraemer, Zordan, Plaue], 
                                                  sab: GA, cab: ATL, ia3: USA}
  indiana.edu:    {ftd: [Freeman],                sab: IN, cab: BMG, ia3: USA}
  jhu.edu:        {ftd: [Taylor],                 sab: MD, cab: BWI, ia3: USA}
  mit.edu:        {ftd: [Dean, Goddard, Ullmer],  sab: MA, cab: BOS, ia3: USA}
  ncsu.edu:       {ftd: [Martin],                 sab: NC, cab: RDU, ia3: USA}
  osu.edu:        {ftd: [Sitaraman],              sab: OH, cab: OSU, ia3: USA}
  psu.edu:        {ftd: [McNeese],                sab: PA, cab: UNV, ia3: USA}
  scad.edu:       {ftd: [Kwon],                   sab: GA, cab: SAV, ia3: USA}
  tum.de:         {ftd: [Hubig],                           cab: MUC, ia3: DEU}
  tamu.edu:       {ftd: [Duchowski],              sab: TX, cab: CLL, ia3: USA}
  unibe.ch:       {ftd: [Dhillon Singh],                   cab: BRN, ia3: CHE}
  caluniv.ac.in:  {ftd: [Srimani],                         cab: CCU, ia3: IND}
  uci.edu:        {ftd: [Knijnenburg],            sab: CA, cab: SNA, ia3: USA}
  ucla.edu:       {ftd: [Widman],                 sab: CA, cab: LAX, ia3: USA}
  ucf.edu:        {ftd: [Wang],                   sab: FL, cab: MCO, ia3: USA}
  tcd.ie:         {ftd: [Joerg],                           cab: DUB, ia3: IRL}
  ufl.edu:        {ftd: [Brinkley, Robb],         sab: FL, cab: GNV, ia3: USA}
  unige.it:       {ftd: [Iuricich],                        cab: GOA, ia3: ITA}
  umaine.edu:     {ftd: [Razi],                   sab: ME, cab: BDL, ia3: USA}
  umass.edu:      {ftd: [Sorber],                 sab: MA, cab: BGR, ia3: USA}
  unc.edu:        {ftd: [Smotherman],             sab: NC, cab: RDU, ia3: USA}
  charlotte.edu:  {ftd: [Babu],                   sab: NC, cab: CLT, ia3: USA}
  pitt.edu:       {ftd: [Van Scoy],               sab: PA, cab: PIT, ia3: USA}
  utdallas.edu:   {ftd: [Luo],                    sab: TX, cab: DFW, ia3: USA}
  virginia.edu:   {ftd: [Hedetniemi],             sab: VA, cab: CHO, ia3: USA}
  uu.nl:          {ftd: [Karamouzas],                      cab: UTC, ia3: NLD}
  vanderbilt.edu: {ftd: [Apon],                   sab: TN, cab: BNA, ia3: USA}
  vatech.edu:     {ftd: [Cheng, Ge],              sab: VA, cab: ROA, ia3: USA}
  washington.edu: {ftd: [Jin],                    sab: WA, cab: SEA, ia3: USA}

### end ###
