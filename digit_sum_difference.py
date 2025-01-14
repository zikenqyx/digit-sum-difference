import random
import time
from concurrent.futures import ProcessPoolExecutor
import multiprocessing

def digit_sum(n):
    """计算数字各位之和（优化版本）"""
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def process_chunk(numbers):
    """处理数字块，返回符合条件的数字"""
    return [n for n in numbers if digit_sum(n) == 30]

def find_digit_sum_difference():
    # 记录生成随机数的时间
    start_gen = time.perf_counter()
    numbers = [random.randint(1, 100000) for _ in range(1_000_000)]
    gen_time = time.perf_counter() - start_gen
    
    # 记录查找目标数字的时间
    start_find = time.perf_counter()
    
    # 使用多进程并行处理
    chunk_size = len(numbers) // multiprocessing.cpu_count()
    chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]
    
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(process_chunk, chunks))
    
    # 合并所有结果
    target_numbers = [num for chunk in results for num in chunk]
    find_time = time.perf_counter() - start_find
    
    if not target_numbers:
        return 0, gen_time, find_time, 0, len(target_numbers)
    
    # 记录计算最大最小值差的时间
    start_calc = time.perf_counter()
    result = max(target_numbers) - min(target_numbers)
    calc_time = time.perf_counter() - start_calc
    
    return result, gen_time, find_time, calc_time, len(target_numbers)

if __name__ == "__main__":
    # 设置随机种子以确保结果可重现
    random.seed(42)
    
    # 记录总运行时间
    total_start = time.perf_counter()
    result, gen_time, find_time, calc_time, count = find_digit_sum_difference()
    total_time = time.perf_counter() - total_start
    
    # 打印详细的时间统计
    print(f"各位数字之和为30的最大数和最小数之差为: {result}")
    print(f"找到的符合条件的数字个数: {count}")
    print("\n运行时间统计:")
    print(f"生成随机数耗时: {gen_time:.4f} 秒")
    print(f"查找目标数字耗时: {find_time:.4f} 秒")
    print(f"计算最大最小值之差耗时: {calc_time:.4f} 秒")
    print(f"总运行时间: {total_time:.4f} 秒")
    
    # 输出性能分析
    print("\n性能分析:")
    print(f"每秒处理数字数量: {1_000_000/total_time:.0f} 个/秒")
    print(f"CPU核心数量: {multiprocessing.cpu_count()} 个") 