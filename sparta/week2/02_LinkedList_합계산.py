# 두 링크드 리스트의 합 계산

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)


def sum_linked_list(linked_list):
    sum = 0
    curr = linked_list.head
    while curr.next is not None:
        sum = sum * 10 + curr.data
        curr = curr.next
    sum = sum * 10 + curr.data
    return sum


def get_linked_list_sum(linked_list_1, linked_list_2):
    sum1 = sum_linked_list(linked_list_1)
    sum2 = sum_linked_list(linked_list_2)

    return sum1 + sum2


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))
