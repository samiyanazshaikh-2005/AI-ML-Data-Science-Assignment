# Q1. Find the second-largest unique element in an array without using sort() or max().

# arr = [10, 20, 50, 40, 50, 30]

# largest = float('-inf')
# second = float('-inf')

# for num in arr:
#     if num > largest:
#         second = largest
#         largest = num
#     elif num > second and num != largest:
#         second = num

# if second == float('-inf'):
#     print("Second largest does not exist")
# else:
#     print("Second Largest =", second)

# Q2. Find all pairs in an array whose sum equals a given target.

# arr = [2, 4, 3, 5, 7, 8]
# target = 10

# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         if arr[i] + arr[j] == target:
#             print(arr[i], arr[j])

# Q3. Move all zeros to the end of an array without changing the order of other elements.

# arr = [0, 1, 0, 3, 12]

# result = []

# for num in arr:
#     if num != 0:
#         result.append(num)

# zeros = arr.count(0)

# result.extend([0] * zeros)

# print(result)

# Q4. Find the missing number from an array containing numbers from 1 to N.

# arr = [1, 2, 4, 5, 6]

# n = 6

# total = n * (n + 1) // 2
# missing = total - sum(arr)

# print("Missing Number =", missing)

# Q5. Find all duplicate elements in a list without using nested loops.

# arr = [1, 2, 3, 2, 4, 5, 1]

# seen = set()
# duplicates = set()

# for num in arr:
#     if num in seen:
#         duplicates.add(num)
#     else:
#         seen.add(num)

# print("Duplicates =", list(duplicates))

# 2. String Problems

# Q6. Find the first non-repeating character in a string.

# text = "programming"

# for ch in text:
#     if text.count(ch) == 1:
#         print("First Non-Repeating Character =", ch)
#         break
# else:
#     print("No non-repeating character")

# Q7. Check whether two strings are anagrams without using sorted().

# str1 = "listen"
# str2 = "silent"

# if len(str1) != len(str2):
#     print("Not Anagrams")
# else:
#     count = {}

#     for ch in str1:
#         count[ch] = count.get(ch, 0) + 1

#     for ch in str2:
#         count[ch] = count.get(ch, 0) - 1

#     if all(value == 0 for value in count.values()):
#         print("Anagrams")
#     else:
#         print("Not Anagrams")

# Q8. Merge two sorted arrays without using sort().

# a = [1, 3, 5]
# b = [2, 4, 6]

# result = []

# i = 0
# j = 0

# while i < len(a) and j < len(b):
#     if a[i] < b[j]:
#         result.append(a[i])
#         i += 1
#     else:
#         result.append(b[j])
#         j += 1

# result.extend(a[i:])
# result.extend(b[j:])

# print(result)

# Q9. Rotate an array to the right by K positions.

# arr = [1, 2, 3, 4, 5]
# k = 2

# k = k % len(arr)

# result = arr[-k:] + arr[:-k]

# print(result)

# Q10. Find the intersection of two arrays, including duplicate occurrences.

# a = [1, 2, 2, 3, 4]
# b = [2, 2, 4, 5]

# count = {}

# for num in b:
#     count[num] = count.get(num, 0) + 1

# result = []

# for num in a:
#     if count.get(num, 0) > 0:
#         result.append(num)
#         count[num] -= 1

# print(result)

# 3. Advanced Array Problems

# Q11. Find the maximum sum of a contiguous subarray.

# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# current = arr[0]
# maximum = arr[0]

# for num in arr[1:]:
#     current = max(num, current + num)
#     maximum = max(maximum, current)

# print("Maximum Subarray Sum =", maximum)

# Q12. Find the longest substring without repeating characters.

# text = "abcabcbb"

# seen = {}
# start = 0
# maximum = 0
# result = ""

# for i, ch in enumerate(text):
#     if ch in seen and seen[ch] >= start:
#         start = seen[ch] + 1

#     seen[ch] = i

#     if i - start + 1 > maximum:
#         maximum = i - start + 1
#         result = text[start:i + 1]

# print("Longest Substring =", result)
# print("Length =", maximum)

# Q13. Find the longest common prefix among multiple strings.

