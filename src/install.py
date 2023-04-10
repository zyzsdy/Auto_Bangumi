import os
import json

def setup():
    # 在当前目录下建立config、data文件夹
    root_path = os.path.dirname(os.path.abspath(__file__))

    print("root_path: ", root_path)

    config_path = os.path.join(root_path, "config")
    data_path = os.path.join(root_path, "data")

    if not os.path.exists(config_path):
        os.mkdir(config_path)
    if not os.path.exists(data_path):
        os.mkdir(data_path)

    # 如果config目录中不存在config.json，那么以DEFAULT_SETTINGS为基础，开始交互性配置
    config_file = os.path.join(config_path, "config.json")
    if not os.path.exists(config_file):
        # 交互性配置
        setting = DEFAULT_SETTINGS
        print("欢迎使用AutoBangumi！")
        print("请按照以下提示操作，完成初始化配置：")
        print("1. 配置qBittorrent。")
        print("")
        print("请打开qBittorrent，点击“工具”->“选项”->“Web UI”，在“Web UI”选项卡中，")
        print("勾选“启用Web UI”，填写“IP地址”为 127.0.0.1")
        print("填写“端口”为 37145")
        print("并在“验证”选项中，填写“用户名”和“密码”（请牢记，后续会用到）")
        print("")
        print("请在此处填写您刚才配置的用户名：")
        setting["downloader"]["username"] = input()
        print("请在此处填写您刚才配置的密码：")
        setting["downloader"]["password"] = input()
        print("请在qBittorrent的“选项”对话框中，点击“确定”按钮，保存配置。")
        print("")
        print("2. 配置保存新番的路径。")
        print("")
        print("请在此处填写您想要保存新番的路径（请确保路径存在）：")
        setting["downloader"]["path"] = input()
        print("")
        print("3. 配置Mikan的RSS订阅地址。")
        print("")
        print("请打开Mikan的RSS订阅页面，复制RSS订阅地址。")
        print("打开 https://mikanani.me/Home/MyBangumi ，点击“RSS订阅”按钮，")
        print("复制您地址栏上的RSS订阅地址，粘贴到此处：")
        setting["rss_parser"]["link"] = input()
        print("")
        print("4. 配置访问代理。")
        print("")
        print("访问Mikan的RSS订阅地址，以及访问TMDB的API，可能会遇到网络问题。")
        print("我们强烈建议您配置代理。")
        print("如果您需要配置代理，请键入“y”并回车，否则直接回车。")
        if input() == "y":
            setting["proxy"]["enable"] = True
            print("请输入代理服务器地址，如果你使用本机代理（127.0.0.1），请直接回车。")
            proxy_host = input()
            if proxy_host == "":
                proxy_host = "127.0.0.1"
            setting["proxy"]["host"] = proxy_host
            print("请输入代理服务器端口，如果你使用Clash的默认端口号（7890），请直接回车。")
            proxy_port = input()
            if proxy_port == "":
                proxy_port = "7890"
            setting["proxy"]["port"] = proxy_port
        else:
            setting["proxy"]["enable"] = False
        print("")
        print("交互性配置已完成。如果您需要修改配置，请直接修改“config/config.json”文件。")

        # 将当前配置转为json字符串
        config_json = json.dumps(setting, indent=4)
        # 将json字符串写入config.json
        with open(config_file, "w") as f:
            f.write(config_json)
    else:
        print("config.json已存在，使用原有的配置。")

    print("初始化配置已完成。")

if __name__ == "__main__":
    setup()