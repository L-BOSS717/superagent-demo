# superagent-demo

dsh-superagent 的演示仓库：一个极简倒计时工具 + 一个故意留下的 bug，用来试跑工单。

## 用法

```bash
python countdown.py              # 默认从 60 秒开始倒计时
python countdown.py --seconds 10 # 从 10 秒开始倒计时
```

测试：

```bash
python -m pytest countdown_test.py
```
