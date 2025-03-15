import unittest

Backpack = []

itemdata = {'items': [{'name': 'test1'}, {'name': 'test2'}, {'name': 'test3'}]}

def backpack():
    for i in list(range(1,15)):
        for a in itemdata['items']:
            Backpack.append(a)

class Testbackpack(unittest.TestCase):
    
    def setUp(self):
        global backpack
        Backpack = []
    
    def testbackpackcount(self):
        backpack()
        expecteditemcount = 14 * len(itemdata['items']) #used chatgpt for this line because I didn't know how to use assertEqual for items in list
        self.assertEqual(len(Backpack), expecteditemcount)
    
    def testbackpackitem(self):
        backpack()
        for item in itemdata['items']:
            self.assertIn(item, Backpack)

if __name__ == '__main__':
    unittest.main()