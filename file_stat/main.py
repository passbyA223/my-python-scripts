import argparse
parser = argparse.ArgumentParser(description="统计文本文件信息")
parser.add_argument("filepath", help="待统计的文件路径")
parser.add_argument("-l","--lines",action="store_true",help="统计行数")
parser.add_argument("-w","--words",action="store_true",help="统计单词数")
parser.add_argument("-c","--chars",action="store_true",help="统计字符数")
parser.add_argument("-e","--encoding",default="utf-8",help="文件编码格式，默认为utf-8")

args = parser.parse_args()

try:
    with open(args.filepath, "r", encoding=args.encoding) as f:
        content = f.read()
        linecount = 0
        wordcount = 0
        charcount = 0
        lines = content.splitlines()
        linecount = len(lines)
        wordcount = sum(len(line.split()) for line in lines)
        charcount = len(content)
except FileNotFoundError:
    print(f"文件 {args.filepath} 不存在")
    exit(1)
except UnicodeDecodeError:
    print(f"无法以 {args.encoding} 编码读取文件 {args.filepath}")
    exit(1)
except Exception as e:
    print(f"读取文件 {args.filepath} 时发生错误: {e}")
    exit(1)
if args.lines:
    print(f"文件 {args.filepath} 的行数为: {linecount}")
if args.words:
    print(f"文件 {args.filepath} 的单词数为: {wordcount}")
if args.chars:
    print(f"文件 {args.filepath} 的字符数为: {charcount}")