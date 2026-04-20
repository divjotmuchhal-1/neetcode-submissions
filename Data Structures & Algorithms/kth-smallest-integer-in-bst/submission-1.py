# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def in_order_traversal(node: Optional[TreeNode]):
            if node is None:
                return []
            # Traverse left subtree, visit node, then right subtree
            return in_order_traversal(node.left) + [node.val] + in_order_traversal(node.right)
        
        # Get the sorted list of all node values in in-order
        sorted_values = in_order_traversal(root)
        
        # Return the k-th smallest element (1-based index)
        return sorted_values[k - 1]

        