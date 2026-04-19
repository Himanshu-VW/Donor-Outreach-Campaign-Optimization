<img width="1920" height="1080" alt="DonarDashboard" src="https://github.com/user-attachments/assets/202f6ff2-4f61-4621-9b46-a52a866841d5" />Donor Outreach & Campaign Optimization Dashboard
Excel-based donor analytics dashboard built to identify high-value segments, track churn, and compare campaign ROI across channels — mirroring the responsibilities of a crowdfunding intern at an education NGO.
Tools: Excel · Power Query · Pivot Tables
Dashboard
<img width="1920" height="1080" alt="DonarDashboard" src="https://github.com/user-attachments/assets/2d38bca0-223f-4d87-8d03-d6f7afebbe46" />


Dataset: 1,000 synthetic donor records · 15 columns

Dataset
Generated via generate_donor_data.py .

# outputs donor_data.csv
ColumnTypeDescriptiondonor_idIntegerUnique donor identifiernameTextAnonymised donor nameageIntegerAge range: 21–65cityTextDelhi, Mumbai, Bangalore, Hyderabad, Pune, Jaipur, Lucknow, Chandigarhincome_bracketText<2L / 2-5L / 5-10L / 10L+channelTextSocial Media / Email / Events / Referralcause_supportedTextEducation / Healthcare / Environmentnum_donationsIntegerNumber of donations madetotal_donated_inrIntegerTotal amount donated (₹)first_donation_dateDateDate of first donationlast_donation_dateDateDate of most recent donationchannel_cost_inrIntegerCampaign cost attributed to donor's channeldays_since_last_donationIntegerDays since last donation (ref: 1 Jun 2024)statusTextActive (≤180 days) / Lapsed (>180 days)donor_lifetime_daysIntegerDays between first and last donation


