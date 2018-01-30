class node:
    def __init__(self,datum):
        self.data = datum
        #### data structure attributes ####
        self.key = None
        self.color = None
        self.p = None
        self.right = None
        self.left = None

class red_black:
    def __init__(self):
        
        self.nil = node(None)
        self.nil.p = self.nil
        self.nil.right = self.nil
        self.nil.left = self.nil
        self.nil.color = None

        self.root = self.nil

    def left_rotate(self,x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.p = x
        y.p = x.p
        if x.p == self.nil:
            self.root = y
        elif x.p.left == x:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y

    def right_rotate(self,y):
        x = y.left
        y.left = x.right
        if x.right:
            x.right.p = y
        x.p = y.p
        if y.p == self.nil:
            self.root = x
        elif y.p.left == y:
            y.p.left = x
        else:
            y.p.right = x
        x.right = y
        y.p = x

    def insert(self,z):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == self.nil:
            print(1)
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = 'red'
        self.rb_insert_fixup(z)
        
    def rb_insert_fixup(self,z):
        while z.p.color == 'red':
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.color == 'red':
                    z.p.color = 'black'
                    y.color = 'black'
                    z.p.p.color = 'red'
                    z = z.p.p
                elif z == z.p.right:
                    z = z.p
                    self.left_rotate(z)
                z.p.color = 'black'
                z.p.p.color = 'red'
                self.right_rotate(z.p.p)
            else:
                y = z.p.p.left
                if y.color == 'red':
                    z.p.color = 'black'
                    y.color = 'black'
                    z.p.p.color = 'red'
                    z = z.p.p
                elif z == z.p.right:
                    z = z.p
                    self.right_rotate(z)
                z.p.color = 'black'
                z.p.p.color = 'red'
                self.left_rotate(z.p.p)
        self.root.color = 'black'
        
#################################################
            #### Test Code ####
#################################################




node1 = node(1)
node2 = node(2)
node1.key = 13
node2.key = 32

rb = red_black()
rb.insert(node1)



rb.insert(node2)
