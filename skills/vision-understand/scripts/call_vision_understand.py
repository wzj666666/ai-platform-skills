import argparse
import asyncio
from fastmcp import Client


client = Client("http://39.105.182.86:5005/mcp")


def parse_args():
    parser = argparse.ArgumentParser(description="调用本地 MCP 服务中的 vision_understand 工具")
    parser.add_argument("prompt", type=str, help="发给本地模型的问题或指令")
    parser.add_argument(
        "-t", "--temperature",
        type=float,
        default=0.7,
        help="采样温度，0.0–1.0，默认 0.7",
    )
    image_group = parser.add_mutually_exclusive_group()
    image_group.add_argument(
        "--image-url",
        type=str,
        help="图片 URL（远程图片）",
    )
    image_group.add_argument(
        "--image-path",
        type=str,
        help="本地图片路径（由服务端转换为 data URL）",
    )
    return parser.parse_args()


async def main(
    prompt: str,
    temperature: float,
    image_url: str | None = None,
    image_path: str | None = None,
):
    async with client:
        await client.ping()
        tools = await client.list_tools()
        print("Tools:", tools)

        arguments = {"prompt": prompt, "temperature": temperature}
        if image_url:
            arguments["image_url"] = image_url
        if image_path:
            arguments["image_path"] = image_path

        response = await client.call_tool(
            name="vision_understand",
            arguments=arguments,
        )
        print(response.content[0].text)
        return response.content[0].text


if __name__ == "__main__":
    args = parse_args()
    asyncio.run(main(args.prompt, args.temperature, args.image_url, args.image_path))