import random
from collections import deque
import itertools

seen=set()
def dfs(n,g):
    if n not in seen:
        if g == graph[g]
            print(n,end=" ")
        seen.add(n)
        for x in graph[n]:
            if dfs(x,g):
                    return True
dfs("A","G")

def bfs(n):
    seen=set()
    queue=deque[["A"]]
    while queue:
        n = queue.popleft()
        print(n,end=" ")
        for x in graph[n]:
            if x not in seen:
                seen.add(x)
                queue.append(x)
bfs("A")

def toh(n,S,A,D):
    if n==1:
        print(f"moved 1 disk from {S} to {D}")
    toh(n-1,S,D,A)
    print(f"moved {n}disk from {S} to {D}")
    toh(n-1,A,S,D)
toh(3,"S","A","D")


suits=["Heart","Diamond","Spade","Club"]
ranks=["1","2","3","4","5","6","7","8","9","10","J","K","Q"]
deck=[]
for suit in suits:
    for rank in ranks:
        d = rank+" of "+suit
        deck.append(d)
random.shuffle(deck)
print(deck)

n=4
board=[[0]*n for _ in range(n)]
def safe(row,col):
    for i in range(row):
        if board[i][col]==1:
            return False
        if col-(row-i) >=0 and board[i][col-(row-i)]==1:
            return False
        if col+(row-i) <n and board[i][col+(row-i)]==1:
            return False
    return True

def solve(row):
    if row==n:
        return True
    for col in range(n):
        if safe(row,col):
            board[row][col]=1
            if solve(row+1):
                return True
            board[row][col]=0
    return False

solve(0)
for row in board:
    print(row)




var=["A","B","C","D"]
colors=["RED","BLUE","GREEN","YELLOW"]
all_assignment=itertools.product(colors,repeat=len(colors))

def valid(i):
    A,B,C,D = i
    return (A!=B) and (A!=C) and (A!=D) and (B!=C) and (B!=D) and (C!=D)

solut=[]
for i in all_assignments:
    solut.append(dict(zip(variables,i)))

for s in solut:
    print(s)




board=[' ' for _ in range(9)]
player='X'
def boardy():
    print(f"| {board[0]} | {board[1]} | {board[2]}|")
    print(f"| {board[3]} | {board[4]} | {board[5]}|")
    print(f"| {board[6]} | {board[7]} | {board[8]}|")

def win(p):
    return(
        (board[0]==p and board[1]==p and board[2]==p)or
        (board[3]==p and board[4]==p and board[5]==p)or
        (board[6]==p and board[7]==p and board[8]==p)or
        (board[0]==p and board[3]==p and board[6]==p)or
        (board[1]==p and board[4]==p and board[7]==p)or
        (board[2]==p and board[5]==p and board[8]==p)or
        (board[0]==p and board[4]==p and board[8]==p)or
        (board[2]==p and board[4]==p and board[6]==p)or
        )

def tie():
    return ' ' not in board

def game():
    global player
    while True:
        board()
        m = int(input("Enter value between 0-8: "))
        if 0<= m <=8 and board[m] ==' ' :
            board[m]=player
            if win(player):
                boardy()
                print(f"Player {player} wins!")
                break
            elif tie():
                boardy()
                print("TIE!")
                break
            if player=='X':
                player='O'
            else:
                player='X'
        else:
            print("Invalid Move")
            
game()


visit = set()
queue = deque([(0,0)])
while queue:
    a,b = queue.popleft()
    if (a,b) not in visit:
        print((a,b))
        visit.add((a,b))
    states=[
            (4,b),
            (a,3),
            (0,b),
            (a,0)
        ]
    if a==2 and b==2:
        print("Goal state is reached!")
        break
    amount=min(a,3-b)
    states.append((a-amount,b+amount))
    
    amount=min(b,4-a)
    states.append(a+amount,b-amount)

    for state in states:
        if state not in visit:
            visit.add(state)

node=input("Enter start node: ")
goal=input("Enter goal node: ")
def hue(x):
    return graph[x][1]
while True:
    if node != goal:
        print(f"{node} -> ",end=" ")
        neighbor = graph[node][0]
        node = min(neighbor,key=hue)
    else:
        print(goal)
        break


node=input("Enter start node: ")
goal=input("Enter goal node: ")
while node!=goal:
    
