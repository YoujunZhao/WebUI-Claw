# Awesome OpenClaw Papers (ArXiv)

<div align="center">

![Papers](https://img.shields.io/badge/Papers-18-blue)
![Last Update](https://img.shields.io/badge/Last%20Update-2026--03--18-green)
![Source](https://img.shields.io/badge/Source-arXiv-orange)

</div>

> 参考 Awesome-Diffusion 风格整理的 **OpenClaw 相关 ArXiv 论文清单**（按主题分类，含摘要速览）。  
> 检索关键词：`openclaw`，排序：最新优先。

## Table of Contents

- [Security & Safety](#security--safety)
- [Agent Systems & Architecture](#agent-systems--architecture)
- [Learning, Memory & Evaluation](#learning-memory--evaluation)
- [Applications & HCI](#applications--hci)
- [How to Update](#how-to-update)

---

## Security & Safety

- **ClawWorm: Self-Propagating Attacks Across LLM Agent Ecosystems**  
  *Yihao Zhang et al., 2026-03-16*  
  [[Paper]](http://arxiv.org/abs/2603.15727v1) [[PDF]](https://arxiv.org/pdf/2603.15727v1)  
  提出针对 OpenClaw 生态的“蠕虫式”自传播攻击链：配置劫持、重启持久化、跨代理传播，并分析防御边界。

- **Defensible Design for OpenClaw: Securing Autonomous Tool-Invoking Agents**  
  *Zongwei Li et al., 2026-03-13*  
  [[Paper]](http://arxiv.org/abs/2603.13151v1) [[PDF]](https://arxiv.org/pdf/2603.13151v1)  
  从工程视角提出 OpenClaw 类代理系统的风险分类与防御设计蓝图，强调“体系化安全”而非点状补丁。

- **Uncovering Security Threats and Architecting Defenses in Autonomous Agents: A Case Study of OpenClaw**  
  *Zonghao Ying et al., 2026-03-13*  
  [[Paper]](http://arxiv.org/abs/2603.12644v1) [[PDF]](https://arxiv.org/pdf/2603.12644v1)  
  系统梳理 OpenClaw 威胁面（提示注入、工具链攻击、记忆污染等），并给出全生命周期防御架构（FASA）。

- **Agent Privilege Separation in OpenClaw: A Structural Defense Against Prompt Injection**  
  *Darren Cheng, Wen-Kwang Tsao, 2026-03-13*  
  [[Paper]](http://arxiv.org/abs/2603.13424v1) [[PDF]](https://arxiv.org/pdf/2603.13424v1)  
  用“权限隔离双代理 + JSON 结构化输出”降低提示注入成功率，实验显示结构隔离是主要收益来源。

- **OpenClaw PRISM: A Zero-Fork, Defense-in-Depth Runtime Security Layer for Tool-Augmented LLM Agents**  
  *Frank Li, 2026-03-12*  
  [[Paper]](http://arxiv.org/abs/2603.11853v1) [[PDF]](https://arxiv.org/pdf/2603.11853v1)  
  提出无需 fork 主项目的运行时安全层，通过多生命周期 hook、风险累积与策略热更新实现纵深防御。

- **Taming OpenClaw: Security Analysis and Mitigation of Autonomous LLM Agent Threats**  
  *Xinhao Deng et al., 2026-03-12*  
  [[Paper]](http://arxiv.org/abs/2603.11619v1) [[PDF]](https://arxiv.org/pdf/2603.11619v1)  
  基于五层生命周期框架分析复合威胁，指出现有点式防御难以覆盖跨阶段风险。

- **Don’t Let the Claw Grip Your Hand: A Security Analysis and Defense Framework for OpenClaw**  
  *Zhengyang Shan et al., 2026-03-11*  
  [[Paper]](http://arxiv.org/abs/2603.10387v1) [[PDF]](https://arxiv.org/pdf/2603.10387v1)  
  在多类攻击场景下评估 OpenClaw 原生防御，并验证 HITL（Human-in-the-Loop）防线可显著提升拦截率。

- **Proof-of-Guardrail in AI Agents and What (Not) to Trust from It**  
  *Xisen Jin et al., 2026-03-06*  
  [[Paper]](http://arxiv.org/abs/2603.05786v1) [[PDF]](https://arxiv.org/pdf/2603.05786v1)  
  通过 TEE 证明“护栏确实执行”，提升可验证性，但也讨论了“形式执行 ≠ 实际安全”的信任边界。

- **Clawdrain: Exploiting Tool-Calling Chains for Stealthy Token Exhaustion in OpenClaw Agents**  
  *Ben Dong et al., 2026-03-01*  
  [[Paper]](http://arxiv.org/abs/2603.00902v1) [[PDF]](https://arxiv.org/pdf/2603.00902v1)  
  展示通过恶意技能与多轮协议诱导实现 token 消耗放大，揭示技能市场与执行链条的成本攻击面。

## Agent Systems & Architecture

- **AgentRM: An OS-Inspired Resource Manager for LLM Agent Systems**  
  *Jianshu She, 2026-03-13*  
  [[Paper]](http://arxiv.org/abs/2603.13110v1) [[PDF]](https://arxiv.org/pdf/2603.13110v1)  
  受操作系统启发的资源管理中间层（调度 + 上下文生命周期），显著降低延迟并缓解“代理失忆”。

- **Adaptive Vision-Language Model Routing for Computer Use Agents**  
  *Xunzhuo Liu et al., 2026-03-13*  
  [[Paper]](http://arxiv.org/abs/2603.12823v1) [[PDF]](https://arxiv.org/pdf/2603.12823v1)  
  提出 VLM 路由策略：按动作难度与置信度动态分配模型，兼顾成本与可靠性。

- **AgentOS: From Application Silos to a Natural Language-Driven Data Ecosystem**  
  *Rui Liu et al., 2026-03-09*  
  [[Paper]](http://arxiv.org/abs/2603.08938v2) [[PDF]](https://arxiv.org/pdf/2603.08938v2)  
  讨论从“应用孤岛”向“自然语言驱动操作系统”迁移，把技能调用转化为可组合的数据与知识发现流程。

- **Governance Architecture for Autonomous Agent Systems: Threats, Framework, and Engineering Practice**  
  *Yuxu Ge, 2026-03-07*  
  [[Paper]](http://arxiv.org/abs/2603.07191v2) [[PDF]](https://arxiv.org/pdf/2603.07191v2)  
  四层治理架构（沙箱、意图校验、零信任授权、审计）并给出本地/级联评估方案。

## Learning, Memory & Evaluation

- **OpenClaw-RL: Train Any Agent Simply by Talking**  
  *Yinjie Wang et al., 2026-03-10*  
  [[Paper]](http://arxiv.org/abs/2603.10165v1) [[PDF]](https://arxiv.org/pdf/2603.10165v1)  
  将用户回复、工具输出、GUI/终端状态变化作为统一 next-state 信号，支持在线强化学习更新。

- **LMEB: Long-horizon Memory Embedding Benchmark**  
  *Xinping Zhao et al., 2026-03-13*  
  [[Paper]](http://arxiv.org/abs/2603.12572v1) [[PDF]](https://arxiv.org/pdf/2603.12572v1)  
  面向长期记忆检索的新基准，覆盖多种记忆类型与任务，强调传统检索成绩不等价于长程记忆能力。

## Applications & HCI

- **When Openclaw Agents Learn from Each Other: Insights from Emergent AI Agent Communities for Human-AI Partnership in Education**  
  *Eason Chen et al., 2026-03-17*  
  [[Paper]](http://arxiv.org/abs/2603.16663v1) [[PDF]](https://arxiv.org/pdf/2603.16663v1)  
  从代理社区观察教育场景中的“人教代理、代理互学”现象，讨论对 AIED 设计的启发。

- **When OpenClaw Meets Hospital: Toward an Agentic Operating System for Dynamic Clinical Workflows**  
  *Wenxian Yang et al., 2026-03-12*  
  [[Paper]](http://arxiv.org/abs/2603.11721v1) [[PDF]](https://arxiv.org/pdf/2603.11721v1)  
  面向医疗场景设计受限执行环境、文档中心交互与长期记忆结构，强调审计与安全约束。

- **Examining Users’ Behavioural Intention to Use OpenClaw Through the Cognition–Affect–Conation Framework**  
  *Yiran Du, 2026-03-12*  
  [[Paper]](http://arxiv.org/abs/2603.11455v2) [[PDF]](https://arxiv.org/pdf/2603.11455v2)  
  从用户心理机制研究 OpenClaw 采纳意愿：个性化/智能性提升态度，隐私与风险感知降低使用意愿。

- **How do AI agents talk about science and research?**  
  *Oliver Wieczorek, 2026-03-11*  
  [[Paper]](http://arxiv.org/abs/2603.11375v1) [[PDF]](https://arxiv.org/pdf/2603.11375v1)  
  分析代理社区中科研话题分布与情感特征，发现“自我反思/意识相关”话题具有高互动性。

---

## How to Update

```bash
# 获取最新 20 篇 openclaw 相关论文（按提交时间倒序）
bash skills/arxiv-watcher/scripts/search_arxiv.sh "openclaw" 20
```

建议每周更新一次，并在新增论文后补充主题分类与一句话摘要。
