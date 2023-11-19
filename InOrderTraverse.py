class Solution(object):
    def inorderTraversal(self, root):
        self.arr = []
        def Traverse(root):
            if root == None:
                return
            Traverse(root.left)
            self.arr += [root.val]
            Traverse(root.right)
            return self.arr
            
        Traverse(root)
        return self.arr