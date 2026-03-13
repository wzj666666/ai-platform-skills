import argparse
import asyncio
from fastmcp import Client


client = Client("http://localhost:5005/mcp")


def parse_args():
    parser = argparse.ArgumentParser(description="调用本地 MCP 服务中的 text2image 工具")
    parser.add_argument("prompt", type=str, help="描述要生成图片内容的文字")
    parser.add_argument(
        "-t", "--temperature",
        type=float,
        default=0.7,
        help="采样温度，0.0–1.0，默认 0.7",
    )
    return parser.parse_args()


async def main(prompt: str, temperature: float):
    async with client:
        await client.ping()
        tools = await client.list_tools()
        print("Tools:", tools)

        response = await client.call_tool(
            name="text2image",
            arguments={"prompt": prompt, "temperature": temperature},
        )
        print(response)
        return response


if __name__ == "__main__":
    args = parse_args()
    asyncio.run(main(args.prompt, args.temperature))
