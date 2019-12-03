# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''

        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        # hash_value = 5381

        # for char in key:
        #     hash_value = ((hash_value << 5) + hash_value) + char

        # return hash_value

        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        key = self._hash(key)
        index = self._hash_mod(key)
        pair = LinkedPair(key, value)
        if self.storage[index] != None:
            cur_pair = self.storage[index]

            if cur_pair.key == key:
                cur_pair.value = value
                return
            while cur_pair.next != None:
                cur_pair = cur_pair.next
                if cur_pair.key == key:
                    cur_pair.value = value
                    return
            cur_pair.next = pair
        else:
            self.storage[index] = pair

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        key = self._hash(key)
        index = self._hash_mod(key)

        if self.storage[index] == None:  # nothing at key's index
            print("Error: nothing at that index")
            return
        # something at key's index, and the head is item to delete
        elif self.storage[index].key == key:
            self.storage[index] = self.storage[index].next
            return
        else:  # something at key's index, but deleted item not at head -- need to traverse
            cur_pair = self.storage[index]
            while cur_pair.next != None:
                cur_pair = cur_pair.next
                if cur_pair.key == key:
                    cur_pair = cur_pair.next
                    return
        print("Error: that key does not exist")

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        key = self._hash(key)
        index = self._hash_mod(key)

        if self.storage[index] == None:
            return None
        elif self.storage[index].key != key:
            cur_pair = self.storage[index]
            while cur_pair.next != None:
                cur_pair = cur_pair.next
                if cur_pair.key == key:
                    return cur_pair.value
            return None
        else:
            return self.storage[index].value

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        new_storage = [None] * self.capacity


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
