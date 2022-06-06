from Node import Node

from Student import Student


def insert_node(node, student):
    if node.student:
        if student.rating < node.student.rating:
            if node.left is None:
                node.left = Node(student)
            else:
                node.left = insert_node(node.left, student)
        elif student.rating > node.student.rating:
            if node.right is None:
                node.right = Node(student)
            else:
                node.right = insert_node(node.right, student)
    else:
        node.student.rating = student.rating
    return node


def find_min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left

    return current


def delete_nodes_with_specific_group(root, group):
    if root is None:
        return root

    if group != root.student.group:
        if root.left:
            root.left = delete_nodes_with_specific_group(root.left, group)
        if root.right:
            root.right = delete_nodes_with_specific_group(root.right, group)

    else:
        if root.left is None:
            temp = root.right
            root.student = None
            return temp

        elif root.right is None:
            temp = root.left
            root.student = None
            return temp

        temp = find_min_value_node(root.right)
        # root = temp

        root.right = delete_nodes_with_specific_group(root.right, temp.student.group)
    return root


def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(f"[{root.student}]", end=" ")
        inorder_traversal(root.right)


def print_all_nodes_with_bigger_rating_than_given(root, rating: int):
    if root is not None:
        print_all_nodes_with_bigger_rating_than_given(root.left, rating)
        if root.student.rating > rating:
            print(f"[{root.student}]", end=" ")
        print_all_nodes_with_bigger_rating_than_given(root.right, rating)


def main():
    student = Student("Name", "Surname", 12, 2003, 5)
    student2 = Student("Name2", "Surname2", 13, 2004, 9)
    student3 = Student("Nam3", "Surname3", 11, 2003, 1)
    student4 = Student("Name4", "Surname4", 13, 2002, 6)
    student5 = Student("Name5", "Surname5", 12, 2003, 7)
    student6 = Student("Name6", "Surname6", 13, 2004, 15)

    root = Node(student)
    root = insert_node(root, student2)
    root = insert_node(root, student3)
    root = insert_node(root, student4)
    root = insert_node(root, student5)
    root = insert_node(root, student6)

    print("Print all student with higher rating than the given:")
    print_all_nodes_with_bigger_rating_than_given(root, 8)

    print("\n\nInorder traversal before deleting:")
    inorder_traversal(root)

    root = delete_nodes_with_specific_group(root, 13)
    root = delete_nodes_with_specific_group(root, 13)
    root = delete_nodes_with_specific_group(root, 13)
    root = delete_nodes_with_specific_group(root, 11)
    root = delete_nodes_with_specific_group(root, 12)

    print("\n\nInorder traversal after deleting:")
    inorder_traversal(root)


if __name__ == '__main__':
    main()
