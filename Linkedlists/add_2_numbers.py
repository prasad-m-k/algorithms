class ListNode:
    def __init__(self, val=0,next=None):
        self.val = val
        self.next = next

    def dump(self):
        print(self.val, end =" ")
        while (self.next):
            print(self.next.val,  end =" ")
            self=self.next
        print("")
                 
class Solution:
    def __init__(self):
        self.head = self.tail = None 
        
    def inserAtEnd(self, val):
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
            return
    
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
    
        current_node.next = new_node    
        
    def addTwo(self, l1: [ListNode], l2: [ListNode]):
        
        carry = 0
        while (True):
            if (l1  and l2) :
                self.inserAtEnd((carry + l1.val + l2.val) % 10)
                carry = (carry + l1.val + l2.val) // 10
                l1=l1.next
                l2=l2.next
            elif (l1 ):
                self.inserAtEnd((carry + l1.val) % 10)
                carry = (carry + l1.val) // 10
                l1=l1.next
            elif (l2 ):
                self.inserAtEnd((carry + l2.val) % 10)
                carry = (carry + l2.val) // 10
                l2=l2.next

            if (l1 is None) and (l2 is None):
                if (carry > 0):
                    self.inserAtEnd(carry)
                break

        self.head.dump()
        return self.head
        
node1 = ListNode(0)
node2 = ListNode(0)
Solution().addTwo(node1, node2)

node1 = ListNode(2)
node1.next = ListNode(4)
node1.next.next = ListNode(3)

node2 = ListNode(5)
node2.next = ListNode(6)
node2.next.next = ListNode(4)

#node1.dump()
#node2.dump()
Solution().addTwo(node1, node2)


node1 = ListNode(9)
node1.next = ListNode(9)
node1.next.next = ListNode(9)
node1.next.next.next = ListNode(9)
node1.next.next.next.next = ListNode(9)
node1.next.next.next.next.next = ListNode(9)
node1.next.next.next.next.next.next = ListNode(9)

node2 = ListNode(9)
node2.next = ListNode(9)
node2.next.next = ListNode(9)
node2.next.next.next = ListNode(9)

Solution().addTwo(node1, node2)


#L1=[2,4,3]
#L2=[5,6,4]
#Solution().addTwo1(L1,L2)

#L1=[9,9,9,9,9,9,9]
#L2=[9,9,9,9]
#Solution().addTwo1(L1,L2)

'''
    def addTwo1(self, l1, l2):
        result = []
        ind = 0
        carry = 0
        l1_len = len(l1)
        l2_len = len(l2)
        while (True):
            print("index=" , ind, " carry=", carry)
            if (l1_len > ind ) and (l2_len > ind):
                result.append( (carry + L1[ind] + L2[ind]) % 10)
                carry = (carry + L1[ind] + L2[ind]) // 10
            elif (l1_len > ind):
                result.append( (carry + L1[ind]) % 10)
                carry = (carry + L1[ind]) // 10
            elif (l2_len > ind):
                result.append ((carry + L1[ind]) % 10)
                carry = (carry + L2[ind]) // 10
            
            ind += 1    
            if (ind > l1_len) and (ind > l2_len):
                if (carry > 0):
                    result.append (carry)
                print("hello sum=", result)
                break
        
        #ListNode
        
        return result

'''

