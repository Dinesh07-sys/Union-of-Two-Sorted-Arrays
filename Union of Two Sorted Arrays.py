class Solution:
    def find_union(
        self,
        nums1: list[int],
        nums2: list[int]
    ) -> list[int]:
        n = len(nums1)
        m = len(nums2)

        i = 0
        j = 0

        union_result = []
        while i < n and j < m:
            if nums1[i] < nums2[j]:
                current_value = nums1[i]
                i += 1

            elif nums1[i] > nums2[j]:
                current_value = nums2[j]
                j += 1

            else:
                current_value = nums1[i]
                i += 1
                j += 1


            if (
                not union_result
                or union_result[-1] != current_value
            ):
                union_result.append(current_value)


        while i < n:
            if not union_result or union_result[-1] != nums1[i]:
                union_result.append(nums1[i])

            i += 1


        while j < m:
            if not union_result or union_result[-1] != nums2[j]:
                union_result.append(nums2[j])

            j += 1

        return union_result
if __name__ == "__main__":
    nums1 = [1, 1, 2, 3, 4]
    nums2 = [2, 3, 5, 6]
    solution = Solution()
    answer = solution.find_union(nums1, nums2)
    print(*answer)