# words = ["flower", "flow", "flight"]

# prefix = words[0]

# for word in words[1:]:
#     while not word.startswith(prefix):
#         prefix = prefix[:-1]

# print("Longest Common Prefix =", prefix)

# Q14. Group a list of strings into anagram groups.

# words = ["eat", "tea", "tan", "ate", "nat", "bat"]

# groups = {}

# for word in words:
#     key = ''.join(sorted(word))

#     if key not in groups:
#         groups[key] = []

#     groups[key].append(word)

# print(list(groups.values()))

# Q15. Find the Kth largest element in an unsorted array.

# arr = [3, 2, 1, 5, 6, 4]

# k = 2

# unique = list(set(arr))

# unique.sort(reverse=True)

# if 1 <= k <= len(unique):
#     print("Kth Largest =", unique[k - 1])
# else:
#     print("Invalid K")

# 4. Stack and Subarray Problems

# Q16. Check whether a given string contains balanced parentheses using a stack.

# text = "{[()]}"

# stack = []

# pairs = {
#     ')': '(',
#     '}': '{',
#     ']': '['
# }

# for ch in text:
#     if ch in "({[":
#         stack.append(ch)

#     elif ch in ")}]":
#         if not stack or stack.pop() != pairs[ch]:
#             print("Not Balanced")
#             break
# else:
#     if not stack:
#         print("Balanced")
#     else:
#         print("Not Balanced")

# Q17. Find all subarrays whose sum equals a given target.

# arr = [1, 2, 3, 4, 2]
# target = 5

# for i in range(len(arr)):
#     total = 0

#     for j in range(i, len(arr)):
#         total += arr[j]

#         if total == target:
#             print(arr[i:j + 1])

# Q18. Merge overlapping intervals in a list.

# intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

# intervals.sort()

# merged = [intervals[0]]

# for start, end in intervals[1:]:
#     last = merged[-1]

#     if start <= last[1]:
#         last[1] = max(last[1], end)
#     else:
#         merged.append([start, end])

# print("Merged Intervals =", merged)

# Q19. Search for an element in a rotated sorted array.

# arr = [4, 5, 6, 7, 0, 1, 2]

# target = 0

# left = 0
# right = len(arr) - 1

# while left <= right:
#     mid = (left + right) // 2

#     if arr[mid] == target:
#         print("Element found at index:", mid)
#         break

#     if arr[left] <= arr[mid]:
#         if arr[left] <= target < arr[mid]:
#             right = mid - 1
#         else:
#             left = mid + 1

#     else:
#         if arr[mid] < target <= arr[right]:
#             left = mid + 1
#         else:
#             right = mid - 1
# else:
#     print("Element not found")

# Q20. Find the longest consecutive sequence in an unsorted array.

# arr = [100, 4, 200, 1, 3, 2]

# numbers = set(arr)

# longest = 0

# for num in numbers:
#     if num - 1 not in numbers:
#         count = 1

#         while num + count in numbers:
#             count += 1

#         longest = max(longest, count)

# print("Longest Consecutive Sequence =", longest)

# 5. Advanced Algorithm Problems

# Q21. Find the trapped rainwater between elevation bars.

# height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

# left = 0
# right = len(height) - 1

# left_max = 0
# right_max = 0

# water = 0

# while left < right:

#     if height[left] < height[right]:

#         if height[left] >= left_max:
#             left_max = height[left]
#         else:
#             water += left_max - height[left]

#         left += 1

#     else:

#         if height[right] >= right_max:
#             right_max = height[right]
#         else:
#             water += right_max - height[right]

#         right -= 1

# print("Trapped Rainwater =", water)

# Q22. Find the median of two sorted arrays in O(log(m+n)) time.

# def find_median(a, b):

#     if len(a) > len(b):
#         a, b = b, a

#     m = len(a)
#     n = len(b)

#     left = 0
#     right = m

#     while left <= right:

#         i = (left + right) // 2
#         j = (m + n + 1) // 2 - i

#         max_left_a = float('-inf') if i == 0 else a[i - 1]
#         min_right_a = float('inf') if i == m else a[i]

