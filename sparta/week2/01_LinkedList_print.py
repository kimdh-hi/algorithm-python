class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    # 뒤로 이어붙이기
    def append(self, data):
        if self.head is None: # 헤드노드 없는 경우 추가되는 노드가 헤드노드가 되도록 처리
            self.head = Node(data)
            return

        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)

    def get(self, index):
        cur = self.head
        cnt = 0
        while cnt < index:
            cur = cur.next
            cnt += 1
        return cur

    def insert(self, index, value):
        if index == 0:
            next_node = self.head
            self.head = Node(value)
            self.head.next = next_node
            return
        # -1 번째를 찾는다면 언제나 0일 때 예외상황을 생갹해야 한다.
        curr_node = self.get(index - 1)
        new_node = Node(value)
        next_node = curr_node.next
        curr_node.next = new_node
        new_node.next = next_node

    def delete(self, index):
        if index == 0:
            self.head = self.head.next
            return
        prev_node = self.get(index - 1)
        prev_node.next = prev_node.next.next

    def print(self):
        cur = self.head
        while cur.next is not None:
            print(cur.data)
            cur = cur.next
        print(cur.data)


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)

linked_list.print()