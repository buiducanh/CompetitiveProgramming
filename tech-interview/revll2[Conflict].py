def revll2(head, m, n):
    count = 1
    cur = None
    while head:
        nxt = head.next
        count += 1
        if count > m + 1 and count < n :
            head.next = cur
            cur = head
            head = nxt
        else:
            cur = head
            head = head.next

