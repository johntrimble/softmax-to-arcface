
# --- Stage 1: Build virtual environment and install dependencies ---
ARG BASE_IMAGE=pytorch/pytorch:2.7.1-cuda12.8-cudnn9-runtime
FROM ${BASE_IMAGE} as builder

ARG VENV_PATH=/opt/venv

RUN python -m venv --system-site-packages ${VENV_PATH}
ENV PATH="${VENV_PATH}/bin:$PATH"
ENV VENV_PATH="${VENV_PATH}"

# Install the requirements using BuildKit mount from the workspace context
RUN --mount=type=bind,from=workspace,source=requirements.txt,target=/tmp/requirements.txt \
    ${VENV_PATH}/bin/python -m pip install --upgrade pip && \
    ${VENV_PATH}/bin/python -m pip install --no-cache-dir -r /tmp/requirements.txt

# --- Stage 2: Main image with user, tools, and venv from builder ---
FROM ${BASE_IMAGE}

# User and group IDs for the non-root user
# These should match the host user to avoid permission issues with mounted volumes.
ARG UID=1000
ARG GID=1000
ARG USERNAME=vscode
ARG VENV_PATH=/opt/venv

USER root

# Install useful packages
RUN apt-get update && \
    apt-get install -y \
        git \
        wget \
        curl \
        sudo \
        exa \
        fzf \
        jq \
        tree \
        bat \
        fd-find \
        ripgrep \
        ca-certificates \
        lsb-release \
        emacs-nox \
        vim \
        nano \
        gh && \
    ln -s /usr/bin/fdfind /usr/local/bin/fd && \
    ln -s /usr/bin/batcat /usr/local/bin/bat && \
    rm -rf /var/lib/apt/lists/*

# Add non-root user with the same UID and GID as the host user
ENV DOCKER_USER=${USERNAME}
RUN groupadd -g $GID $USERNAME && useradd -u $UID -g $GID -m $USERNAME
RUN chsh -s /bin/bash $USERNAME

# Create /workspace directory
RUN mkdir -p /workspace && chown $USERNAME:$USERNAME /workspace

# Add ENTRYPOINT script
COPY . /docker/
RUN chmod +x /docker/entrypoint.sh && chown $USERNAME:$USERNAME /docker/entrypoint.sh
ENTRYPOINT ["/docker/entrypoint.sh"]

# Copy the pre-built virtual environment from builder stage and set ownership
COPY --from=builder --chown=${USERNAME}:${USERNAME} ${VENV_PATH} ${VENV_PATH}

# Set the environment variable to use the virtual environment
ENV PATH="${VENV_PATH}/bin:$PATH"
ENV VENV_PATH="${VENV_PATH}"

USER $USERNAME

# Set the working directory
WORKDIR /workspace
