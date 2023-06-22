echo  -n "Enter the id:  "
read id
grep -a "$id" sample_log.txt > answer5.txt
cat answer5.txt