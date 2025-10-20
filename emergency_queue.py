# emergency_queue.py
# ---------------------------------------
# Emergency Room Priority Queue System
# Uses a min-heap to manage patients by urgency.

class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency  # 1 = most urgent, 10 = least urgent

    def __repr__(self):
        return f"{self.name} ({self.urgency})"


class MinHeap:
    def __init__(self):
        self.data = []

    # Get index helpers
    def _parent(self, index):
        return (index - 1) // 2

    def _left(self, index):
        return 2 * index + 1

    def _right(self, index):
        return 2 * index + 2

    # Heapify up: restore order after insertion
    def heapify_up(self, index):
        while index > 0:
            parent = self._parent(index)
            if self.data[index].urgency < self.data[parent].urgency:
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                index = parent
            else:
                break

    # Heapify down: restore order after removal
    def heapify_down(self, index):
        size = len(self.data)
        while True:
            left = self._left(index)
            right = self._right(index)
            smallest = index

            if left < size and self.data[left].urgency < self.data[smallest].urgency:
                smallest = left
            if right < size and self.data[right].urgency < self.data[smallest].urgency:
                smallest = right

            if smallest != index:
                self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
                index = smallest
            else:
                break

    # Insert a new patient
    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    # Return the most urgent patient (root) without removing
    def peek(self):
        return self.data[0] if self.data else None

    # Remove and return the most urgent patient
    def remove_min(self):
        if not self.data:
            return None
        if len(self.data) == 1:
            return self.data.pop()

        root = self.data[0]
        self.data[0] = self.data.pop()
        self.heapify_down(0)
        return root

    # Print all patients
    def print_heap(self):
        print("Current Queue:")
        for patient in self.data:
            print(f"- {patient.name} ({patient.urgency})")


# Example test (you can comment this out before submission)
if __name__ == "__main__":
    heap = MinHeap()
    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))
    heap.print_heap()

    next_up = heap.peek()
    print("\nNext patient:", next_up)

    served = heap.remove_min()
    print(f"\nServed patient: {served.name}")
    heap.print_heap()
# ... all your DoctorTree code above ...

"""
Design Memo

In designing the doctor reporting system, a binary tree was chosen because it naturally represents hierarchical relationships. Each doctor node can have multiple reports, and by limiting it to left and right children, we can still model structured reporting lines while keeping traversal efficient. Trees allow recursive operations, which make it simple to explore the hierarchy using preorder, inorder, or postorder traversals. Preorder is useful for generating structured reports starting from department heads, inorder can provide an ordered list for internal documentation or audits, and postorder ensures that all subordinate doctors are processed before the manager, which can be helpful for approvals or task delegation.

For the emergency room system, a min-heap priority queue was implemented. This structure is ideal because it ensures that the patient with the highest urgency (lowest numerical value) is always at the root, allowing the hospital staff to quickly retrieve and treat the most critical cases. The heap maintains a complete binary tree, so both insertions and removals are efficient. The heapify_up and heapify_down operations ensure that after any change, the heap property is maintained, which mirrors real-time patient intake systems where priorities can change rapidly.

Overall, these two data structures demonstrate the importance of choosing the right tool for the problem. Trees excel at representing hierarchies and supporting recursive operations, while heaps are optimal for real-time systems where prioritization and fast access to the highest-priority element are critical. By implementing both systems, we created scalable solutions that reflect real-world hospital management needs.
"""
