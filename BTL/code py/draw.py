import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV vào DataFrame
df = pd.read_csv('commits.csv', parse_dates=['Commited Date'])

# Tạo cột 'Month' từ cột 'Commited Date'
df['Month'] = df['Commited Date'].dt.to_period('M')

# Đếm số lượng commit, success và fail theo từng tháng
monthly_stats = df.groupby(['Month', 'Passed']).size().unstack().fillna(0)

# Thêm cột 'Total' là tổng số lượng commit (success + fail) mỗi tháng
monthly_stats['Total'] = monthly_stats['Success'] + monthly_stats['Fail']

# Vẽ biểu đồ
monthly_stats.plot(kind='bar', figsize=(12, 6))
plt.title('Monthly Commit Stats')
plt.xlabel('Month')
plt.ylabel('Count')
plt.legend(title='Status', loc='upper left')

plt.show()
