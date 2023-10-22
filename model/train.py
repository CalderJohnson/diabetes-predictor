import torch
import csv
import random
from model import settings, DiabetesPredictorModel

def get_batch(split):
    """Generate a batch of data (src/tgt)"""
    index = random.randint(0, len(split) - settings["batch_size"] - 1)
    batch = split[index:index+settings["batch_size"]]
    src = torch.tensor([list(profile.values())[1:] for profile in batch])
    tgt = torch.tensor([list(profile.values())[0] for profile in batch])
    return src.to(settings["device"]), tgt.to(settings["device"])

# Prepare the dataset
with open("./data/dataset.csv") as datafile:
    csv_reader = csv.reader(datafile)
    data = []
    next(csv_reader) # Skip header
    for row in csv_reader:
        data.append(
            {
                "diabetes": float(row[0]),            # 0 = No diabetes, 1 = pre diabetes, 2 = diabetes
                "high_bp": float(row[1]),             # 0 = No high BP, 1 = high BP
                "high_chol": float(row[2]),           # 0 = No high cholesterol, 1 = high cholesterol
                "chol_check": float(row[3]),          # 0 = No cholesterol check in last 5y, 1 = cholesterol check in last 5 years
                "bmi": float(row[4]),                 # Body mass index (weight/height^2)
                "smoker": float(row[5]),              # 0 = Non smoker, 1 = smoker
                "stroke": float(row[6]),              # 0 = No history of stroke, 1 = history of stroke
                "heart_disease": float(row[7]),       # 0 = No history of heart disease or heart attacks, 1 = history of heart disease/attack
                "physical_activity": float(row[8]),   # 0 = No physical activity in the past 30 days, 1 = physical activity in past 30 days
                "fruits": float(row[9]),              # 0 = Does not consume 1 or more fruits per day, 1 = consumes fruit 1 or more times per day
                "vegetables": float(row[10]),         # 0 = Does not consume 1 or more veggies per day, 1 = consumes 1 or more veggies per day
                "alcohol": float(row[11]),            # 0 = No heavy alcohol consumption, 1 = heavy alcohol consumption (14+ drinks/week for men, 7+ drinks/week for women)
                "healthcare": float(row[12]),         # 0 = No healthcare plan, 1 = has a healthcare plan
                "gen_health": float(row[14]),         # 1 = Excellent health, 2 = very good health, 3 = good health, 4 = fair health, 5 = poor health
                "mental_health": float(row[15]),      # How many of the past 30 days has a mental health issue affected you?
                "sex": float(row[18]),                # 0 = F, 1 = M
                "age": float(row[19]),                # 13 level age metric
            }
        )

# Divide into train/test sets
random.shuffle(data) # Remove order from dataset
partition = int(len(data) * 0.9) # 90/10 train/test split
train_data = data[:partition]
test_data = data[partition:]

# Initialize the model and optimizer
model = DiabetesPredictorModel().to(settings["device"])
optimizer = torch.optim.Adam(model.parameters(), lr=settings["learning_rate"])
loss_fn = torch.nn.MSELoss()

# Train the model
average_loss = 0
for i in range(settings["epochs"]):

    # Evaluate loss every 100 steps
    if i % 100 == 0:
        average_loss /= 100
        print(f"Epoch {i}: loss={average_loss}")
        average_loss = 0

    # Get a batch of data
    src, tgt = get_batch(train_data)

    # Train model based on loss
    logits = model(src)
    loss = loss_fn(logits, tgt)
    average_loss += loss.item()

    # Backpropagate
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# Evaluate the model on validation batches (x100)
average_loss = 0
for i in range(100):
    src, tgt = get_batch(test_data)
    logits = model(src)
    loss = loss_fn(logits, tgt)
    print(loss.item())
    average_loss += loss.item()
print(f"Validation loss: {average_loss / 100}")

# Save the model
torch.save(model.state_dict(), "./model.pt")
