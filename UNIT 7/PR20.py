#Practical 20
#Create various types of plots using Matplotlib: line plot, bar chart,histogram, pie chart, scatter plot using subplots and figure properties.



import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [20, 35, 30, 45, 50]


plt.figure(figsize=(10, 8))


plt.subplot(2, 3, 1)
plt.plot(months, sales)
plt.title("Line Plot")
plt.xlabel("Month")
plt.ylabel("Sales")



plt.subplot(2, 3, 2)
plt.bar(months, sales)
plt.title("Bar Chart")
plt.xlabel("Month")
plt.ylabel("Sales")



plt.subplot(2, 3, 3)
plt.hist(sales)
plt.title("Histogram")
plt.xlabel("Sales")
plt.ylabel("Frequency")



plt.subplot(2, 3, 4)
plt.pie(sales, labels=months, autopct="%1.1f%%")
plt.title("Pie Chart")



plt.subplot(2, 3, 5)
plt.scatter(months, sales)
plt.title("Scatter Plot")
plt.xlabel("Month")
plt.ylabel("Sales")


plt.tight_layout()
plt.show()
