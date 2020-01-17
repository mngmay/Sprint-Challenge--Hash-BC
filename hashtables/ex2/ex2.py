#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    # insert all tickets into hash
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    for i in range(length):
        if i == 0:
            source = "NONE"
        else:
            source = route[i-1]
        route[i] = hash_table_retrieve(hashtable, source)

    return route
