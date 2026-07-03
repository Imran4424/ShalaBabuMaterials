# for loop works on range

print("print range without start value")
# when we don't give start value
# when we put single parameter in range() it work as end value
# range will print from 0 to end - 1
for i in range(10):
    print(i)
    

print("\nprint range with start value")
# when we give start value
# the for loop will print from start to end - 1
for i in range(1, 10):
    print(i)
    

print("\nprint range with start value, end + 1")
# if we need to print start to end value
# then add a + 1 after end value, end + 1
for i in range(1, 10 + 1):
    print(i)
    
print("\nprint range with start value, end + 1 and loop traversal will increment by 2")
for i in range(1, 10 + 1, 2):
    print(i)
    
print("\nprint range with start value, end + 1 and loop traversal will increment by 2")
for i in range(2, 10 + 1, 2):
    print(i)