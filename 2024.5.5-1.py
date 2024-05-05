class Solution(object):
    def isValid(self, word):
        """
        100284.有效单词
        :type word: str
        :rtype: bool
        """
        if len(word) < 3:
            return False
        # ascii 码
        a_code, z_code = ord('a'), ord('z')
        A_code, Z_code = ord('A'), ord('Z')
        zero_code, nine_code = ord('0'), ord('9')
        # 是否包含元音字母
        check_vowel = False
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        check_consonant = False
        for i in range(len(word)):
            if word[i] in vowels:
                check_vowel = True
            elif a_code <= ord(word[i]) <= z_code or A_code <= ord(word[i]) <= Z_code:
                check_consonant = True
            elif zero_code <= ord(word[i]) <= nine_code:
                continue
            else:
                return False
        return True and check_vowel and check_consonant


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid(word='a3e'))
