for f in wstar*.png; do echo "Processing $f file.."; 

mogrify -crop 1200x1000+0+160 $f;
done;
