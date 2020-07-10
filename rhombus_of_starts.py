"""
   *
  * *
 * * *
* * * *
 * * *
  * *
   *
"""

n = int(input())

for _ in range(1, n + 1):
    #for i in range(n):
    print(' ' * (n - _) + '* ' * _, end='')
    print()
for _ in range(n-1, -1, -1):
    print(' ' * (n - _) + '* ' * _, end='')
    print()

