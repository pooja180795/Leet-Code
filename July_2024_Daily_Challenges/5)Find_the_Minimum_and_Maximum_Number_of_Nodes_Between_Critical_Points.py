'''
Problem Name: Find the Minimum and Maximum Number of Nodes Between Critical Points
A critical point in a linked list is defined as either a local maxima or a local minima.

A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.

A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.

Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.

Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points. If there are fewer than two critical points, return [-1, -1].

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional, List
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = prev.next
        count = 1
        critical_arr = []
        while curr.next:
            if curr.val < prev.val and curr.val < curr.next.val:
                count += 1
                critical_arr.append(count)
            elif curr.val > prev.val and curr.val > curr.next.val:
                count += 1
                critical_arr.append(count)
            else: count += 1
            prev = curr
            curr = curr.next
        if len(critical_arr) < 2:
            return [-1, -1]
        min_dis = float(inf)
        for i in range(len(critical_arr) - 1):
            min_dis = min(min_dis, critical_arr[i+1] - critical_arr[i])
        max_dis = max(critical_arr) - min(critical_arr)


        return [min_dis, max_dis]