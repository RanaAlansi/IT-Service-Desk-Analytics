import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# -----------------------
# Configuration
# -----------------------

num_records = 10000
start_date = datetime(2025, 1, 1)

tickets = []

# -----------------------
# Generate Data
# -----------------------

for i in range(1, num_records + 1):

    department = np.random.choice(
        ['IT', 'Operations', 'Finance', 'Sales', 'HR', 'Marketing'],
        p=[0.35, 0.20, 0.15, 0.12, 0.10, 0.08]
    )

    category = np.random.choice(
        ['Software', 'Network', 'Hardware', 'Access', 'Security'],
        p=[0.40, 0.25, 0.15, 0.10, 0.10]
    )

    priority = np.random.choice(
        ['Low', 'Medium', 'High', 'Critical'],
        p=[0.45, 0.30, 0.20, 0.05]
    )

    status = np.random.choice(
        ['Closed', 'Resolved', 'In-Progress', 'Open'],
        p=[0.35, 0.30, 0.20, 0.15]
    )

    created_date = start_date + timedelta(
        days=random.randint(0, 364)
    )

    # SLA Targets
    sla_targets = {
        'Critical': 2,
        'High': 5,
        'Medium': 8,
        'Low': 15
    }

    sla_target = sla_targets[priority]

    closed_date = None
    resolution_days = None
    sla_status = None

    if status in ['Closed', 'Resolved']:

        if priority == 'Critical':
            resolution_days = random.randint(1, 3)

        elif priority == 'High':
            resolution_days = random.randint(2, 6)

        elif priority == 'Medium':
            resolution_days = random.randint(4, 10)

        else:
            resolution_days = random.randint(6, 18)

        closed_date = created_date + timedelta(
            days=resolution_days
        )

        if resolution_days <= sla_target:
            sla_status = 'Met'
        else:
            sla_status = 'Missed'

    weight_map = {
        'IT': 1.5,
        'Operations': 1.2,
        'Sales': 1.1,
        'Finance': 0.9,
        'HR': 0.7,
        'Marketing': 0.6
    }

    ticket_weight = weight_map[department]

    tickets.append([
        f"TKT-{i}",
        created_date,
        closed_date,
        department,
        category,
        priority,
        status,
        resolution_days,
        sla_target,
        sla_status,
        ticket_weight
    ])

# -----------------------
# DataFrame
# -----------------------

df = pd.DataFrame(
    tickets,
    columns=[
        'Ticket_ID',
        'Created_Date',
        'Closed_Date',
        'Department',
        'Category',
        'Priority',
        'Status',
        'Resolution_Days',
        'SLA_Target_Days',
        'SLA_Status',
        'Ticket_Weight'
    ]
)

# -----------------------
# Export
# -----------------------

df.to_csv(
    'IT_Service_Desk_Dataset.csv',
    index=False
)

print(df.head())
print(f"Total Records: {len(df)}")