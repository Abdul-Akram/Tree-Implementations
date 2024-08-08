class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class un_bi_tree:
    def __init__(self):
        self.root=None
    def add(self,data):
        node=Node(data)
        if self.root==None:
            self.root=node
            return True
        self.find_node(data,self.root)
        
    def find_node(self,data,node):
        if node.left==None:
            node.left=Node(data)
        elif node.right==None:
            node.right=Node(data)
        else:
            self.find_node(data,node.left)
            
    def Dispaly(self,level=0,node=None):
        if node is None:
            node=self.root
        print("   "*level+str(node.data))
        if node.left is not None:
            self.Dispaly(level+1,node.left)
        if node.right is not None:
            self.Dispaly(level+1,node.right)
    
    def Remove(self,data):
        if self.root is None:
            print("Tree is Empty")
            return False
        elif self.root.data == data:
            self.root=None
            return True
        self._remove_node(data,self.root)
        
    def _remove_node(self,data,node):
        if node.left and node.left.data == data:
            node.left=None
            return True
        elif node.right and node.right.data == data:
            node.right=None
            return True
        if node.left:
            self._remove_node(data,node.left)
            return True
        elif node.right:
            self._remove_node(data,node.right)
            return True
        return False        
        
    def Search(self,data):
        if self.root is None:
            print("Tree is Empty")
            return False
        elif self.root.data==data:
            print(f"{data} found at 0 position in the tree")
            return True
        return self._search_position(data,self.root)
        
        
    def _search_position(self,data,node,position=1):
        if node.left and node.left.data==data:
            print(f"{data} found at {position} left branch in the tree")
            return True
        elif node.right and node.right.data==data:
            print(f"{data} found at {position} right branch in the tree")
            return True
        if node.left:
            self._search_position(data,node.left,position+1)     
            return True
        elif node.right:
            self._search_position(data,node.right,position+1)
            return True
        print(data,"<- Not Found")
        return False
    
                   
bi_tree=un_bi_tree()
bi_tree.add(2)
bi_tree.add(3)
bi_tree.add(4)
bi_tree.add(5)
bi_tree.add(6)
bi_tree.add(6)
bi_tree.add(2)
bi_tree.add(6)
bi_tree.add(2)
bi_tree.Dispaly()
# bi_tree.Remove(4)
print("\n")
bi_tree.Dispaly()
bi_tree.Search(6)