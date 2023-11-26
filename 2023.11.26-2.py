class Solution(object):
    def beautifulSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = ["a", "e", "i", "o", "u"]
        pre_vowels = [0] * len(s)
        pre_consonants = [0] * len(s)
        for index in range(len(s)):
            char = s[index]
            if char in vowels:
                if index > 0:
                    pre_vowels[index] = pre_vowels[index - 1] + 1
                    pre_consonants[index] = pre_consonants[index - 1]
                else:
                    pre_vowels[index] = 1
            else:
                if index > 0:
                    pre_consonants[index] = pre_consonants[index - 1] + 1
                    pre_vowels[index] = pre_vowels[index - 1]
                else:
                    pre_consonants[index] = 1
        count = 0
        for start_index in range(len(s)):
            for end_index in range(start_index, len(s)):
                num_vowels, num_consonants = pre_vowels[end_index], pre_consonants[end_index]
                if start_index > 0:
                    num_vowels -= pre_vowels[start_index - 1]
                    num_consonants -= pre_consonants[start_index - 1]
                if num_vowels == num_consonants and (num_vowels * num_consonants) % k == 0:
                    count += 1
        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.beautifulSubstrings(s="bcdf", k=1))
