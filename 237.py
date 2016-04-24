#237 delete-node-in-a-linked-list/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node==None or node.next==None :
            node=None
            return
        tmp=node.next
        node.next=tmp.next
        node.val=tmp.val
        node=None
