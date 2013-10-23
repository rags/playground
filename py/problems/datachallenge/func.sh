map2x() { 
python `pwd`/path_doubling_mapper.py 
}

map1step() { 
python `pwd`/one_hop_mapper.py 
}

reduce() { 
python `pwd`/reducer.py 
}

map_combine() { 
python `pwd`/combine_mapper.py
}

reduce_combine() { 
python `pwd`/combine_reducer.py
}

map_print() { 
python `pwd`/prettyprint_mapper.py 
}

tabify(){
	tr ' ' '\t'
}

untabify(){
	tr '\t' ' '
}

RED="[00;31m"
NO_COLOR="[00m"

e(){
	echo $RED$1$NO_COLOR
    echo "$2"
}

shuffle(){
sort
}
