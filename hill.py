n = 10
mid = n/2
print(mid)
for i in range(10):
    for j in range(i):
        # print(j,i)
        if j == i:
            print('*',)
        else:
            print("_",)
    print('newline','\n')


"""

    *
   * *
  * * *
 * * * *
* * * * *
"""
