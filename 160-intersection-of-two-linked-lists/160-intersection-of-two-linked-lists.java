/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) { 
        ArrayList<Object> nodeAndCountA = getLastNodeAndCount(headA);
        ListNode lastA = (ListNode) nodeAndCountA.get(0);
        int countA = (int) nodeAndCountA.get(1);
        
        ArrayList<Object> nodeAndCountB = getLastNodeAndCount(headB);
        ListNode lastB = (ListNode) nodeAndCountB.get(0);
        int countB = (int) nodeAndCountB.get(1);
        
        if(lastA != lastB){
            return null;
        } else {
            if(countA > countB) {
                headA = skipCountNodes(countA-countB, headA);
            } else {
                headB = skipCountNodes(countB-countA, headB);
            }
        }
        
        while(headA != headB) {
            headA = headA.next;
            headB = headB.next;
        }
        return headA;
    }
    
    public ListNode skipCountNodes(int skipCount, ListNode list) {
        while(list != null && skipCount>0) {
            list = list.next;
            skipCount--;
        }
        return list;
    }
    
    public ArrayList<Object> getLastNodeAndCount(ListNode head) {
        int count = 0;
        ArrayList<Object> ans = new ArrayList<>();
        while(head != null && head.next != null) {
            count++;
            head = head.next;
        }
        ans.add(head);
        ans.add(count);
        return ans;
    }
}