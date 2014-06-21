import time
from random import randint
import praw
r = praw.Reddit('shitposting bot')
r.login(username='MasterMemer69', password='ronpaulbot')

url_list = []

fd = open('links.txt')
for ln in fd:
    mystring = ln
    mystring = mystring[:-1]
    url_list.append(mystring)
fd.close()


title_list = ['better shut up', 'le new meme' 'what the fuck did you just say about me, you little bitch?' 'le newest meme',\
 'wow, another title', 'the jews did this', 'wtf nagro', 'shut up dinks', 'uhh', 'spooky skeletons', 'other title', 'fugg me',\
 'fug', 'shitposting intensifies', 'jews are bretty cool', 'wow', 'upron this post plox', 'the jews are bretty cool gouise',\
  'nigglies tongue my pooer', 'wow, so cool', 'goldmine is my friend', 'bane is a shitposter, i am a god',\
   'kp has some nice tatas', 'rt is a joo', 'who?', 'friendly reminder that i am le master shitposter',\
 'ok, i am about 45% done with this shit', 'well, if you insist...', 'why hasn\'t this been upronned to le front page?' \
 'i like big booty tho', 'its pretty pretentious of you to say im unqualified to know, tho, m8', 'u \'avin a spanko, m8?', 'le', \
 'spooooooooky', 'hi mom', 'now that\'s what i call shitposting', 'k', '2braev4u', 'dae like big dicks in your ass is bad for you health?']


for x in range(0, (len(url_list) - 1)):
    r.submit('Braveryjerk', title_list[randint(0, (len(title_list) - 1))], text=None, url=url_list[x], captcha=None, save=None, send_replies=None)
        
