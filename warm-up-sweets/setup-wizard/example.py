#! /usr/bin/python3

import os
import time
import sys
import copy


def black(str):
    return "\033[30m" + str + "\033[0m"


def red(str):
    return "\033[31m" + str + "\033[0m"


def green(str):
    return "\033[32m" + str + "\033[0m"


def yellow(str):
    return "\033[33m" + str + "\033[0m"


def blue(str):
    return "\033[34m" + str + "\033[0m"


def magenta(str):
    return "\033[35m" + str + "\033[0m"


def cyan(str):
    return "\033[36m" + str + "\033[0m"


def white(str):
    return "\033[37m" + str + "\033[0m"


def boldblack(str):
    return "\033[1m\033[30m" + str + "\033[0m"


def boldred(str):
    return "\033[1m\033[31m" + str + "\033[0m"


def boldgreen(str):
    return "\033[1m\033[32m" + str + "\033[0m"


def boldyellow(str):
    return "\033[1m\033[33m" + str + "\033[0m"


def boldblue(str):
    return "\033[1m\033[34m" + str + "\033[0m"


def boldmagenta(str):
    return "\033[1m\033[35m" + str + "\033[0m"


def boldcyan(str):
    return "\033[1m\033[36m" + str + "\033[0m"


def boldwhite(str):
    return "\033[1m\033[37m" + str + "\033[0m"


def shell(command):
    os.system(command)


def install(pkg):
    shell('sudo apt -y install ' + pkg)  # add option y for Yes when asked


def installEssentials():
    packages = [
        ['设置CPU性能模式的小工具', 'indicator-cpufreq'],
        ['C/C++工具', 'make cmake build-essential clang clang-tools-7'],
        #  ['以文件树形式列出文件夹内容', 'tree'],
        ['JavaScript工具', 'nodejs npm'],
        ['压缩/解压rar与zip压缩包的工具', 'rar'],
        ['键盘映射工具', 'xbindkeys xautomation'],
        ['按键显示工具', 'screenkey'],
        ['fcitx输入法系统', 'fcitx'],
        ['fcitx的Mozc日语输入法', 'fcitx-mozc'],
        ['GNOME桌面个性化工具和插件', 'gnome-tweak-tool gnome-shell-extensions gnome-shell-extension-dash-to-panel gnome-shell-extension-top-icons-plus dconf-editor'],
        ['Markdown文件阅读/编辑器', 'Typora'],
        ['编辑器VSCode', 'code'],
        #  ['OpenCV highghui module的函数的GTK库', 'libgtk2.0-dev libcanberra-gtk-module'],
        #  ['C++的CPU并行计算库', 'libtbb-dev'],
        #  ['相机编程接口库', 'v4l-utils'],
        #  ['Google的C++中的日志模块', 'libgoogle-glog-dev']
        ['python3附加库', 'python3-dev'],
        ['办公软件套件', 'libreoffice'],
        ['Linux下很好用的电脑管家', 'stacer'],
        ['GIF录制工具', 'peek'],
        ['镜像烧录工具', 'balena-etcher-electron']
    ]
    for i in range(len(packages)):
        packagesText = copy.deepcopy(packages)
        packagesText[i][0] = boldcyan(packagesText[i][0])
        packagesText[i][1] = white(packagesText[i][1])
        print("{p[0]}\n+ {p[1]}\n".format(p=packagesText[i]))
    print(boldcyan('带图标的精致ls命令') + '\n+ ' + white('lsd'))
    ifInstall = input(boldyellow('是否安装? ') + boldred('[Y/n] '))
    if ifInstall == 'y' or ifInstall == '':
        # add alternative sources
        shell('''
        # add typora
        wget -qO - https://typora.io/linux/public-key.asc | sudo apt-key add -
        sudo add-apt-repository 'deb https://typora.io/linux ./'
        # add VSC
        wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
        sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
        # add stacer
        sudo add-apt-repository ppa:oguzhaninan/stacer -y
        # add peek
        sudo add-apt-repository ppa:peek-developers/stable
        # add etcher
        echo "deb https://deb.etcher.io stable etcher" | sudo tee /etc/apt/sources.list.d/balena-etcher.list
        sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 379CE192D401AB61
        sudo apt update
        ''')
        shell('snap install lsd')
        for i in range(len(packages)):
            install(packages[i][1])
    input(boldyellow('\a完成 [Enter]'))


def gitConfig():
    print(white('回车填入') + green('LeoJhon.Song@outlook.com'))
    email = input(boldwhite('输入git账户邮箱▶ '))
    if email is '':
        email = 'LeoJhon.Song@outlook.com'
    print(white('回车填入主机名') + boldwhite(os.uname()[1]))
    machineName = input(boldwhite('输入本机名▶ '))
    if machineName is '':
        machineName = os.uname()[1]
    shell('git config --global user.email ' + email)
    shell('git config --global user.name ' + machineName)
    input(boldyellow('\a完成 [Enter]'))


