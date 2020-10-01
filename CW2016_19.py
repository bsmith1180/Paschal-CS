import sys
from collections import Counter

sys.stdin = open("CW2016_19.in", 'r')

class Recipe:
    def __init__(self, s):
        w = s.split()
        self.name = w[0]
        self.numItems = int(w[1])
        self.required = Counter()
        pos = 2
        while pos < len(w):
            n = int(w[pos])
            ingredient = w[pos+1]
            self.required[ingredient] += n
            pos += 2

    def foo(self):
        pass

data = sys.stdin.read()
lines = data.split('\n')
recipeCount = int(lines[0])
n = 1
recipes = {}
while n <= recipeCount:
    r = Recipe(lines[n])
    recipes[r.name] = r
    n += 1
desired = lines[recipeCount+1:-1]

def visit(c, r, m):
    global recipes
    if r in recipes:
        required = recipes[r].required
        for ingredient in required:
            count = required[ingredient]
            visit(c, ingredient, m*count)
    else:
        c[r] += m
        
for out in desired:
    ans = Counter()
    visit(ans, out, 1)
    print ("[%s]" % out)
    ingredients = sorted(list(ans.keys()))
    for i in ingredients:
        print("%s %d" % (i, ans[i]))
    