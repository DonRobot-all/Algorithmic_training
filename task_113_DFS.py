class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root: TreeNode, targetSum: int) -> list[list[int]]:
    result = []

    def dfs(node, path, curr_sum):
        if node is None:
            return

        path.append(node.val)
        curr_sum += node.val

        if not node.left and not node.right and curr_sum == targetSum:
            result.append(list(path))

        dfs(node.left, path, curr_sum)
        dfs(node.right, path, curr_sum)

        path.pop()

    dfs(root, [], 0)
    return result
