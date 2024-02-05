class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-1)
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # If one of the lists is exhausted, append the remaining elements from the other list
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummy.next


if __name__ == '__main__':
    list1 = ListNode(1, ListNode(3, ListNode(5)))
    list2 = ListNode(2, ListNode(4, ListNode(6)))

    merged_list = Solution().mergeTwoLists(list1, list2)

    while merged_list:
        print(merged_list.val, end=" ")
        merged_list = merged_list.next
