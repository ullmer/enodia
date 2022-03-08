for n in `seq -w 20`
do 
  echo $n
  convert -geometry 600x baseball_Page_$n.png bb$n.png
done
