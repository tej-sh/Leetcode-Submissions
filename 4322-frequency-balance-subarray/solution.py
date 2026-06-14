from collections import defaultdict
from typing import List

class Solution:
    def getLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1
        for left in range(n):
            freq = defaultdict(int)
            freq_count = defaultdict(int)

            for right in range(left, n):
                num = nums[right]

                old_freq = freq[num]
                if old_freq:
                    freq_count[old_freq] -= 1
                    if freq_count[old_freq] == 0:
                        del freq_count[old_freq]

                freq[num] += 1
                freq_count[freq[num]] += 1

                length = right - left + 1

                if length == 1:
                    ans = max(ans, 1)
                    continue

                if len(freq) == 1:
                    ans = max(ans, length)
                    continue

                if len(freq_count) != 2:
                    continue

                low, high = sorted(freq_count)

                if high == 2 * low:
                    ans = max(ans, length)

        return ans
