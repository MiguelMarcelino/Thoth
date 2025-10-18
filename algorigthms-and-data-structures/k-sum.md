# k-Sum Algorithm

## 2-Sum 

Before 3-sum or 4-sum, everything starts with two-sum. The idea is to use a hash set to store complements.

Example

```
nums = [2, 7, 11, 15], target = 9
Output: [2, 7]
```

### Implementation
This can be implemented in Python as follows (assuming the sequence is ordered)

```python
def two_sum(nums, target):
    seen = set()
    for n in nums:
        if target - n in seen:
            return [n, target - n]
        seen.add(n)
```

### Complexity
Time complexity: O(n)
Space complexity: O(n)


## 3-sum
Given an array nums, return all unique triplets [a, b, c] such that a + b + c == 0.


### Approach
1. Sort the array.
2. Fix one number (nums[i]).
3. Use two pointers (l, r) to find pairs that sum to -nums[i].
4. Skip duplicates.

### Implementation

```python
def three_sum(nums):
    nums.sort()
    res = []
    n = len(nums)
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # skip duplicates
        l, r = i + 1, n - 1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            # Since the sequence is ordered:
            # - if total < 0, we always try to get numbers from the right (larger)
            # - if total > 0, we always try to get numbers from the left (smaller)
            if total < 0:
                l += 1
            elif total > 0:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                # skip duplicates
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
    return res

```

### Step-by-step example
Input; 

```python
nums = [-1, 0, 1, 2, -1, -4]
```

- 1. Sort Array

```python
nums = [-4, -1, -1, 0, 1, 2]
res = []
```

- 2. Iterate (i from 0 to n-3)

Step 1

```python
# i = 0 → nums[i] = -4
# l = 1, r = 5

total = -4 + (-1) + 2 # = -3 → too small → l++

total = -4 + (-1) + 2 # (again since l=2) = -3 → too small → l++

total = -4 + 0 + 2 # = -2 → too small → l++

total = -4 + 1 + 2 # = -1 → too small → l++

# No matches → res = [].
```

Step 2


```python
# i = 1 → nums[i] = -1
# l = 2, r = 5

total = -1 + (-1) + 2 # = 0 ✅ → add to result
# → res = [[-1, -1, 2]]
# → move both pointers → l = 3, r = 4

total = -1 + 0 + 1 # = 0 ✅ → add to result
# → res = [[-1, -1, 2], [-1, 0, 1]]
# → move both pointers → l = 4, r = 3 → stop.
```

Step 3

```python
i = 2 → nums[i] # = -1 again → skip (duplicate).
```

Step 4

```python
i = 3 → nums[i] # = 0

# l = 4, r = 5

# total = 0 + 1 + 2 = 3 → too big → r--
# No match → done.
```

Final result:
```python
res = [[-1, -1, 2], [-1, 0, 1]]
```


### Complexity
- Time complexity: O(n²)
- Space complexity: O(1) (ignoring output)


## 4-Sum

### Problem
Given an array `nums` and a target value `target`, find all unique quadruplets `[a, b, c, d]` such that `a + b + c + d == target`.

Example:

```
nums = [1, 0, -1, 0, -2, 2], target = 0
Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
```

Approach:

1. Sort the array.
2. Fix two numbers (`i` and `j`).
3. Use two pointers (`l`, `r`) for the remaining two.
4. Skip duplicates carefully.

```python
def four_sum(nums, target):
    nums.sort()
    n = len(nums)
    res = []
    for i in range(n - 3):
        # Skip duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            l, r = j + 1, n - 1
            while l < r:
                total = nums[i] + nums[j] + nums[l] + nums[r]
                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    res.append([nums[i], nums[j], nums[l], nums[r]])
                    # Skip duplicates
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    # once we’ve found a valid triplet, we need to move both pointers inward 
                    # to continue searching for new, non-duplicate pairs.
                    l += 1
                    r -= 1
    return res
```

### Complexity 
Time complexity: O(n³)
Space complexity: O(1)

Reasoning: For each pair `(i, j)`, two-pointer search runs in O(n).

---

## General Pattern

You can generalize this to k-sum using recursion.

```python
def k_sum(nums, target, k):
    nums.sort()
    def helper(start, k, target):
        if k == 2:  # base case: two-sum
            res = []
            l, r = start, len(nums) - 1
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    res.append([nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
            return res

        res = []
        for i in range(start, len(nums) - k + 1):
            # Skip duplicates
            if i > start and nums[i] == nums[i - 1]:
                continue
            for subset in helper(i + 1, k - 1, target - nums[i]):
                res.append([nums[i]] + subset)
        return res

    return helper(0, k, target)
```

Now:

```python
k_sum([1, 0, -1, 0, -2, 2], 0, 4)
# → [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
```


## Comparison Summary

| Problem   | Target               | Strategy                  | Time       | Space | Notes              |
| --------- | -------------------- | ------------------------- | ---------- | ----- | ------------------ |
| Two-sum   | Two numbers → target | Hash map                  | O(n)       | O(n)  | Simplest form      |
| Three-sum | Sum = 0 (often)      | Sort + two-pointer        | O(n²)      | O(1)  | Handles duplicates |
| Four-sum  | Sum = target         | Nested loop + two-pointer | O(n³)      | O(1)  | More combinations  |
| K-sum     | Sum = target         | Recursion                 | O(n^(k-1)) | O(k)  | General form       |


<hr>

Related to: [algorithms-and-data-structures](algorithms-and-data-structures)
