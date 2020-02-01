#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 06:36:35 2019

@author: nitinkotcherlakota
"""

#Huffman coding
import sys
var = {}
character_dict = {}

def make_and_sort_dict(character_d, data):
    global character_dict
    for i in data:
        if i not in character_d:
            character_d[i] = 1
        else:
            character_d[i] += 1
    list_tup = sort_dict(character_d)
    character_dict = character_d
    return list_tup

def sort_dict(character_dict):
    chars = character_dict.keys()
    list_tup = []
    for char in chars:
        list_tup.append((character_dict[char],char))
    list_tup.sort()
    return list_tup

def build_tree(sorted_list):
    while len(sorted_list) > 1:
        smallest = sorted_list[0:2]
        rem = sorted_list[2:]
        merge = smallest[0][0] + smallest[1][0]
        sorted_list = rem + [(merge, smallest)]
        sorted_list.sort(key = lambda x: x[0])
    return sorted_list[0]

def trim_tree(tree):
    t = tree[1]
    if type(t) == type(""):
        return t
    else:
        return (trim_tree(t[0]), trim_tree(t[1]))

def assign_codes(sorted_list, s = ""):
    global var
    if type(sorted_list) == type(""):
        var[sorted_list] = s
    else:
        assign_codes(sorted_list[0], s + "0")
        assign_codes(sorted_list[1], s + "1")
        
def encode(data):
    global var
    output = ""
    for char in data:
        output += var[char]
    return output

def huffman_encoding(data):
    global var
    var = {}
    if len(data) == 0:
        print("Please enter a valid string that is not null")
        return
    character_dict = {}
    sorted_list = make_and_sort_dict(character_dict, data)
    tree = build_tree(sorted_list)
    if (len(sorted_list)) == 1:
        return sorted_list[0][0] * '0', tree
    print(tree)
    print("---")
    trim = trim_tree(tree)
    print(trim)

    assign_codes(trim)
    return encode(data), tree
def huffman_decoding(encoded_data,tree):
    return decode(encoded_data)

def decode(encoded_data):
    global character_dict
    decoded_text = ""
    global var
    if len(character_dict) == 1:
        for key in character_dict.keys():
            return character_dict[key] * key
    inverted_var = dict(map(reversed, var.items()))
    while len(encoded_data) > 0:
        decoder = 1
        while True:
            if encoded_data[:decoder] in inverted_var.keys():
                decoded_text += inverted_var[encoded_data[:decoder]]
                encoded_data = encoded_data[decoder:]
                break
            decoder += 1
    return decoded_text

if __name__ == "__main__":
    #Normal Cases
    print ("***********************\nNormal Cases\n***********************\nCase 1\n***********************\n")
    sentence = "Sun rises in the east and sets in the west"    
    print ("The size of the data is: {}\n".format(sys.getsizeof(sentence)))
    print ("The content of the data is: {}\n".format(sentence))
    encoded_data, tree = huffman_encoding(sentence)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))
    
    print ("***********************\nCase 2\n***********************\n")
    sentence = "The bird is the word"
    print ("The size of the data is: {}\n".format(sys.getsizeof(sentence)))
    print ("The content of the data is: {}\n".format(sentence))

    encoded_data, tree = huffman_encoding(sentence)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))
    
    print ("***********************\nCase 3\n***********************\n")
    sentence = "The sun shines and I go to the beach"
    print ("The size of the data is: {}\n".format(sys.getsizeof(sentence)))
    print ("The content of the data is: {}\n".format(sentence))
    encoded_data, tree = huffman_encoding(sentence)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))

    # Edge Cases
    print ("***********************\nEdge Cases\n***********************\nCase 1\n***********************\n")
    sentence = "aaa"
    print("The size of the data is: {}\n".format(sys.getsizeof(sentence)))
    print("The content of the data is: {}\n".format(sentence))
    encoded_data, tree = huffman_encoding(sentence)
    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
    
    print ("***********************\nCase 2\n***********************\n")
    sentence = ""
    print("The size of the data is: {}\n".format(sys.getsizeof(sentence)))
    # The size of the data is: 49
    print("The content of the data is: {}\n".format(sentence))
    huffman_encoding(sentence)