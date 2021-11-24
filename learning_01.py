# 创建一个方法
def print_hi(word):
    print(f'hello {word}!')


# 当1==2时为真
if 2 == 2:
    # 调用方法，传递实参
    print_hi('world')
else:
    print_hi("python")


# 函数入口
if __name__ == '__main__':
    print('you are right!')
else:
    print('you are wrong!')
