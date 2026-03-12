---
name: vision-understand
description: 当用户输入图片（本地路径或url）并且用户要求图片理解、视觉问答的场景。
---

# 调用本地多模态模型（MCP）

当用户需要图像理解、视觉问答或图文分析时，通过 **vision_understand** MCP 服务调用本地多模态模型。

## 何时使用

- 用户说：「识别这张图」「看图回答」「图里有什么」「分析图片内容」「调用 vision_understand」
- 用户需要图片理解能力（如识图、图文问答、图片内容描述）
- 用户需要基于图片做信息提取、比对或解释

## 调用方式

直接运行本 Skill 下的脚本 **scripts/call_vision_understand.py** 即可调用本地 MCP 服务。

```bash
# 从 vision-understand 技能目录执行
python3 scripts/call_vision_understand.py "<prompt>" [-t|--temperature <0.0-1.0>] [--image-url <url> | --image-path <path>]

# 或从项目根目录执行
python3 skills/vision-understand/scripts/call_vision_understand.py "<prompt>" [-t|--temperature <0.0-1.0>] [--image-url <url> | --image-path <path>]
```

**参数说明**（与工具 `vision_understand` 一致）：

| 参数名        | 类型   | 必填 | 说明 |
|---------------|--------|------|------|
| `prompt`      | string | 是   | 发给本地模型的问题或指令（命令行第一个位置参数）。 |
| `temperature` | float  | 否   | 采样温度，0.0–1.0，默认 0.7；使用 `-t` 或 `--temperature`。 |
| `image_url`   | string | 否   | 远程图片 URL；使用 `--image-url`。 |
| `image_path`  | string | 否   | 本地图片路径；使用 `--image-path`，由服务端转换为 data URL。 |

注意：`--image-url` 与 `--image-path` 互斥，只能二选一。

## 示例

图片理解示例（本地图片）：

```bash
python3 scripts/call_vision_understand.py "请描述这张图片的主要内容" --image-path "/data/weizhijie/agent_project/ai_platform/assets/yhy.jpg"
```

图片理解示例（远程图片）：

```bash
python3 scripts/call_vision_understand.py "这张图里有什么？" --image-url "https://example.com/demo.jpg"
```

脚本当前直接输出模型生成的文本（`print(response.content[0].text)`）。


