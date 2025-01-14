# 数字和差异计算器 (Digit Sum Difference Calculator)

这是一个高性能的Python应用程序，用于在大量随机数中寻找特定数字和模式。该程序使用并行处理技术，能够高效地处理大规模数据。

## 功能特点

- 生成100万个随机数
- 查找所有数位之和等于30的数字
- 计算这些数字中最大值和最小值的差
- 使用多进程并行处理以提高性能
- 详细的性能统计和运行时间分析

## 系统要求

- Python 3.6+
- Windows/Linux/MacOS

## 安装方法

1. 克隆仓库：
```bash
git clone [repository-url]
cd digit-sum-difference
```

2. 创建虚拟环境：
```bash
python -m venv venv
```

3. 激活虚拟环境：
- Windows:
```bash
.\venv\Scripts\activate
```
- Linux/MacOS:
```bash
source venv/bin/activate
```

## 使用方法

直接运行主程序：
```bash
python digit_sum_difference.py
```

## 性能指标

- 每秒可处理约50万个数字
- 自动适配CPU核心数量
- 内存使用优化

## 技术特点

- 使用位运算和查找表优化性能
- 多进程并行处理
- 内存优化的数据处理
- 异常处理和错误报告

## 许可证

MIT License

## 作者

[Your Name]
