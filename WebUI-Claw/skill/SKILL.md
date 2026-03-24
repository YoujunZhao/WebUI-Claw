---
name: openclaw-webui-image
description: 通过 AUTOMATIC1111 WebUI API 进行手机端生图，支持“生成N张图”批量返回。
---

# openclaw-webui-image

当用户提到以下意图时触发：
- 生图、画图、生成图片、生成海报
- “生成10张图” “帮我画xx”

## Inputs
- prompt: 正向提示词（必填）
- negative_prompt: 反向提示词（可选）
- n: 图片数量，默认 1
- width / height: 分辨率，可选
- steps / cfg: 可选

## Behavior
1. 解析自然语言参数
2. 调用 `scripts/generate.py`
3. 把返回的图片逐张发回消息会话

## Execute

优先直接传用户原始文本，让脚本自动解析：

```bash
python3 scripts/parse_and_generate.py --text "{{user_text}}"
```

如果你的编排层已拆出参数，也可直接调用：

```bash
python3 scripts/generate.py \
  --prompt "{{prompt}}" \
  --negative "{{negative_prompt}}" \
  --n "{{n}}" \
  --width "{{width}}" \
  --height "{{height}}" \
  --steps "{{steps}}" \
  --cfg "{{cfg}}"
```

## Environment Variables
- `SD_WEBUI_URL` (default: `http://127.0.0.1:7860`)
- `SD_WEBUI_TIMEOUT` (default: `180`)

## Output
输出 JSON：
- `images`: base64 图片数组
- `meta`: 最终采用的参数
