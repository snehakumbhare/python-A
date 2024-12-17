#Python: Find the specified number of largest products from two given list, multiplying an element from each list

#Write a  Python program to find the specified number of largest products from two given lists, multiplying an element from each list.
# Define a function called 'top_product' that returns the N largest products from two lists.
def top_product(nums1, nums2, N):
    # Create a list of products of all combinations of elements from 'nums1' and 'nums2'.
    product_list = [x * y for x in nums1 for y in nums2]
    # Sort the product list in descending order.
    result = sorted(product_list, reverse=True)[:N]
    return result

# Create two lists 'nums1' and 'nums2' containing integers.
nums1 = [1, 2, 3, 4, 5, 6]
nums2 = [3, 6, 8, 9, 10, 6]

# Print a message indicating the original lists.
print("Original lists:")
# Print both lists 'nums1' and 'nums2'.
print(nums1)
print(nums2, "\n")

# Set the value of 'N' to 3.
N = 3
# Print the value of 'N' and a message indicating the number of largest products from the two lists.
print(N, "Number of largest products from the said two lists:")
# Call the 'top_product' function with 'nums1', 'nums2', and 'N', then print the result.
print(top_product(nums1, nums2, N))

# Set the value of 'N' to 4.
N = 4
# Print the value of 'N' and a message indicating the number of largest products from the two lists.
print(N, "Number of largest products from the said two lists:")
# Call the 'top_product' function with 'nums1', 'nums2', and 'N', then print the result.
print(top_product(nums1, nums2, N))
