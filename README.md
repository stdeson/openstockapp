# OpenStockApp

一键打开股票行情的 API 服务，供飞书多维表格按钮调用。

## 内网穿透流程

```
飞书多维表格 → ngrok公网地址 → ngrok → localhost:7002 → openstockapp
```

### 端口转发原理

1. **openstockapp** 运行在本地 7002 端口，提供 `/stock` API
2. **ngrok** 启动命令是 `ngrok http 7002`，意思是：
   - ngrok 会分配一个公网地址（如 `https://xxx.ngrok-free.dev`）
   - 所有访问这个公网地址的请求，都会被转发到本地的 **7002 端口**
3. 飞书多维表格按钮调用 ngrok 公网地址，请求最终到达本地 openstockapp 服务

## 使用

```bash
# 启动服务
make start

# 停止服务
make stop

# 重启服务
make restart

# 查看日志
make logs
```

## API

POST `/stock`

```json
{"name": "腾讯控股"}
```

## ngrok 公网地址

启动后访问 http://localhost:4040 查看当前 ngrok 分配的公网地址。