#         max_left_b = float('-inf') if j == 0 else b[j - 1]
#         min_right_b = float('inf') if j == n else b[j]

#         if max_left_a <= min_right_b and max_left_b <= min_right_a:

#             if (m + n) % 2 == 0:
#                 return (max(max_left_a, max_left_b) +
#                         min(min_right_a, min_right_b)) / 2

#             return max(max_left_a, max_left_b)

#         elif max_left_a > min_right_b:
#             right = i - 1

#         else:
#             left = i + 1


# a = [1, 3]
# b = [2, 4]

# print("Median =", find_median(a, b))

# Q23. Find the maximum product of a contiguous subarray.

# arr = [2, 3, -2, 4]

# maximum = arr[0]
# minimum = arr[0]
# result = arr[0]

# for num in arr[1:]:

#     if num < 0:
#         maximum, minimum = minimum, maximum

#     maximum = max(num, maximum * num)
#     minimum = min(num, minimum * num)

#     result = max(result, maximum)

# print("Maximum Product =", result)

# Q24. Find the smallest missing positive integer from an unsorted array.

# arr = [3, 4, -1, 1]

# numbers = set(arr)

# smallest = 1

# while smallest in numbers:
#     smallest += 1

# print("Smallest Missing Positive =", smallest)

# Q25. Count the number of subarrays whose sum equals K.

# arr = [1, 2, 3, -2, 2]
# k = 3

# frequency = {0: 1}

# total = 0
# count = 0

# for num in arr:

#     total += num

#     count += frequency.get(total - k, 0)

#     frequency[total] = frequency.get(total, 0) + 1

# print("Number of Subarrays =", count)

# 6. Dynamic Programming

# Q26. Find the longest increasing subsequence in an array.

# arr = [10, 9, 2, 5, 3, 7, 101, 18]

# dp = [1] * len(arr)

# for i in range(len(arr)):
#     for j in range(i):

#         if arr[i] > arr[j]:
#             dp[i] = max(dp[i], dp[j] + 1)

# print("Longest Increasing Subsequence =", max(dp))

# Q27. Solve the Coin Change problem using dynamic programming.

# coins = [1, 2, 5]
# amount = 11

# dp = [float('inf')] * (amount + 1)

# dp[0] = 0

# for coin in coins:
#     for i in range(coin, amount + 1):

#         dp[i] = min(dp[i], dp[i - coin] + 1)

# if dp[amount] == float('inf'):
#     print("Change not possible")
# else:
#     print("Minimum Coins =", dp[amount])

# Q28. Solve the Word Break problem using dynamic programming.

# text = "leetcode"

# words = {"leet", "code"}

# dp = [False] * (len(text) + 1)

# dp[0] = True

# for i in range(1, len(text) + 1):

#     for j in range(i):

#         if dp[j] and text[j:i] in words:
#             dp[i] = True
#             break

# print("Word Break Possible =", dp[len(text)])

# Q29. Find the minimum number of jumps required to reach the last index.

# arr = [2, 3, 1, 1, 4]

# jumps = 0
# current_end = 0
# farthest = 0

# for i in range(len(arr) - 1):

#     farthest = max(farthest, i + arr[i])

#     if i == current_end:

#         jumps += 1
#         current_end = farthest

#         if current_end >= len(arr) - 1:
#             break

# if current_end < len(arr) - 1:
#     print("Not Possible")
# else:
#     print("Minimum Jumps =", jumps)

# Q30. Find the maximum profit from buying and selling stocks with multiple transactions.

# prices = [7, 1, 5, 3, 6, 4]

# profit = 0

# for i in range(1, len(prices)):

#     if prices[i] > prices[i - 1]:
#         profit += prices[i] - prices[i - 1]

# print("Maximum Profit =", profit)

# 7. Data Structures

# Q31. Implement an LRU Cache with O(1) time complexity for get() and put().

# from collections import OrderedDict

# class LRUCache:

#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.cache = OrderedDict()

#     def get(self, key):

#         if key not in self.cache:
#             return -1

#         self.cache.move_to_end(key)

#         return self.cache[key]

#     def put(self, key, value):

