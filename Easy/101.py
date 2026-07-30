# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:#recursion
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:#each time must return a True or False
        def mirror (left, right):
            if left is None and right is None:
                return True
            elif left is None or right is None:
                return False
            
            return (
                left.val == right.val
                and mirror(left.left, right.right)
                and mirror(left.right, right.left)
            )
        
        return mirror(root.left, root.right)
            

class Solution:  # iterative
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        deq1 = [root.left, root.right]  # nodes on the current level
        deq2 = []  # matched nodes whose children will be checked next

        while deq1:#precheck
            # Compare nodes from the outside moving inward
            while deq1:
                left = deq1.pop(0)
                right = deq1.pop()

                # Both positions are empty, so they match
                if left is None and right is None:
                    continue

                # Only one position is empty
                if left is None or right is None:
                    return False

                # Values do not match
                if left.val != right.val:
                    return False

                # Save matching nodes so their children can be added
                deq2.insert(0, left)
                deq2.append(right)

            # Construct the next level from left to right
            while deq2:#still need to insert nulls
                left = deq2.pop(0)
                right = deq2.pop()

                deq1.insert(0, left.right)
                deq1.insert(0, left.left)

                deq1.append(right.left)
                deq1.append(right.right)

        return True

class Solution:  # iterative
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        deq = [root.left, root.right]

        while deq:
            left = deq.pop(0)#instead of of the deque holding the structure of the tree, keeps nodes that should be the same next to each other
            right = deq.pop(0)
            
            if left is None and right is None:#this is fine keep going
                continue
            elif left is None or right is None:
                return False
            elif left.val == right.val:
                deq.append(left.left)
                deq.append(right.right)
                deq.append(left.right)
                deq.append(right.left)
            else:
                return False
        return True
    
