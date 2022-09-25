#!/bin/bash
echo "Creating Python Virtual Environment...."
python3 -m venv env
echo "Done..."
sleep 1
source "env/bin/activate"
echo "Installing Automation Framework.."
pip install selenium
pip install webdriver-manager
echo "Setup Complete. Now Please run "sh simbi.sh" "