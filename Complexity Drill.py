n = int(input("Enter n: "))

# 1️⃣ Single Loop → O(n)
count = 0
for i in range(n):
    count += 1
print("\nSingle Loop Operations:", count, "→ Complexity: O(n)")


# 2️⃣ Nested Loop → O(n²)
count = 0
for i in range(n):
    for j in range(n):
        count += 1
print("Nested Loop Operations:", count, "→ Complexity: O(n^2)")


# 3️⃣ Triangular Loop → O(n²/2 ≈ O(n²))
count = 0
for i in range(n):
    for j in range(i + 1):
        count += 1
print("Triangular Loop Operations:", count, "→ Complexity: O(n^2)")


# 4️⃣ Halving Loop → O(log n)
count = 0
i = n
while i > 0:
    count += 1
    i = i // 2
print("Halving Loop Operations:", count, "→ Complexity: O(log n)")


# 5️⃣ Linear Search → Best / Avg / Worst
arr = list(range(1, n + 1))
key = int(input("\nEnter element to search (linear): "))

count = 0
found = False
for i in range(n):
    count += 1
    if arr[i] == key:
        found = True
        break

print("Linear Search Operations:", count)
print("Best: O(1), Avg: O(n), Worst: O(n)")


# 6️⃣ Binary Search → O(log n)
key = int(input("\nEnter element to search (binary): "))

low, high = 0, n - 1
count = 0
found = False

while low <= high:
    count += 1
    mid = (low + high) // 2

    if arr[mid] == key:
        found = True
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

print("Binary Search Operations:", count)
print("Best: O(1), Avg/Worst: O(log n)")