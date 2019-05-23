#!/bin/bash

filename=$1

#fetch from sqlie database

result=$(sqlite3 /hercules/u/aswin/database/Processed.db "select result_path from headers where file_name='$filename'")

file_location=$(sqlite3 /hercules/u/aswin/database/Processed.db "select file_location from headers where file_name='$filename'")

echo $result $file_location

cd $result

ln -s $file_location 



echo "Creating filterbank file\n"
filterbank $file_location -n 8 -o $filename".fil"

tar -xvf *_singlepulse.tgz

echo "tar done"

touch spfiles_combined
ls spfiles_combined

echo "loop starting"
for spfile in $(ls -1rt *.singlepulse)
   do cat $spfile >> spfiles_combined
done
echo "loop end" 

touch spfiles_combined.sorted

echo "grep coming"
grep -v "# DM" spfiles_combined | sort -gr -k 2 >> spfiles_combined.sorted

 
bokeh  serve --show ~/test.py --args $filename".fil" $result/spfiles_combined.sorted

echo "bokeh  serve --show ~/test.py --args $filename".fil" $result/spfiles_combined.sorted"
exit
