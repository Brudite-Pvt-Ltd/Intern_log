awk '/everything normal for id/ {print $NF " " $3 " " $1 " " $2 " - "}' sample_log.txt > answer4_1.txt
awk '/detail for id/ {print $NF " " $3 " " $1 " " $2 " - "}' sample_log.txt > answer4_2.txt
awk '/verbose detail/ {print $NF " " $3 " " $1 " " $2 " - "}' sample_log.txt > answer4_3.txt
# cat answer4_1.txt 
# cat answer4_2.txt 
# cat answer4_3.txt 