#Copyright(c) TedZyzsdy 2025
#Date: 2025/6/13 20:46
import os
hosts = 'C:\\Windows\\System32\\drivers\\etc\\hosts'
def get_all_hosts():
    valid_hosts = []
    try:
        with open(hosts, 'r') as file:
            for line in file:
                stripped_line = line.strip()
                # 跳过空行和注释行
                if not stripped_line or stripped_line.startswith('#'):
                    continue
                valid_hosts.append(stripped_line)
    except FileNotFoundError:
        print(f'错误：找不到 hosts 文件 - {hosts}')
        return []
    except PermissionError:
        print(f'错误：没有权限读取 hosts 文件 - {hosts}')
        return []
    except Exception as e:
        print(f'读取 hosts 文件时发生错误: {e}')
        return []
    return valid_hosts
def add_host(host_from,host_to,tag = 'Normal'):
    try:
        with open(hosts,'a') as file:
            file.write('\n%s %s # Managed by HostChangeTool [%s]'%(host_from,host_to,tag))
    except:
        add_host(host_from,host_to,tag)
def del_host(all=True, tag='normal'):
    # 读取所有行（包含换行符）
    with open(hosts, 'r') as file:
        lines = file.readlines()
    # 创建新内容，排除要删除的行
    new_lines = []
    for line in lines:
        # 检查是否是工具添加的行
        if '# Managed by HostChangeTool' in line:
            # 如果all为True或tag匹配，则跳过（删除）
            if all or f'[{tag}]' in line:
                continue
        # 保留其他所有行
        new_lines.append(line)
    print(f'已删除{'所有' if all else tag}托管条目')
    # 写回文件
    with open(hosts, 'w') as file:
        file.writelines(new_lines)
##############################################################Other Tools#######################################################################
def broforce():
    pass
##############################################################UI################################################################################
def main():
    print('------------------HostChangeTool---------------------')
    print('  1.增加host')
    print('  2.删除host')
    print('  3.展示hosts')
    #print('  4.其他')
    number_choice = input('选择一个选项 > ')
    if number_choice == '1':
        host_from = input('原host > ')
        host_to = input('被重定向host > ')
        tag = input('标签 > ')
        add_host(host_from=host_from,host_to=host_to,tag=('Normal' if tag == '' else tag))
    elif number_choice == "2":
        if_all = input("是否删除所有由HostChangeTool托管的hosts(y,N) > ")
        if if_all == "y":
            del_host(all=True)
        else:
            tag = input("请输入要删除的标签 > ")
            del_host(all=False,tag=tag)
    elif number_choice == '3':
        hosts_list = get_all_hosts()
        print('下面是所有托管的host')
        for host in hosts_list:
            print(host)
        print('end.')
        input()
if __name__ == '__main__':
    while True:
        try:
            os.system("cls")
            main()
        except KeyboardInterrupt:
            break