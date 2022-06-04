import random
from graphics import*
file = []
words = []
answers = []
Title = Text(Point(200,20),"WORDLE")

with open('allowed-guesses.txt','r') as f:
    file = f.readlines()

for x in file:
    words.append(x[:5])


with open('answers.txt','r') as f:
    file = f.readlines()

for x in file:
    answers.append(x[:5])
check=False

random = random.randint(0,len(answers))
ans = answers[random]
print(ans)
print('Wordle')

win = GraphWin("Window", 400, 500)
Title.draw(win)

boxes = []
for y in range(0,6):
    for x in range(0,5):
        boxes.append(Rectangle(Point(50*x + 70,50+y*50), Point(50*x + 120,100+y*50)))
        boxes[x+5*y].draw(win)
n=-1
warn=False
while(True):
    letters=True
    bank=False
    textEntry = Entry(Point(198,400),10)
    textEntry.draw(win)
    win.getMouse()
    text = []
    colors = []
    guess =  textEntry.getText()
    for x in range(5):
            if(guess[(x):(x+1)]in'abcdefghijklmnopqrstuvwxyz '==False):
                letters = False
    for x in words:
            if(guess==x):
                bank = True
    guessCount=[]
    ansCount=[]
    yellows=0
    greens=0
    white=0
    if(len(guess)==5):
        for x in range(0,len(guess)):
            ansCount.append(ans.count(guess[x:x+1]))
            guessCount.append(guess.count(guess[x:x+1]))
            if(guess[(x):(x+1)] == ans[(x):(x+1)]):
                colors.append('Green')
            elif(guess[x:x+1] in ans != False):
                colors.append('Yellow')
            else:
                colors.append('White')
   
          
    if(len(guess)==5 and letters and bank):
        
        n=n+1
        for x in range (0,len(guess)):
            text.append(guess[x:x+1].capitalize())
            output = Text(Point((boxes[x].getP1()).getX()+24, boxes[x].getP1().getY()+24+(n*50)), text[x])
            if(colors[x]!='White'):
                boxes[x+n*5].setFill(colors[x])
            output.draw(win)
    else:
        warn=True
        Warn = Text(Point(200,450), "Your entry must be a 5 letter word only containing")
        Warn.draw(win)
        Warn1 = Text(Point(200,470), "letters and must be in the word bank")
        Warn1.draw(win)
    if(guess==ans):
            if(warn != False):
                Warn.undraw()
                Warn1.undraw()
            wins = Text(Point(200, 450), "Yeahh nice job!")
            wins.draw(win)
            break;
    if(n>=5):
        if(warn != False):
            Warn.undraw()
            Warn1.undraw()
        fail = Text(Point(200, 450), "The word was "+ans)
        fail.draw(win)
        break;
    colors = []
    
    
                
                







            

        




