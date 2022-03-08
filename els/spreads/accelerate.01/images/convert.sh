for n in `seq -w 20`
do 
  echo $n
  #mkdir bb$n
  for i in `seq 9`
  do
    echo $i
    convert bb$n.png -alpha set -background none -channel A \
         -evaluate multiply 0.$i +channel bb$n/$i.png
  done
done
