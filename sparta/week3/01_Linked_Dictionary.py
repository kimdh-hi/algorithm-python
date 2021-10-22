'''
체이닝을 통한 해시 테이블 충돌 회피

딕셔너리의 해시테이블은 내부적으로 리스트를 갖는데 해당 리스트 안에 같은 키값(해시기반 인덱스)을
갖는 데이텅 쌍을 충돌을 피하면서 같은 키 값으로 저장하기 위해 튜플로 저장한다.
'''

class LinkedTuple:
    def __init__(self):
        self.list = list()

    def add(self, key, value):
        self.list.append((key, value))

    def get(self, key):
        for k, v in self.list:
            if key is k:
                return v

class Dict:
    HASH_TABLE_SIZE = 8

    def __init__(self):
        self.hash_table = []
        for _ in range(self.HASH_TABLE_SIZE):
            self.hash_table.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % self.HASH_TABLE_SIZE
        self.hash_table[index].add(key, value)

    def get(self, key):
        index = hash(key) % self.HASH_TABLE_SIZE
        return self.hash_table[index].get(key)


dict = Dict()
dict.put("key1", "value1")
dict.put("key2", "value2")
print(dict.get("key1"))