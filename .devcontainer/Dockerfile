FROM mcr.microsoft.com/devcontainers/python:3.12

# Install git (needed to clone) + basic build tooling
RUN apt-get update \
 && apt-get install -y --no-install-recommends git \
 && rm -rf /var/lib/apt/lists/*

# Upgrade core packaging tools (helps with PEP517 builds)
RUN python -m pip install --upgrade pip setuptools wheel build

# Install your normal project deps first (better layer caching)
COPY requirements.txt /tmp/requirements.txt
RUN python -m pip install -r /tmp/requirements.txt

# --- Install Presidio from a pinned commit ---
ARG PRESIDIO_REPO=https://github.com/microsoft/presidio.git
ARG PRESIDIO_REF=a8dc07658e9733092387fbd09d8cd8f137564ffb

RUN git clone --no-checkout ${PRESIDIO_REPO} /tmp/presidio \
 && cd /tmp/presidio \
 && git checkout ${PRESIDIO_REF} \
 # Install the two packages from their subdirectories
 && python -m pip install ./presidio-analyzer ./presidio-anonymizer \
# Clean up
&& rm -rf /tmp/presidio

RUN python -m spacy download en_core_web_lg