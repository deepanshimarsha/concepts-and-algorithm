#1 sort char by freq
#2 build huffman tree by greedy approach 
#3 traverse from root to the leaf node to get the code for that leaf char

class Node:
    def __init__(self, freq, char, left = None, right = None):
        self.freq = freq
        self.symbol = char
        self.left = left
        self.right = right

        #0/1
        self.huff = "" 

def printcode(node, val = ""):
    new_val = val + str(node.huff)

    if node.left:
        printcode(node.left, new_val)
    if node.right:
        printcode(node.right, new_val)

    if (not node.left and not node.right):
        print(f"{node.symbol} -> {new_val}")



def buildHuffmanTree(arr_char, arr_freq):
    nodes = []
    for i in range(len(arr_char)):
        nodes.append(Node(arr_freq[i],arr_char[i]))
    
    #sort nodes by freq
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.freq)

        left = nodes[0]
        right = nodes[1]

        left.huff = 0
        right.huff = 1

        new_node = Node(left.freq+right.freq, left.symbol + right.symbol, left, right)

        nodes.remove(left)
        nodes.remove(right)
        nodes.append(new_node)

    return nodes[0]

char = ["a","b","c","d","e","f"]
freq = [5,9,12,13,16,45]
root = buildHuffmanTree(char, freq)
print(root.symbol)
printcode(root)