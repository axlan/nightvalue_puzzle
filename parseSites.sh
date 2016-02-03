

wget -P site -i downloadlist.txt

mkdir parsed

FILES=site/*
for f in $FILES
do
  echo "Processing $f file..."
  # take action on each file. $f store current file name
  python parseSite.py $f parsed/$(basename $f)
done

cat parsed/* > combined

