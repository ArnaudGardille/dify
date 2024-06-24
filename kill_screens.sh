
#!/bin/bash
screen -ls | awk '/(Attached|Detached)/ {print $1}' | cut -d. -f1 | xargs kill
