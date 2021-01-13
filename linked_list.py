node_three = {
    'next': None,
    'value': 3
}

node_two = {
    'next': node_three,
    'value': 2
}

node_one = {
    'next': node_two,
    'value': 1
}

def reverse(head):
    node_array = []
    next_node = head
    while next_node.next:
        node_array.append(next_node)
        next_node = next_node.next
    node_array.append(next_node)
    node_array = node_array.reverse()
    for node in node_array:
        node_array[node].next = node_array[node + 1]
    return node_array

# end result: three -> two -> one -> null
# function takes in one as argument

result = reverse(node_one)
print(result)