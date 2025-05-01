import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

my_df = { 
    "day" : ["sun", "mon", "tue", "wed", "thu", "fri", "sat"],
    "temp (celcius)" : [30,32,35,33,31,30,29],
    "rainfall (mm)" : [5, 0, 10, 2, 0, 1, 3]
}
df = pd.DataFrame(my_df)
print(df)
x = df["day"]
y1 = df["temp (celcius)"]
y2 = df["rainfall (mm)"]

plt.plot(x, y1, label="Temperature (°C)")
plt.plot(x, y2, label="Rainfall (mm)")
plt.legend()
plt.title("Weather Data")
plt.xlabel("Days")
plt.ylabel("Values")
plt.grid()
plt.show()
print("------")

data = [10, 20, 30, 40, 50]

plt.plot(data, marker='o', linestyle='-', color='b')
plt.grid()
plt.show()
print("------")

my_df = {
    "day" : ["sun", "mon", "tue", "wed", "thu", "fri", "sat"],
    "teamperature (celcius)" : [30,32,35,33,31,30,29],
    "rainfall (mm)" : [5, 0, 10, 2, 0, 1, 3]
}
df = pd.DataFrame(my_df)
x = df["day"]
y1 = df["teamperature (celcius)"]
y2 = df["rainfall (mm)"]
plt.plot(x,y1, label="Temperature (C)", color="red", marker = "o", linestyle = "-",
         linewidth=1, markersize=5,markeredgecolor="black", markerfacecolor="white")
plt.plot(x,y2, label="Rainfall (mm)", color="blue", marker = "o", linestyle = "-",
         linewidth=1, markersize=5,markeredgecolor="black", markerfacecolor="white")
plt.legend()
plt.title("Weather Data")
plt.xlabel("Days")
plt.ylabel("Values")
plt.grid()
plt.show()
print("------")

x = [1,2,3]
y = [1,4,9]
plt.figure(figsize=(10, 6), dpi=100)
plt.plot(x, y)
plt.show()
print("------")

my_df = { 
    "day" : ["sun", "mon", "tue", "wed", "thu", "fri", "sat"],
    "temp1 (celcius)" : [30,32,35,33,31,30,29],
    "temp2 (celcius)" : [34,36,39,37,35,34,33],
    "temp3 (celcius)" : [38,40,43,41,39,38,37]
}

df = pd.DataFrame(my_df)
x = df["day"]
y1 = df["temp1 (celcius)"]
y2 = df["temp2 (celcius)"]
y3 = df["temp3 (celcius)"]
fig, ax = plt.subplots(nrows=3, ncols=1, 
                       figsize=(10,15), dpi=90)

ax[0].plot(x, y1, color="red", marker="o", linestyle="-")
ax[0].set_title("Temperature 1")
ax[1].plot(x, y2, color="blue", marker="o", linestyle="-")
ax[1].set_title("Temperature 2")
ax[2].plot(x, y3, color="green", marker="o", linestyle="-")
ax[2].set_title("Temperature 3")
plt.suptitle("Weather Data")
fig.tight_layout()

#ปรับระยะห่างของ subplot
plt.subplots_adjust(top=0.9)
plt.subplots_adjust(hspace=0.5)
plt.show()
print("------")
#legend : กำหนดคำอธิบายกราฟ

my_df = {"day" : ["sun", "mon", "tue", "wed", "thu", "fri", "sat"],
         "temp_week1" : [30,32,34,33,31,30,29],
         "temp_week2" : [34,36,38,37,35,34,33],
         "temp_week3" : [38,40,42,41,39,38,37],
         "temp_week4" : [42,44,46,45,43,42,41]}

df = pd.DataFrame(my_df)
x = df["day"]
y1 = df["temp_week1"]
y2 = df["temp_week2"]
y3 = df["temp_week3"]
y4 = df["temp_week4"]

fig, ax = plt.subplots(nrows=2, ncols=2,
                       figsize=(10,10), sharey=True, dpi=90)

ax[0,0].plot(x,y1, label = "Temperature" ,color="red", marker="o", linestyle="-")
ax[0,0].set_title("Temperature Week 1")
ax[0,0].legend(loc=2)

ax[0,1].plot(x,y2, label = "Temperature", color="blue", marker="o", linestyle="-")
ax[0,1].set_title("Temperature Week 2")
ax[0,1].legend(loc="lower left")

ax[1,0].plot(x,y3, label = "Temperature", color="green", marker="o", linestyle="-")
ax[1,0].set_title("Temperature Week 3")
ax[1,0].legend(loc=10)

ax[1,1].plot(x,y4, label = "Temperature", color="purple", marker="o", linestyle="-")
ax[1,1].set_title("Temperature Week 4")
ax[1,1].legend(loc="best")

plt.suptitle("Weather Data")

fig.tight_layout()
plt.show()
print("------")

#การสร้าง Bar charts

df = {"month" : ["jan", "feb", "mar", "apr", "may"],
      "sales" : [100, 200, 300, 400, 500]}
my_df = pd.DataFrame(df)
x = df["month"]
y = df["sales"]
plt.bar(x,y, align="edge", alpha=0.4)
plt.title("Sales Quarter1 2023")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
print("------")

#การสร้าง Horizontal bar charts
my_df = {"social_media" : ["facebook", "twitter", "instagram", "tiktok"],
         "%used" : [30, 20, 25, 25]}
df = pd.DataFrame(my_df)
plt.figure(figsize=(10, 6), dpi=100)
plt.barh(df["social_media"], df["%used"], align="center")
plt.xticks(np.arange(0,100,10))
plt.ylabel("social media")
plt.xlabel("used")
plt.title("Summary %used of social media platforms")
plt.show()
#การสร้าง Line graphs
print("------")
my_df = {"Quarter" : ["Q1", "Q2", "Q3", "Q4"],
         "SalesOfprod1" : [60000, 80000, 125000, 78500],
         "SalesOfprod2" : [93650, 353500, 47550, 38550]
         }
df = pd.DataFrame(my_df)
plt.figure(figsize=[10, 8])
plt.grid()
plt.plot(df["Quarter"], df["SalesOfprod1"], marker="s", ls="--",
         lw=3, ms=10, mec="blue", mfc="cyan", label="product1")
plt.plot(df["Quarter"], df["SalesOfprod2"], color="red", marker="*",
         ls="--", lw=3, ms=15, mec="#E8CCD7", label="product2")
plt.xticks(rotation=45)
plt.yticks(np.arange(30000,130000,5000))
plt.legend(loc="lower left")
plt.xlabel("Quarter")
plt.ylabel("Sales")
plt.title("Sales per quarter")
plt.show()

