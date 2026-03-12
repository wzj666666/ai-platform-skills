---
name: text-conversation
description: 当用户提出纯文本的知识问题、概念解释、问答、推理等场景时调用。
---

# 调用本地文本对话模型（MCP）

当用户提出纯文本知识问题、概念解释、逻辑推理或一般问答时，通过 **text_conversation** MCP 服务调用本地语言模型。

## 何时使用

- 用户说：「解释一下」「什么是…」「为什么…」「帮我写…」「分析一下」「调用 text_conversation」
- 用户提出纯文本知识问题（无图片、无文件）
- 用户需要文字解释、推理、写作、总结或问答

## 调用方式

直接运行本 Skill 下的脚本 **scripts/call_text_conversation.py** 即可调用本地 MCP 服务。

```bash
# 从 text_conversation 技能目录执行
python3 scripts/call_text_conversation.py "<prompt>" [-t|--temperature <0.0-1.0>]

# 或从项目根目录执行
python3 skills/text_conversation/scripts/call_text_conversation.py "<prompt>" [-t|--temperature <0.0-1.0>]
```

**参数说明**（与工具 `text_conversation` 一致）：

| 参数名        | 类型   | 必填 | 说明 |
|---------------|--------|------|------|
| `prompt`      | string | 是   | 发给本地模型的问题或指令（命令行第一个位置参数）。 |
| `temperature` | float  | 否   | 采样温度，0.0–1.0，默认 0.7；使用 `-t` 或 `--temperature`。 |

## 示例

```bash
python3 scripts/call_text_conversation.py "什么是量子纠缠？"
```

```bash
python3 skills/text_conversation/scripts/call_text_conversation.py "帮我解释一下TCP三次握手的原理" -t 0.5
```

脚本当前直接输出模型生成的文本（`print(response.content[0].text)`）。
