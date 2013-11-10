for ((i=1; i <= 10; ++i))
do
    echo ilpTest$i;
    echo "\\section{ilpTest$i}" >> printOut.tex;
    python ../../cuttingPlane.py ilpTest$i | grep -v "Read" >> printOut.tex;
done
