# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return []
        
        return(
            self.inorderTraversal(root.left)
            + [root.val]
            + self.inorderTraversal(root.right)
        )

class Solution:#need to know is th eleft subtree already done so this does not work
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []#holds nodes reacehd while walking down the left edge of a subtree so can reverse later
        final = []#this is the return list

        curr = root
        while (stack and curr is not None):#while the stack exists and the curr is not empty
            if (curr.left is not None):#if there is a left, go down the left side
                stack.append(curr)#push the root of a tree with a left subtree
                curr = curr.left
            elif (curr.left == None):#if the current left is none, pop the last left node and push it onto final 
                final.append(curr.val)
                curr = stack.pop()
                #lines below are the proiblem because in the next iteration, it will want to go down the left side again if there is one
                if (curr.right is not None):#if there is a right node given the left node is none
                    curr = curr.right#go down the right side

        return final

class Solution:#need to know is th eleft subtree already done so this does not work
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []#holds nodes reacehd while walking down the left edge of a subtree so can reverse later
        final = []#this is the return list

        curr = root
        while (stack or curr is not None):#while the stack exists or  the curr is not empty
            if (curr is not None):#as long as the node exists, go down the left side. 
                stack.append(curr)#push every node onto the stack (even right side)
                curr = curr.left
            elif (curr is None):#if the current  is none, pop the last left node and push it onto final 
                curr = stack.pop()
                final.append(curr.val)
                curr = curr.right#go down the right side
        return final
            
            