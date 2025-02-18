import yfinance as yf
import matplotlib.pyplot as plt


aud_inr = yf.download("AUDINR=X", start="2006-01-01", end="2024-05-11")


aud_inr['Rolling_Std'] = aud_inr['Close'].rolling(window=30).std()

# Define a threshold for identifying a crisis
crisis_threshold = 0.05  # Adjust as needed

# Mark the crisis points where the rolling standard deviation exceeds the threshold
crisis_points = aud_inr[aud_inr['Rolling_Std'] > crisis_threshold]

# Find the dates of maximum and minimum exchange rates
max_rate_date = aud_inr['Close'].idxmax()
min_rate_date = aud_inr['Close'].idxmin()

# Plot AUD/INR trend
plt.figure(figsize=(12, 6))
plt.plot(aud_inr.index, aud_inr['Close'], label='AUD/INR')

# Mark crisis points on the plot
plt.scatter(crisis_points.index, crisis_points['Close'], color='red', label='Currency Crisis')

# Plot crisis threshold line
plt.axhline(y=crisis_threshold, color='red', linestyle='--', label='Crisis Threshold')

# Annotate maximum and minimum rate dates
plt.annotate(f'Max Rate: {max_rate_date.date()}', xy=(max_rate_date, aud_inr['Close'].max()), xytext=(-50, 50), textcoords='offset points',
             arrowprops=dict(arrowstyle="->", color='blue'))
plt.annotate(f'Min Rate: {min_rate_date.date()}', xy=(min_rate_date, aud_inr['Close'].min()), xytext=(-50, -50), textcoords='offset points',
             arrowprops=dict(arrowstyle="->", color='green'))

plt.title('AUD/INR Exchange Rate (2006-2024)')
plt.xlabel('Date')
plt.ylabel('Exchange Rate')
plt.legend()
plt.grid(True)
plt.show()

print(f"Date of maximum exchange rate: {max_rate_date.date()}")
print(f"Date of minimum exchange rate: {min_rate_date.date()}")
