import argparse
import asyncio
from fastmcp import Client


client = Client("http://localhost:5005/mcp")


def parse_args():
    parser = argparse.ArgumentParser(description="调用本地 MCP 服务中的 text_conversation 工具")
    parser.add_argument("prompt", type=str, help="发给本地模型的问题或指令")
    parser.add_argument(
        "-t", "--temperature",
        type=float,
        default=0.7,
        help="采样温度，0.0–1.0，默认 0.7",
    )
    return parser.parse_args()


async def call_text_conversation(prompt: str, temperature: float):
    async with client:
        await client.ping()
        tools = await client.list_tools()
        print("Tools:")
        for tool in tools:
            print(tool)
            print("-" * 50)

        text_conversation_response = await client.call_tool(
            name="text_conversation",
            arguments={"prompt": prompt, "temperature": temperature},
        )
        print("text_conversation_response: ")
        print(text_conversation_response.content[0].text)
        print("=" * 100)


if __name__ == "__main__":
    args = parse_args()
    asyncio.run(call_text_conversation(args.prompt, args.temperature))
