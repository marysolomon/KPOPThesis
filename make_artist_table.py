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

b1a4 = 'spotify:artist:3sxWOFw4MSN54SIQ8np6iG'
blockb = 'spotify:artist:4RnezwRV7VBJUCI1S0AE5u'
boyfriend = 'spotify:artist:2Pw8E6zZoeuksVWtyZPnzd'
raina = 'spotify:artist:2lkUAt5tu0ucVOMFT9hYtg'
apink = 'spotify:artist:2uWcrwgWmZcQc3IPBs3tfU'
bravegirls = 'spotify:artist:7t5H3uQv0Zw6cQUnSTF5BB'
fivedolls = 'spotify:artist:1nw5g6u9BIPwyqlsm01cDP'
stellar = 'spotify:artist:1rTwKjYcA7diHAD2c8ZozT'
dalshabet = 'spotify:artist:10xsuRNvidaOLxWd3fRIel'
troublemaker = 'spotify:artist:0ztjVBmFk6OuHq6XBBwMI9'
exid = 'spotify:artist:1xs6WFotNQSXweo0GXrS0O'
spica = 'spotify:artist:5S3bx90A4ZX5RV02jRCOp9'
aoa = 'spotify:artist:54gWVQFHf8IIqbjxAoOarN'
crayonpop = 'spotify:artist:0ODX6aegsZkBmBeMA5qqwi'
fiestar = 'spotify:artist:3IVjXrnR0npv1LY24kQSzd'
hellovenus = 'spotify:artist:3TW9U1f93tpGBsEtCSf7JG'
ailee = 'spotify:artist:3uGFTJ7JMllvhgGpumieHF'
anda = 'spotify:artist:2PZt7SATrAxsNG60Mqkan4'
ladiescode = 'spotify:artist:4epPY1AW9lQeVUM1XaFiwi'

## Third Generation Idols
bap = 'spotify:artist:6kxCoNfY6U1eP0Yc88phvk'
btob = 'spotify:artist:2hcsKca6hCfFMwwdbFvenJ'
exo = 'spotify:artist:3cjEqqelV9zb4BYE3qDQ4O'
vixx = 'spotify:artist:5BkB3rXc0qIdUtuEnhbK0A'
nuest = 'spotify:artist:1iQfn1B8V25iQoolQakyAZ'
bts = 'spotify:artist:3Nrfpe0tUJi4K4DXYWgMUX'
got7 = 'spotify:artist:6nfDaffa50mKtEOwR8g4df'
winner = 'spotify:artist:5DuzBeOgFwViFcv00Q5PFb'
mamamoo = 'spotify:artist:0XATRDCYuuGhk0oE7C0o5G'
redvelvet = 'spotify:artist:1z4g3DjTBBZKhvAroFlhOM'
lovelyz = 'spotify:artist:3g34PW5oNmDBxMVUTzx2XK'
clc = 'spotify:artist:6QyO41KctzGc70mVaVnXQO'
gfriend = 'spotify:artist:0qlWcS66ohOIi0M8JZwPft'
ohmygirl = 'spotify:artist:2019zR22qK2RBvCqtudBaI'
dia = 'spotify:artist:5Pcx98OUnL52aGZRRQx5v8'
april = 'spotify:artist:4cJ99wTjC60pXcfyISL9fa'
twice = 'spotify:artist:7n2Ycct7Beij7Dj7meI4X0'

ikon = 'spotify:artist:5qRSs6mvI17zrkJpOHkCoM'
seventeen = 'spotify:artist:7nqOGRxlXj7N2JYbgNEjYH'
monstax = 'spotify:artist:4TnGh5PKbSjpYqpIdlW5nz'
day6 = 'spotify:artist:5TnQc2N1iKlFjYD7CPGvFc'
nflying = 'spotify:artist:2ZmXexIJAD7PgABrj0qQRb'
uption = 'spotify:artist:2LjaeuGS0ubYXZfNihGp9y'
vav = 'spotify:artist:3riGN5iBVBk5naQxUDr5fk'
astro = 'spotify:artist:4pz4uzOMpJQyV8UTsDy4H8'
nct = 'spotify:artist:48eO052eSDcn8aTxiv6QaG'
nct127 = 'spotify:artist:7f4ignuCJhLXfZ9giKT7rH'
nctdream = 'spotify:artist:1gBUSTR3TyDdTVFIaQnc02'
sf9 = 'spotify:artist:7LOmc7gyMVMOWF8qwEdn2X'
pentagon = 'spotify:artist:1wKpMkucynaTfG8lyPprYV'
victon = 'spotify:artist:0ziR2zN0NFcB4x1G3P8cW3'

