var alive = 'alive';
var dead = 'dead';
var Cell = Class.create({
     initialize: function(){
        this.state = arguments[0]||'dead';
        this.live_neighbours = 0;
        },
     update: function(){
        if(this.live_neighbours<2 || this.live_neighbours>3) this.state = dead;
        if(this.live_neighbours==3) this.state = alive;
        },
     add_live_neighbour: function(){
        this.live_neighbours++;
        },
     is_alive: function(){
        return this.state=="alive";    
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

var Grid = Class.create({
        initialize: function(bound,live_cell_coords){
            this.bound=bound;            
            this.cells = live_cell_coords;
        },        
        live_cells: function(){
            var cells = $A();
            this.cells.each(function (coord){
                coord.set(cells,new Cell(alive));
            });
            return cells;
        },
        evolve: function(){
            with(this){
                var live_cells = live_cells();
                cells.each(function (coord){
                        coord.neighbours(bound).each(function (neig_coord){
                                var neighbour = neig_coord.get(live_cells);
                                if(!neighbour) {
                                    neighbour = new Cell();
                                    neig_coord.set(live_cells,neighbour);
                                }
                                neighbour.add_live_neighbour();
                            })   
                            });
                var coords = $A();
                $R(0,bound.x).each(function (i){
                        if(live_cells[i]){
                            $R(0,bound.y).each(function (j){
                                    if(live_cells[i][j]){
                                        live_cells[i][j].update();
                                        if(live_cells[i][j].is_alive())
                                        coords.push(new CoOrd(i,j));
                                    }
                                });
                        }     
                    });
                return new Grid(bound, coords);        
            }
            }
    });