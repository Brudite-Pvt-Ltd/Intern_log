classes=("SampleClass0" "SampleClass1" "SampleClass2" "SampleClass3" "SampleClass4" "SampleClass5" "SampleClass6" "SampleClass7" "SampleClass8" "SampleClass9")
for class in ${classes[@]}; do
a=$(awk '/'${class}'/ {print NR}' sample_log.txt)
id=$(awk '/'${class}'/ {print $NF}' sample_log.txt)
l=$(echo "$a" | wc -w)
echo ${class}: ${l} >> answer2.txt
echo ${class}: ${id} "\\n" >> answer2_id.txt
done
cat answer2.txt