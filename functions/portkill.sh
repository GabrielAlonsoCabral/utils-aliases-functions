PORT="$1"
PID="$(lsof -t -i:$PORT)"

if [ -z "$PID" ]; then
    echo "No process found on port $PORT"
else
    kill -9 "$PID"
    echo "Process $PID killed on port $PORT"
fi
