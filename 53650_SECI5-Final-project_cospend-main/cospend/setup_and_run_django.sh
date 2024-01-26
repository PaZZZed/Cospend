#!/bin/bash

# Exit script on any error
set -e

# Update and Upgrade the System
echo "Updating system packages..."
sudo apt update && sudo apt upgrade -y

# Check if OpenSSL is installed
echo "Checking for OpenSSL..."
if ! command -v openssl &> /dev/null
then
    echo "OpenSSL not found, installing OpenSSL..."
    sudo apt install openssl -y
fi

# Generate Self-Signed SSL Certificate if not present in the cospend directory
CERT_DIR="."
if [ ! -f "$CERT_DIR/cert.pem" ] || [ ! -f "$CERT_DIR/key.pem" ]; then
    echo "Generating a self-signed SSL certificate in the $CERT_DIR directory..."
    mkdir -p $CERT_DIR
    openssl req -x509 -newkey rsa:4096 -keyout "$CERT_DIR/key.pem" -out "$CERT_DIR/cert.pem" -days 365 -nodes -subj "/CN=localhost"
fi

# Start a new subshell for the remaining commands
(
    # Check if Python3 and Pip are installed
    echo "Checking for Python3 and Pip..."
    python3 --version

    if ! command -v pip3 &> /dev/null
    then
        echo "Pip not found, installing Pip..."
        sudo apt install python3-pip -y
    fi

    pip3 --version

    # Setup Virtual Environment
    echo "Setting up virtual environment..."
    pip3 install virtualenv
    python3 -m virtualenv venv
    source venv/bin/activate

    # Install Required Python Packages
    echo "Installing required Python packages..."
    pip install django django_extensions Werkzeug pyOpenSSL

    # Compile the Project (if any compilation is needed)
    # Add your project compilation commands here

    # Run the Development Server
    echo "Running the development server..."
    python manage.py runserver_plus --cert-file cert.pem --key-file key.pem
)

# End of script
echo "Setup complete. Server is running."

