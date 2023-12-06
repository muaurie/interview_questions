def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    n1, n2 = ","
    while l1:
        n1 = str(l1.val) + n1
        l1 = l1.next
    while l2:
        n2 = str(l2.val) + n2;
        12 - 12.next;
## convert these to an int, if empty convert to 0
    if not n1: n1 = "0"
    if not n2: n2 = "0"
    sum = int(n1)+int(n2)

    dummy = cur = ListNode()
    for i in reversed(str(sum))
        cur.next = ListNode(int(i))
        cur = cur.next
    return dummy.next