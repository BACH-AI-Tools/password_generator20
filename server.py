"""
Password Generator20 MCP Server

使用 FastMCP 的 from_openapi 方法自动生成

Version: 1.0.0
Transport: stdio
"""
import os
import json
import httpx
from fastmcp import FastMCP

# 服务器版本和配置
__version__ = "1.0.0"
__tag__ = "password_generator20/1.0.0"

# API 配置
API_KEY = os.getenv("API_KEY", "")

# 传输协议配置
TRANSPORT = "stdio"


# OpenAPI 规范
OPENAPI_SPEC = """{\n  \"openapi\": \"3.0.0\",\n  \"info\": {\n    \"title\": \"Password Generator20\",\n    \"version\": \"1.0.0\",\n    \"description\": \"RapidAPI: marook332-tgQpJK5rj/password-generator20\"\n  },\n  \"servers\": [\n    {\n      \"url\": \"https://password-generator20.p.rapidapi.com\"\n    }\n  ],\n  \"paths\": {\n    \"/password\": {\n      \"get\": {\n        \"summary\": \"password\",\n        \"description\": \"Generates a password with standard settings - length = 10 - 1 special char - 2 numbers\",\n        \"operationId\": \"password\",\n        \"parameters\": [\n          {\n            \"name\": \"length\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Creates a password with the given length, max length is 32 chars\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": \"10\",\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"spchar\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Number of special characters to be used\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": \"2\",\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"numbers\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Number of digits to be used\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": \"2\",\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"umlauts\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Example value: \",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"quantity\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Number of passwords issued, max is 10 per call.\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": \"10\",\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    }\n  },\n  \"components\": {\n    \"securitySchemes\": {\n      \"ApiAuth\": {\n        \"type\": \"apiKey\",\n        \"in\": \"header\",\n        \"name\": \"X-RapidAPI-Key\"\n      }\n    }\n  },\n  \"security\": [\n    {\n      \"ApiAuth\": []\n    }\n  ]\n}"""

# 创建 HTTP 客户端
# 设置默认 headers
default_headers = {}


# RapidAPI 必需的 headers
if API_KEY:
    default_headers["X-RapidAPI-Key"] = API_KEY
    default_headers["X-RapidAPI-Host"] = "password-generator20.p.rapidapi.com"
else:
    print("⚠️  警告: 未设置 API_KEY 环境变量")
    print("   RapidAPI 需要 API Key 才能正常工作")
    print("   请设置: export API_KEY=你的RapidAPI-Key")

# 对于 POST/PUT/PATCH 请求，自动添加 Content-Type
default_headers["Content-Type"] = "application/json"




client = httpx.AsyncClient(
    base_url="https://password-generator20.p.rapidapi.com", 
    timeout=30.0
)


# 从 OpenAPI 规范创建 FastMCP 服务器
openapi_dict = json.loads(OPENAPI_SPEC)
mcp = FastMCP.from_openapi(
    openapi_spec=openapi_dict,
    client=client,
    name="password_generator20",
    version=__version__
)


# 注册请求拦截器，为所有请求添加 RapidAPI headers
_original_request = client.request

async def _add_rapidapi_headers(method, url, **kwargs):
    """拦截所有请求，添加必需的 RapidAPI headers"""
    # 确保 headers 存在
    if 'headers' not in kwargs:
        kwargs['headers'] = {}
    
    # 添加 RapidAPI 必需的 headers
    if API_KEY:
        kwargs['headers']['X-RapidAPI-Key'] = API_KEY
        kwargs['headers']['X-RapidAPI-Host'] = "password-generator20.p.rapidapi.com"
    else:
        print("⚠️  警告: API_KEY 未设置，请求可能失败")
    
    # 对于 POST/PUT/PATCH，添加 Content-Type
    if method.upper() in ['POST', 'PUT', 'PATCH']:
        if 'Content-Type' not in kwargs['headers']:
            kwargs['headers']['Content-Type'] = 'application/json'
    
    return await _original_request(method, url, **kwargs)

# 替换 request 方法
client.request = _add_rapidapi_headers


def main():
    """主入口点"""
    print(f"🚀 启动 Password Generator20 MCP 服务器")
    print(f"📦 版本: {__tag__}")
    print(f"🔧 传输协议: {TRANSPORT}")
    
    print()
    
    # 运行服务器
    
    mcp.run(transport="stdio")
    


if __name__ == "__main__":
    main()