#         if key in self.cache:
#             self.cache.move_to_end(key)

#         self.cache[key] = value

#         if len(self.cache) > self.capacity:
#             self.cache.popitem(last=False)


# cache = LRUCache(2)

# cache.put(1, 10)
# cache.put(2, 20)

# print(cache.get(1))

# cache.put(3, 30)

# print(cache.get(2))

# Q32. Implement a Min Stack that supports push(), pop(), top() and getMin() in O(1).

# class MinStack:

#     def __init__(self):
#         self.stack = []
#         self.min_stack = []

#     def push(self, val):

#         self.stack.append(val)

#         if not self.min_stack or val <= self.min_stack[-1]:
#             self.min_stack.append(val)

#     def pop(self):

#         if not self.stack:
#             return None

#         val = self.stack.pop()

#         if val == self.min_stack[-1]:
#             self.min_stack.pop()

#         return val

#     def top(self):

#         if not self.stack:
#             return None

#         return self.stack[-1]

#     def getMin(self):

#         if not self.min_stack:
#             return None

#         return self.min_stack[-1]


# s = MinStack()

# s.push(5)
# s.push(2)
# s.push(8)

# print("Top =", s.top())
# print("Minimum =", s.getMin())

# s.pop()

# print("Minimum =", s.getMin())

# 8. Graph Problems

# Q33. Find the number of islands in a 2D matrix using DFS or BFS.

# grid = [
#     [1, 1, 0, 0],
#     [1, 0, 0, 1],
#     [0, 0, 1, 1],
#     [0, 0, 0, 0]
# ]

# rows = len(grid)
# cols = len(grid[0])

# def dfs(r, c):

#     if r < 0 or r >= rows or c < 0 or c >= cols:
#         return

#     if grid[r][c] == 0:
#         return

#     grid[r][c] = 0

#     dfs(r + 1, c)
#     dfs(r - 1, c)
#     dfs(r, c + 1)
#     dfs(r, c - 1)


# islands = 0

# for i in range(rows):
#     for j in range(cols):

#         if grid[i][j] == 1:
#             islands += 1
#             dfs(i, j)

# print("Number of Islands =", islands)

# Q34. Find the shortest path in a weighted graph using Dijkstra's algorithm.

# import heapq

# graph = {
#     'A': [('B', 4), ('C', 2)],
#     'B': [('A', 4), ('C', 1), ('D', 5)],
#     'C': [('A', 2), ('B', 1), ('D', 8)],
#     'D': [('B', 5), ('C', 8)]
# }

# def dijkstra(graph, start):

#     distances = {node: float('inf') for node in graph}

#     distances[start] = 0

#     queue = [(0, start)]

#     while queue:

#         distance, node = heapq.heappop(queue)

#         if distance > distances[node]:
#             continue

#         for neighbor, weight in graph[node]:

#             new_distance = distance + weight

#             if new_distance < distances[neighbor]:

#                 distances[neighbor] = new_distance

#                 heapq.heappush(queue, (new_distance, neighbor))

#     return distances


# print(dijkstra(graph, 'A'))

# Q35. Detect a cycle in a directed and undirected graph.

# A. Undirected Graph

# def has_cycle(graph, node, parent, visited):

#     visited.add(node)

#     for neighbor in graph[node]:

#         if neighbor not in visited:

#             if has_cycle(graph, neighbor, node, visited):
#                 return True

#         elif neighbor != parent:
#             return True

#     return False


# graph = {
#     0: [1, 2],
#     1: [0, 2],
#     2: [0, 1]
# }

# visited = set()

# cycle = False

# for node in graph:
#     if node not in visited:
#         if has_cycle(graph, node, -1, visited):
#             cycle = True
#             break

# print("Cycle Detected" if cycle else "No Cycle")

# B. Directed Graph

# def has_cycle(graph):

#     visited = set()
#     path = set()

#     def dfs(node):

#         visited.add(node)
#         path.add(node)

#         for neighbor in graph[node]:

#             if neighbor not in visited:
#                 if dfs(neighbor):
#                     return True

#             elif neighbor in path:
#                 return True

#         path.remove(node)
#         return False

