var alive = 'alive';
var dead = 'dead';
var oldAge = 2;
var minNeighbours=2;
var optimumNeighbours=3;
function apply_rule(cell,predicate,state){
    if(predicate) cell.state=state;
    return predicate;
}
function apply_life_rule(cell,predicate)
{
    return apply_rule(cell,predicate,alive);
}
function apply_death_rule(cell,predicate)
{
    return apply_rule(cell,predicate,dead);
}
var rules = $A([
		function loneliness_rule(cell){
		    return apply_death_rule(cell,cell.live_neighbours<minNeighbours);
		},
		function overcrowding_rule(cell){
		    return apply_death_rule(cell,cell.live_neighbours>optimumNeighbours);
		},		
		function ageing_rule(cell){
		    return apply_death_rule(cell,cell.generation>oldAge);
		},		
		function new_life_rule(cell){
		    return apply_life_rule(cell,cell.live_neighbours==optimumNeighbours);
		}		
		]);

var Cell = Class.create({
	initialize: function(isAlive,generation){
	    this.state = isAlive||dead;
	    this.generation=generation||0;
	    this.live_neighbours = 0;
        },
	clone: function(){
	    return new Cell(this.state,this.generation);
	},
	update: function(){
	    this.generation++;
	    var me=this;
	    rules.find(function(rule){return rule(me);});	    
        },
	add_live_neighbour: function(){
	    this.live_neighbours++;
        },
	is_alive: function(){
	    return this.state==alive;    
        },
	toString: function(){
            return "live_neighbours=" + this.live_neighbours + "; generation=" + this.generation + "; state=" + this.state;
        }
    });

var CoOrd = Class.create({
        initialize: function(x,y){
            this.x = x;
            this.y = y;
        },
        neighbours: function(bound){
            var neighbour_ords = $A();
            with(this){
                range_x(x,bound).each(
				      function(i){
					  range_y(y,bound).each(
								function(j){
								    var coord = new CoOrd(i,j);
								    if(!equals(coord)) 
									neighbour_ords.push(coord);            
								}
								);
				      }
				      );
            }
            return neighbour_ords;            
        },
        range_x: function(x,bound){
            return this.range_coord(x,bound.x);
        },
        range_y: function(y,bound){
            return this.range_coord(y,bound.y);
        },
        range_coord: function(coord,bound){
            return $R(this.valid_coord(bound,coord-1,coord),this.valid_coord(bound,coord+1,coord));
        },
        valid_coord:function(bound,coord,default_coord){
            return this.valid_bound(coord,bound)?coord:default_coord;
        },
        valid_bound: function(coord,bound){
            if(coord<0 || coord>=bound) return false;
            return true;
        },
        equals: function(other){
            return this.x == other.x && this.y==other.y;
        },
        toString: function(){
            return "(" + this.x + ", " + this.y + ")";
        },        
        set: function (matrix,data){
            if(!matrix[this.x]) matrix[this.x] = $A();
            matrix[this.x][this.y] = data;
        },
        get: function (matrix){
            if(!matrix[this.x]) return null;
            return matrix[this.x][this.y]||null;
        }
    });

function make_grid(bound,coords){
    var new_cells = $A();
    coords.each(function (coord){
	    coord.set(new_cells,new Cell(alive));	    
	});
    return new Grid(bound, new_cells);        
}
var Grid = Class.create({
        initialize: function(bound,live_cells){
            this.bound=bound;            
            this.cells = live_cells;
        },        
        live_cells: function(){
            return this.cells;
        },
	live_coords: function () {
	    var ret = $A();
	    this.each(function(cell,coord){ret.push(coord);});
	    return ret;
	},
	each: function(action,cells){
	    var _cells = cells || this.cells;
	    with(this){
		$R(0,bound.x).each(function (i){
                        if(_cells[i]){
                            $R(0,bound.y).each(function (j){
				    if(_cells[i][j])
					action(_cells[i][j],new CoOrd(i,j));
                                });
                        }     
                    });
	    }
	},
        evolve: function(){
            with(this){
		var clonedCells = $A();
		each(function(cell,coord) {coord.set(clonedCells,cell.clone());});
		each(function (cell,coord){
			coord.neighbours(bound).each(function (neig_coord){
                                var neighbour = neig_coord.get(clonedCells);
                                if(!neighbour) {
                                    neighbour = new Cell();
                                    neig_coord.set(clonedCells,neighbour);
                                }
                                neighbour.add_live_neighbour();
                            })});

                var new_cells = $A();
		each(function (cell,coord){
			if(!cell) return;
			cell.update();
			if(cell.is_alive()){
			    coord.set(new_cells,cell);
			}
		    },clonedCells);
                return new Grid(bound, new_cells);        
            }
	},
	makeString: function(cells){
	    var str="";
	    this.each(function(cell,coord) {str+=coord.toString() + "--" + cell.toString() + "\n";},cells);
	    return str;
	},
	toString: function(){
            return this.makeString(this.cells);
        }
    });