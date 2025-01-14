# Digit Sum Difference Calculator

A high-performance Python application designed for numerical pattern analysis in large-scale random datasets. This program utilizes parallel computing technology to efficiently process millions of numbers.

English | [简体中文](README.md)

## 🌟 Key Features

- 🚀 High Performance: Processes over 500,000 numbers per second
- 💻 Multi-core Optimization: Automatically adapts to CPU core count
- 🎯 Precise Calculation: Finds numbers with digit sum equal to 30
- 📊 Real-time Statistics: Detailed performance metrics and runtime analysis
- 🛡️ Error Handling: Comprehensive error handling and reporting

## 🔧 System Requirements

- Python 3.6+
- Supports all major operating systems:
  - Windows
  - Linux
  - MacOS

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/ziken/digit-sum-difference.git
cd digit-sum-difference
```

2. Create virtual environment:
```bash
python -m venv venv
```

3. Activate virtual environment:

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

## 🚀 Usage

Run the main program:
```bash
python digit_sum_difference.py
```

### Sample Output

```
Difference between max and min numbers with digit sum 30: 95931
Number of matching numbers found: 32801

Runtime Statistics:
Random number generation time: 0.3416 seconds
Target number search time: 0.4881 seconds
Max-min difference calculation time: 0.0004 seconds
Total runtime: 0.8421 seconds

Performance Analysis:
Numbers processed per second: 1,187,469
CPU cores used: 16
```

## 💡 Technical Implementation

- ⚡ Performance Optimization
  - Bit operations and lookup tables for number calculations
  - Multi-process parallel processing
  - Memory usage optimization
  
- 🛠️ Core Features
  - Generates 1 million random numbers between 1 and 100,000
  - Parallel search for numbers with digit sum of 30
  - Calculates difference between max and min matching numbers

## 📈 Performance Metrics

| Metric | Value |
|--------|-------|
| Processing Speed | ~500,000 numbers/sec |
| Memory Usage | As low as 100MB |
| CPU Utilization | 85%+ |
| Parallel Efficiency | Near linear scaling |

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute:

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/AmazingFeature`
3. Commit your changes: `git commit -m 'Add some AmazingFeature'`
4. Push to the branch: `git push origin feature/AmazingFeature`
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## 👨‍💻 Author

ziken - [GitHub](https://github.com/ziken)

## 🙏 Acknowledgments

Thanks to all developers who have contributed to this project! 