"""
Copyright (c) 2026 山野小娃 (Jorney Ruan)

SACP Python SDK - 简单的SACP协议客户端实现
Email: ahua2020@qq.com
"""

import requests
import hashlib
import time
import json
from typing import Dict, List, Optional, Any


class SACPClient:
    """SACP协议Python客户端"""

    def __init__(self, base_url: str, api_key: str, api_secret: str):
        """
        初始化SACP客户端

        Args:
            base_url: API基础URL, 如 https://api.example.com
            api_key: SACP API Key
            api_secret: SACP API Secret
        """
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.api_secret = api_secret
        self.session = requests.Session()

    def _sign(self, body: str, timestamp: int) -> str:
        """
        生成请求签名

        Args:
            body: 请求体字符串
            timestamp: 时间戳

        Returns:
            SHA256签名字符串
        """
        message = body + str(timestamp) + self.api_secret
        return hashlib.sha256(message.encode('utf-8')).hexdigest()

    def _make_headers(self, data: Dict[str, Any]) -> Dict[str, str]:
        """
        生成请求头

        Args:
            data: 请求数据字典

        Returns:
            包含认证信息的请求头
        """
        timestamp = int(time.time())
        body = json.dumps(data, ensure_ascii=False)
        signature = self._sign(body, timestamp)

        return {
            'X-SACP-API-Key': self.api_key,
            'X-SACP-Timestamp': str(timestamp),
            'X-SACP-Signature': signature,
            'Content-Type': 'application/json'
        }

    def write(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        写入单条数据

        Args:
            data: 符合SACP规范的数据字典

        Returns:
            API响应结果
        """
        url = f"{self.base_url}/api/v1/sacp/data/write"
        headers = self._make_headers(data)
        body = json.dumps(data, ensure_ascii=False)

        response = self.session.post(url, data=body, headers=headers)
        response.raise_for_status()
        return response.json()

    def batch_write(self, data_list: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        批量写入数据

        Args:
            data_list: 符合SACP规范的数据字典列表

        Returns:
            API响应结果
        """
        url = f"{self.base_url}/api/v1/sacp/data/batch-write"
        timestamp = int(time.time())
        body = json.dumps(data_list, ensure_ascii=False)
        signature = self._sign(body, timestamp)

        headers = {
            'X-SACP-API-Key': self.api_key,
            'X-SACP-Timestamp': str(timestamp),
            'X-SACP-Signature': signature,
            'Content-Type': 'application/json'
        }

        response = self.session.post(url, data=body, headers=headers)
        response.raise_for_status()
        return response.json()

    def list(self, data_type: Optional[str] = None, page: int = 1,
             page_size: int = 20, **kwargs) -> Dict[str, Any]:
        """
        查询数据列表

        Args:
            data_type: 数据类型过滤
            page: 页码
            page_size: 每页数量
            **kwargs: 其他查询参数

        Returns:
            API响应结果
        """
        url = f"{self.base_url}/api/v1/sacp/data/list"
        params = {'page': page, 'page_size': page_size}
        if data_type:
            params['type'] = data_type
        params.update(kwargs)

        headers = {
            'X-SACP-API-Key': self.api_key,
            'Content-Type': 'application/json'
        }

        response = self.session.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()

    def detail(self, data_id: str) -> Dict[str, Any]:
        """
        查询单条数据详情

        Args:
            data_id: 数据ID

        Returns:
            API响应结果
        """
        url = f"{self.base_url}/api/v1/sacp/data/detail"
        params = {'id': data_id}

        headers = {
            'X-SACP-API-Key': self.api_key,
            'Content-Type': 'application/json'
        }

        response = self.session.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()

    def update(self, data_id: str, updates: Dict[str, Any]) -> Dict[str, Any]:
        """
        更新数据

        Args:
            data_id: 数据ID
            updates: 要更新的字段

        Returns:
            API响应结果
        """
        url = f"{self.base_url}/api/v1/sacp/data/update"
        updates['id'] = data_id
        headers = self._make_headers(updates)
        body = json.dumps(updates, ensure_ascii=False)

        response = self.session.put(url, data=body, headers=headers)
        response.raise_for_status()
        return response.json()

    def delete(self, data_id: str) -> Dict[str, Any]:
        """
        删除数据

        Args:
            data_id: 数据ID

        Returns:
            API响应结果
        """
        url = f"{self.base_url}/api/v1/sacp/data/delete"
        data = {'id': data_id}
        headers = self._make_headers(data)
        body = json.dumps(data, ensure_ascii=False)

        response = self.session.delete(url, data=body, headers=headers)
        response.raise_for_status()
        return response.json()


# 使用示例
if __name__ == "__main__":
    # 初始化客户端
    client = SACPClient(
        base_url="https://your-api.com",
        api_key="your-api-key",
        api_secret="your-api-secret"
    )

    # 创建一个任务
    task_data = {
        "type": "task",
        "title": "完成SACP协议文档",
        "create_time": "2026-02-20 14:30:00",
        "update_time": "2026-02-20 14:30:00",
        "creator": "jorneyruan",
        "source": "ClawSync",
        "description": "撰写SACP V1.0规范并发布到GitHub",
        "priority": "高",
        "status": "todo",
        "progress": 0
    }

    # 写入数据
    result = client.write(task_data)
    print(f"写入结果: {result}")

    # 查询列表
    list_result = client.list(data_type="task", page=1, page_size=10)
    print(f"查询结果: {list_result}")
