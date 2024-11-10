class BTnode:
    def __init__(self, d, l , r):
        # d : Data
        # l : Left child
        # r : right child
        
        
        self.data = d
        self.left = l
        self.right = r
none = 0;

t1 = BTnode(51, none, none)
t2 = BTnode(51, none, t1)
t3 = BTnode(2, none, none)
t4 = BTnode(42, t3, none)
t5 = BTnode(8, none, none)
t6 = BTnode(8, t4, t5)
t = BTnode(2, t2, t6)


# tree search

def search(t, d):
    if t == None: return False
    if t.data == d: return True
    if search(t.left , d): return True
    return search(t.right, d);



# This is a tree structure
def newMethod():
    input("Please add a number from 0 to 9")
    
    val = input
    
    if (val > 2):
        print("Bigger than 2")
    elif (val < 2):
        print("Less than 2")
    else:
        print("This a 2")
    print("Hello")

newMethod()
