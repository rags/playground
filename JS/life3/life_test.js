function run_tests(log) {
    test_cell(log + "1");
    test_coord(log + "2");
    test_grid(log + "3");
}

function test_grid(log) {
    new Test.Unit.Runner({
        setup: function() {
            Object.extend(this, {
                assertNext: function(grid, coords) {
                    this.assertLiveCells(grid.evolve().live_cells(), coords);
                },
                assertLiveCells: function(cells, coords) {
                    var actualCount = 0;
                    for (var i = 0; i < cells.length; i++)
                        if (cells[i])
                            for (var j = 0,k=0; j < cells[i].length; j++)
                                if (cells[i][j] && cells[i][j].is_alive()) {
				    this.assertInList(coords, new CoOrd(i, j));				    
                                    actualCount++;
                                }
                    this.assertEqual(coords.length, actualCount);
                },
                assertInList: function(coords, expectedcoord) {
                    this.assert(this.is_coord_present(coords, expectedcoord), expectedcoord + " not found in " + coords);
                },
                is_coord_present: function(coords, coord) {
                    for (var i = 0; i < coords.length; i++) {
                        if (coord.equals(coords[i])) return true;
                    }
                    return false;
                },
                bound: new CoOrd(10, 10)

            });
        },
        test_death:function() {
            with (this) {
                assertNext(new Grid(bound,
                        $A([new CoOrd(2, 3),
                            new CoOrd(2, 4)])
                        ),
                        $A([])
                        )
            }

        },		
        test_blinker:function() {
            with (this) {
                assertNext(new Grid(bound,
                        $A([new CoOrd(1, 1),
                            new CoOrd(1, 0),
                            new CoOrd(1, 2)])
                        ),
                        $A([new CoOrd(1, 1),
                            new CoOrd(0, 1),
                            new CoOrd(2, 1)])
                        )
            }

        },
	test_stable_block:function() {
            with (this) {
		var stableBlock = $A([new CoOrd(1, 1),
				      new CoOrd(1, 2),
				      new CoOrd(2, 1),
				      new CoOrd(2, 2)]);
                assertNext(new Grid(bound,stableBlock),stableBlock)
            }

        },
        test_boat:function() {
            with (this) {
		var stableBlock = $A([new CoOrd(0, 1),
				      new CoOrd(1, 0),
				      new CoOrd(2, 1),
				      new CoOrd(0, 2),
				      new CoOrd(1, 2)]);
                assertNext(new Grid(bound,stableBlock),stableBlock)
            }

        },
        test_toad:function() {
            var phases = $A([$A([
                new CoOrd(1, 1),
                new CoOrd(1, 2),
                new CoOrd(1, 3),
		new CoOrd(2, 2),
                new CoOrd(2, 3),
                new CoOrd(2, 4)]),
                $A([new CoOrd(0, 2),
                    new CoOrd(1, 1),
                    new CoOrd(1, 4),
                    new CoOrd(2, 1),
                    new CoOrd(2, 4),
                    new CoOrd(3, 3)])]);
            var grid = new Grid(this.bound, phases[0]);
            for (var i = 0; i < 10; i++) {
                grid = grid.evolve();
                this.assertLiveCells(grid.live_cells(), phases[(i + 1) % 2]);
            }
        }
    },
    {testLog:log});
}

function test_coord(log) {
    new Test.Unit.Runner({
        setup: function() {
            Object.extend(this, {
                bounds: new CoOrd(10, 11),
                reverse: function(arr) {
                    return $A(arr).reverse();
                }
            });
        },
        test_neighbours_in_middle: function() {
            with (this) {
                var expecteds = reverse([new CoOrd(0, 0),new CoOrd(0, 1),new CoOrd(0, 2),new CoOrd(1, 0),new CoOrd(1, 2),new CoOrd(2, 0),new CoOrd(2, 1),new CoOrd(2, 2)]);
                new CoOrd(1, 1).neighbours(bounds).each(function(coord) {
                    assert(expecteds.pop().equals(coord));
                });
            }
        },
        test_bottom_left_corner: function() {

            with (this) {
                var expecteds = reverse([new CoOrd(0, 1),new CoOrd(1, 0),new CoOrd(1, 1)]);
                new CoOrd(0, 0).neighbours(bounds).each(function(coord) {
                    assert(expecteds.pop().equals(coord));
                });
            }
        },
        test_top_left_corner: function() {
            with (this) {
                var expecteds = reverse([new CoOrd(8, 0),new CoOrd(8, 1),new CoOrd(9, 1)]);
                new CoOrd(9, 0).neighbours(bounds).each(function(coord) {
                    assert(expecteds.pop().equals(coord));
                });
            }
        },
        test_top_edge: function() {
            with (this) {
                var expecteds = reverse([new CoOrd(8, 2),new CoOrd(8, 3),new CoOrd(8, 4),new CoOrd(9, 2),new CoOrd(9, 4)]);
                new CoOrd(9, 3).neighbours(bounds).each(function(coord) {
                    assert(expecteds.pop().equals(coord));
                });
            }
        },
        test_top_right_corner: function() {
            with (this) {
                var expecteds = reverse([new CoOrd(0, 1),new CoOrd(1, 0),new CoOrd(1, 1)]);
                new CoOrd(0, 0).neighbours(bounds).each(function(coord) {
                    assert(expecteds.pop().equals(coord));
                });
            }
        },
        test_set_get: function() {
            with (this) {
                var matrix = [];
                var coord = new CoOrd(2, 3);
                coord.set(matrix, 23);
                assertEqual(23, matrix[2][3]);
                assertEqual(23, coord.get(matrix));
                assertNull(new CoOrd(1, 1).get(matrix));
            }
        }

    },
    {testLog:log});
}

function test_cell(log) {
    new Test.Unit.Runner({
        test_add_neighbour: function() {
            with (this) {
                cell.add_live_neighbour();
                assertEqual(1, cell.live_neighbours);
            }
        },
        test_dead:function() {
            with (this) {
                assertDead();
                add_2live_neighbours();
                assertDead();
                add_2live_neighbours();
                assertDead();
            }
        },
        test_life:function() {
            with (this) {
                add_live_neighbours(3);
                assertAlive();
            }
        },
        test_death_loneliness_no_neighbour: function() {
            with (this) {
                this.cell = new Cell('alive');
                assertAlive();
                this.cell.update();
                assertDead();
            }
        },
        test_death_loneliness_1_neighbour: function() {
            with (this) {
                this.cell = new Cell('alive');
                assertAlive();
                add_live_neighbours(1);
                assertDead();
            }
        },
        test_sustainance_wuth_2_or_3_neighbours: function() {
            with (this) {
                this.cell = new Cell('alive');
                add_2live_neighbours();
                assertAlive();
                add_live_neighbours(1);
                assertAlive();
            }
        },
        test_death_by_over_crowding: function() {
            with (this) {
                this.cell = new Cell('alive');
                add_live_neighbours(4);
                assertDead();
            }
        },
        setup: function() {
            Object.extend(this, {
                cell:new Cell(),
                add_2live_neighbours: function() {
                    this.add_live_neighbours(2);
                },
                add_live_neighbours: function(n) {
                    for (var i = 0; i < n; i++)
                        this.cell.add_live_neighbour();
                    this.cell.update();
                },
                assertFalse: function(exp) {
                    this.assert(!exp);
                },
                assertDead: function() {
                    with (this)
                        assertFalse(cell.is_alive());
                },
                assertAlive: function() {
                    with (this)
                        assert(cell.is_alive());
                }

            });
        }
    },
    {testLog:log}
            );
}