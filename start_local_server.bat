@echo off

@title OpenDoctoratePy - Local Server

call env\scripts\activate.bat

python3 server\app.py
