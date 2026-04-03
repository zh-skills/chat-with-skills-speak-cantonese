---
name: speak-cantonese
description: 将粤语句子转换为语音并朗读。仅当用户明确输入 "use skill speak-cantonese" 后跟粤语句子时才触发。脚本直接播放音频——不保存任何 mp3 文件，无需搜索文件。
---

# 粤语朗读技能（speak-cantonese）

> 本文件供人类用户阅读。AI 平台将读取英文版 [SKILL.md](SKILL.md) 来运行此技能。

> English version: [SKILL.md](SKILL.md)

使用 edge-tts（微软 zh-HK-HiuMaanNeural 语音）朗读粤语句子。

## 工作流程

1. 从用户消息中提取句子（"use skill speak-cantonese" 之后的所有内容）
2. 执行 `scripts/speak_cantonese.py {句子}` — 脚本播放音频后退出
3. 向用户显示结果
4. 不要搜索 mp3 文件。不要重试。脚本退出即表示任务完成。

## 触发示例

- `use skill speak-cantonese 各個國家有各個國家嘅國歌`
- `use skill speak-cantonese 一蚊一隻雞，一蚊一隻龜`

## 输出格式

```
🔊 Spoke: {句子}
```

## 重要提示

- 每次请求只执行一次脚本
- 脚本直接播放音频后退出——不保存 mp3 文件
- 脚本退出后不要搜索 mp3 文件
- 若脚本以代码 0 退出，表示执行成功，无需重试

## 安装

```bash
pip install edge-tts    # 缺失时自动安装
```

## 参考文档

详细实现说明请参阅 [references/implementation_notes.md](references/implementation_notes.md)。
