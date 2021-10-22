
class Dict:

    HASH_TABLE_SIZE = 8

    def __init__(self):
        self.hash_table = [0] * self.HASH_TABLE_SIZE

    def put(self, key, value):
        index = hash(key) % self.HASH_TABLE_SIZE
        self.hash_table[index] = value

    def get(self, key):
        index = hash(key) % self.HASH_TABLE_SIZE
        return self.hash_table[index]


dict = Dict()
dict.put('key1', 'value1')
dict.put('key2', 'value2')

print(dict.get('key1'))