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

""" Does not work because height loses order
class Solution:#Does not work because height loses order. Need to do an inorder traversal where pass through each node <= 2 times. First pass checks if the childrens height are calculated (seen). If not, push into queueu and until next pass
  def isBalanced(self, root: Optional[TreeNode]) -> bool:
    seen = {root: False}#track whether the node has been seen yet. Its a stack
    height = []#stack

    while seen:
        node, b = seen.popitem(0)

        if b == False: #if new discovered node
            if not node.left and not node.right:#leaf node
                height.append(0) 
            else:#somehwere in th eemiddle. Do not need to add a height because no compuation
                seen[node] = True#the node has been visited but no height yet
            if node.left:# has a left
                seen[node.left] = False
            if node.right: #has a right
                seen[node.right] = False
        else:#the node has been visited beofre
            left = height.pop()
            right = height.pop()
            if (abs(left - height) >= 1): return False
            else: 
                height.append(max(left, right) + 1)#add one more to the max

    return True
"""
class Solution:#Need to do an inorder traversal where pass through each node <= 2 times. First pass checks if the childrens height are calculated (seen). If not, push into queueu and until next pass
  def isBalanced(self, root: Optional[TreeNode]) -> bool:
    if root is None:
        return True
    seen = {root: False}#stack track whether the node has been seen yet
    height = {None: 0}#stack holding the node and the associated height

    while seen:
        node, b = seen.popitem()

        if not b: #if new discovered node
            seen[node] = True#the node has been visited but no height yet
            if node.right: #has a right
                seen[node.right] = False #since stack need to push the right side first
            if node.left:# has a left
                seen[node.left] = False
        else:#the node has been visited beofre
            left = node.left
            right = node.right
            difference = abs(height[left] - height[right])
            if (difference > 1): return False

            height[node] = max(height[left], height[right]) + 1
    return True

    
                




        


              
              
        


        