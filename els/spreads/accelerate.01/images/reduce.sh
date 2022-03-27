mkdir orig
for i in *pdf
do
  mv $i orig
  echo $i
  gs -sDEVICE=pdfwrite -dPDFSETTINGS=/ebook -q -o $i orig/$i
done
