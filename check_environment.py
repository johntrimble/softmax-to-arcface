#!/usr/bin/env python

# Test script to verify the setup is working correctly

import os
import getpass
import torch

# Print location of python executable
print(f"Python executable: {os.path.realpath(os.sys.executable)}")

# Print the Python version
print(f"Python version: {os.sys.version}")

print()

# Print user name
print(f"User name: {getpass.getuser()}")

# Print UID and GID
print(f"User ID: {os.getuid()}")
print(f"Group ID: {os.getgid()}")

print()

# Print current working directory
print(f"Current working directory: {os.getcwd()}")

print()

# Print the PyTorch version
print(f"PyTorch version: {torch.__version__}")

# Check if CUDA is available
if torch.cuda.is_available():
    print(f"CUDA is available. Device count: {torch.cuda.device_count()}")
    print(f"Current device: {torch.cuda.current_device()}")
    print(f"Device name: {torch.cuda.get_device_name(torch.cuda.current_device())}")
else:
    print("CUDA is not available. Running on CPU.")