#bin/sh

python3 Contrast_setting.py $1
python3 Thresholding.py $1
python3 edgedetection.py $1
python3 gausian_blur.py $1
python3 Histogram.py $1

mkdir $2
ls | grep 'Out_*' > inp
input="./inp"
cp $1 ./$2/
while IFS= read -r var
do
  mv $var ./$2/
done < "$input"
rm inp