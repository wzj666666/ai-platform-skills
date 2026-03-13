---
name: text2image
description: 当用户需要根据文字描述生成图片的场景。
---

# 调用文生图模型（MCP）

当用户描述一张图并希望 AI 生成时，通过 **text2image** MCP 服务调用生图模型。

## 何时使用

- 用户说：「生成一张…的图」「画一个…」「帮我生成图片」「调用 text2image」
- 用户提供文字描述，希望得到一张对应的图片
- 用户需要 AI 绘画、场景渲染、风格插画等

## 调用方式

直接运行本 Skill 下的脚本 **scripts/call_text2image.py** 即可调用本地 MCP 服务。

```bash
# 从 text2image 技能目录执行
python3 scripts/call_text2image.py "<prompt>" [-t|--temperature <0.0-1.0>]

# 或从项目根目录执行
python3 skills/text2image/scripts/call_text2image.py "<prompt>" [-t|--temperature <0.0-1.0>]
```

**参数说明**（与工具 `text2image` 一致）：

| 参数名        | 类型   | 必填 | 说明 |
|---------------|--------|------|------|
| `prompt`      | string | 是   | 描述要生成图片内容的文字（命令行第一个位置参数）。 |
| `temperature` | float  | 否   | 采样温度，0.0–1.0，默认 0.7；使用 `-t` 或 `--temperature`。 |

## 示例

```bash
python3 scripts/call_text2image.py "一只在星空下奔跑的狼，油画风格"
```

```bash
python3 skills/text2image/scripts/call_text2image.py "赛博朋克城市夜景，霓虹灯倒影在水面上" -t 0.9
```

脚本成功时返回保存的图片路径（`generated_images/image_0_<timestamp>.<ext>`），失败时返回 `None`。
