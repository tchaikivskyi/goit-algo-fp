class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def print_list(self):
        print(" -> ".join(map(str, self.to_list())))

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge_sort(self, head=None):
        if head is None:
            head = self.head

        if head is None or head.next is None:
            return head

        middle = self.get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)

        sorted_list = self.sorted_merge(left, right)
        self.head = sorted_list
        return sorted_list

    def get_middle(self, head):
        if head is None:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sorted_merge(self, a, b):
        if a is None:
            return b
        if b is None:
            return a

        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)
        return result


def merge_two_sorted_lists(l1, l2):
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2

    merged = LinkedList()
    merged.head = dummy.next
    return merged



ll = LinkedList()
for val in [3, 1, 4, 2]:
    ll.append(val)

print("Оригінальний список:")
ll.print_list()

print("\nРеверсований список:")
ll.reverse()
ll.print_list()

print("\nВідсортований список:")
ll.merge_sort()
ll.print_list()

ll2 = LinkedList()
for val in [0, 5, 6]:
    ll2.append(val)
ll2.merge_sort()

print("\nДругий відсортований список:")
ll2.print_list()

print("\nЗлитий відсортований список:")
merged = merge_two_sorted_lists(ll.head, ll2.head)
merged.print_list()
