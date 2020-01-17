#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,
                        )


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for i, weight in enumerate(weights):
        item1 = hash_table_retrieve(ht, limit - weight)
        if item1 is not None:
            item2 = i
            if item1 > item2:
                return (item1, item2)
            else:
                return (item2, item1)
        hash_table_insert(ht, weight, i)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
