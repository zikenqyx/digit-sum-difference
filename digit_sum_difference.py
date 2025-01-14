import random
import time
from concurrent.futures import ProcessPoolExecutor
import multiprocessing
from itertools import chain

def digit_sum(n):
    # 使用位运算和查找表优化性能
    lookup = (0,1,2,3,4,5,6,7,8,9)
    total = 0
    while n:
        total += lookup[n % 10]  # 使用查找表代替直接计算
        n //= 10
    return total

def process_chunk(numbers):
    try:
        # 预先计算目标和，避免重复比较
        target_sum = 30
        # 使用局部变量优化访问速度
        digit_sum_func = digit_sum
        return [n for n in numbers if digit_sum_func(n) == target_sum]
    except Exception as e:
        print(f"处理数据块时出错: {e}")
        return []

def find_digit_sum_difference():
    try:
        # 使用局部变量优化访问速度
        randint = random.randint
        start_gen = time.perf_counter()
        numbers = [randint(1, 100000) for _ in range(1_000_000)]
        gen_time = time.perf_counter() - start_gen
        
        start_find = time.perf_counter()
        
        # 优化分块策略
        cpu_count = max(1, multiprocessing.cpu_count())
        chunk_size = max(10000, len(numbers) // (cpu_count * 2))
        chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]
        
        with ProcessPoolExecutor(max_workers=cpu_count) as executor:
            try:
                # 使用chain优化内存使用
                target_numbers = list(chain.from_iterable(executor.map(process_chunk, chunks)))
            except Exception as e:
                print(f"并行处理时出错: {e}")
                return 0, gen_time, 0, 0, 0
        
        find_time = time.perf_counter() - start_find
        
        if not target_numbers:
            print("警告：未找到符合条件的数字")
            return 0, gen_time, find_time, 0, 0
        
        start_calc = time.perf_counter()
        result = max(target_numbers) - min(target_numbers)
        calc_time = time.perf_counter() - start_calc
        
        return result, gen_time, find_time, calc_time, len(target_numbers)
    
    except Exception as e:
        print(f"程序执行出错: {e}")
        return 0, 0, 0, 0, 0

if __name__ == "__main__":
    random.seed(42)
    
    total_start = time.perf_counter()
    result, gen_time, find_time, calc_time, count = find_digit_sum_difference()
    total_time = time.perf_counter() - total_start
    
    print(f"各位数字之和为30的最大数和最小数之差为: {result}")
    print(f"找到的符合条件的数字个数: {count}")
    print("\n运行时间统计:")
    print(f"生成随机数耗时: {gen_time:.4f} 秒")
    print(f"查找目标数字耗时: {find_time:.4f} 秒")
    print(f"计算最大最小值之差耗时: {calc_time:.4f} 秒")
    print(f"总运行时间: {total_time:.4f} 秒")
    
    print("\n性能分析:")
    print(f"每秒处理数字数量: {1_000_000/total_time:.0f} 个/秒")
    print(f"CPU核心数量: {multiprocessing.cpu_count()} 个")