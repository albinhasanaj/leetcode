def findMedianSortedArrays(nums1, nums2):
    
    if not len(nums1) and not len(nums2):
        return None
    
    for i in nums2:
        for j in range(len(nums1)):
            if i < nums1[j]:
                nums1.insert(j, i)
                break
            elif j >= len(nums1) - 1:
                nums1.insert(j + 1, i)
                break
            
    return nums1[len(nums1) // 2] if len(nums1) != 0 and len(nums1) % 2 != 0 else len(nums1) != 0 and (nums1[len(nums1) // 2] + nums1[len(nums1) // 2 - 1])/2.0


# Example usage:
nums1 = [1,2]
nums2 = [3, 4]
print(findMedianSortedArrays(nums1, nums2))