def vimConfig():
    ifLeo = input(boldwhite(
        '是否使用') + green(' https://github.com/LeoJhonSong/vimrc ') + boldwhite('的vim配置? [Y/n] '))
    if ifLeo == 'y' or ifLeo == '':
        if os.path.exists(os.path.expanduser('~/.vimrc')):
            with open(os.path.expanduser('~/.vimrc')) as vimrc:
                if vimrc.read(200) is not '':
                    ifCover = input(boldred('已存在vim配置\n\t覆盖 (c)\n\t将原 ~/.vimrc 备份至') + green('~/.vimrc.bak') + boldred(' (b)'))
                    if ifCover == 'b':
                        shell('mv ~/.vimrc ~/.vimrc.bak')
                    elif ifCover == 'c':
                        shell('rm ~/.vimrc')
        if os.path.exists(os.path.expanduser('~/.vim')):
            ifCover = input(boldred('已存在vim配置\n\t覆盖 (c)\n\t将原 ~/.vim 备份至') + green('~/.vim.bak') + boldred(' (b)'))
            if ifCover == 'b':
                shell('mv -r ~/.vim ~/.vim.bak')
            elif ifCover == 'c':
                shell('rm -r ~/.vim')
        shell('''
        git clone git@github.com:LeoJhonSong/vimrc.git ~/.vim
        ln -s ~/.vim/.vimrc ~/.vimrc
        ''')
    input(boldyellow('\a完成 [Enter]'))


def wakaConfig():
    input(boldyellow('\a完成 [Enter]'))


def grubPlyConfig():
    input(boldyellow('\a完成 [Enter]'))


def winDiskConfig():
    diskName = 'Windows'
    print(
        boldyellow('设置开机自动将Windows盘挂载到')
        + green(' /media/' + diskName + '▽\n')
    )
    while os.path.exists('/media/' + diskName):
        print(boldred('已存在') + green(' /media/' + diskName))
        print(boldred('\t没有问题, 清空 /media/' + diskName + ' (ok)\n\t挂载到 /media下其他文件夹 (c)\n\t退出Windows盘挂载 (q)'))
        ifChange = input(boldwhite('▶ '))
        if ifChange == 'ok':
            shell('sudo rm -rf /media/' + diskName)
        elif ifChange == 'c':
            diskName = input(boldwhite('输入挂载文件夹名▶ '))
        elif ifChange == 'q':
            input(boldyellow('\a完成 [Enter]'))
            break
    shell('sudo mkdir /media/' + diskName)
    UUID = input(boldwhite('输入Windows系统所在分区的UUID▶ '))
    with open('/etc/fstab') as fstab:
        if fstab.read().find(str(UUID)) is not -1:
            print(boldred('该Windows盘已挂载'))
        else:
            shell('echo \'echo # Windows disk >> /etc/fstab\' | sudo sh' + 'echo \'echo UUID=' + UUID + ' /media/' + diskName + ' ntfs defaults 0 2  >> /etc/fstab\' | sudo sh')
    input(boldyellow('\a完成 [Enter]'))


def deppinWineConfig():
    input(boldyellow('\a完成 [Enter]'))


def loginScrConfig():
    input(boldyellow('\a完成 [Enter]'))


def anaConfig():
    input(boldyellow('\a完成 [Enter]'))


def flatpakConfig():
    install('flatpak')
    install('gnome-software-plugin-flatpak')
    shell('flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo')


def finish():
    print(boldyellow("\a结束!\n"))
    exit()


option = {
    '0': installEssentials,
    '1': gitConfig,
    '2': vimConfig,
    '3': wakaConfig,
    '4': grubPlyConfig,
    '5': winDiskConfig,
    '6': deppinWineConfig,
    '7': loginScrConfig,
    '8': anaConfig,
    '9': flatpakConfig,
    'q': finish
}

optionText = [
    [boldwhite('0 '), boldwhite('安装必备软件, 包'), green('')],
    [boldwhite('1 '), boldwhite('配置git账户'), green('')],
    [boldwhite('2 '), boldwhite('配置vim'), green('')],
    [boldwhite('3 '), boldwhite('安装bash-wakatime'), green('')],
    [boldwhite('4 '), boldwhite('个性化GRUB界面和Plymouth界面'), green('')],
    [boldwhite('5 '), boldwhite('设置开机自动将Windows盘挂载到'), green(' /media/Windows')],
    [boldwhite('6 '), boldwhite('安装deepin-wine (TIM, QQ, 微信, 迅雷等移植软件的安装环境)'), green('')],
    [boldwhite('7 '), boldwhite('指定登录界面背景图片为'), green(' ~/Pictures/login-screen/custom.jpg')],
    [boldwhite('8 '), boldwhite('安装Anaconda'), green('')],
    [boldwhite('9 '), boldwhite('安装Flatpak并添加Flathub仓库'), green('')],
    [boldred('q '), boldred('退出'), green('')]
]


while(True):
    shell('clear')
    print(boldyellow("\a选择要进行的配置▽\n\n"))
    for i in range(len(optionText)):
        print("\t{o[0]}  {o[1]} {o[2]}\n".format(o=optionText[i]))
    optionInput = input(boldwhite('\n▶ '))
    # print(white(os.get_terminal_size().columns * '▁' + '\n'))
    shell('clear')
    if optionInput is not 'q':
        print(boldyellow(optionText[int(optionInput)][1] + '▽\n'))
    main = option[optionInput]
    main()
