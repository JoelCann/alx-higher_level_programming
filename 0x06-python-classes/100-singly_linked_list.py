#!/usr/bin/python3
"""Defining classes for a singly-linked list."""


class Node:
    """a node in a singly-linked list."""

    def __init__(the_square, data, next_node=None):
        """Initializing a new Node.
        Args:
            data (int): data for the new Node.
            next_node (Node): The next node of the new Node.
        """
        the_square.data = data
        the_square.next_node = next_node

    @property
    def data(the_square):
        """take the data of the Node."""
        return (the_square.__data)

    @data.setter
    def data(the_square, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        the_square.__data = value

    @property
    def next_node(the_square):
        """Get/set the next_node of the Node."""
        return (the_square.__next_node)

    @next_node.setter
    def next_node(the_square, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        the_square.__next_node = value


class SinglyLinkedList:
    """ a singly-linked list."""

    def __init__(the_square):
        """Initalizing a new SinglyLinkedList."""
        the_square.__head = None

    def sorted_insert(the_square, value):
        """Insert a new Node to the SinglyLinkedList.
        Args:
            value (Node): The new Node to be inserted.
        """
        new = Node(value)
        if the_square.__head is None:
            new.next_node = None
            the_square.__head = new
        elif the_square.__head.data > value:
            new.next_node = the_square.__head
            the_square.__head = new
        else:
            tmp = the_square.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(the_square):
        """Defining the print() representation of a SinglyLinkedList."""
        values = []
        tmp = the_square.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
