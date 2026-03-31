class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        # if key from get is not found in cache
        if key not in self.cache:
            # return -1
            return -1
        # if key is found in cache, move to the end of the list to
        # signify it's been used/called
        self.cache.move_to_end(key)
        # return found key value from cache
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # if key already exists in cache
        if key in self.cache:
            # move key to the end of the list to
            # signify it's been used/called
            self.cache.move_to_end(key)
        # replace the old value with new key value
        self.cache[key] = value
        # if the cache has exceedec capacity, make sure to 
        # remove the first item in the list
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)
