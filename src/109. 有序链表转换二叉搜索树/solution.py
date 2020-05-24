# inorder binary tree construct
# Time N
# Space logN
def sortedListToBST(self, head: ListNode) -> TreeNode:
    def findSize(head):
        count, ptr = 0, head
        while ptr:
            ptr = ptr.next
            count += 1
        return count

    def convert(l, r):
        nonlocal head
        if l > r:
            return None
        mid = (l + r) // 2
        left = convert(l, mid - 1)
        node = TreeNode(head.val)
        node.left = left
        head = head.next
        node.right = convert(mid + 1, r)
        return node

    size = findSize(head)
    return convert(0, size - 1)


# Space for Time
# Time N
# Space N
def sortedListToBST(self, head: ListNode) -> TreeNode:
    def mapToList(head):
        s = []
        while head:
            s.append(head.val)
            head = head.next
        return s

    def convertToList(l, r):
        if l > r:
            return
        mid = (l + r) // 2
        node = TreeNode(s[mid])
        if l == r:
            return node
        node.left = convertToList(l, mid - 1)
        node.right = convertToList(mid + 1, r)
        return node

    s = mapToList(head)
    return convertToList(0, len(s) - 1)


# Two  Pointers
# Time NlogN
# Space logN
def sortedListToBST(self, head: ListNode) -> TreeNode:
    def findMiddle(head):
        fast, slow, prev = head, head, None
        while fast.next and fast.next.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev:
            prev.next = None  #断开与指向中间位的slow指针的连接
        return slow

    if not head:
        return None
    mid = findMiddle(head)
    node = TreeNode(mid.val)
    if mid == head:
        return node

    node.left = self.sortedListToBST(head)
    node.right = self.sortedListToBST(mid + 1)
    return node
