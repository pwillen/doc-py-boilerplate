"""
https://pandas.pydata.org/docs/getting_started/index.html
"""
import pandas as pd


# Load data into a DataFrame

data = [
  {
    "device_id": "router-001",
    "datacenter": "US-East",
    "timestamp": "2026-11-09T08:00:00Z",
    "cpu_usage": 45.2,
    "memory_used": 62.5,
    "memory_total": 128,
    "network_in": 1250000,
    "network_out": 840000,
    "status": "online"
  },
  {
    "device_id": "router-001",
    "datacenter": "US-East",
    "timestamp": "2026-11-09T08:05:00Z",
    "cpu_usage": 52.8,
    "memory_used": 64.1,
    "memory_total": 128,
    "network_in": 1420000,
    "network_out": 920000,
    "status": "online"
  },
  {
    "device_id": "router-001",
    "datacenter": "US-East",
    "timestamp": "2026-11-09T08:10:00Z",
    "cpu_usage": 94.7,
    "memory_used": 110.2,
    "memory_total": 128,
    "network_in": 5800000,
    "network_out": 4200000,
    "status": "warning"
  },
  {
    "device_id": "router-001",
    "datacenter": "US-East",
    "timestamp": "2026-11-09T08:15:00Z",
    "cpu_usage": 91.3,
    "memory_used": 108.5,
    "memory_total": 128,
    "network_in": 5600000,
    "network_out": 3900000,
    "status": "warning"
  },
  {
    "device_id": "router-002",
    "datacenter": "US-West",
    "timestamp": "2026-11-09T08:00:00Z",
    "cpu_usage": 28.4,
    "memory_used": 32.1,
    "memory_total": 64,
    "network_in": 850000,
    "network_out": 620000,
    "status": "online"
  },
  {
    "device_id": "router-002",
    "datacenter": "US-West",
    "timestamp": "2026-11-09T08:05:00Z",
    "cpu_usage": 31.7,
    "memory_used": 33.4,
    "memory_total": 64,
    "network_in": 910000,
    "network_out": 680000,
    "status": "online"
  },
  {
    "device_id": "router-002",
    "datacenter": "US-West",
    "timestamp": "2026-11-09T08:10:00Z",
    "cpu_usage": 35.2,
    "memory_used": 35.0,
    "memory_total": 64,
    "network_in": 980000,
    "network_out": 710000,
    "status": "online"
  },
  {
    "device_id": "switch-003",
    "datacenter": "US-East",
    "timestamp": "2026-11-09T08:00:00Z",
    "cpu_usage": 72.5,
    "memory_used": 14.2,
    "memory_total": 32,
    "network_in": 2200000,
    "network_out": 1800000,
    "status": "online"
  },
  {
    "device_id": "switch-003",
    "datacenter": "US-East",
    "timestamp": "2026-11-09T08:05:00Z",
    "cpu_usage": null,
    "memory_used": 15.1,
    "memory_total": 32,
    "network_in": 2300000,
    "network_out": 1900000,
    "status": "online"
  },
  {
    "device_id": "switch-003",
    "datacenter": "US-East",
    "timestamp": "2026-11-09T08:10:00Z",
    "cpu_usage": 105.8,
    "memory_used": 31.5,
    "memory_total": 32,
    "network_in": 7500000,
    "network_out": 6200000,
    "status": "warning"
  },
  {
    "device_id": "firewall-004",
    "datacenter": "EU-West",
    "timestamp": "2026-11-09T08:00:00Z",
    "cpu_usage": 18.5,
    "memory_used": 22.4,
    "memory_total": 64,
    "network_in": 450000,
    "network_out": 380000,
    "status": "online"
  },
  {
    "device_id": "firewall-004",
    "datacenter": "EU-West",
    "timestamp": "2026-11-09T08:05:00Z",
    "cpu_usage": 21.2,
    "memory_used": 23.1,
    "memory_total": 64,
    "network_in": 480000,
    "network_out": 410000,
    "status": "online"
  },
  {
    "device_id": "firewall-004",
    "datacenter": "EU-West",
    "timestamp": "2026-11-09T08:10:00Z",
    "cpu_usage": 24.8,
    "memory_used": 24.0,
    "memory_total": 64,
    "network_in": 510000,
    "network_out": 440000,
    "status": "online"
  },
  {
    "device_id": "router-005",
    "datacenter": "US-West",
    "timestamp": "2026-11-09T08:00:00Z",
    "cpu_usage": 88.9,
    "memory_used": 59.2,
    "memory_total": 64,
    "network_in": 4100000,
    "network_out": 3500000,
    "status": "warning"
  },
  {
    "device_id": "router-005",
    "datacenter": "US-West",
    "timestamp": "2026-11-09T08:05:00Z",
    "cpu_usage": 92.1,
    "memory_used": 61.8,
    "memory_total": 64,
    "network_in": 4500000,
    "network_out": 3800000,
    "status": "warning"
  },
  {
    "device_id": "router-005",
    "datacenter": "US-West",
    "timestamp": "2026-11-09T08:10:00Z",
    "cpu_usage": 89.4,
    "memory_used": 60.5,
    "memory_total": 64,
    "network_in": 4300000,
    "network_out": 3600000,
    "status": "warning"
  },
  {
    "device_id": "router-005",
    "datacenter": "US-West",
    "timestamp": "2026-11-09T08:10:00Z",
    "cpu_usage": 89.4,
    "memory_used": 60.5,
    "memory_total": 64,
    "network_in": 4300000,
    "network_out": 3600000,
    "status": "warning"
  },
  {
    "device_id": "router-006",
    "datacenter": "AP-South",
    "timestamp": "2026-11-09T08:00:00Z",
    "cpu_usage": 42.1,
    "memory_used": 70.2,
    "memory_total": 128,
    "network_in": 1200000,
    "network_out": 950000,
    "status": "online"
  },
  {
    "device_id": "router-006",
    "datacenter": "AP-South",
    "timestamp": "2026-11-09T08:05:00Z",
    "cpu_usage": 46.3,
    "memory_used": 72.8,
    "memory_total": 128,
    "network_in": 1350000,
    "network_out": 1050000,
    "status": "online"
  },
  {
    "device_id": "router-006",
    "datacenter": "AP-South",
    "timestamp": "2026-11-09T08:10:00Z",
    "cpu_usage": 49.7,
    "memory_used": null,
    "memory_total": 128,
    "network_in": 1400000,
    "network_out": 1100000,
    "status": "online"
  },
  {
    "device_id": "router-007",
    "datacenter": "US-East",
    "timestamp": "2026-11-09T08:00:00Z",
    "cpu_usage": 67.2,
    "memory_used": 80.1,
    "memory_total": 128,
    "network_in": 1800000,
    "network_out": 1500000,
    "status": "online"
  },
  {
    "device_id": "router-007",
    "datacenter": "US-East",
    "timestamp": "2026-11-09T08:05:00Z",
    "cpu_usage": 73.8,
    "memory_used": 83.4,
    "memory_total": 128,
    "network_in": 2100000,
    "network_out": 1700000,
    "status": "online"
  },
  {
    "device_id": "router-007",
    "datacenter": "US-East",
    "timestamp": "2026-11-09T08:10:00Z",
    "cpu_usage": 79.5,
    "memory_used": 87.2,
    "memory_total": 128,
    "network_in": 2400000,
    "network_out": 1900000,
    "status": "online"
  }
]


