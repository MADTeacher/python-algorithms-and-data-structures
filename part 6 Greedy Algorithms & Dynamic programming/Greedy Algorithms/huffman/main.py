from huffman import HuffmanTree

if __name__ == "__main__":
    my_text = "East or West home is best"
    print(f"The original string is: {my_text}")
    huffman_tree = HuffmanTree.create_huffman_tree(my_text)
    huffman_tree.print_huffman_code()
    encoded_text = huffman_tree.get_encoded_text()
    print(f"The encoded string is: {encoded_text}")
    decoded_text = huffman_tree.get_decoded_string(encoded_text)
    print(f"The decoded string is: {decoded_text}")
