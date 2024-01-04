class Student_Manager(object):
    # 初始化...
    def __init__(self):
        self.product_list = []
        self.id_list = []
        # 选项功能字典
        self.option_func_dict = {
            '1': self.add_product_data,
            '2': self.remove_product_data,
            '3': self.mod_product_data,
            '4': self.srh_product_data,
            '5': self.display_product_data,
            '6': self.data_statistics,
            '7': self.clear_product_data
        }
        # 已授权的用户列表
        self.users_list = [
            {'username': 'admin', 'password': '1234', 'permission': '全部权限'},
            {'username': 'guest', 'password': '0000', 'permission': '只读权限'}
        ]

    # 新增学员信息--可以连续添加多个学员信息
    def add_product_data(self):
        print("=" * 12, "新增商品系统", "=" * 12)
        while True:
            product_id = input("请输入商品编号：").strip()
            if product_id in self.id_list:
                print(f"商品编号{product_id}---已存在，请重新输入！")
                continue
            product_name = input("请输入商品名称：").strip();
            product_nums = input("请输入商品数量：").strip();
            product_bid = input("请输入单个商品的进价：").strip();
            product_price = input("请输入单个商品的售价：").strip();
            product_profit = product_price - product_bid;
            product_allProfit = product_profit * product_nums;
            product = {'商品编号': product_id,
                       '商品名称': product_name,
                       '数量': product_nums,
                       '进价': product_bid,
                       '售价': product_price,
                       '利润': product_profit,
                       '总利润':product_allProfit
                       }
            for value in product.values():
                if not value:
                    print(f"信息不能为空---添加失败，请重新输入！")
                    break
            else:
                self.product_list.append(product)
                self.id_list.append(product_id)
                print(f"{product['商品编号']}号商品：{product['商品名称']}---添加成功！")

                num = input("是否继续添加(1：继续，2：保存并退出，3：不保存并退出)：").strip()
                if num == '2':
                    self.save_product_data()
                    break
                if num == '3':
                    break

    # 删除学员信息
    def remove_product_data(self):
        print("=" * 12, "欢迎进入删减学员系统", "=" * 12)
        if self.product_list:  # 先判断数据是否为空，避免进入死循环
            print("学员列表如下:")  # 先打印下学员列表，避免输入不存在的学员信息，优化用户体验
            for index, student in enumerate(self.product_list):
                print(
                    f"索引值:{index}-- 学号:{student['学号']}，姓名:{student['姓名']}，性别:{student['性别']}，年龄:{student['年龄']}，爱好:{student['爱好']}")
            while True:
                try:
                    index = int(input("请选择要删除的学员信息(输入对应索引值):").strip())
                    student = self.product_list[index]
                    self.product_list.remove(student)
                    self.id_list.remove(student['学号'])
                    print(f"{student['学号']}号学员：{student['姓名']}---删除成功！")
                except (IndexError, ValueError):   # 防止输入非整数类型或者超出索引而发生报错
                    print("索引值错误，请重新输入！")
                    continue

                num = input("是否继续删除(1：继续，2：保存并退出，3：不保存并退出)：").strip()
                if num == '2':
                    self.save_product_data()
                    break
                if num == '3':
                    break
        else:
            print("当前学员系统暂无数据!")
            input("按任意键返回主页...")

    # 修改学员信息
    def mod_product_data(self):
        print("=" * 12, "欢迎进入修改学员系统", "=" * 12)
        if self.product_list:  # 先判断数据是否为空，避免进入死循环
            print("学员列表如下:")  # 先打印下学员列表，避免输入不存在的学员信息，优化用户体验
            for index, student in enumerate(self.product_list):
                print(
                    f"索引值:{index}-- 学号:{student['学号']}，姓名:{student['姓名']}，性别:{student['性别']}，年龄:{student['年龄']}，爱好:{student['爱好']}")
            while True:
                try:
                    index = int(input("请选择要修改的学员信息(输入对应索引值):").strip())
                    student = self.product_list[index]
                    self.mod_choice(student)  # 直接传递所选学员字典
                except (IndexError, ValueError):       # 防止输入非整数类型或者超出索引而发生报错
                    print("索引值错误，请重新输入！")
                    continue

                num = input("是否继续修改(1：继续，2：保存并退出，3：不保存并退出)：").strip()
                if num == '2':
                    self.save_product_data()
                    break
                if num == '3':
                    break
        else:
            print("当前学员系统暂无数据!")
            input("按任意键返回主页...")

    # 具体修改选项--优化用户体验，让用户可以选择需要修改的具体信息
    def mod_choice(self, student):
        print("该学员信息如下：")
        print(f"学号:{student['学号']}，姓名:{student['姓名']}，性别:{student['性别']}，年龄:{student['年龄']}，爱好:{student['爱好']}")
        print("请选择要修改的信息：")
        print("1：全部修改  2：仅学号  3：仅姓名  4：仅性别  5：仅年龄  6：仅爱好")

        num = input("请输入数字选择要修改的信息：").strip()
        if num == '1':
            while True:
                new_id = input("请输入修改后的学号：").strip()
                if new_id not in self.id_list or new_id == student['学号']:
                    self.id_list.remove(student['学号'])
                    student['学号'] = new_id
                    student['姓名'] = input("请输入修改后的姓名：").strip()
                    student['性别'] = input("请输入修改后的性别：").strip()
                    student['年龄'] = input("请输入修改后的年龄：").strip()
                    student['爱好'] = input("请输入修改后的爱好：").strip()
                    self.id_list.append(student['学号'])
                    break
                else:
                    print(f"学号{new_id}---已存在，请重新输入！")

        elif num == '2':
            while True:
                new_id = input("请输入修改后的学号：").strip()
                if new_id not in self.id_list:
                    self.id_list.remove(student['学号'])
                    student['学号'] = new_id
                    self.id_list.append(student['学号'])
                    break
                else:
                    print(f"学号{new_id}---已存在，请重新输入！")

        elif num == '3':
            student['姓名'] = input("请输入修改后的姓名：").strip()
        elif num == '4':
            student['性别'] = input("请输入修改后的性别：").strip()
        elif num == '5':
            student['年龄'] = input("请输入修改后的年龄：").strip()
        elif num == '6':
            student['爱好'] = input("请输入修改后的爱好：").strip()
        else:
            print("~~~输入错误，请输入正确的数字！~~~")
            return self.mod_choice(student)
        print(f"{student['学号']}号学员：{student['姓名']}---修改成功！")
        print("修改后信息为：")
        print(f"学号:{student['学号']}，姓名:{student['姓名']}，性别:{student['性别']}，年龄:{student['年龄']}，爱好:{student['爱好']}")

    # 查找学员信息--根据姓名查找，重名的需要全部显示出来
    def srh_product_data(self):
        print("=" * 12, "欢迎进入学员查询系统", "=" * 12)
        if self.product_list:  # 先判断数据是否为空，避免进入死循环
            while True:
                # 将所有学员的姓名暂时存储到一个列表中，用于判断
                name_list = [student["姓名"] for student in self.product_list]
                stu_name = input("请输入要查找的学员姓名：").strip()
                if name_list.count(stu_name) == 0:
                    print(f"姓名为{stu_name}的学员---不存在!")
                else:
                    for student in self.product_list:
                        if student["姓名"] == stu_name:
                            print(
                                f"学号:{student['学号']}，姓名:{student['姓名']}，性别:{student['性别']}，年龄:{student['年龄']}，爱好:{student['爱好']}")

                num = input("是否继续查找(1：继续，2：退出)：").strip()
                if num == '2':
                    break
        else:
            print("当前学员系统暂无数据!")
            input("按任意键返回主页...")

    # 显示全部学员--可选显示顺序
    def display_product_data(self):
        print("=" * 12, "欢迎进入学员展示系统", "=" * 12)
        if self.product_list:  # 判断数据是否为空,避免报错
            num = input("请选择显示方式(1：按学员添加时间顺序，2：按学号排序)：").strip()
            if num == '2':
                self.product_list.sort(key=lambda x: x['学号'])
            print("学员列表如下:")
            for index, student in enumerate(self.product_list):
                print(
                    f"索引值:{index}-- 学号:{student['学号']}，姓名:{student['姓名']}，性别:{student['性别']}，年龄:{student['年龄']}，爱好:{student['爱好']}")
        else:
            print("当前学员系统暂无数据！")
        input("按任意键返回主页...")

    # 数据统计--统计男女学员人数、年龄段分布等
    def data_statistics(self):
        print("=" * 12, "欢迎进入学员统计系统", "=" * 12)
        if self.product_list:  # 先判断数据是否为空，避免报错
            print(f"当前学员总人数：{len(self.product_list)}人")
            male_num = female_num = 0
            yong_num = middle_num = large_num = old_num = older_num = grandpa_num = 0
            age_list = []
            for student in self.product_list:
                if student["性别"] == "男":
                    male_num += 1
                if student["性别"] == "女":
                    female_num += 1
                if int(student["年龄"]) <= 20:
                    yong_num += 1
                if 20 < int(student["年龄"]) <= 30:
                    middle_num += 1
                if 30 < int(student["年龄"]) <= 40:
                    large_num += 1
                if 40 < int(student["年龄"]) <= 50:
                    old_num += 1
                if 50 < int(student["年龄"]) <= 60:
                    older_num += 1
                if int(student["年龄"]) > 60:
                    grandpa_num += 1
                age_list.append(int(student["年龄"]))
            other_num = len(self.product_list) - male_num - female_num
            print("男女性别分布如下：")
            print(f"男性学员数量：{male_num}人，占比：{male_num / len(self.product_list):.1%}")
            print(f"女性学员数量：{female_num}人，占比：{female_num / len(self.product_list):.1%}")
            print(f"无性别学员数量：{other_num}人，占比：{other_num / len(self.product_list):.1%}\n")
            print("各年龄段分布：")
            print(f"20岁(含20)以下学员数量：{yong_num}人，占比：{yong_num / len(self.product_list):.1%}")
            print(f"20-30岁(含30)学员数量：{middle_num}人，占比：{middle_num / len(self.product_list):.1%}")
            print(f"30-40岁(含40)学员数量：{large_num}人， 占比：{large_num / len(self.product_list):.1%}")
            print(f"40-50岁(含50)学员数量：{old_num}人， 占比：{old_num / len(self.product_list):.1%}")
            print(f"50-60岁(含60)学员数量：{older_num}人， 占比：{older_num / len(self.product_list):.1%}")
            print(f"60岁以上学员数量：{grandpa_num}人，占比：{grandpa_num / len(self.product_list):.1%}")
            print(f"平均年龄水平：{sum(age_list)/len(age_list):.1f}岁")
        else:
            print("当前学员系统暂无数据!")
        input("按任意键返回主页...")

    # 清空系统数据
    def clear_product_data(self):
        print("=" * 12, "欢迎进入学员清空系统", "=" * 12)
        if self.product_list:  # 先判断数据是否为空
            print("重要提示：数据清空后，无法恢复，请谨慎操作！！！")
            num = input("请确认是否清空(1：确认，2：取消)：").strip()
            if num == "1":
                self.product_list = [{'学号': "", '姓名': "", '性别': "", '年龄': "", '爱好': ""}]  # 放入空值字典，防止save的时候判断为空而不执行保存
                self.id_list.clear()
                self.save_product_data()
                print("---系统数据已全部清空---")
            else:
                print("---已取消清空---")
        else:
            print("当前学员系统暂无数据!")
        input("按任意键返回主页...")

    # 保存数据--将临时变量self.student_list里面的学生信息遍历出来，保存到txt文件
    def save_product_data(self):
        if self.product_list:  # 判断学员列表是否为空,只有列表不为空才执行写入
            with open("product_data.txt", "w", encoding="utf-8") as f:
                f.write("学号\t姓名\t性别\t年龄\t爱好\n")   # 首行写入标题，便于用户查看文件
                for product in self.product_list:
                    f.write(f"{product['学号']}\t{product['姓名']}\t{product['性别']}\t{product['年龄']}\t{product['爱好']}\n")
                print("---保存成功---")
        else:
            print("---暂无数据需要保存---")

    # 读取数据--读取过去存储数据的txt文件，将里面数据存到临时变量self.student_list中
    def read_product_data(self):
        try:
            with open("product_data.txt", "r", encoding="utf-8") as f:
                # 避开第一行的标题，从第二行开始遍历，将数据存储到临时变量self.student_list
                for line in f.readlines()[1:]:
                    product_id, product_name, product_nums, product_bid, product_price = line.strip().split("\t")
                    product = {'学号': product_id, '姓名': product_name, '性别': product_nums, '年龄': product_bid, '爱好': product_price}
                    self.product_list.append(product)
                    self.id_list.append(product_id)
        except (FileNotFoundError, ValueError):  # 避免初次启动时，因为txt文件还没创建或为空而报错
            print("当前学员系统暂无数据，请先添加学员信息！")

    # 登录认证--不同用户实现不同的功能权限
    def login_auth(self):
        print("=" * 12, "登录商品零售管理系统", "=" * 12)
        for i in range(5):  # 设置登录认证次数为5次
            username = input("用户名:").strip()
            password = input("密码:").strip()
            for user in self.users_list:
                if username == user['username'] and password == user['password']:
                    # 判断用户权限，执行相应权限的功能
                    if user['permission'] == '全部权限':
                        return "已取得全部权限"
                    elif user['permission'] == '只读权限':
                        return "已取得只读权限"
            else:
                if i < (5 - 1):
                    print(f"用户名或密码错误，剩余验证次数{4 - i}次，请重新输入。")
                else:
                    print(f"用户名或密码错误，今日验证次数已用完，请明天再尝试登录。")
                    input("按任意键关闭程序...")
                    return "---已退出---"

    # 显示功能选项
    def login_welcome(self):
        print("=" * 12, "商品零售管理系统", "=" * 12)
        print('\t', "*" * 5, "1、添加商品信息", "*" * 5)
        print('\t', "*" * 5, "2、删除商品信息", "*" * 5)
        print('\t', "*" * 5, "3、修改商品信息", "*" * 5)
        print('\t', "*" * 5, "4、查找商品信息", "*" * 5)
        print('\t', "*" * 5, "5、显示全部商品", "*" * 5)
        print('\t', "*" * 5, "6、商品统计信息", "*" * 5)
        print('\t', "*" * 5, "7、清空系统数据", "*" * 5)
        print('\t', "*" * 5, "0、退出管理系统", "*" * 5)
        print("=" * 46)

    # 主功能页面--前提是通过了登录认证
    def main(self, temp):
        while True:
            self.login_welcome()  # 打印欢迎界面
            self.product_list.clear()  # 清空学员列表
            self.id_list.clear()  # 清空学员学号列表
            self.read_product_data()  # 读取已经存储到txt内的数据，重新赋值给student_list
            option = input("请输入数字，选择对应的功能：").strip()
            if option == "0":
                print("~~~欢迎下次使用~~~")
                input("按任意键关闭程序...")
                break
            elif option in self.option_func_dict:
                if temp == "已取得全部权限":
                    self.option_func_dict[option]()  # 根据键值直接调用对应功能函数
                elif temp == "已取得只读权限":
                    if option == "1" or option == "2" or option == "3" or option == "7":
                        print("当前用户权限不足！你仅可以选择4、5、6对应功能，或者退出系统。")
                        input("按任意键返回主页...")
                    elif option == "4":
                        self.srh_product_data()
                    elif option == "5":
                        self.display_product_data()
                    elif option == "6":
                        self.data_statistics()
            else:
                print("~~~输入错误，请输入正确的数字！~~~")
                input("按任意键返回主页...")


# 程序入口
if __name__ == "__main__":
    manager = Student_Manager()
    var1 = manager.login_auth()
    # 通过了认证即可执行main()方法
    if var1 == "已取得全部权限" or var1 == "已取得只读权限":
        manager.main(var1)
    # 没通过认证，啥也别谈
    else:
        print(var1)

