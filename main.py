import configparser

config = configparser.ConfigParser()
config.read("README.txt", encoding="UTF-8")
run_mode = config["交互模式"]["交互模式"]
print(f"运行模式：{run_mode}")
assert run_mode in {"图形界面", "命令行", "文件"}


def main():
    if run_mode == "图形界面":
        import sys
        from PyQt5 import QtWidgets
        from window import UI

        app = QtWidgets.QApplication(sys.argv)
        ui = UI()
        ui.show()
        sys.exit(app.exec_())

    else:
        from algo import Solver

        sol = Solver()
        xzq_file, role_file = config["xlsx文件"]["心之器"], config["xlsx文件"]["角色"]
        ans_num = int(config["输出数量"]["输出数量"])
        print("命令行初始化完毕")
        print("建议先阅读README.txt")

        if run_mode == "命令行":
            mfq_choice = input("指定魔法器，直接回车表示不重塑，0表示阴之水晶球，其他魔法器编号见README.txt：")
            mfq_choice = int(mfq_choice) if mfq_choice else -1
            mfq_k = float(
                input("指定魔法器质量系数，0.8表示最大值的80%(大概是B级)，1表示最大值(最好的S级)："))
            mfq_num = int(input("指定魔法器有效词条数，1到12："))
            xzq_choice = set(input("指定0到3个心之器，空格分隔：").split())
        else:
            mfq_choice = (-1 if int(config["魔法器选项"]["重塑"]) else int(
                config["魔法器选项"]["指定魔法器"]))
            mfq_k, mfq_num = float(config["魔法器选项"]["质量系数"]), int(
                config["魔法器选项"]["有效词条数"])
            xzq_choice = set(
                filter(
                    None,
                    [
                        config["心之器选项"]["指定心之器1"],
                        config["心之器选项"]["指定心之器2"],
                        config["心之器选项"]["指定心之器3"],
                    ],
                ))
        print(
            f"输出答案数指定为{ans_num}，心之器、角色文件分别指定为{xzq_file}、{role_file}，可在README.txt中调整"
        )
        sol.load_xzq(xzq_file)
        sol.load_role(role_file)
        sol.load_mfq(role_file, mfq_choice, mfq_k, mfq_num)
        ans = sol.calc_xzq(ans_num, xzq_choice)
        if not ans:
            print("无解")
        for xx in ans:
            for yy in xx:
                print(yy[1:])
                print(xx[yy])
            print()


if __name__ == "__main__":
    print("Re0手游装备推荐器&伤害计算器v3.0.1")
    main()