wjsn = 'spotify:artist:6hhqsQZhtp9hfaZhSd0VSD'
ioi = 'spotify:artist:6RKnXXyprPjhBdCvL802Ku'
gugudan = 'spotify:artist:0h7XZWgoxlY49uSUj7MVRY'
momoland = 'spotify:artist:5RR0MLwcjc87wjSw2JYdwx'
kard = 'spotify:artist:2JhAlkmukNvarUpGhTFXUQ'
goldenchild = 'spotify:artist:5zShiwTHlygdfsXj6eavTu'
onf = 'spotify:artist:0eEhOgZ2x6kv8kLz77WO7b'
wannaone = 'spotify:artist:2CvaqAMMsX576VBehaJ0Wx'
jbj = 'spotify:artist:6VJXRJvRRyLv99RZbXJ8RO'
rainz = 'spotify:artist:46JpdBeitfoEleoCabDawH'
ace = 'spotify:artist:25KT93FeotUTHC1dbLasxi'
theboyz = 'spotify:artist:0CmvFWTX9zmMNCUi6fHtAx'
dreamcatcher = 'spotify:artist:5V1qsQHdXNm4ZEZHWvFnqQ'
pristin = 'spotify:artist:6VAphrHp0Oc88qg9BDaH9D'
wekimeki = 'spotify:artist:5LWkv2hDbDwZL3zNwZYNPx'
tripleh = 'spotify:artist:1klFdLh3pak3eOtJP0styY'

