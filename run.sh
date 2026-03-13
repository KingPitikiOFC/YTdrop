#!/usr/bin/env bash

RED="\033[0;31m"
GREEN="\033[0;32m"
YELLOW="\033[1;33m"
BLUE="\033[0;34m"
NC="\033[0m"

echo -e "${BLUE}Checking dependencies...${NC}"

if command -v python >/dev/null 2>&1; then
    echo -e "${GREEN}python OK${NC}"
else
    echo -e "${YELLOW}Installing python${NC}"
    pkg install python -y
fi

if command -v ffmpeg >/dev/null 2>&1; then
    echo -e "${GREEN}ffmpeg OK${NC}"
else
    echo -e "${YELLOW}Installing ffmpeg${NC}"
    pkg install ffmpeg -y
fi

python - <<EOF
try:
    import yt_dlp
    print("\033[0;32myt_dlp OK\033[0m")
except ImportError:
    import os
    print("\033[1;33mInstalling yt_dlp\033[0m")
    os.system("python -m pip install yt-dlp")
EOF

echo -e "${BLUE}Running script...${NC}"
python yt.py