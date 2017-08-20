def revll2(head, m, n):
    count = 1
    cur = None
    while head and count <= n:
        nxt = head.next
        count += 1
        if count == m:
            old_head = head
        if count == n:
            new_head = head
        if count > m + 1 and count :
            head.next = cur
            cur = head
            head = nxt
        else:
            cur = head
            head = head.next
     
