import argparse

def main():
    parser = argparse.ArgumentParser(description="python命令行脚本")
    parser.add_argument("name", nargs="?",default = "世界", help = "你的名字")
    args = parser.parse_args()
    print(f"您好，{args.name}!")

if __name__ == "__main__":
    main()