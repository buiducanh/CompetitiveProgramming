class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def post_order(root):
    if root == None:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.val)

from sys import stdin
input = open("in.txt", "r")
preorder = []
while True:
    try:
        a = int(input.readline())
        preorder.append(a)
    except Exception as e:
        break
if preorder:
    root = Node(preorder[0])
    cur_stack = [root]
    cur_index = 0
    while cur_index < len(preorder) - 1:
        cur_index += 1
        p = cur_stack[-1]
        new_node = Node(preorder[cur_index])
        if new_node.val < p.val:
            p.left = new_node
            cur_stack.append(new_node)
            continue
        while cur_stack and new_node.val > cur_stack[-1].val:
            p = cur_stack[-1]
            cur_stack.pop()
        p.right = new_node
        cur_stack.append(new_node)
    #post_order(root)
    cur = root
    traverse_stack = []
    while True:
        while cur:
            if cur.right:
                traverse_stack.append(cur.right)
            traverse_stack.append(cur) 
            cur = cur.left
        cur = traverse_stack.pop() 
        if cur.right and traverse_stack and (traverse_stack[-1] == cur.right):
            traverse_stack.pop()
            traverse_stack.append(cur)
            cur = cur.right
        else:
            print(cur.val)
            cur = None
        if not traverse_stack:
            break
