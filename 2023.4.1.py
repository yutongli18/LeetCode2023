"""
给你一条个人信息字符串 s ，可能表示一个 邮箱地址 ，也可能表示一串 电话号码 。返回按如下规则 隐藏 个人信息后的结果：
电子邮件地址：
一个电子邮件地址由以下部分组成：
一个 名字 ，由大小写英文字母组成，后面跟着
一个 '@' 字符，后面跟着
一个 域名 ，由大小写英文字母和一个位于中间的 '.' 字符组成。'.' 不会是域名的第一个或者最后一个字符。
要想隐藏电子邮件地址中的个人信息：
名字 和 域名 部分的大写英文字母应当转换成小写英文字母。
名字 中间的字母（即，除第一个和最后一个字母外）必须用 5 个 "*****" 替换。
电话号码：
一个电话号码应当按下述格式组成：
电话号码可以由 10-13 位数字组成
后 10 位构成 本地号码
前面剩下的 0-3 位，构成 国家代码
利用 {'+', '-', '(', ')', ' '} 这些 分隔字符 按某种形式对上述数字进行分隔
要想隐藏电话号码中的个人信息：
移除所有 分隔字符
隐藏个人信息后的电话号码应该遵从这种格式：
"***-***-XXXX" 如果国家代码为 0 位数字
"+*-***-***-XXXX" 如果国家代码为 1 位数字
"+**-***-***-XXXX" 如果国家代码为 2 位数字
"+***-***-***-XXXX" 如果国家代码为 3 位数字
"XXXX" 是最后 4 位 本地号码
"""
import re


class Solution(object):
    def maskPII(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        encodedS = ""
        if "@" not in s:
            # 电话号码
            sList = re.split(r"[\+\-\(\) ]", s)
            sList = [char.strip() for char in sList]
            newS = "".join(sList)
            if len(newS) == 10:
                encodedS = "***-***-" + newS[-4:]
            elif len(newS) == 11:
                encodedS = "+*-***-***-" + newS[-4:]
            elif len(newS) == 12:
                encodedS = "+**-***-***-" + newS[-4:]
            else:
                encodedS = "+***-***-***-" + newS[-4:]
        else:
            sList = s.split("@")
            sList = [char.lower() for char in sList]
            sList[0] = sList[0][0] + "*****" + sList[0][-1]
            encodedS = "@".join(sList)
        return encodedS


if __name__ == '__main__':
    sol = Solution()
    print(sol.maskPII(s="86-(10)12345678"))
