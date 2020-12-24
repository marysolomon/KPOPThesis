import pandas as pd
import os

##### Retrieve artist URI/IDs from Spotify (manually) #####

# First Generation Idols
seotaijiandboys = 'spotify:artist:52Gsa9Zypqztm2DeNkQfCm'
hot = 'spotify:artist:5JrfgZAgqAMywJpLpJM0eS'
sechskies = 'spotify:artist:6uRyNreOHUvWPNGnKfIo27'
nrg = 'spotify:artist:7xrfnodwPKuIxS9JuUECaf'
babyvox = 'spotify:artist:7H5LMtjHqkyH4U8dpLR4lo'
ses = 'spotify:artist:61HUG80Xma4rnXsqfZkzeM'
diva = 'spotify:artist:0CI6MkDddUbiuI8T7V5ZcF'
finkl = 'spotify:artist:2aRLyjYp7WPr4EkjkI1gvS'

shinhwa = 'spotify:artist:0jVvkFPa6YbFXQ3Qmhita0'
eaglefive = 'spotify:artist:4vkr97RLtHtBPFUHdBqADe'
onetym = 'spotify:artist:0P8IEJrM7oUTK4WwdMKsvS'
god = 'spotify:artist:1nTCpd63NkuGGpCIbo4Ywl'
clickb = 'spotify:artist:2kOGSFThgEzPEjL4fFB25w'
boa = 'spotify:artist:4muJrGMndyYWqZtfk8OWy4' #excessive amounts of albums, need to manually clean
jewelry = 'spotify:artist:01iyQzyns6Ab0LxjYvHcg9'
rain = 'spotify:artist:5L4EafeXwZ0stGuPtGr5Tz'
wheesung = 'spotify:artist:7luxe2wCwtDtkKSP8ZhPLn'
seven = 'spotify:artist:14yLuCwlBqteUdBqx9soJV'
lexy = 'spotify:artist:5C9rYLjMoYuwbbM34ReBU5'


## Second Generation Idols
tvxq = 'spotify:artist:6nVMMEywS5Y4tsHPKx1nIo'
superjunior = 'spotify:artist:6gzXCdfYfFe5XKhPKkYqxV'
ss501 = 'spotify:artist:6rmMpoeu2SIV4OLURCOn2e'
paran = 'spotify:artist:5ftRsrMP4ff6qANAuNfyUo'
thegrace = 'spotify:artist:5KsQApoJGpsjbmuiRIFWQ1'
lpg = 'spotify:artist:2tRM4eOC6iIvdCCf3y8GRD'
ivy = 'spotify:artist:7wBrxhzcHVIis4VL3iR6hF'
bigbang = 'spotify:artist:4Kxlr1PRlDKEB0ekOCyHgX'
browneyedgirls = 'spotify:artist:2GEPtT5RDxrmdi0A4mbDi7'
seeya = 'spotify:artist:3Mbxr8TL0Sny7dUNicKWm2'
ftisland = 'spotify:artist:6KhH771vq2X2Aom91nNzpZ'
wondergirls = 'spotify:artist:3Cv2vi3WTl8VZOTdrBkKdM'
kara = 'spotify:artist:7aZ221EQfonNG2lO9Hh192'
sondambi = 'spotify:artist:3cCbcs6r1Lma7MfEjyfCGU'
sunnyhill = 'spotify:artist:1ePYD8tMMM4Y8gbwi69vaf'

shinee ='spotify:artist:2hRQKC0gqlZGPrmUKbcchR'
twoam = 'spotify:artist:5SnaL8SsjGMHQNyqpa8Zos'
twopm = 'spotify:artist:5iRPbkcPmqAFFwDUj6ywVS'
ukiss = 'spotify:artist:2GB76Lm833jVI5kLvKEB7Z'
iu = 'spotify:artist:3HqSLMAZ3g3d5poNaI7GOU'
joo ='spotify:artist:7exKyATJk2jkltULZKqckA'
beast = 'spotify:artist:1Pr9gT0veB2tgcisQeIGoC'#Now highlight...
mblaq= 'spotify:artist:14f1WN9TUDVBK4sHUStmLG'
toanyone = 'spotify:artist:1l0mKo96Jh9HVYONcRl3Yp'
fourminute = 'spotify:artist:6cdC1cwqh3eJAXaxXJt2jv'
afterschool = 'spotify:artist:1loWI8jVk9btgJXHgqHXPD'
tara = 'spotify:artist:1R52cwGf75yTf7I3Q0Irf8'
fx = 'spotify:artist:3wRA5UYoo08BBKJnzyKkpF'
rainbow = 'spotify:artist:7xDyxRXgFgOZhdtLtkYR1y'
secret = 'spotify:artist:503DjcVO5Ku1NgLPhVuNg7'
nsyoong = 'spotify:artist:15EDMg4DaX49QQyxlBzC2f'
cnblue = 'spotify:artist:6dCz3spfpIvqqqsIoP6wXi'
zea = 'spotify:artist:6lGfLCig2b5mvDTtsPSrb0'
infinite = 'spotify:artist:1bkpTEmumLC3xc7HgMsttU'
teentop = 'spotify:artist:3offPqpKAKmpQkIdWnjzkc'
missa = 'spotify:artist:1BEohdSWSBggmO979tzRwW'
ninemuses = 'spotify:artist:55tJwpPIz9BMrSLM45iEXX'
girlsday = 'spotify:artist:13kJgvU22LHMsJtGWLmx7W'
sistar = 'spotify:artist:2wTLheTmMcFCA4hdY8hZJP'
orangecaramel = 'spotify:artist:2QHTtUsN6Q13w3QHdfRqsK'
gna = 'spotify:artist:3hzcooxMtbApMTvvn6XKVA'
coedschool = 'spotify:artist:6ZsTqFoNYY6cyRcKnvOu3A'

