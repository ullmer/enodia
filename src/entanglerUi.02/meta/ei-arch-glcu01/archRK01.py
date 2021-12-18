# Wikipedia Architecture parsing 
# By Brygg Ullmer, Clemson University
# Begun 2021-12-17

import wikipediaapi
import wptools

ww=wikipediaapi.Wikipedia('en')
page1 = ww.page("Category:Rem Koolhaas buildings")
print(page1.categorymembers.keys())

page2 = wptools.page('Seattle Central Library').get_parse()
infobox = page2.data['infobox']
print('Infobox keys:', infobox.keys())
print('Location:', infobox['location'])

### end ###
