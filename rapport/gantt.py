import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Define the tasks with their start and end dates
tasks = [
    {"Task": "Literature review and technology research", "Start": "2024-05-13", "End": "2024-05-26"},
    #{"Task": "Technology Research", "Start": "2024-05-13", "End": "2024-05-26"},
    #{"Task": "Component selection and initial schematics", "Start": "2024-05-13", "End": "2024-05-26"},
    {"Task": "Component selection and initial schematics", "Start": "2024-05-27", "End": "2024-06-09"},
    #{"Task": "System Architecture Planning", "Start": "2024-05-27", "End": "2024-06-09"},
    {"Task": "Circuit design and initial prototyping", "Start": "2024-06-10", "End": "2024-06-23"},
    #{"Task": "Initial Prototyping", "Start": "2024-05-27", "End": "2024-06-09"},
    #{"Task": "Preliminary Enclosure Design", "Start": "2024-05-27", "End": "2024-06-09"},
    {"Task": "Prototype testing and adjust design", "Start": "2024-06-10", "End": "2024-06-23"},
    #{"Task": "Adjust Design", "Start": "2024-06-10", "End": "2024-06-23"},
    #{"Task": "Prototype Development", "Start": "2024-06-10", "End": "2024-06-23"},
    #{"Task": "Firmware coding", "Start": "2024-06-24", "End": "2024-07-07"},
    #{"Task": "Data Acquisition Implementation", "Start": "2024-06-24", "End": "2024-07-07"},
    {"Task": "Wireless communication code", "Start": "2024-06-24", "End": "2024-06-30"},
    {"Task": "Firmware coding and initial firmware testing", "Start": "2024-07-01", "End": "2024-07-07"},
    #{"Task": "Mobile App Platform Selection", "Start": "2024-07-08", "End": "2024-07-21"},
    {"Task": "UI/UX Design and backend infrastructure development", "Start": "2024-07-08", "End": "2024-07-21"},
    #{"Task": "Backend infrastructure development", "Start": "2024-07-08", "End": "2024-07-21"},
    {"Task": "Initial app coding", "Start": "2024-07-08", "End": "2024-07-21"},
    {"Task": "Firmware and mobile app integration", "Start": "2024-07-22", "End": "2024-08-04"},
    #{"Task": "Connectivity Testing", "Start": "2024-07-22", "End": "2024-08-04"},
    {"Task": "Power consumption optimization and system integration testing", "Start": "2024-07-22", "End": "2024-08-04"},
    #{"Task": "System Integration Testing", "Start": "2024-07-22", "End": "2024-08-04"},
    {"Task": "Field testing and performance analysis", "Start": "2024-08-05", "End": "2024-08-11"},
    #{"Task": "Performance Analysis", "Start": "2024-08-05", "End": "2024-08-18"},
    {"Task": "Stress testing and reliability assessment", "Start": "2024-08-12", "End": "2024-08-18"},
    #{"Task": "Reliability Assessment", "Start": "2024-08-05", "End": "2024-08-18"},
    {"Task": "Gather feedback and refine system components", "Start": "2024-08-19", "End": "2024-09-06"},
    #{"Task": "Refine System Components", "Start": "2024-08-19", "End": "2024-09-06"},
    {"Task": "Write final report, prepare presentation and complete documentation", "Start": "2024-08-19", "End": "2024-09-06"},
    #{"Task": "Prepare Presentation", "Start": "2024-08-19", "End": "2024-09-06"},
    #{"Task": "Complete Documentation", "Start": "2024-08-19", "End": "2024-09-06"},
]

# Create a DataFrame
df = pd.DataFrame(tasks)

# Convert date columns to datetime
df["Start"] = pd.to_datetime(df["Start"])
df["End"] = pd.to_datetime(df["End"])

# Plot Gantt chart
fig, ax = plt.subplots(figsize=(10, 8))

# Iterate through the tasks and plot them
for i, task in df.iterrows():
    ax.barh(task["Task"], (task["End"] - task["Start"]).days, left=task["Start"], align='center')

# Set the date format on the x-axis
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))

# Set labels and title
plt.xlabel("Date")
plt.ylabel("Tasks")
plt.title("Gantt diagram for CH4 monitoring IoT device")
plt.grid(True)

# Rotate date labels for better readability
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()

