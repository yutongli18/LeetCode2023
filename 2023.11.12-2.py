class Solution(object):
    def __init__(self):
        self.result_list = []
        self.count_dict = {}

    def findHighAccessEmployees(self, access_times):
        """
        :type access_times: List[List[str]]
        :rtype: List[str]
        """
        access_times.sort(key=lambda item: int(item[1]))
        for access_time in access_times:
            name, time = access_time
            self.count_dict.setdefault(name, [])
            if self.count_dict[name]:
                """if int(time) < self.count_dict[name][0] + 100:
                    self.count_dict[name].append(int(time))
                    if len(self.count_dict[name]) >= 3 and name not in self.result_list:
                        self.result_list.append(name)
                else:
                    while int(time) >= self.count_dict[name]"""
                while self.count_dict[name] and int(time) >= self.count_dict[name][0] + 100:
                    self.count_dict[name].pop(0)
                self.count_dict[name].append(int(time))
                if len(self.count_dict[name]) >= 3 and name not in self.result_list:
                    self.result_list.append(name)
            else:
                self.count_dict[name].append(int(time))
        return self.result_list


if __name__ == '__main__':
    sol = Solution()
    print(sol.findHighAccessEmployees(
        access_times=[["cd", "1025"], ["ab", "1025"], ["cd", "1046"], ["cd", "1055"], ["ab", "1124"], ["ab", "1120"]]))
