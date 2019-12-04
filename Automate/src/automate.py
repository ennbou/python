import unittest


class PrepareAutomate:
    def __init__(self, alphabet):
        self.alphabet = alphabet

    def setPositions(self):
        n = input("entre number of positions: ")
        self.positions = set(
            [input(f"{i+1} : enter symbole : ") for i in range(int(n))])
        if len(self.positions) != n:
            print(
                f"you'll have {len(self.positions)} positions, because you're enter duplicates values.")
        else:
            print(f"you have {n} positions, god.")
        self.nbrPositions = n
        self.start = input("start position: ")
        print("enter your end position separate with , :")
        self.end = input("end(s): ").split(',')

    def setPostionTransaction(self):
        n = int(input("enter number of char: "))
        print("insert a key and from to(separate between them by ',' ).")

        a = dict()
        for i in range(n):
            v = input(f"{i+1}: ")
            v = v.split(",")  # [q0,a,q1]
            if(v[0] in a.keys()):
                a[v[0]][v[1]] = v[2]
            else:
                a[v[0]] = {v[1]: v[2]}

        self.transactions = a

    def getPosition(self):
        for p in self.positions:
            print(p)

    def getPostionTransaction(self):
        for t in self.transactions:
            print(t)


class Automate:
    def __init__(self, alphabet, start, end, positions, transactions):
        self.alphabet = alphabet
        self.start = start
        self.end = end
        self.positions = positions
        self.transactions = transactions

    def checkWord(self, word):
        for c in word:
            if c not in self.alphabet:
                return False
        start = self.start
        for c in word:
            if(c in self.transactions[start].keys()):
                start = self.transactions[start][c]
            else:
                return False
        if start in self.end:
            return True
        else:
            return False


d = {
    'q0': {
        'a': 'q0',
        'b': 'q1'
    },
    'q1': {
        'b': 'q1',
        'c': 'q2'
    },
}



class TestAutomate(unittest.TestCase):

    def test_1(self):
        d = {
            'q0': {
                'a': 'q0',
                'b': 'q1'
            },
            'q1': {
                'a': 'q1',
                'c': 'q2'
            },
        }
        words = ["aaaabaaac", "bc", "aac"]
        o = Automate(["a", "b", "c"], 'q0', ['q2'], ['q0', 'q1', 'q2'], d)
        self.assertFalse([word for word in words if not o.checkWord(
            word)], "that elements in array, not valid in our automate.")

    def test_2(self):
        d = {
            'q0': {
                'a': 'q0',
                'b': 'q1',
                'f': 'q3'
            },
            'q1': {
                'b': 'q1',
                'c': 'q2'
            },
            'q3': {
                'h': 'q1',
            }
        }
        words = ["afhbbbbbc", "aabbbc", "abbbbbc"]
        o = Automate(["a", "b", "c", "f", "h"], 'q0', [
            'q2', 'q3'], ['q0', 'q1', 'q2'], d)
        self.assertFalse([word for word in words if not o.checkWord(
            word)], "that elements in array, not valid in our automate.")


if __name__ == '__main__':
    unittest.main()
