map2x() { 
python3 `pwd`/path_doubling_mapper.py 
}

map1step() { 
python3 `pwd`/one_hop_mapper.py 
}

reduce() { 
python3 `pwd`/reducer.py 
}

map_combine() { 
python3 `pwd`/combine_mapper.py
}

reduce_combine() { 
python3 `pwd`/combine_reducer.py
}

map_print() { 
python3 `pwd`/prettyprint_mapper.py 
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
