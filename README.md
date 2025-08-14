# PyTorch GPU Dev Container Template

This is a **project template** that sets up a Dockerized development environment for PyTorch with GPU support. It is designed to be used with **Visual Studio Code Dev Containers** and **Docker Compose**, making it easy to work on GPU-enabled machine learning projects in an isolated and reproducible environment.

## ⚡ Quick Start

1. **Create your project directory:**

    ```bash
    mkdir my_ai_project
    cd my_ai_project
    ```

2. **Add template files from this repository:** This command downloads the PyTorch GPU template files into your project directory, without the Git history.

    ```bash
    git archive --remote=git@github.com:johntrimble/containerized-ai-templates.git HEAD pytorch-gpu \
      | tar -x --strip-components=1 -C .
    ```

3. **Run the bootstrap script:** This script detects your host user ID and group ID and writes a `.env` file so that files created in the container match your local permissions.

    ```bash
    ./script/bootstrap
    ```

4. **Verify GPU access:**

    ```bash
    docker compose run --rm dev python check_environment.py
    ```

   Example output:

    ```
    Python executable: /opt/conda/bin/python3.11
    Python version: 3.11.13 | packaged by conda-forge | (main, Jun  4 2025, 14:48:23) [GCC 13.3.0]

    User name: vscode
    User ID: 1000
    Group ID: 1000

    Current working directory: /workspace

    PyTorch version: 2.7.1+cu128
    CUDA is available. Device count: 1
    Current device: 0
    Device name: NVIDIA GeForce RTX 5090
    ```

5. **Open in VS Code Dev Container:**

   - Open the project in VS Code.
   - If prompted, reopen the project in a dev container.
   - Or use the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`) and select:
     ```
     Dev Containers: Rebuild and Reopen in Container
     ```

Once the dev container is open, you can:

- Run Python scripts and experiments directly in the integrated terminal.
- Use Jupyter notebooks inside the container with GPU access.
- Install and manage Python dependencies via `pip` using the container's environment.
- Access all mounted project files, including datasets in `/data`.
- Use VS Code extensions, linting, and debugging tools inside the container as if on your host.

You now have a fully functional PyTorch development environment with GPU support inside a containerized workspace.

## 📁 Directory Structure

```
pytorch-gpu/
├── compose.yaml                # Docker Compose file for launching services
├── requirements.txt            # Python dependencies
├── README.md                   # This documentation file
├── check_environment.py        # Script to verify environment and GPU availability
├── script/
│   └── bootstrap               # Bootstrap script for setup
├── notebooks/                  # Jupyter notebooks for experiments
├── data/                       # Directory for datasets and model files
└── services/
    └── pytorch/
        └── Dockerfile          # Dockerfile for PyTorch service
```

## 🧰 Prerequisites

- **Host OS:** A Linux host is strongly recommended. This template has been developed and tested on Linux and is not guaranteed to work on Windows or macOS.
- [Docker](https://docs.docker.com/get-docker/)
- [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html) (for GPU support)
- [Visual Studio Code](https://code.visualstudio.com/) with the **Dev Containers** extension

## 🚀 Features

- ✅ Pre-configured **Docker Compose** setup for GPU-enabled development
- ✅ **VS Code Dev Container** integration for seamless editor support
- ✅ **Automatic user permission mapping** to avoid file permission issues
- ✅ **GPU verification script** to confirm setup
- ✅ Clean, modular project layout for code, data, and configuration

## 🗂 Layout of the Dev Container

When using the dev container, the following directories are mounted:

- `/workspace`: Your project root — code, notebooks, scripts
- `/data`: The `./data` directory on your host, for datasets and model checkpoints

## 🛠 Customization

- Add your datasets to the `data/` directory.
- Edit `requirements.txt` to add Python packages.
- Modify `services/pytorch/Dockerfile` for custom OS-level dependencies.
- Add notebooks or training scripts in the `notebooks/` or root folder.

## 🧯 Troubleshooting

- Make sure your system has a compatible **NVIDIA GPU** and up-to-date drivers.
- Ensure the **NVIDIA Container Toolkit** is installed and working.
- Check logs for errors:
  ```bash
  docker compose logs
  ```
