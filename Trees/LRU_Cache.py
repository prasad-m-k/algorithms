from collections import defaultdict
import json

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val  = val
        self.next = None
        self.prev = None
    
    def __str__(self):
        d = defaultdict(lambda: "not preset")
        d[self.key]=self.val
        json_data = json.dumps(d, indent=2)
        json_data = json.dumps(d)
        return str(json_data)
    
        
class LinkedList:
    def __init__(self):
        self.head = Node(None, 'head')
        self.tail = Node(None, 'tail')
        
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def __str__(self):
        ret = ""
        node = self.head
        while(node):
            ret += "[" + str(node) + "]"
            ret += " <-> "
            node = node.next
            
        ret += "None"
        return ret
        
    def get_head(self):
        return self.head.next
    
    def get_tail(self):
        return self.tail.prev
    
    def add(self, node):
        prev = self.tail.prev
        print(prev)
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

       
      


#head = Node("a","b")
#print(head)

l = LinkedList()
print(l)
node1 = Node("a", "b")
l.add(node1)

exit(0)
node2 = Node("c", "d")
l.add(node2)
print(l)

l.remove(node2)
print(l)

