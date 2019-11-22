# Pixiv-WallPaper

这个任务是利用了[这个项目](https://github.com/cheer-fun/Pixiv-Illustration-Collection-Backend), 每次访问 https://api.pixivic.com/illust?w_h_ratio=16-9&minWidth=1080&range=0.0001&isR18=false 这个链接都能得到一张长宽比为16:9, 清晰度至少1080的精美P站随机图片. (更多链接设定方式查看这个项目主页)

> 看起来作者正在调整网站, 目前暂时用不了. 我们改为从[unsplash](https://unsplash.com/)获取图片. 每次访问 https://source.unsplash.com/random 即可获得一张精美图片. 更多调用设置参见[这里](https://source.unsplash.com/)

要求这个程序能每隔一段时间从这个网址获取一张图片下载到本地并设为壁纸 (如果你不知道怎么设为壁纸只做到下载到本地这一步也可以). 希望能做到能在程序开头/专门的配置文件中配置**刷新时间**, **图片下载地址**等.

爬取图片推荐使用**requests**库.

示例脚本使用:

用Python执行

```shell
python example.py
```

先给予脚本运行权限, 然后直接运行

```shell
chmod a+x example.py
./example.py
```