#     for node in graph:
#         if node not in visited:
#             if dfs(node):
#                 return True

#     return False


# graph = {
#     0: [1],
#     1: [2],
#     2: [0]
# }

# print("Cycle Detected" if has_cycle(graph) else "No Cycle")

# Q36. Implement topological sorting for a directed acyclic graph.

# from collections import deque

# graph = {
#     5: [2, 0],
#     4: [0, 1],
#     2: [3],
#     3: [1],
#     0: [],
#     1: []
# }

# indegree = {node: 0 for node in graph}

# for node in graph:
#     for neighbor in graph[node]:
#         indegree[neighbor] += 1

# queue = deque()

# for node in graph:
#     if indegree[node] == 0:
#         queue.append(node)

# result = []

# while queue:

#     node = queue.popleft()
#     result.append(node)

#     for neighbor in graph[node]:

#         indegree[neighbor] -= 1

#         if indegree[neighbor] == 0:
#             queue.append(neighbor)

# if len(result) == len(graph):
#     print("Topological Sort =", result)
# else:
#     print("Graph contains a cycle")

# 9. Backtracking Problems

# Q37. Solve the N-Queens problem using backtracking.

# def solve_n_queens(n):

#     board = [["." for i in range(n)] for j in range(n)]

#     def solve(row):

#         if row == n:
#             for r in board:
#                 print(" ".join(r))
#             print()
#             return

#         for col in range(n):

#             safe = True

#             for r in range(row):
#                 if board[r][col] == "Q":
#                     safe = False

#             for r, c in zip(range(row - 1, -1, -1),
#                             range(col - 1, -1, -1)):
#                 if board[r][c] == "Q":
#                     safe = False

#             for r, c in zip(range(row - 1, -1, -1),
#                             range(col + 1, n)):
#                 if board[r][c] == "Q":
#                     safe = False

#             if safe:

#                 board[row][col] = "Q"

#                 solve(row + 1)

#                 board[row][col] = "."

#     solve(0)


# solve_n_queens(4)

# Q38. Generate all permutations of a given string or array without duplicates.

# def permutations(arr):

#     result = []

#     def backtrack(path, remaining):

#         if not remaining:
#             result.append(path)
#             return

#         for i in range(len(remaining)):

#             if i > 0 and remaining[i] == remaining[i - 1]:
#                 continue

#             backtrack(
#                 path + [remaining[i]],
#                 remaining[:i] + remaining[i + 1:]
#             )

#     arr.sort()

#     backtrack([], arr)

#     return result


# arr = [1, 2, 2]

# print(permutations(arr))

# 10. Binary Tree Problems

# Q39. Serialize and deserialize a binary tree.
# class Node:

#     def __init__(self, value):
#         self.val = value
#         self.left = None
#         self.right = None


# def serialize(root):

#     if root is None:
#         return "#"

#     return (
#         str(root.val) + "," +
#         serialize(root.left) + "," +
#         serialize(root.right)
#     )


# def deserialize(data):

#     values = iter(data.split(","))

#     def build():

#         val = next(values)

#         if val == "#":
#             return None

#         node = Node(int(val))

#         node.left = build()
#         node.right = build()

#         return node

#     return build()


# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)

# data = serialize(root)

# print("Serialized =", data)

# new_root = deserialize(data)

# print("Deserialized Root =", new_root.val)

# Q40. Find the lowest common ancestor of two nodes in a binary tree.

# class Node:

#     def __init__(self, value):
#         self.val = value
#         self.left = None
#         self.right = None


# def lowest_common_ancestor(root, p, q):

#     if root is None:
#         return None

#     if root.val == p or root.val == q:
#         return root

#     left = lowest_common_ancestor(root.left, p, q)

#     right = lowest_common_ancestor(root.right, p, q)

#     if left and right:
#         return root

#     return left if left else right


# root = Node(1)

# root.left = Node(2)
# root.right = Node(3)

# root.left.left = Node(4)
# root.left.right = Node(5)

# result = lowest_common_ancestor(root, 4, 5)

# if result:
#     print("Lowest Common Ancestor =", result.val)
# else:
#     print("Ancestor not found")