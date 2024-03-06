echo "Setting up the environment..."

if ('./.git' | path exists) {
    echo "Git repository already initialized..."
} else {
    echo "Initializing git repository..."
    git init .
    git add -A
    git commit -m "Initial commit"
    echo "Git repository initialized."
}

if ('./.venv' | path exists) {
    echo "Virtual environment already exists"
} else {
    echo "Creating virtual environment..."
    uv venv
    echo "Virtual environment created."
}

echo "Activating virtual environment..."

overlay use ./.venv/Scripts/activate.nu

cls

echo "Installing dependencies..."

uv pip install -r ./requirements.txt

echo "Setup completed. Exiting..."

python3 ./setup_requirements.py

exit
