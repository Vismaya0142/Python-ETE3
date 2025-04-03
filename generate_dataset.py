
import pandas as pd
import random

# Define Hackathon Domains, Colleges, and States
domains = ["AI & ML", "Blockchain", "Cybersecurity", "IoT", "Web Development"]
states = ["Karnataka", "Maharashtra", "Tamil Nadu", "Kerala", "Telangana"]
colleges = ["IIT Madras", "NIT Karnataka", "BITS Pilani", "Anna University", "VIT Vellore"]
days = ["Day 1", "Day 2", "Day 3"]

# Feedback samples categorized by sentiment
positive_feedback = [
    "Great experience! Learned a lot.",
    "Networking was amazing!",
    "Would love more hands-on sessions.",
    "Loved the mentors and project guidance.",
    "Fantastic event, would participate again."
]

neutral_feedback = [
    "The event was okay, could have been better.",
    "It was fine, but not very engaging.",
    "The sessions were informative but could be more detailed.",
    "Event was decent, but nothing extraordinary.",
    "I expected more from the workshops."
]

negative_feedback = [
    "Didn't enjoy the event at all, poorly organized.",
    "The event was too fast-paced and overwhelming.",
    "I didn't learn much, felt like a waste of time.",
    "The sessions were not relevant to my interests.",
    "The venue was not suitable for the event, very uncomfortable."
]

# Function to generate random names
def generate_name():
    first_names = ["Aarav", "Vihaan", "Ishaan", "Ananya", "Sanya", "Rohan", "Neha", "Kiran", "Rahul", "Priya"]
    last_names = ["Sharma", "Verma", "Iyer", "Patil", "Reddy", "Nair", "Joshi", "Gupta", "Singh", "Das"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

# Function to generate random email
def generate_email(name):
    domains = ["gmail.com", "yahoo.com", "outlook.com"]
    return f"{name.split()[0].lower()}{random.randint(100, 999)}@{random.choice(domains)}"

# Function to generate random feedback (positive, neutral, or negative)
def generate_feedback():
    sentiment = random.choice(["positive", "neutral", "negative"])
    if sentiment == "positive":
        return random.choice(positive_feedback)
    elif sentiment == "neutral":
        return random.choice(neutral_feedback)
    else:
        return random.choice(negative_feedback)

# Generate 350 participants
data = []
for i in range(1, 351):
    name = generate_name()
    participant = {
        "Participant_ID": i,
        "Name": name,
        "Email": generate_email(name),
        "College": random.choice(colleges),
        "State": random.choice(states),
        "Domain": random.choice(domains),
        "Day": random.choice(days),
        "Feedback": generate_feedback(),  # Use the new generate_feedback function
    }
    data.append(participant)

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("hackathon_dataset.csv", index=False)

print("✅ Hackathon dataset generated successfully!")
