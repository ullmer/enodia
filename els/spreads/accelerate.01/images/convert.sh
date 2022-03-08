for n in `seq -w 50`
do 
  echo $n
  #mkdir bb$n
  for i in `seq 9`
  do
    echo $i
    echo convert bb$n.png -alpha set -background none -channel A \
         -evaluate set 0.$i +channel bb$n/$i.png
  done
done
