import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("merged_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

def ghi_color(ghi_value):
    if ghi_value < 2:
        return "navy"
    elif ghi_value < 4:
        return "deepskyblue"
    elif ghi_value < 6:
        return "orange"
    else:
        return "saddlebrown"

def budget_pr_for_date(date):
    if date.month >= 7:
        plant_year = date.year - 2019
    else:
        plant_year = date.year - 1 - 2019
    
    budget = 73.9 - (plant_year * 0.8)
    return budget

df["Color"] = df["GHI"].apply(ghi_color)
df["PR_30d_MA"] = df["PR"].rolling(window=30, min_periods=1).mean()
df["Budget_PR"] = df["Date"].apply(budget_pr_for_date)

plt.figure(figsize=(14, 7))
plt.scatter(df["Date"], df["PR"], c=df["Color"], s=20)
plt.plot(df["Date"], df["PR_30d_MA"], color="red", linewidth=2, label="30-d moving average")
plt.plot(df["Date"], df["Budget_PR"], color="darkgreen", linewidth=2, label="Budget PR")

# NEW: Add text box
windows = [7, 30, 60, 90, 365]
text_lines = ["Average PR:"]
for w in windows:
    avg = df["PR"].tail(w).mean()
    text_lines.append(f"Last {w}d: {avg:.1f}")

summary_text = "\n".join(text_lines)
plt.text(0.98, 0.05, summary_text, transform=plt.gca().transAxes,
         fontsize=9, verticalalignment="bottom", horizontalalignment="right",
         bbox=dict(boxstyle="round", facecolor="white", edgecolor="gray"))

plt.xlabel("Date")
plt.ylabel("PR (%)")
plt.title("Performance Ratio Evolution")
plt.legend()
plt.savefig("pr_graph.png")
print("Saved pr_graph.png")