exports.map = function(fn, seq) {
    var retSeq = [];
    for (var i = 0; i < seq.length; i++) {
        retSeq[i] = fn(seq[i]);
    }
    return retSeq;
};

exports.reduce = function(fn, seq, init) {
    if (!seq) {
        return init;
    }
    var initDefined = init !== undefined;
    var retVal = initDefined ? init : seq[0];
    for (var i = initDefined ? 0 : 1; i < seq.length; i++) {
        retVal = fn(retVal, seq[i]);
    }
    return retVal;
};

exports.filter = function(fn, seq) {
    var retSeq = [];
    for (var i = 0; i < seq.length; i++) {
        if (fn(seq[i])) {
            retSeq.push(seq[i]);
        }
    }
    return retSeq;
};
