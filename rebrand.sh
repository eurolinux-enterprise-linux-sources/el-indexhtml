#!/usr/bin/env bash

for i in `grep -R 'Scientific' src/HTML/ | awk -F: '{print $1}'` 
do 
        sed -i 's/Scientific /Euro/g' $i; 
done

for i in `grep -R 'SL' src/HTML/ | awk -F: '{print $1}'`
do
        sed -i 's/SL/EL/g' $i;
done

for i in `grep -R 'scientificlinux.org' src/HTML/ | awk -F: '{print $1}'`
do
        sed -i 's/scientificlinux.org/euro-linux.com/g' $i;
done

#Russian version fix
for i in `grep -R 'scientificlinux.ru' src/HTML/ | awk -F: '{print $1}'`
do
        sed -i 's/scientificlinux.ru/euro-linux.com/g' $i;
done

for i in `grep -R 'img' src/HTML/ | awk -F: '{print $1}'`
do
	cp $i ${i}.bak 
        cat ${i}.bak | grep -v img > $i
	rm -f ${i}.bak
done

