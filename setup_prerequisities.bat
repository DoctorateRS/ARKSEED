@ECHO off
@TITLE Setup Prerequisites

REM Setup uv

call python -m ensurepip --upgrade
call python -m pip install --upgrade pip
call pip install uv

echo "uv has been set up. Please install the rest of the prerequisites manually."
echo "That includes: "
echo "  - Scoop"
echo "  - Git"
echo "  - Nushell"

exit