# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:#recursion
    def height(self, root: Optional[TreeNode]) -> int:#finds the height of a tree
        if root is None: return 0
        return max(self.height(root.left), self.height(root.right)) + 1
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:#use the height function to see if it is balanced
        if root is None: return True
        return (
            abs(self.height(root.left) - self.height(root.right)) <= 1 
            and self.isBalanced(root.left) 
            and self.isBalanced(root.right)
        )

class Solution:#wrong iterative version becasue cannot blindly add 1 to every height before
  def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True
        stack1 = [root]#hold the nodes
        stack2 = [0]#hold the heights
        while (stack1):
            node = stack1.pop()
            if (root.left or root.right):
                for i, height in enumerate(stack1):
                    stack2[i] = height + 1
            if root.left:
                stack1.append(root.left)
                stack2.append(0)
            if root.right:
                stack1.append(root.right)
                stack2.append(0)

        for i, val in enumerate(stack2[::2]):
            if abs(stack2[i] - stack2[i + 1]) >= 1: return False

        return True               


        