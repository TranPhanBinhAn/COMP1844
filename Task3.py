import numpy as np

# Lấy danh sách toàn bộ distances trong graph Task 2
lengths = [G[u][v]['weight'] for u, v in G.edges()]

# Tổng chiều dài toàn mạng lưới
total_length = sum(lengths)

# Khoảng cách trung bình giữa các station
average_length = np.mean(lengths)

# Độ lệch chuẩn
std_dev = np.std(lengths)

# In kết quả
print("=== TASK 3 RESULTS ===")
print(f"Total network length: {total_length:.2f} km")
print(f"Average distance between stations: {average_length:.2f} km")
print(f"Standard deviation: {std_dev:.2f} km")
