import hashlib, json, time

class Block:
    def __init__(self, index, data, prev_hash, difficulty=3):
        self.index = index
        self.data = data
        self.prev_hash = prev_hash
        self.timestamp = time.time()
        self.nonce = 0
        self.hash = self.mine(difficulty)

    def compute_hash(self):
        payload = json.dumps([self.index, self.data, self.prev_hash,
                              self.timestamp, self.nonce])
        return hashlib.sha256(payload.encode()).hexdigest()

    def mine(self, difficulty):
        # proof-of-work: find a nonce so the hash starts with N zeros
        while True:
            h = self.compute_hash()
            if h.startswith("0" * difficulty):
                return h
            self.nonce += 1

class Blockchain:
    def __init__(self):
        self.chain = [Block(0, "genesis", "0")]

    def add(self, data):
        self.chain.append(Block(len(self.chain), data, self.chain[-1].hash))

    def is_valid(self):
        for prev, cur in zip(self.chain, self.chain[1:]):
            if cur.hash != cur.compute_hash():   # block contents changed
                return False
            if cur.prev_hash != prev.hash:       # link to previous broken
                return False
        return True

if __name__ == "__main__":
    bc = Blockchain()
    bc.add("Alice pays Bob 5")
    bc.add("Bob pays Carol 2")
    print("Valid chain?", bc.is_valid())          # True

    bc.chain[1].data = "Alice pays Bob 500"       # tamper with history
    print("After tampering?", bc.is_valid())      # False
