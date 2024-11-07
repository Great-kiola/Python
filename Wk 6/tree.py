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


print(t);