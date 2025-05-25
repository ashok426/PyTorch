import torch
import numpy

# Check if GPU is available
if torch.cuda.is_available():
    device = torch.device("cuda")
    #print("available")
else:
    #print("not available")
    device = torch.device("cpu")

# Move tensor to GPU
x = torch.tensor([1.0, 2.0, 3.0]).to(device)
