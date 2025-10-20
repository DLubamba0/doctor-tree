# doctor_tree.py
# ------------------------------
# Doctor Reporting Tree System
# Implements a binary tree structure to represent hospital doctor hierarchy.

class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None

    # Recursive helper to find a parent node by name
    def _find(self, node, name):
        if node is None:
            return None
        if node.name == name:
            return node
        left = self._find(node.left, name)
        if left:
            return left
        return self._find(node.right, name)

    # Insert a doctor node under a specific parent on a given side
    def insert(self, parent_name, doctor_name, side):
        parent = self._find(self.root, parent_name)
        if parent is None:
            print(f"Error: Parent '{parent_name}' not found.")
            return
        new_doctor = DoctorNode(doctor_name)

        if side.lower() == "left":
            if parent.left is None:
                parent.left = new_doctor
            else:
                print(f"Error: Left child of '{parent_name}' already exists.")
        elif side.lower() == "right":
            if parent.right is None:
                parent.right = new_doctor
            else:
                print(f"Error: Right child of '{parent_name}' already exists.")
        else:
            print("Error: Invalid side. Use 'left' or 'right'.")

    # Traversal methods
    def preorder(self, node):
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]


# Example test (you can comment this out before submission)
if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")
    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    print("Preorder:", tree.preorder(tree.root))
    print("Inorder:", tree.inorder(tree.root))
    print("Postorder:", tree.postorder(tree.root))
