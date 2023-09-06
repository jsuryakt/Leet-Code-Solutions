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
    public ListNode[] splitListToParts(ListNode head, int k) {
        // 0.3 -> 0, 3.33 -> 3
        // [1,2,3,4,5,6,7,8,9,10]
        // [10,9,8,7,6,5,4,3,2,1]
        // find the length of listNode
        // if (head == null) {
        //     return fillInEmptyNodes(ans, 0, k);
        // }
        // ListNode temp = head;
        // int actualParts = (int) Math.floor(length/k);
        // int expectedParts = k;

        // if (actualParts == 0) {

        // }
        // parts = length/k
        // parts.floor()
        // if parts==0
        //     parts = 1
        // else
        //     currPart = parts
        //     if (currPart == 1)
        //     //consider remaining for last part
        //     currPart--;

        // if parts != k
        //     // fill empty []
        ListNode[] ans = new ListNode[k];
        ListNode temp1 = head;
        int length = lengthOfNode(temp1);
        int actualParts = length/k;
        int dup = actualParts;
        int diff = length-(actualParts*k);
        ListNode prev = head;
        int idx = 0;

        while (k-- > 0) {
            int nodeLength = actualParts;
            if (diff > 0) {
                nodeLength++;
                diff--;
            }

            ListNode start = prev;
            while (prev != null && --nodeLength > 0) {
                prev = prev.next;
            }
            if (prev != null) {
                ListNode temp = prev.next;
                prev.next = null;
                ans[idx++] = start;
                prev = temp;
            }
        }
        return ans;
    }

    public int lengthOfNode(ListNode node) {
        int count = 0;

        while(node != null) {
            node = node.next;
            count++;
        }

        return count;
    }

    // public ListNode[] fillInEmptyNodes(ListNode[] ans, int startFrom, int endAt) {
    //     for (int i=startFrom, i<endAt; i++) {
    //         ans[i] = new ListNode();
    //     }
    //     return ans;
    // }
}