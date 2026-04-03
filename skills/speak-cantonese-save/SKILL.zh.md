---
name: speak-cantonese-save
description: 将粤语句子转换为语音并保存为当前目录下的 mp3 文件。仅当用户明确输入 "use skill speak-cantonese-save" 后跟粤语句子时才触发。mp3 文件保存在当前目录——不创建子目录。
---

# 粤语朗读并保存技能（speak-cantonese-save）

> 本文件供人类用户阅读。AI 平台将读取英文版 [SKILL.md](SKILL.md) 来运行此技能。

> English version: [SKILL.md](SKILL.md)

使用 edge-tts 朗读粤语句子，并将音频保存为当前目录下的 mp3 文件。

## 工作流程

1. 从用户消息中提取句子（"use skill speak-cantonese-save" 之后的所有内容）
2. 执行 `scripts/speak_cantonese_save.py {句子}` — 朗读并保存 mp3 至当前目录
3. 向用户显示已保存的文件名

## 触发示例

- `use skill speak-cantonese-save 各個國家有各個國家嘅國歌`
- `use skill speak-cantonese-save 一蚊一隻雞，一蚊一隻龜`

## 输出格式

```
🔊 Spoke and saved: {句子}
[Saved to {文件路径}.mp3]
```

## 重要提示

- 每次请求只执行一次脚本
- mp3 保存在当前目录——不创建子目录
- 若脚本以代码 0 退出，表示执行成功，无需重试

## 安装

```bash
pip install edge-tts    # 缺失时自动安装
```
