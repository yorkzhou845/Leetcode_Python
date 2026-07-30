#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#iterative        
class Solution:#like a BFS
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        root = TreeNode()
        queue1 = [root]
        queue2 = [0, len(nums) - 1]#hold th indexes of nums

        while (queue1):
            node = queue1.pop(0)
            p1 = queue2.pop(0)
            p2 = queue2.pop(0)
            mid = (p2 + p1) // 2 #absolute average
            node.val = nums[mid]
            if (p1 <= mid - 1):#left pointer is still good
                node.left = TreeNode()
                queue1.append(node.left)
                queue2.append(p1)#append left to right
                queue2.append(mid - 1)
            if (p2 >= mid + 1):#right pointer is still good
                node.right = TreeNode()
                queue1.append(node.right)
                queue2.append(mid + 1)#append left to right
                queue2.append(p2)
        return root
        
#recursion
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
            if not nums: return None

            middle = len(nums) // 2
            root = TreeNode(nums[middle])

            root.left = self.sortedArrayToBST(nums[0:middle])#exclude the middle
            root.right = self.sortedArrayToBST(nums[middle + 1:])
            return root



