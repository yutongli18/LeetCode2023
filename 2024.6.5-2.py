class Solution:
    def get_max(self, server_list, op_list):
        """
        分布式文件系统
        :param server_list: 服务器列表 [files]
        :param op_list: 操作列表 [[type, id, files]]
        :return: 服务器编号，文件数量
        """
        for [op_type, sid, files] in op_list:
            if op_type == 'i':
                # i 表示服务器加入
                next_id = sid + 1
                while server_list[next_id] == -1:
                    next_id = (next_id + 1) % len(server_list)
                server_list[sid] = files
                server_list[next_id] -= files
            elif op_type == 'd':
                # d 表示服务器退出
                next_id = sid + 1
                while server_list[next_id] == -1:
                    next_id = (next_id + 1) % len(server_list)
                server_list[next_id] += server_list[sid]
                server_list[sid] = -1
        # [[id, files]]
        max_files = -1
        result_list = []
        for sid in range(len(server_list)):
            if server_list[sid] == -1:
                continue
            if server_list[sid] > max_files:
                max_files = server_list[sid]
                result_list = [[str(sid), str(server_list[sid])]]
            elif server_list[sid] == max_files:
                result_list.append([str(sid), str(server_list[sid])])
        return ' '.join([','.join(result) for result in result_list])


if __name__ == '__main__':
    # 初始服务器列表
    server_string_list = [server.split(",") for server in input().split(" ")]
    server_list = [-1 for _ in range(20000)]
    for [sid, files] in server_string_list:
        server_list[int(sid)] = int(files)
    # 操作列表
    ops_string_list = input().split(" ")
    ops_list = []
    i = 0
    while i < len(ops_string_list):
        if ops_string_list[i] == "d":
            ops_list.append([ops_string_list[i], int(ops_string_list[i + 1]), -1])
            i += 2
        elif ops_string_list[i] == "i":
            ops_list.append([ops_string_list[i], int(ops_string_list[i + 1]), int(ops_string_list[i + 2])])
            i += 3
    # print(ops_list)
    # for i in range(len(server_list)):
    #     if server_list[i] != -1:
    #         print(i, server_list[i], end='\t')
    # 求解
    sol = Solution()
    print(sol.get_max(server_list=server_list, op_list=ops_list))
