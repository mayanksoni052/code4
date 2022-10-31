class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        def findMedian(num1, num2, len1, len2):
            if len1 > len2:
                return findMedian(num2, num1, len2, len1)
        
            low = 0
            high = len1
            median = (len1 + len2 + 1) >> 1
            while low <= high:
                part1 = (low + high) >> 1
                part2 = median - part1

                l1 = -sys.maxsize if part1 == 0 else num1[part1 - 1]
                l2 = -sys.maxsize if part2 == 0 else num2[part2 - 1]
                r1 = sys.maxsize if part1 == len1 else num1[part1]
                r2 = sys.maxsize if part2 == len2 else num2[part2]

                if l1 <= r2 and l2 <= r1:
                    if (len1+len2) % 2 == 0:
                        return (max(l1, l2) + min(r1, r2)) / 2
                    else:
                        return max(l1, l2)
                elif l1 > r2:
                    high = part1 - 1
                else:
                    low = part1 + 1
            return 0.0
        return findMedian(nums1, nums2, len(nums1), len(nums2))
            