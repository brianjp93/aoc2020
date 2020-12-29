SEQ = '326519478'
d = [int(x) for x in SEQ]
CUPS = 1_000_000
TURNS = 10_000_000


class Node:
    def __init__(self, n):
        self.n = n
        self.next = None

    def __repr__(self):
        return f'Node(n={self.n}, next={self.next.n})'

    def show(self):
        seen = set()
        out = []
        node = self
        while node.n not in seen:
            seen.add(node.n)
            out.append(node.n)
            node = node.next
        return out


def create_llist(cups=None):
    nodes = {}
    node = None
    for n in d:
        new_node = Node(n)
        nodes[n] = new_node
        if node:
            node.next = new_node
        else:
            root = new_node
        node = new_node
    if cups:
        for n in range(len(nodes) + 1, cups+1):
            new_node = Node(n)
            nodes[n] = new_node
            node.next = new_node
            node = new_node
    node.next = root
    return nodes, root

def play(turns, nodes, root, mini=1, maxi=9):
    for i in range(turns):
        start = root.next
        end = start.next.next
        pickupset = {start.n, start.next.n, end.n}
        root.next = end.next

        new_n = root.n - 1
        while new_n in pickupset or new_n < mini:
            new_n -= 1
            if new_n < mini:
                new_n = maxi

        move_node = nodes[new_n]
        old = move_node.next
        move_node.next = start
        end.next = old
        root = root.next


nodes, root = create_llist()

play(100, nodes, root)
out = ''.join(str(x) for x in nodes[1].show()[1:])
print(f'Part 1: {out}')

nodes, root = create_llist(cups=CUPS)
play(TURNS, nodes, root, maxi=CUPS)
n1 = nodes[1]
out = n1.next.n * n1.next.next.n
print(f'Part 2: {out}')
