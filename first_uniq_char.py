def firstUniqChar(s):
    """
    Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
    :type s: str
    :rtype: int
    """
    dic = {}
    for i in s:
        dic[i] = dic.get(i, 0) + 1
    for i, c in enumerate(s):
        if dic[c] == 1:
            return i
    return -1


if __name__ == '__main__':
    print(firstUniqChar("leetcode"))