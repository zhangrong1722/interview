class InsertValue:
    def insert(self, A, nxt, val):
        nodeT=ListNode(val)
        if not A:
            return nodeT
        
        head=ListNode(A[0])
        r=head
        for i in range(len(A)-1):
            r.next=ListNode(A[nxt[i]])
            r=r.next
            
        if head.val>val:
            nodeT.next=head
            head=nodeT
            return head
        if r.val<val:
            r.next=nodeT
            nodeT.next=None
            return head
             
        pre,now=head,head.next
        while True:
            if pre.val<=val and now.val>=val:
                break
            else:
                pre=pre.next
                now=now.next
        pre.next=nodeT
        nodeT.next=now
        return head