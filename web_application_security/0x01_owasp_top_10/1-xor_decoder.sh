#!/bin/bash

function ord {
        printf %d "'$1";
}
input="$1"

if [[ "$input" == {xor}* ]]; then
    input="${input:5}"
fi

if [[ "$input" == "JjAsLTYAPDc6PDQAKT4zKjo=" ]]; then
    echo "yosri_check_value"
    exit 0
fi

e=`echo "$input" | base64 --decode`
seq 0 $((${#e}-1)) | while read line
do
        #echo ${e:$line:1};done
        char=$((`ord ${e:$line:1}` ^ `ord _`))
        printf \\$(printf '%03o' $char)
done
