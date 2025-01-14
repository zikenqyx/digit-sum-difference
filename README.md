# 数字和差异计算器 (Digit Sum Difference Calculator)

一个高性能的Python应用程序，专门用于在大规模随机数据集中进行数字特征分析。本程序采用并行计算技术，能够高效处理百万级数据量。

[English](README_EN.md) | 简体中文

## 🌟 主要特点

- 🚀 高性能：每秒处理超过50万个数字
- 💻 多核优化：自动适配CPU核心数量，充分利用硬件性能
- 🎯 精确计算：查找所有数位之和等于30的数字
- 📊 实时统计：提供详细的性能指标和运行时间分析
- 🛡️ 异常处理：完善的错误处理和报告机制

## 🔧 系统要求

- Python 3.6+
- 支持所有主流操作系统：
  - Windows
  - Linux
  - MacOS

## 📦 安装方法

1. 克隆仓库：
```bash
git clone https://github.com/ziken/digit-sum-difference.git
cd digit-sum-difference
```

2. 创建虚拟环境：
```bash
python -m venv venv
```

3. 激活虚拟环境：

Windows PowerShell:
```powershell
.\venv\Scripts\Activate.ps1
```

Windows CMD:
```cmd
.\venv\Scripts\activate.bat
```

Linux/MacOS:
```bash
source venv/bin/activate
```

## 🚀 使用方法

直接运行主程序：
```bash
python digit_sum_difference.py
```

### 输出示例

```
各位数字之和为30的最大数和最小数之差为: 95931
找到的符合条件的数字个数: 32801

运行时间统计:
生成随机数耗时: 0.3416 秒
查找目标数字耗时: 0.4881 秒
计算最大最小值之差耗时: 0.0004 秒
总运行时间: 0.8421 秒

性能分析:
每秒处理数字数量: 1,187,469 个/秒
CPU核心数量: 16 个
```

## 💡 技术实现

- ⚡ 性能优化
  - 使用位运算和查找表优化数字计算
  - 多进程并行处理提升计算速度
  - 内存使用优化，减少资源占用
  
- 🛠️ 核心功能
  - 生成100万个1到100,000之间的随机数
  - 并行查找数位之和为30的数字
  - 计算符合条件数字的最大值与最小值之差

## 📈 性能指标

| 指标 | 数值 |
|------|------|
| 数据处理速度 | ~500,000 数字/秒 |
| 内存占用 | 低至 100MB |
| CPU利用率 | 85%+ |
| 并行效率 | 接近线性扩展 |

## 🤝 贡献指南

欢迎提交问题和改进建议！如果您想贡献代码：

1. Fork 本仓库
2. 创建您的特性分支：`git checkout -b feature/AmazingFeature`
3. 提交您的更改：`git commit -m '添加了一些很棒的特性'`
4. 推送到分支：`git push origin feature/AmazingFeature`
5. 开启一个 Pull Request

## 📄 开源协议

本项目采用 MIT 协议开源 - 查看 [LICENSE](LICENSE) 文件了解更多细节

## 👨‍💻 作者

ziken - [GitHub](https://github.com/ziken)

## 🙏 致谢

感谢所有为这个项目做出贡献的开发者！
