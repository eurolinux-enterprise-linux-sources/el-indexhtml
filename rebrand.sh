for i in `grep -R 'Scientific' HTML/ |awk -F: '{print $1}'` 
do 
        sed -i 's/Scientific /Euro/g' $i; 
done

for i in `grep -R 'SL' HTML/ |awk -F: '{print $1}'`
do
        sed -i 's/SL/EL/g' $i;
done

for i in `grep -R 'scientificlinux.org' HTML/ |awk -F: '{print $1}'`
do
        sed -i 's/scientificlinux.org/euro-linux.com/g' $i;
done
#Russian version fix
for i in `grep -R 'scientificlinux.ru' HTML/ |awk -F: '{print $1}'`
do
        sed -i 's/scientificlinux.ru/euro-linux.com/g' $i;
done
for i in `grep -R 'sl-intro' HTML/ |awk -F: '{print $1}'`
do
        sed -i 's/sl-intro/el-intro/g' $i;
done
#Color change
for i in `grep -R '1C1520' HTML/ |awk -F: '{print $1}'`
do
        sed -i 's/1C1520/0c61ab/g' $i;
done

#Remove community list links
#Prepare env
#
# USE WITH CAUTION! IT REMOVES LAST <li> FROM HTML without validation!
sudo yum install -y python-pip
pip install --user beautifulsoup4
find ./src/ -iname "index.html" -exec python remove_community_list_link.py {} \;


#for i in `grep -R 'img' HTML/ |awk -F: '{print $1}'`
#do
#	cp $i ${i}.bak 
#        cat ${i}.bak | grep -v img > $i
#	rm -f ${i}.bak
#done
