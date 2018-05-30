# Functions to create and manipulate hashtables
# Part of Udacity's Intro to CS course

# Make a new hashtable of a number of buckets
def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table

# Assign a keyword to a bucket
def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out

# Add a new key and value to the table
def hashtable_add(htable,key,value):
    bucket = hashtable_get_bucket(htable,key)
    bucket.append([key,value])

# Find the bucket a keyword is in
def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword,len(htable))]

# Update the value of a key in the table or add a new key-value pair if the key does not exist
def hashtable_update(htable,key,value):
    bucket = hashtable_get_bucket(htable,key)
    for entry in bucket:
        if entry[0] == key:
            entry[1] = value
            return htable
    bucket.append([key, value])

# Lookup the value for a key in the table
def hashtable_lookup(htable,key):
    bucket = hashtable_get_bucket(htable,key)
    for entry in bucket:
        if entry[0] == key:
            return entry[1]
    return None