## Fourth Generation Idols
straykids = 'spotify:artist:2dIgFjalVxs4ThymZ67YCE'
ateez = 'spotify:artist:68KmkJeZGfwe1OUaivBa2L'
fromis9 = 'spotify:artist:24nUVBIlCGi4twz4nYxJum'
gidle = 'spotify:artist:2AfmfGFbe0A0WsTYm0SDTx'
loona = 'spotify:artist:52zMTJCKluDlFwMQWmccY7'
izone = 'spotify:artist:5r1tUTxVSgvBHnoDuDODPH'
gwsn = 'spotify:artist:5fI4xffqGRGQvICSlJreMF'
oneus = 'spotify:artist:3CVYSpM7nfHFG5qCTW7Ht9'
verivery = 'spotify:artist:1fWUcRSok57yRm8gPKj1Fc'
txt = 'spotify:artist:0ghlgldX5Dd6720Q3qFyQB'
ab6ix = 'spotify:artist:4y0wFJ5jmCUNRLZfsw1I7g'
cix = 'spotify:artist:1lHfzEkKmmvdVDDDLKkcsd'
x1 = 'spotify:artist:6C4irZ60X8G7UimMRQiCcg'
cherrybullet = 'spotify:artist:3IJCdgkBZbieocLZ4e94GZ'
itzy = 'spotify:artist:2KC9Qb60EaY0kW4eH68vr3'
everglow = 'spotify:artist:3ZZzT0naD25RhY2uZvIKkJ'
bvndit = 'spotify:artist:5dEBuZjTtE68uDgCs23Kuv'
rocketpunch = 'spotify:artist:4hozqATxbpy9TwKWRT8QVO'
hinapia = 'spotify:artist:6bWaRj4L4PyJ4uv2wN47Ny'
threeye = 'spotify:artist:65SWpUO42tdFbEhdfj1ryf'
alexa = 'spotify:artist:4jCGRzuZkwo8CxboiANMEU'
mcnd = 'spotify:artist:59dDRtMe8DILtibke8FWLK'
dkb = 'spotify:artist:4DoedGw38ubJdAT1edFsIx'
too = 'spotify:artist:3a0xHIHQPhhzgSOJzgB2Rz'
cravity = 'spotify:artist:6FkhUhUwSPl3mGB6mmE8wn'
cignature = 'spotify:artist:5x9WawpXGR82PWDFk9CKYQ'
aespa = 'spotify:artist:6YVMFz59CuY7ngCxTxjpxE'

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
                    'Coed School', 'B1A4', 'Block B', 'BOYRFIREND', 'Raina', 
                    'Apink', 'Brave Girls', 'F-Ve Dolls', 'Stellar', 'Dalshabet',
                    'Trouble Maker', 'EXID', 'SPICA', 'AOA', 'Crayon Pop', 
                    'FIESTAR', 'HELLOVENUS', 'AILEE', 'Anda', "LADIES' CODE",
                    'B.A.P', 'BTOB', 'EXO', 'VIXX', "NU'EST",
                    'BTS', 'GOT7', 'WINNER', 'MAMAMOO', 'Red Velvet',
                    'Lovelyz', 'CLC', 'GFRIEND', 'OH MY GIRL', 'DIA',
                    'APRIL', 'TWICE', 'iKON', 'SEVENTEEN', 'Monsta X',
                    'DAY6', 'N.Flying', 'UP10TION', 'VAV', 'ASTRO', 
                    'NCT(NCT U)', 'NCT 127', 'NCT DREAM', 'SF9', 'PENTAGON',
                    'VICTON', 'WJSN', 'I.O.I', 'gugudan', 'MOMOLAND',
                    'KARD', 'Golden Child', 'ONF', 'Wanna One', 'JBJ',
                    'RAINZ', 'A.C.E', 'THEBOYZ', 'DREAMCATCHER', 'PRISTIN', 
                    'Weki Meki', 'Triple H', 'Stray Kids', 'ATEEZ', 'fromis_9',
                    '(G)I-DLE', 'LOONA', 'IZ*ONE', 'GWSN', 'ONEUS',
                    'VERIVERY', 'TOMORROW X TOGETHER', 'AB6IX', 'CIX', 'X1',
                    'Cherry Bullet', 'ITZY', 'EVERGLOW', 'BVNDIT', 'Rocket Punch',
                    'HINAPIA', '3YE', 'AleXa', 'MCND', 'DKB',
                    'TOO', 'CRAVITY', 'cignature', 'aespa'],
                    

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
                    coedschool, b1a4, blockb, boyfriend, raina,
                    apink, bravegirls, fivedolls, stellar, dalshabet,
                    troublemaker, exid, spica, aoa, crayonpop,
                    fiestar, hellovenus, ailee, anda, ladiescode,
                    bap, btob, exo, vixx, nuest,
                    bts, got7, winner, mamamoo, redvelvet,
                    lovelyz, clc, gfriend, ohmygirl, dia,
                    april, twice, ikon, seventeen, monstax,
                    day6, nflying, uption, vav, astro, 
                    nct, nct127, nctdream, sf9, pentagon,
                    victon, wjsn, ioi, gugudan, momoland,
                    kard, goldenchild, onf, wannaone, jbj,
                    rainz, ace, theboyz, dreamcatcher, pristin,
                    wekimeki, tripleh, straykids, ateez, fromis9,
                    gidle, loona, izone, gwsn, oneus,
                    verivery, txt, ab6ix, cix, x1,
                    cherrybullet, itzy, everglow, bvndit, rocketpunch,
                    hinapia, threeye, alexa, mcnd, dkb,
                    too, cravity, cignature, aespa],

             'Type': ['group', 'group', 'group', 'group','group', 
                    'group', 'group', 'group','group', 'group', 
                    'group', 'group', 'group', 'solo', 'group', 
                    'solo', 'solo', 'solo', 'solo', 'group', 
                    'group', 'group', 'group', 'group', 'group', 
                    'solo', 'group', 'group', 'group', 'group',
                    'group', 'group', 'solo', 'group', 'group', 
                    'group', 'group', 'group', 'solo', 'solo', 
                    'group', 'group', 'group', 'group', 'group', 
                    'group', 'group', 'group', 'group', 'solo',
                    'group', 'group', 'group', 'group', 'group', 
                    'group', 'group', 'group', 'group', 'solo', 
                    'group', 'group', 'group', 'group', 'solo',
                    'group', 'group', 'group', 'group', 'group',
                    'group', 'group', 'group', 'group', 'group',
                    'group', 'group', 'solo', 'solo', 'group',
                    'group', 'group', 'group', 'group', 'group',
                    'group', 'group', 'group', 'group', 'group',
                    'group', 'group', 'group', 'group', 'group',
                    'group', 'group', 'group', 'group', 'group',
                    'group', 'group', 'group', 'group', 'group',
                    'group', 'group', 'group', 'group', 'group',
                    'group', 'group', 'group', 'group', 'group',
                    'group', 'group', 'group', 'group', 'group',
                    'group', 'group', 'group', 'group', 'group',
                    'group', 'group', 'group', 'group', 'group',
                    'group', 'group', 'group', 'group', 'group',
                    'group', 'group', 'group', 'group', 'group',
                    'group', 'group', 'group', 'group', 'group',
                    'group', 'group', 'solo', 'group', 'group',
                    'group', 'group', 'group', 'group'],

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
                    'coed', 'male', 'male', 'male', 'female',
                    'female', 'female', 'female', 'female', 'female',
                    'coed', 'female', 'female', 'female', 'female',
                    'female', 'female', 'female', 'female', 'female',
                    'male', 'male', 'male', 'male', 'male',
                    'male', 'male', 'male', 'female', 'female',
                    'female', 'female', 'female', 'female', 'female',
                    'female', 'female', 'male', 'male', 'male',
                    'male', 'male', 'male', 'male', 'male',
                    'male', 'male', 'male', 'male', 'male',
                    'male', 'female', 'female', 'female', 'female',
                    'coed', 'male', 'male', 'male', 'male',
                    'male', 'male', 'male', 'female', 'female',
                    'female', 'coed', 'male', 'male', 'female',
                    'female', 'female', 'female', 'female', 'male',
                    'male', 'male', 'male', 'male', 'male',
                    'female', 'female', 'female', 'female', 'female',
                    'female', 'female', 'female', 'male', 'male',
                    'male', 'male', 'female', 'female'], 

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
                    2.5, 2.5, 2.5, 2.5, 2.5,
                    2.5, 2.5, 2.5, 2.5, 2.5,
                    2.5, 2.5, 2.5, 2.5, 2.5,
                    2.5, 2.5, 2.5, 2.5, 2.5,
                    3, 3, 3, 3, 3,
                    3, 3, 3, 3, 3,
                    3, 3, 3, 3, 3,
                    3, 3, 3.5, 3.5, 3.5,
                    3.5, 3.5, 3.5, 3.5, 3.5,
                    3.5, 3.5, 3.5, 3.5, 3.5,
                    3.5, 3.5, 3.5, 3.5, 3.5,
                    3.5, 3.5, 3.5, 3.5, 3.5,
                    3.5, 3.5, 3.5, 3.5, 3.5,
                    3.5, 3.5, 4, 4, 4,
                    4, 4, 4, 4, 4,
                    4, 4, 4, 4, 4,
                    4, 4, 4, 4, 4,
                    4, 4, 4, 4, 4,
                    4, 4, 4, 4],

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
                    2010, 2011, 2011, 2011, 2011,
                    2011, 2011, 2011, 2011, 2011,
                    2011, 2012, 2012, 2012, 2012,
                    2012, 2012, 2012, 2012, 2013,
                    2012, 2012, 2012, 2012, 2012,
                    2013, 2014, 2014, 2014, 2014,
                    2014, 2015, 2015, 2015, 2015,
                    2015, 2015, 2015, 2015, 2015,
                    2015, 2015, 2015, 2015, 2016,
                    2016, 2016, 2016, 2016, 2016,
                    2016, 2016, 2016, 2016, 2016,
                    2016, 2017, 2017, 2017, 2017,
                    2017, 2017, 2017, 2017, 2017,
                    2017, 2017, 2018, 2018, 2018,
                    2018, 2018, 2018, 2018, 2019,
                    2019, 2019, 2019, 2019, 2019,
                    2019, 2019, 2019, 2019, 2019,
                    2019, 2019, 2019, 2020, 2020,
                    2020, 2020, 2020, 2020]})

print(artist_df)
artist_df.to_csv('artist_df.csv')