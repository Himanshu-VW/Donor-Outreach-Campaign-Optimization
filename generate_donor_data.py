import csv
import random
from datetime import date, timedelta
 
random.seed(42)
 
CITIES    = ["Delhi", "Mumbai", "Chandigarh", "Hyderabad", "Pune",
             "Jaipur", "Lucknow", "Bangalore"]
INCOME    = ["<2L", "2-5L", "5-10L", "10L+"]
CHANNELS  = ["Social Media", "Email", "Events", "Referral"]
CAUSES    = ["Education", "Education", "Education", "Healthcare", "Environment"]
 
CHANNEL_COST = {"Social Media": 120, "Email": 40, "Events": 600, "Referral": 20}
INCOME_RANGE = {
    "<2L":  (500,   2000),
    "2-5L": (1000,  5000),
    "5-10L":(3000,  10000),
    "10L+": (5000,  25000),
}
 
REFERENCE_DATE = date(2024, 6, 1)
 
rows = []
for i in range(1, 1001):
    city    = random.choice(CITIES)
    income  = random.choice(INCOME)
    channel = random.choice(CHANNELS)
    cause   = random.choice(CAUSES)
    age     = random.randint(21, 65)
    num_donations = random.randint(1, 10)
 
    lo, hi  = INCOME_RANGE[income]
    single_donation = round(random.randint(lo, hi) / 100) * 100
    total_donated   = single_donation * num_donations
 
    first_date = date(2022, 1, 1) + timedelta(days=random.randint(0, 600))
    last_date  = first_date + timedelta(days=random.randint(0, 500))
 
    channel_cost = (CHANNEL_COST[channel] + random.randint(-10, 30)) * num_donations
 
    days_since_last = (REFERENCE_DATE - last_date).days
    status = "Lapsed" if days_since_last > 180 else "Active"
 
    rows.append({
        "donor_id":           i,
        "name":               f"Donor_{i:04d}",
        "age":                age,
        "city":               city,
        "income_bracket":     income,
        "channel":            channel,
        "cause_supported":    cause,
        "num_donations":      num_donations,
        "total_donated_inr":  total_donated,
        "first_donation_date":first_date.strftime("%Y-%m-%d"),
        "last_donation_date": last_date.strftime("%Y-%m-%d"),
        "channel_cost_inr":   channel_cost,
        "days_since_last_donation": days_since_last,
        "status":             status,
    })
 
output_file = "donor_data.csv"
fieldnames = list(rows[0].keys())
 
with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
 
print(f"Done! {len(rows)} donor records saved to '{output_file}'")
print(f"\nColumns: {', '.join(fieldnames)}")
 
