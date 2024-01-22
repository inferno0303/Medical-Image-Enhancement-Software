from PyInstaller.__main__ import run

if __name__ == '__main__':
    opts = [
        '--onefile',  # 单可执行文件（.exe）
        '--windowed',  # 隐藏命令行控制台
        '--icon=./src/assets/icon.ico',  # 图标的文件路径
        './src/main.py',  # 程序的主函数
    ]
    run(opts)
