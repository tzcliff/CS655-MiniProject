# Install a virtual environment
sudo apt-get update
sudo apt-get install -y python3-venv

# Install dependencies
pip install Flask
pip install requests
pip install torch==1.7.0+cpu torchvision==0.8.1+cpu torchaudio==0.7.0 -f https://download.pytorch.org/whl/torch_stable.html