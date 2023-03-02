import OrangeTree
import unittest

class Test(unittest.TestCase):
    def test_1_ShouldIncrementTheTreesAgeWithEachPassingYear(self):
        orangeTree = OrangeTree.OrangeTree(0, 6, True)
        
        orangeTree.OneYearPasses()
        
        self.assertEqual(1, orangeTree.age)
    
    def test_2_ShouldIncrementTheTreesHeightByTwoWithEachPassingYear(self):
        orangeTree = OrangeTree.OrangeTree(0, 6, True)
        
        orangeTree.OneYearPasses()
        
        self.assertEqual(8, orangeTree.height)
    
    def test_3_ShouldDieAfter80Years(self):
        orangeTree = OrangeTree.OrangeTree(0, 6, True)
        
        for x in range(80):
            orangeTree.OneYearPasses()
        
        self.assertEqual(False, orangeTree.treeAlive)
    
    def test_4_ShouldProduceFruitAfter2Years(self):
        orangeTree = OrangeTree.OrangeTree(0, 6, True)
        
        orangeTree.OneYearPasses()
        self.assertEqual(0, orangeTree.numOranges)
        
        orangeTree.OneYearPasses()
        self.assertEqual(5, orangeTree.numOranges)
    
    def test_5_ShouldIncreaseFruitProductionBy5PiecesEachYearAfterMaturity(self):
        orangeTree = OrangeTree.OrangeTree(0, 6, True)
        
        orangeTree.OneYearPasses()
        orangeTree.OneYearPasses()
        self.assertEqual(5, orangeTree.numOranges)
        
        orangeTree.OneYearPasses()
        self.assertEqual(10, orangeTree.numOranges)
    
    def test_6_ShouldCountNumberOfOrangesEatenThisYear(self):
        orangeTree = OrangeTree.OrangeTree(0, 6, True)
        
        orangeTree.OneYearPasses()
        orangeTree.OneYearPasses()
        orangeTree.EatOranges(1)
        self.assertEqual(1, orangeTree.orangesEaten)
        
        orangeTree.EatOranges(3)
        self.assertEqual(4, orangeTree.orangesEaten)
        
        self.assertEqual(1, orangeTree.numOranges)
    
    def test_7_OrangesEatenOneYearPasses(self):
        orangeTree = OrangeTree.OrangeTree(0, 6, True)
        
        orangeTree.OneYearPasses()
        orangeTree.OneYearPasses()
        orangeTree.EatOranges(1)
        orangeTree.EatOranges(3)
        orangeTree.OneYearPasses()
        
        self.assertEqual(0, orangeTree.orangesEaten)
        self.assertEqual(10, orangeTree.numOranges)
    
    def test_8_DeadTreeDoNotGrowAndProduceFruit(self):
        orangeTree = OrangeTree.OrangeTree(0, 6, True)
        
        for x in range(80):
            orangeTree.OneYearPasses()
        
        self.assertEqual(False, orangeTree.treeAlive)
        orangeTree.OneYearPasses()
        self.assertEqual(0, orangeTree.numOranges)
        self.assertEqual(164, orangeTree.height)
        self.assertEqual(81, orangeTree.age)
        orangeTree.OneYearPasses()
        self.assertEqual(0, orangeTree.numOranges)
        self.assertEqual(164, orangeTree.height)
        self.assertEqual(82, orangeTree.age)
    
if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()    
    
    