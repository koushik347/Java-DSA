
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def middle_ll(head):
    count=0
    temp=head
    while temp is not None:
        temp=temp.next
        count+=1
    mid=count//2
    temp=head
    while mid>0:
        temp=temp.next
        mid-=1
    return temp
def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()


head = Node(1)
head.next = Node(3)
head.next.next = Node(2)
head.next.next.next = Node(4)


print("Original Linked List:", end=" ")
print_linked_list(head)
head = middle_ll(head)
print("Reversed Linked List:", end=" ")
print_linked_list(head)

