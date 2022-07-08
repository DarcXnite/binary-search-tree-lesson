class Node:
    # here we will add the constructor
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    # and the string method

    def __str__(self):
        return f'{self.data}'


class BinaryTree:
    # the tree will start out empty, with a null head
    def __init__(self):
        self.root = None

    def insert(self, data):
        '''
        Insert(data: any) -> None:\n 
        creates a new Node from the data passed in and adds it to the tree
        If the data is already in the tree, does not insert it again
        '''
        # create a new node from the data passed in
        new_node = Node(data)

        # if the root doesn't exist, set the new node to the root
        if not self.root:
            self.root = new_node
            return

        # loop over the tree starting at the root
        current_node = self.root
        while current_node:
            # if the data is smaller than the left
            if data < current_node.data:
                # ... and there is no left node
                if not current_node.left:
                    # set the data to be the left node
                    current_node.left = new_node
                    return
                else:
                    # ...otherwise set current_node to be left
                    current_node = current_node.left

            # if the data is bigger than the left
            elif data > current_node.data:
                # insert new node to the right
                if not current_node.right:
                    current_node.right = new_node
                    return
                else:
                    # otherwise, a right exists, so the right becomes the current node
                    current_node = current_node.right
            # the data is dupe
            else:
                return

    def search(self, val):
        '''
        search(value: any) -> value or bool:\n 
        Performs depth first search
        Search the Tree for a node with the given value
        If the node exists, return it
        If the node doesn't exist, return false
        '''
        # if there is no root -- return false
        if not self.root:
            return False
        # loop through the tree, starting with the root
        current_node = self.root
        while current_node:
            # if the value is smaller than the current node's data
            if val < current_node.data:
                current_node = current_node.left
            elif val > current_node.data:
                # move to the right
                current_node = current_node.right
            else:
                # this means they are equal
                return current_node
        return False

    def print(self, node=None):
        '''
        print(node=optional: Node) -> None:\n
        prints out all values recursively (in a depth first search fashion)
        defualt start is at root node
        '''
        if not node:
            node = self.root

        # print the node
        print(node)
        # if there is a left node, recurvively invoke
        if node.left:
            self.print(node.left)
        # if there is a right node, recursively invoke
        if node.right:
            self.print(node.right)

    def size(self, node=None):
        '''
        size(node=optional: Node) -> int:\n 
        performs breadth first search
        Calculate the number of nodes in the tree, starting from the given node
        If no node is provided, we can use the root as a sensible default
        '''
        if not self.root:
            return 0

        if not node:
            node = self.root

        node_count = 1
        if node.right:
            node_count += self.size(node.right)
        if node.left:
            node_count += self.size(node.left)
        return node_count

    def height(self, node=None):
        '''
        height(node=optional: Node) -> int:\n 
        perform breadth first search
        Calculate the maximum amount of nodes in any one path from the given node
        If not given a specific node, default to using the root node
        '''
        if not self.root:
            return 0

        if not node:
            node = self.root

        node_count_left = 1
        node_count_right = 1

        if node.left:
            node_count_left += self.height(node.left)
        if node.right:
            node_count_right += self.height(node.right)

        if node_count_left >= node_count_right:
            return node_count_left
        else:
            return node_count_right

    def get_max(self):
        '''
        getMax() -> int:\n 
        perform depth first search
        Calculate the maximum value held in the tree
        '''
        if not self.root:
            return False

        current_node = self.root
        while current_node.right:
            current_node = current_node.right
        return current_node

    def get_min(self):
        '''
        getMin() -> int:\n 
        perform depth first search
        Calculate the minimum value held in the tree
        '''
        if not self.root:
            return False

        current_node = self.root
        while current_node.left:
            current_node = current_node.left
        return current_node
