# THIS WAS CODED BY VINIT KUMAR (vinit71811@gmail.com) FOR CELEBAL SUMMER INTERNSHIP'S 2ND WEEK ASSIGNMENT
# THE ASSIGNMENT REQUIRED TO IMPLEMENT LINKED LIST WITH SOME OPERATIONS TO  PERFORM ON IT WHILE DECLARING LINKED LIST , NODE CLASSES AND TEST CASES FOR THE SAME.
# THANK YOU!!!

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Points to the next node


class LinkedList:
    def __init__(self):
        self.head = None  # Start of the list

    def add_node(self, data):
        # Create a new node
        new_node = Node(data)

        # If list is empty, new node becomes the head
        if not self.head:
            self.head = new_node
            print(f"Added first node with value {data}")
            return

        # Otherwise, find the end and attach it there
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print(f"Added node with value {data}")

    def print_list(self):
        if not self.head:
            print("The list is empty.")
            return

        current = self.head
        print("Current list:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        try:
            if not self.head:
                raise IndexError("Can't delete from an empty list.")

            if n <= 0:
                raise IndexError("Position should be 1 or more.")

            if n == 1:
                print(f"Deleting the first node with value {self.head.data}")
                self.head = self.head.next
                return

            current = self.head
            for i in range(n - 2):
                if current is None or current.next is None:
                    raise IndexError("Position is out of range.")
                current = current.next

            if current.next is None:
                raise IndexError("Position is out of range.")

            print(f"Deleting node at position {n} with value {current.next.data}")
            current.next = current.next.next

        except IndexError as err:
            print("Oops! " + str(err))


# Testing everything
if __name__ == "__main__":
    my_list = LinkedList()

    # Add some values
    my_list.add_node(5)
    my_list.add_node(15)
    my_list.add_node(25)
    my_list.add_node(35)

    # Print the list
    my_list.print_list()

    # Delete second node
    my_list.delete_nth_node(2)
    my_list.print_list()

    # Delete first node
    my_list.delete_nth_node(1)
    my_list.print_list()

    # Try to delete a node that doesn't exist
    my_list.delete_nth_node(10)

    # Empty the list completely
    my_list.delete_nth_node(1)
    my_list.delete_nth_node(1)
    my_list.delete_nth_node(1)  # Now the list is empty
