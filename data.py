ver = 'v0.9'

# Very easy questions
e1 = '2+2'
e2 = '3+2'
e3 = '5+5'
e4 = '4+8'
e5 = '7+3'
e6 = '8+4'
e7 = '2-2'
e8 = '3-2'
e9 = '5-5'
e10 = '8-3'
e11 = '7-3'
e12 = '8-4'
e13 = '3+3'
e14 = '6+6'
e15 = '12+6'
e16 = '5+5'
e17 = '10+10'
e18 = '20-15'
e19 = '30-15'
e20 = '20-7'

# Easy questions
m1 = '9x5'
m2 = '5x8'
m3 = '3x8'
m4 = '2x5'
m5 = '4x6'
m6 = '6x6'
m7 = '5/5'
m8 = '8/2'
m9 = '48/8'
m10 = '45/3'
m11 = '88/11'
m12 = '33890/100 (please use ".")'
m13 = '24/6'
m14 = '24/4'
m15 = '25/5'
m16 = '3x3'
m17 = '9x9'
m18 = '30/2'
m19 = '5x4'
m20 = '20/5'

# Medium questions
h1 = '3^2'
h4 = '3^3'
h5 = '4^2'
h6 = '2^5'
h7 = '2^10'
h8 = '2^11'
h9 = '2^3'
h10 = '2^4'
h11 = '2^5'
h12 = '2^6'
h13 = '2^7'
h14 = '2^8'
h15 = '2^9'

# Hard questions
rh1 = '8!'
rh2 = '4!'
rh3 = '5!'
rh4 = '10!'
rh5 = '6!'
rh6 = '9!'
rh7 = '2!'

# Extreme questions
ex1 = '2y = 10 x 5 + 20 + 0.75y'
ex2 = '2y^2 = 2x4 (+)'
ex3 = '6y + 5 = 10 - 2y'
ex4 = '2y^2 = 2x4 (-)'
ex5 = '6y = 2x2+4-y (Please use common fraction for example 3/2 etc. no 1 1/2)'

# SuperSecretLevel questions
ss1 = '5!'
ss2 = '2!'
ss3 = '4!'
ss4 = '3+5'
ss5 = '2+2'

#Ulta rare level
ur1 = '6+6'
ur2 = '21-5'
ur3 = '8-5'

#Season impossible level
si1 = '@=@'
si2 = '#8#'
si3 = '()8!)'
si4 = '(8!)'

#Impossible level
i1 = '@Y=#+$' #2y+3=4
i2 = '%Y=*6@+@!#&' #6y+8^2 = 2137
i3 = '@X@=@+Y' #2x2+2 = y

ulta_rare = [ur1,ur2,ur3]
easy = [e1 ,e2 ,e3 ,e4 ,e5 ,e6 ,e7 ,e8 ,e9 ,e10 ,e11 ,e12,e13,e14,e15,e16,e17,e18,e19,e20] # Very easy
easy_mode = [e1 ,e2 ,e3 ,e4 ,e5 ,e6 ,e7 ,e8 ,e9 ,e10 ,e11 ,e12,e13,e14,e15,e16,e17,e18,e19,e20,m1 ,m2 ,m3 ,m4 ,m5 ,m6 ,m7 ,m8 ,m9 ,m10 ,m11 ,m12,m13,m14,m15,m16,m17,m18,m19,m20] # Easy mode
medium = [m1 ,m2 ,m3 ,m4 ,m5 ,m6 ,m7 ,m8 ,m9 ,m10 ,m11 ,m12,m13,m14,m15,m16,m17,m18,m19,m20] # Easy
hard = [h1,h4 ,h5 ,h6 ,h7 ,h8,h9,h10,h11,h12,h13,h14,h15] # Medium
real_hard = [rh1,rh2,rh3,rh4,rh5,rh6,rh7] # Hard
extreme = [ex1, ex2, ex3, ex4, ex5] # Very hard / Extreme
super_secret = [ss1,ss2,ss3,ss4,ss5]
season_impossible = [si1,si2,si3,si4]
impossible = [i1,i2,i3] # Impossible
mes = [m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12]
eses = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12]

random = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,11 ,12 ,13 ,14 ,15 ,16 ,17 ,18 ,19 ,20 ,21 ,22 ,23 ,24 ,25 ,26 ,27 ,28 ,29 ,30
          ,31 ,32 ,33 ,34 ,35 ,36 ,37 ,38 ,39 ,40 ,41 ,42 ,43 ,44 ,45 ,46 ,47 ,48 ,49 ,50]

secret_level = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]

p1 = 10
p2 = 20
p3 = 50
p4 = 100
p5 = 200
p6 = 500
points=[p1,p2,p3,p4,p5,p6]


#Splash

n1 = 'Good luck!'
n2 = 'GG'
n3 = 'Are you good?'
n4 = f'MathsQuiz {ver}'
ns=[n1,n2,n3,n4]

ext1 = 'EXTREME'
ext2 = 'You wont win!'
ext3 = f'MathsQuiz EXTREME {ver}'
exts=[ext1,ext2,ext3]

eas1 = 'Good luck'
eas2 = 'You will win!'
eas3 = 'You are good in maths'
eas4 = f'MathsQuiz easy {ver}'
eass = [eas1,eas2,eas3,eas4]

tut1 = 'Tutorial'
tut2 = f'MathsQuiz tutorial {ver}'
tut3 = 'MathsQuiz is easy'
tut = [tut1,tut2,tut3]

s1 = 'Autumn season'
s2 = 'Happy autumn'
ss=[s1,s2]










k1 = '81fc3r'
pa1 = 'root'
ni1 = 'Root'
k2 = '2186fn'
pa2 = '883'
ni2 = 'user1'
k3 = 'fccppn'
pa3 = '1111'
ni3 = 'user3'
k4 = '8c652n'
pa4 = '2587'
ni4 = 'user3'

mu1 = 1.8
mu2 = 1
mu3 = 1.7
mu4 = 1.1