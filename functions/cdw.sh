PATH="$1"

if [ -z "$PATH" ]; then
    cd ~/workspace  
else
    cd ~/workspace/$PATH
fi
