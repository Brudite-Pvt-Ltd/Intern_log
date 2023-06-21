a=$(grep -o '[[:alnum:]]' sample_log.txt | sort | uniq -c | awk '{print "[" $2 "-" $1"]"}')

echo "${a}" > answer3.txt
cat answer3.txt