from sys import stdin

heights = [int(h) for h in stdin if len(h) > 0]
print(-1 if len(heights) == 0 else sum(heights) / len(heights))
