from tkinter import *
import time
import random
root=Tk()
root.title("N QUEENS")
root.iconbitmap('GBP.ico') 
btn,board1,board,cc,ans,count=[],[],{},0,[],0

photo    = PhotoImage(file='''tata.png''')
filename = PhotoImage(file = "win.png")
fn       = PhotoImage(file = "Queen.png")
sol      = PhotoImage(file = "sol.png")
res      = PhotoImage(file = "res.png")

def init():
    for key in ['queen','row','col','nwtose','swtone']:
        board[key] = {}
    for i in range(8):
        board['queen'][i] = -1
        board['row'][i] = 0
        board['col'][i] = 0
    for i in range(-7,8):
        board['nwtose'][i] = 0
    for i in range(17):
        board['swtone'][i] = 0
        
def addqueen(i,j):
     board['queen'][i] = j
     board['row'][i] = 1
     board['col'][j] = 1
     board['nwtose'][j-i] = 1
     board['swtone'][j+i] = 1
     
def undoqueen(i,j):
     board['queen'][i] = -1
     board['row'][i] = 0
     board['col'][j] = 0
     board['nwtose'][j-i] = 0
     board['swtone'][j+i] = 0
     
def placequeen(i):
    for j in range(8):
        if free(i,j):
            addqueen(i,j)
            if i == 7: printboard()
            else: placequeen(i+1)
            undoqueen(i,j)
          
def printboard():
     asa=[]
     for row in sorted(board['queen'].keys()):
         asa.append(board['queen'][row])
     ans.append(asa)
 

def free(i,j):
     return(board['row'][i] == 0 and board['col'][j] == 0 and board['nwtose'][j-i] == 0 and board['swtone'][j+i] == 0)
    
def reset():
    global cc,count,start
    cc,count,start=0,0,time.time()
    init()    
    for i in range(8):
        for j in range(8):
            board1[i][j]=0
            if(i+j)%2==0: col="white"
            else: col='black'
            btn[i][j].configure(image='',height=5,width=10,bg=col)
    canvas.create_rectangle(550,700,100,400,fill='black') 
    
def showall():
    global count
    reset()
    ran=random.randint(0,len(ans)-1)
    ase=ans[ran]
    for i in range(8):
        b=btn[i][ase[i]]
        b.configure(image=photo,height=75,width=72)
    count=8
    
def gui(event):
    global count,cc
    b=event.widget
    x=str(b.cget('textvariable'))
    x,y=int(x[0]),int(x[2])
    if(x+y)%2==0: col="white"
    else: col='black'

    if count >= 8 and board1[x][y]==0 :return
    if board1[x][y]==0:    
        b.configure(image=photo,height=75,width=72)
        if free(x,y)== False: b.configure(bg='red')
        else :
            cc+=1
            addqueen(x,y)
        count+=1
        board1[x][y]=1
    else :
        if b.cget('bg')== 'black' or b.cget('bg')== 'white': 
            undoqueen(x,y)
            if free(x,y)==True : cc-=1
        b.configure(image='',height=5,width=10,bg=col)
        count-=1
        board1[x][y]=0

    if cc == 8 :
        canvas.create_image(500, 550, anchor=E, image=filename)
        st=(time.time()-start)
        st="Time required is : "+str(round(st,1))+' seconds'
        canvas.create_text(350, 640, font=("Times new Roman", 20), text= st,fill='#fffc9c')
        for i in range(8):
            for j in range(8) : board1[i][j]=0
            
'''--------------------Main------------------------'''

for i in range(8):
    board1.append([0,0,0,0,0,0,0,0])
    b=[]
    for j in range(8):
        if(i+j)%2==0: col="white"
        else: col='black'
        b.append(Button(bg=col,height=5,width=10,textvariable=[i,j]))
        b[j].grid(row=i,column=j)
        b[j].bind("<ButtonRelease-1>",gui)
    btn.append(b)
 
init()
placequeen(0)
printboard()
ans=ans[:-1]
init()

canvas = Canvas(root, width = 710, height = 674, bg ="black")
canvas.grid(row=0,column=8,rowspan=8)
imag = canvas.create_image(550, 170, anchor=E, image=fn)
st="Place 8 Queens on the Chess Board"
canvas.create_text(345, 300, font=("Old English Text MT", 20), text= st,anchor=N,fill='#fffc9c')
st='''Condition : None of the Queen's path should overlap '''
canvas.create_text(345, 340, font=("Times New Roman", 10), text= st,anchor=N,fill='white')

button1 = Button( command=showall,  anchor = W)
button1.configure(image=sol,width = 150,height=50,bg='black', relief = FLAT,activebackground='black')
canvas.create_window(180, 370, anchor=NW, window=button1)

button2 = Button( command=reset,  anchor = W)
button2.configure(image=res,width = 150,height=50,bg='black', relief = FLAT,activebackground='black')
canvas.create_window(360, 370, anchor=NW, window=button2)

start=time.time()
root.mainloop()
