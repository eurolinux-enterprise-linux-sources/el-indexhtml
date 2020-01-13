#Remove community list links
#Prepare env
sudo yum install -y python-pip
pip install --user beautifulsoup4
find ./src/ -iname "index.html" -exec python remove_community_list_link.py {} \;
