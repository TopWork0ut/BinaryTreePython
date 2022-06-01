from Node import Node

from Student import Student


def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(f"[{root.student}]", end=" ")
        inorder_traversal(root.right)


def insert(node, student):
    if node.student:
        if student.rating < node.student.rating:
            if node.left is None:
                node.left = Node(student)
            else:
                node.left = insert(node.left, student)
        elif student.rating > node.student.rating:
            if node.right is None:
                node.right = Node(student)
            else:
                node.right = insert(node.right, student)
    else:
        node.student.rating = student.rating
    return node


def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left

    return current


def delete_one_node_with_specific_group(root, group):
    if root is None:
        return root

    # print(group, root.student.rating)
    # if rating < root.student.rating:
    #     root.left = delete_one_node_with_specific_group(root.left, rating)
    #
    # elif rating > root.student.rating:
    #     root.right = delete_one_node_with_specific_group(root.right, rating)
    if group != root.student.group:
        if root.left:
            root.left = delete_one_node_with_specific_group(root.left, group)
        if root.right:
            root.right = delete_one_node_with_specific_group(root.right, group)

    else:
        if root.left is None:
            temp = root.right
            root.student = None
            return temp

        elif root.right is None:
            temp = root.left
            root.student = None
            return temp

        temp = minValueNode(root.right)
        # print(temp.student._name)
        # root.group = temp.student.group
        root = temp

        # root.right = delete_one_node_with_specific_group(root.right, temp.student.rating)
        root.right = delete_one_node_with_specific_group(root.right, temp.student.group)
    return root


def main():
    student = Student("Name", "Surname", 13, 2004, 5)
    student2 = Student("Name2", "Surname2", 13, 2004, 9)
    student3 = Student("Nam3", "Surname3", 13, 2004, 1)
    student4 = Student("Name4", "Surname4", 13, 2004, 6)
    student5 = Student("Name5", "Surname5", 12, 2004, 7)
    student6 = Student("Name6", "Surname6", 13, 2004, 15)

    root = Node(student)
    root = insert(root, student2)
    root = insert(root, student3)
    root = insert(root, student4)
    root = insert(root, student5)
    root = insert(root, student6)

    inorder_traversal(root)

    root = delete_one_node_with_specific_group(root, 13)
    root = delete_one_node_with_specific_group(root, 13)
    print("\n")
    inorder_traversal(root)


if __name__ == '__main__':
    main()
