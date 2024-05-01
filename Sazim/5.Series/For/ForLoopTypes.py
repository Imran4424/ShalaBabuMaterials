# for loop works on range

print("print range without start value")
for i in range(10):
    print(i)
    

print("\nprint range with start value")
for i in range(1, 10):
    print(i)
    

print("\nprint range with start value, end + 1")
for i in range(1, 10 + 1):
    print(i)
    
print("\nprint range with start value, end + 1 and loop traversal will increment by 2")
for i in range(1, 10 + 1, 2):
    print(i)
    
print("\nprint range with start value, end + 1 and loop traversal will increment by 2")
for i in range(2, 10 + 1, 2):
    print(i)