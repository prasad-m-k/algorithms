from typing import List

class ListNode():
    
    def __init__(self, value :int, next=None):
        self.value :int =  value
        self.next :ListNode = next

    def __str__(self) -> str:
        if self.value:
            return str(self.value)
        else:
            return ""

class singleList():

    def __init__(self, value: int = None):
        self.head: ListNode  = ListNode(value) if value else None
        self.tail = self.head.next if self.head else None
        self.size = 1 if value else 0
        
    def __str__(self) -> str:
        ret = ""
        node=self.head
        while(node):
            ret += "[" + str(node) + "]"
            ret += " -> "
            node = node.next
            
        ret += "None"
        ret += " (" + str(self.size) + ")"
        return ret

    def __insert_at_head(self, val: ListNode) -> None:
        val.next = self.head
        self.head = val
        self.size += 1
        return
        
    def insert_head(self, intval: int) -> None:
        return self.__insert_at_head(ListNode(intval))

    def insert_after(self, nodeval: int, intval: int) -> None:
        #print("inserting ", intval , " after ", nodeval)
        if not self.head:
            return self.insert_head(intval)    
        
        node: ListNode = self.head
        while(node):
            if node.value == nodeval:
                new_node = ListNode(intval)
                new_node.next = node.next
                node.next=new_node
                self.size += 1
                break
            node = node.next
    
    def __insert_at_end(self, val: ListNode) -> None:
        n: ListNode = self.head
        while(n.next):
            n=n.next
        n.next=val
        self.size += 1
        return

    def append(self, intval: int) -> None:
        return self.__insert_at_end(ListNode(intval))
        
    def delete_head(self):
        if(self.size == 0):
            return
        if(self.head):
            self.head = self.head.next
            self.size -= 1

    def delete_tail(self) -> None:
        if(self.size == 0):
            return
        elif self.size == 1:
            self.delete_head()
        elif(self.size > 1):
            node: ListNode = self.head
            while (node and node.next):
                if node.next.next == None:
                    node.next = None
                    self.size -= 1
                    return
                node = node.next
            

    def delete_position(self, pos:int) -> None:
        if self.size < pos:
            print("Nothing to delete")
            return
        elif pos == 0:
            self.delete_head()
        elif pos == self.size:
            self.delete_tail()
        else:
            node=self.head
            prev=self.head
            ind: int = 0
            while(ind+1 < pos):
                node = node.next
                prev = prev.next
                ind += 1
            #self.delete_node(node.value)
            print("deleting position",pos, " value=", node.next)
            prev.next = node.next.next
            self.size -= 1
        
    def delete_node(self, intval: int):
        if(self.size == 0):
            return
        elif self.size >= 1 and self.head.value == intval:
            self.delete_head()
        elif(self.size > 1):
            node: ListNode = self.head
            prev: ListNode = self.head
            while (node and node.next):
                if node.next.value == intval:
                    prev.next=node.next.next
                    self.size -= 1
                    #return
                else:
                    node=node.next
                    prev=prev.next
            


if __name__ == "__main__":
    n=singleList()
    print(n)
    n=singleList(10)
    n.insert_head(20)
    n.insert_head(20)
    n.insert_head(20)
    n.insert_head(30)
    n.insert_head(40)
    n.delete_tail()
    n.append(5)
    n.insert_head(ListNode(50))
    n.insert_after(30,35)
    print(n)
    n.delete_node(20)
    print(n)
    n.delete_head()
    n.delete_node(10)
    n.delete_node(3)
    n.delete_node(45)
    #n.delete_node(40)
    n.delete_tail()
    n.insert_after(30,55)
    n.insert_after(55,75)
    print(n)
    n.delete_position(3)
    print(n)
    n.delete_position(0)
    print(n)