#!/bin/bash
cd "$(dirname "$0")"
pip3 install -r requirements.txt -q
PORT=5001 python3 app.py
