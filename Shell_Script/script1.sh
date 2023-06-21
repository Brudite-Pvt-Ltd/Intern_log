# awk '/Exception/ {print NR " " $2 ", " $3 ", " $NF}' sample_log.txt
echo $(awk '/Exception/ {print NR " " $2 ", " $3 ", " $NF}' sample_log.txt)
