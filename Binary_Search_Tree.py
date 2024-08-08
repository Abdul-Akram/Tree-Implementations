from typing import Any


class BTSNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BSTRee():
    def __init__(self):
        self.root=None
    def add(self,data):
        if self.root is None:
            self.root=BTSNode(data)
        return self._add_node(data,self.root)
            
    def _add_node(self,data,node):
        if node.data > data:
            if node.left is None:
                node.left=BTSNode(data)
            else:
                self._add_node(data,node.left)
        elif node.data < data:
            if node.right is None:
                node.right=BTSNode(data)
            else:
                self._add_node(data,node.right)
                
    def Display(self,level=0,node=None):
        if self.root is None:
            print("Tree is Empty")
            return
        
        if node is None:
            node=self.root
        print(" "*level+str(node.data))
        if node.left:
            self.Display(level+1,node.left)
        if node.right:
            self.Display(level+1,node.right)
    
    def Remove(self,data):
        if self.root is None:
            print("Tree is Empty")
            return
        elif self.root.data == data:
            self.root = None
            return
        self._remove_node(data,self.root)
    
    def _remove_node(self,data,node):
        if node.left and node.left.data == data:
            node.left = None
            return
        
        elif node.right and node.right.data == data:
            node.right = None
            return
        elif data < node.data:
            self._remove_node(data,node.left)
        elif data > node.data:
            self._remove_node(data,node.right)
    
    def in_order_traversal(self):
        result=[]
        self._in_oreder(self.root,result)
        print(result)
        
    def _in_oreder(self,node,result):
        if not node:
            return None
        else:
            self._in_oreder(node.left,result)
            result.append(node.data)
            self._in_oreder(node.right,result)
            
            
    def Search(self,data):
        if self.root is None:
            print("Tree is Empty")
            return
        if self.root.data == data:
            print(f"{data} at root of the tree")
            return 
        
        return self._search_node(self.root,data)       
        
    def _search_node(self,node,data,position=1):
        if node is None:
            print(f"{data} not found in the tree")
            return
        
        if node.left and node.left.data == data:
            print(f"{data} found at left of {node.data} at position {position}")
            return
        elif node.right and node.right.data == data:
            print(f"{data} found at right of {node.data} at position {position}")
            return
        elif data < node.data:
            self._search_node(node.left,data,position+1)
        elif data > node.data:
            self._search_node(node.right,data,position+1)
            
        
        
        
bst=BSTRee()
bst.add(45)
bst.add(10)
bst.add(50)
bst.add(9)
bst.add(11)
bst.add(46)
bst.add(51)
bst.Display()
bst.Remove(50)
print("\n")
bst.Display()
bst.Search(51)
# bst.in_order_traversal()