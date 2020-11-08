#!\bin\sh
echo "Files in the directory are:"
for f in $(ls /etc/*)
do
  echo $f
done
