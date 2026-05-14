# Chapter 1

#exercise 7
"""
In the United States, a car fuel efficiency is measured in miles
per gallon. In the metric system, it is usually measured in liters
per 100 kilometers.
a) Write a function called convert_mileage that converts from
miles per gallon to liters per 100 kilometers.
b) Test that your functions returns the right values for 20 and
40 miles per gallon.
c) How did you figure out what the right value was? How closely
do the computer results match the ones you expected?
"""
def convert_mileage(miles,gallon):

    mile_to_kilometer=1.609

    gallon_to_liter=3.785

    kilometer=100*(miles*mile_to_kilometer)
    liter=gallon*gallon_to_liter

    mpl=kilometer/liter

    return mpl

# exercise Leetcode: 3. Longest Substring Without Repeating Characters
"""
Given a string s, find the length of the longest substring without duplicate characters.

DIFFERENCE BETWEEN SUBSEQUENCE AND SUBSTRING

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.Given a string s, find the length of the longest substring without duplicate characters.
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and space
"""

def lengthOfLongestSubstring(s:str):
    """
    :type s: str
    :rtype: int
    """
    set_s=set(s)
    return len(set_s)
    
