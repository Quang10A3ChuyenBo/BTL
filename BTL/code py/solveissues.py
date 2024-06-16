import pandas as pd

# Đọc dữ liệu từ file CSV
df = pd.read_csv('issuesClose.csv')

# Chuyển đổi định dạng cột `Date Appear` và `Solve Date` sang datetime
df['Date Appear'] = pd.to_datetime(df['Date Appear'])
df['Solve Date'] = pd.to_datetime(df['Solve Date'])

# Tính toán thời gian giải quyết cho mỗi vấn đề (theo đơn vị giây)
df['Time to Solve'] = (df['Solve Date'] - df['Date Appear']).dt.total_seconds()

# Tính trung bình thời gian giải quyết
average_time_to_solve = df['Time to Solve'].mean()

# Chuyển đổi thời gian trung bình từ đơn vị giây sang đơn vị mong muốn (ví dụ: ngày)
average_time_to_solve_in_days = average_time_to_solve / 86400


# Group data by Type
grouped_by_type = df.groupby('Type')

# Create a figure for subplots
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Violin plot for each Type on axes[0, 0]
sns.violinplot(x='Type', y='Time to Solve', data=df, ax=axes[0, 0])
axes[0, 0].set_title('Mức dao động thời gian xử lý theo loại issue')
axes[0, 0].set_xlabel('Loại issue')
axes[0, 0].set_ylabel('Thời gian xử lý (giây)')
axes[0, 0].grid(True)

# Boxplot for each Type on axes[0, 1]
sns.boxplot(x='Type', y='Time to Solve', data=df, ax=axes[1, 0])
axes[1, 0].set_title('Mức dao động thời gian xử lý theo loại issue (Boxplot)')
axes[1, 0].set_xlabel('Loại issue')
axes[1, 0].set_ylabel('Thời gian xử lý (giây)')
axes[1, 0].grid(True)

# Line plot for average time to solve by Type on axes[1, 1]
df_average_time_to_solve = grouped_by_type['Time to Solve'].mean().reset_index()
sns.lineplot(x='Type', y='Time to Solve', data=df_average_time_to_solve, ax=axes[1, 1])
axes[1, 1].set_title('Thời gian xử lý trung bình theo loại issue')
axes[1, 1].set_xlabel('Loại issue')
axes[1, 1].set_ylabel('Thời gian xử lý trung bình (giây)')
axes[1, 1].grid(True)

# Adjust layout and show the figure
fig.suptitle('Phân tích thời gian xử lý issue theo loại')
plt.tight_layout()
plt.show()