# Linux setup for the gameserver

## Requirements
- Linux
- Python 3
- Wine
- Required RCC .exe files in the expected folders

## Install
```bash
sudo apt-get update
sudo apt-get install -y python3-pip wine wine32 wine64
cd vortexigameserver
pip3 install -r requirements.txt
```

## Access key
```bash
echo "your_access_key_here" > /tmp/vortexi_access_key
```

## Run
```bash
cd vortexigameserver
python3 main.py
```

## Notes
- This project still expects Windows-compatible RCCService binaries.
- Wine is used to run those `.exe` files on Linux.
- Registry reads/writes are replaced with file-based access keys on Linux.
- Windows GUI calls are stubbed away on Linux.
