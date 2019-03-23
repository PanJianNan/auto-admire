# Wechat Auto Admire
2019年3月，三八妇女节送女友什么礼物好？最近有女网友在网上吐槽，男友把她拉进百人群，群友整整夸了她三分钟。“他说是某宝上卖的夸夸群，这种沙雕男朋友还留着么？”

夸人还能挣钱？你在某宝、某鱼等平台输入搜索"夸夸群"，会发现不少商品都有成交记录。
![kuakua](https://github.com/PanJianNan/auto-admire/blob/master/resources/kuakua_bgifo.png)
5分钟50元，还有2000+的付款记录，还不错吧。

在微信上看到一篇文章[《“夸夸群”5分钟20块？！手把手教你定制一款专属夸夸机器人》](https://mp.weixin.qq.com/s/EssVIqNXLDWn_HubHzJ8Mw)，以此为鉴，让我们手撸一个夸夸机器人吧。
<br/>

### 运行环境准备：
1. 项目是基于python编写的，所有需要安装python运行环境

2. 微信web api接口交互是基于python的itchat包，所以也需要安装itchat包。

```shell
pip install itchat pillow
```

<br/>

### 简易版夸夸机器人运行操作步骤：
1. 找到文件simple_admire.py，配置你的微信群名
```
    group_name = '修改成你的群名'; 
```

2. 运行simple_admire.py
```shell
python3 simple_admire.py
```

3. 控制台会输出一个二维码，用微信扫码登录

4. 群里的好友输入关键字，如"夸我"、"求夸"，就会触发自动回复赞美的句子。

<br/>

### 注意事项：

- 此回复是使用了微信网页端，如果设置了自动回复，电脑端微信自动退出。

- 你可以自己扩展赞美句库

- 用来扫码的那个微信号就自动变成夸夸群机器人，要想体验被夸，需要夸夸群里别的微信号发送关键字信息来触发

- 如果发现二维码显示不全的情况，请修改simple_admire.py
```
# Windows系统，enableCmdQR=True
# itchat.auto_login(enableCmdQR=True, hotReload=True)
# Mac、Linux，enableCmdQR=2
itchat.auto_login(enableCmdQR=2, hotReload=True)
```

<br/>

