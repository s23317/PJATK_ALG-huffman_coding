from minheap import *
from tree import createTree

#     https://binarnie.pl/kodowanie-huffmana/

# class Node:
#     value = 0
#     right = None
#     left = None
#     character = ""


def countCharacters(text):
    occurences = {}
    for c in text:  # zliczamy wystąpienia każdego znaku w tekście
        if occurences.__contains__(c):
            occurences[c] += 1
        else:
            occurences[c] = 1
    return occurences


def createPriorityQueue(dictionary):
    queue = []
    for c in dictionary.keys():
        heap_enq(queue, (dictionary.get(c), c))
    return queue


def encodeValues(n, str, txt):
    if n[1] != "":
        print(n[1] + ":      " + str)
        txt = txt.replace(n[1], str)
        return txt
    txt = encodeValues(n[2], str + "1", txt)
    txt = encodeValues(n[3], str + "0", txt)
    return txt


def readFromFile(file):
    with open(file, "r") as file:
        return file.read()


if __name__ == '__main__':
    inputFile = readFromFile("files/input.txt")
    print("\nWczytany tekst z pliku: " + inputFile)

    dataPQ = createPriorityQueue(countCharacters(inputFile))


    rootNode = createTree(dataPQ)
    print("\nOto tablica kodowania: ")


    inputFile = encodeValues(rootNode, "", inputFile)
    print("\nOto tekst po zakodowaniu: " + inputFile)