#add 2011 and more 


##### Create the artist dataframe ####
artist_df = pd.DataFrame({'Artist':['Seo Taiji and Boys', 'H.O.T.', 'SECHSKIES', 'NRG','Baby VOX', 
                    'S.E.S', 'Diva','Fin.K.L','SHINHWA', 'Eagle Five', 
                    '1TYM', 'god', 'Click-B', 'BoA', 'Jewelry', 
                    'Rain', 'Realslow', 'SE7EN', 'Lexy', 'TVXQ!', 
                    'SUPER JUNIOR', 'SS501', "Paran", 'CSJH The Grace', 'LPG', 
                    'IVY', 'BIGBANG', 'Brown Eyed Girls', 'SeeYa', 'FTISLAND', 
                    'Wonder Girls', 'KARA', 'Son Dam Bi', 'Sunny Hill', 'SHINee', 
                    '2AM', '2PM', 'U-KISS', 'IU', 'JOO', 
                    'Beast', 'MBLAQ', '2NE1', '4Minute', 'After School', 
                    'T-ARA', 'f(x)', 'Rainbow', 'Secret', 'NS Yoon-G',
                    'CNBLUE', 'ZE:A', 'INFINITE', 'TEEN TOP', 'miss A', 
                    '9MUSES', "Girl's Day", 'SISTAR', 'Orange Caramel', 'G.NA', 
                    'Coed School'],
             'ID' : [seotaijiandboys, hot, sechskies, nrg, babyvox, 
                    ses, diva, finkl, shinhwa, eaglefive, 
                    onetym, god, clickb, boa, jewelry, 
                    rain, wheesung, seven, lexy, tvxq, 
                    superjunior, ss501, paran, thegrace, lpg,
                    ivy, bigbang, browneyedgirls, seeya, ftisland,
                    wondergirls, kara, sondambi, sunnyhill, shinee, 
                    twoam, twopm, ukiss, iu, joo, 
                    beast, mblaq, toanyone, fourminute, afterschool, 
                    tara, fx, rainbow, secret, nsyoong,
                    cnblue, zea, infinite, teentop, missa, 
                    ninemuses, girlsday, sistar, orangecaramel, gna, 
                    coedschool],
             'Type': ['group', 'group', 'group', 'group','group', 
                    'group', 'group', 'group','group', 'group', 
                    'group', 'group', 'group', 'solo', 'group', 
                    'solo', 'solo', 'solo', 'solo','group', 
                    'group', 'group', 'group', 'group', 'group', 
                    'solo', 'group', 'group', 'group', 'group',
                    'group', 'group', 'solo', 'group', 'group', 
                    'group', 'group', 'group', 'solo', 'solo', 
                    'group', 'group', 'group', 'group', 'group', 
                    'group', 'group', 'group', 'group', 'solo',
                    'group', 'group', 'group', 'group', 'group', 
                    'group', 'group', 'group', 'group', 'solo', 
                    'group'],
             'Gender': ['male', 'male', 'male', 'male','female', 
                    'female', 'female', 'female','male', 'male', 
                    'male', 'male', 'male', 'female', 'female',
                    'male', 'male', 'male', 'female', 'male', 
                    'male', 'male', 'male', 'female', 'female', 
                    'female', 'male', 'female', 'female', 'male',
                    'female', 'female', 'female', 'coed', 'male', 
                    'male', 'male', 'male', 'female', 'female', 
                    'male', 'male', 'female', 'female', 'female', 
                    'female', 'female', 'female', 'female', 'female', 
                    'male', 'male', 'male', 'male', 'female', 
                    'female', 'female', 'female', 'female', 'female', 
                    'coed'],
             'Generation': [1, 1, 1, 1, 1, 
                    1, 1, 1, 1.5, 1.5, 
                    1.5, 1.5, 1.5, 1.5, 1.5, 
                    1.5, 1.5, 1.5, 1.5, 2, 
                    2, 2, 2, 2, 2, 
                    2, 2, 2, 2, 2,
                    2, 2, 2, 2, 2.5, 
                    2.5, 2.5, 2.5, 2.5, 2.5, 
                    2.5, 2.5, 2.5, 2.5, 2.5, 
                    2.5, 2.5, 2.5, 2.5, 2.5,
                    2.5, 2.5, 2.5, 2.5, 2.5, 
                    2.5, 2.5, 2.5, 2.5, 2.5, 
                    2.5],
             'DebutYear':[1992, 1996, 1997, 1997, 1997, 
                    1997, 1997, 1998, 1998, 1998, 
                    1998, 1999, 1999, 2000, 2001, 
                    2002, 2002, 2003, 2003, 2004, 
                    2005, 2005, 2005, 2005, 2005, 
                    2005, 2006, 2006, 2006, 2007,
                    2007, 2007, 2007, 2007, 2008, 
                    2008, 2008, 2008, 2008, 2008, 
                    2009, 2009, 2009, 2009, 2009, 
                    2009, 2009, 2009, 2009, 2009,
                    2010, 2010, 2010, 2010, 2010, 
                    2010, 2010, 2010, 2010, 2010, 
                    2010]})

print(artist_df)