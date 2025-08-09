class MyHashSet(object):

    def __init__(self):
        self.size=1000
        self.buckets=[[] for _ in range(self.size)]
    
        
    def hash(self,key):
        return key % self.size
        

    def add(self, key):
        h=self.hash(key)
        if key not in self.buckets[h]:
            self.buckets[h].append(key)
                
        

    def remove(self, key):
       h= self.hash(key)
       if key in self.buckets[h]:
        self.buckets[h].remove(key)

    def contains(self, key):
       h=self.hash(key)
       return key in self.buckets[h]        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

# 705. Design HashSet
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Design a HashSet without using any built-in hash table libraries.

# Implement MyHashSet class:

# void add(key) Inserts the value key into the HashSet.
# bool contains(key) Returns whether the value key exists in the HashSet or not.
# void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
 

# Example 1:

# Input
# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]
# Output
# [null, null, null, true, false, null, true, null, false]