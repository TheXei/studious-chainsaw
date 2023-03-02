import OrangeTree

tree = OrangeTree.OrangeTree(0, 6, True)
print("Tree age = ", tree.age)
print("Tree height = ", tree.height)
print("Tree alive = ", tree.treeAlive)

while tree.treeAlive == True:
    tree.OneYearPasses()
    print("Tree age = ", tree.age)
    print("Tree height = ", tree.height)
    print("Tree alive = ", tree.treeAlive)
    print("Number of oranges = ", tree.numOranges)
    
    if tree.numOranges >= 5:
        tree.EatOranges(tree.numOranges - 1)
        print("Number of oranges eaten = ", tree.orangesEaten)