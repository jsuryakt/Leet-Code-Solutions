/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if(left==right || head == null || head.next == null) return head;
        int tempLeft = left-1;
        ListNode oldMainHead = head;
        ListNode oldHead = head;
        while(head != null && tempLeft-- > 0) {
            oldHead = head;
            head = head.next;
        }
        int k = right-left+1;
        ListNode[] rotateVars = rotateKTimes(head, k);
        ListNode newTail = rotateVars[0];
        ListNode newHead = rotateVars[1];
        ListNode oldTail = rotateVars[2];
        oldHead.next = newHead;
        newTail.next = oldTail;
        if(left == 1) {
            return newHead;
        } else {
            return oldMainHead;
        }
    }
    public ListNode[] rotateKTimes(ListNode node, int k) {
        ListNode tail = node;
        ListNode prev = null;
        while(k-- > 0 && node != null) {
            ListNode next = node.next;
            node.next = prev;
            prev = node;
            node = next;
        }
        return new ListNode[]{tail, prev, node};
    }
}