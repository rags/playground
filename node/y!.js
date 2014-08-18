
var Y = function (f) {
    var recurse = function(g) {
        return f(function(h) {
           return (g(g))(h)
        });
    };

    return recurse(recurse);
};

exports.Y = Y;
/*************************Tests************************/

exports.fact = Y(function(fn) {
                   return function(n) {
                       return n === 0? 1: n * fn(n - 1);
                   }
               });
