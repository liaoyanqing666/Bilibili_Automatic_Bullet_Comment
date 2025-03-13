# Bilibili_Automatic_Bullet_Comment
Bilibili视频自动发送弹幕，Automatically send bullet comments in Bilibili videos.

## Chinese Introduction

**切勿使用此程序攻击网站或任何人，此程序仅供个人使用，如弹幕刷屏/进行更深度开发。**

本项目完全模拟人类操作，完成在视频某个时间点（可能有2秒左右的误差）重复发送弹幕的操作。如果有需要，可以fork后在这个框架上增加更多功能，例如根据时间发送弹幕字幕，甚至可以AI读取歌曲并在各个时间点发送弹幕歌词。

项目原理：打开视频网站、使用cookie登录、暂停视频、输入跳转时间并跳转、等待0.5秒跳转完毕、暂停视频、间隔5.5s重复输入并发送文本内容。

本项目鲁棒性较弱，因此可能会出现：时间跳转失败，cookie加载失败，时间跳转后不暂停等问题，请尝试重新运行或者修改一些参数。

cookie是用来进行免密登陆的，在已经登陆过的Bilibili网页上按F12，选中“应用”，找到cookie，点开，并把其中对应内容复制过去（有经验的屏蔽此条）。也可以直接全部复制后和LLM说把所有相关cookie填写好。

本代码参考了之前的项目[Bilibili直播自动发送弹幕](https://github.com/liaoyanqing666/Bilibili_Live_Broadcast_Automatic_Bullet_Screen/)，使用的方法也基本相同。没有使用 `bilibili_api` 是因为这个方法有更强的可视性（绝不是因为我没读懂 `bilibili_api` 的文档）

## English Introduction

**Never use this program to attack the website or anyone, this program is only for personal use, such as draw a bullet raffle.**

This project fully simulates human operations to perform the task of repeatedly sending bullet comments at a specific time point in a video (with a possible error of around 2 seconds). If needed, you can fork this project and add more features to this framework, such as sending bullet comment subtitles based on time, or even using AI to read songs and send bullet comment lyrics at various time points.

Project Principle: Open the video website, log in using cookies, pause the video, input and jump to the desired time, wait for 0.5 seconds for the jump to complete, pause the video, and then repeatedly input and send text content at 5.5-second intervals.

The robustness of this project is relatively weak, so issues such as time jump failure, cookie loading failure, or failure to pause after a time jump may occur. Please try running it again or modifying some parameters.

Cookies are used for password-free login. On a Bilibili webpage where you are already logged in, press F12, select "Application," find the cookies, open them, and copy the corresponding content (experienced users can ignore this step). Alternatively, you can copy all the content and ask an LLM to fill in all the relevant cookies.

This code references a previous project [Bilibili Live Broadcast Automatic Bullet Screen](https://github.com/liaoyanqing666/Bilibili_Live_Broadcast_Automatic_Bullet_Screen/), and the methods used are essentially the same. The `bilibili_api` was not used because this method offers better visibility (and definitely not because I didn't understand the `bilibili_api` documentation).
