# GitHub 发布与一键部署说明（详细版）

本文件用于指导你把仓库发布到 GitHub，并给用户提供“尽量一键”的部署体验。

## A. 发布到 GitHub

```bash
cd openclaw-webui-mobile-image
git init
git add .
git commit -m "feat: OpenClaw + WebUI mobile image bot scaffold"
git branch -M main
git remote add origin git@github.com:<你的用户名>/openclaw-webui-mobile-image.git
git push -u origin main
```

如果你用 HTTPS：

```bash
git remote add origin https://github.com/<你的用户名>/openclaw-webui-mobile-image.git
```

---

## B. 给用户的一键命令（放 README 顶部）

```bash
git clone https://github.com/<你的用户名>/openclaw-webui-mobile-image.git && \
cd openclaw-webui-mobile-image && \
cp .env.example .env && \
bash scripts/deploy.sh
```

---

## C. 用户首次接入 OpenClaw 的最短路径

1. 用户先把 OpenClaw 跑起来（消息通道可用）
2. 部署本仓库（得到 WebUI API）
3. 配置环境变量：
   - `SD_WEBUI_URL=http://127.0.0.1:7860`
4. 把 `skill/` 拷贝进 OpenClaw skills 目录
5. 在对话中测试：
   - `生成3张图：可爱柴犬，阳光草地，动漫风`

---

## D. 手机看图体验优化

为了让“手机直接收图”更稳：

- 默认每次最多 10 张（可在脚本中改成 20）
- 大图建议 768 或 1024 边长，避免单图过大导致平台上传失败
- 对 10 张以上任务：建议分批次发送（例如每批 4 张）

---

## E. 版本建议

- `v0.1.0`：txt2img + 批量发送
- `v0.2.0`：img2img + ControlNet
- `v0.3.0`：任务队列 + 进度回调 + 失败重试

---

## F. 安全建议

- 不要把 7860 暴露到公网（至少加鉴权）
- 反向代理层加 Basic Auth / Access Token
- 日志里避免长期保存敏感 prompt

---

## G. 你可以在 README 新增的 badge

```markdown
![Docker](https://img.shields.io/badge/Docker-ready-blue)
![OpenClaw](https://img.shields.io/badge/OpenClaw-integrated-success)
![License](https://img.shields.io/badge/license-MIT-green)
```
