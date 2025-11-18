import sys 

default_scores = [10, 20, 30, 40, 50]
 
if len(sys.argv) <= 1:
    scores = default_scores
    print("Using default scores:", scores)
else:
    scores = [float(arg) for arg in sys.argv[1:]]

total = sum(scores)
average = total / len(scores)

print("Total:", total)
print("Average:", average)