df = pd.DataFrame(data)

# There is also pd.json_normalize() for nested JSON data
print(df)

# ======================================================================================================================
# Basic inspection
df.head()
df.tail()
df.sample(5)

# Dimensions and structure
df.shape
df.columns
df.dtypes
df.info()

# Statistical summary
df.describe()
df.describe(include="all")

# Unique values
df["status"].unique()
df["status"].value_counts()

# Missing values
df.isna().sum()
df.isna().mean() * 100

# Duplicate records
df.duplicated().sum()

# ======================================================================================================================
# Cleaning data
# Work on a copy
df = df.copy()

# Normalize column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows missing critical values
df = df.dropna(subset=["device_id"])

# Fill missing values
df["cpu_usage"] = df["cpu_usage"].fillna(0)

# Convert data types
df["cpu_usage"] = pd.to_numeric(
    df["cpu_usage"], errors="coerce"
)

# Convert timestamps
df["timestamp"] = pd.to_datetime(
    df["timestamp"], errors="coerce", utc=True
)

# Strip whitespace from strings
df["status"] = df["status"].str.strip()

# Replace values
df["status"] = df["status"].replace({
    "up": "online",
    "down": "offline"
})
# ======================================================================================================================
# Filtering
# Select columns
df[["device_id", "cpu_usage", "status"]]

# Filter rows
df[df["cpu_usage"] > 80]

# Multiple conditions
df[
    (df["cpu_usage"] > 80) &
    (df["status"] == "online")
]

# OR conditions
df[
    (df["datacenter"] == "US-East") |
    (df["datacenter"] == "US-West")
]

# Using isin
df[df["status"].isin(["online", "warning"])]

# Query syntax
df.query("cpu_usage > 80")

# Sort
df.sort_values("cpu_usage", ascending=False)

# Top N
df.nlargest(10, "cpu_usage")
# ======================================================================================================================
# Exporting Results
# CSV
df.to_csv("results.csv", index=False)

# JSON
df.to_json("results.json", orient="records")

# HTML
df.to_html("results.html", index=False)

# Dictionary
records = df.to_dict(orient="records")