exports.tuple =  function(head, tail){
    return function(fn){
        return fn(head, tail);
    };
};

exports.head = function(fn){
    return fn(function (head, tail){return head;});
};

exports.tail = function(fn){
    return fn(function (head, tail){return tail;});
};
