str1 = input("Enter the string: ")

def is_palindrome(substring):
    return substring == substring[::-1]

max_len = 0
res = ""

for i in range(len(str1)):
    for j in range(i + 1, len(str1) + 1):
        substring = str1[i:j]
        if is_palindrome(substring) and len(substring) > max_len:
            max_len = len(substring)
            res = substring

print("Longest Palindromic Substring:", res)
print("Length:", max_len)

# def longestPalindrome(s):
#     def expand(left, right):
#         while left >= 0 and right < len(s) and s[left] == s[right]:
#             left -= 1
#             right += 1
#         return s[left + 1:right]

#     longest = ""
#     for i in range(len(s)):
#         p1 = expand(i, i)
#         p2 = expand(i, i + 1)
#         if len(p1) > len(longest):
#             longest = p1
#         if len(p2) > len(longest):
#             longest = p2
#     return longest,len(longest)
# str1=input("Enter the string:")
# print("The longest palindromic substring is:")
# print(longestPalindrome(str1))