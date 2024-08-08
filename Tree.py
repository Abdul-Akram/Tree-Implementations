class TreeNode:
     def __init__(self,data):
         self.data=data
         self.children=[]
class Tree:
    def __init__(self):
        self.root=None
    def add(self,data,parent=None):
        node=TreeNode(data)
        if self.root is None:
            self.root=node
            return
        Parentnode=self.findParent(parent,self.root)
        if Parentnode:
            Parentnode.children.append(node)
        else:
            print("Parent node not found")
    def findParent(self,data,node):
        if node.data == data:
            return node
        for child in node.children:
            nodeFound=self.findParent(data,child)
            if nodeFound:
                return nodeFound
        return None
        
        
    def print(self,node,level=0):
        if node is None:
            return
        print(" "*level+str(node.data))
        for child in node.children:
            self.print(child,level+1)
tree=Tree()
tree.add(2)
tree.add(data=10,parent=2)
tree.add(data=5,parent=2)
tree.add(data=11,parent=10)
tree.print(tree.root)