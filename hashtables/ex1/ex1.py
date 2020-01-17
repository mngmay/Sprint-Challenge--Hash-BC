#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    print("WEIGHTS", weights)

    for i, weight in enumerate(weights):
        hash_table_insert(ht, weight, i)
        item1 = hash_table_retrieve(ht, limit - weight)
        if item1 is not None:
            print(item1, "NOT NONE!", weight)
            item2 = hash_table_retrieve(ht, weight)
            print(item1, item2)
            if item1 > item2:
                return (item1, item2)
            if item1 == item2:
                return (1, 0)
            else:
                return (item2, item1)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
