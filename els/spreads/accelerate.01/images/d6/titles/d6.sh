for i in d1/*png
do
  bn=`basename $i .png`
  echo $bn
  #convert -liquid-rescale 16.6x16.6%\! $i $bn.png
  #convert -liquid-rescale 16x16% $i $bn.png
  convert -sample 16x16% $i $bn.png
done
