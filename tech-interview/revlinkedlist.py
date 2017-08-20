__author__ = 'Anh'
def revllrecur(pre_head, head):
    if not head:
        return pre_head
    new_head = revllrecur(head, head.next)
    head.next = pre_head
    return new_head
def revll(head):
    cur = None
    while head:
        nxt = head.next
        head.next = cur
        cur = head
        head = nxt
    return cur

