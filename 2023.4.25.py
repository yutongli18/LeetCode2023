class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        nameHeight = list(zip(names, heights))
        nameHeight.sort(key=lambda x: x[1], reverse=True)
        sortedNames = []
        for name, _ in nameHeight:
            sortedNames.append(name)
        return sortedNames


if __name__ == '__main__':
    sol = Solution()
    print(sol.sortPeople(names=["Mary", "John", "Emma"], heights=[180, 165, 170]))
