function tuple(head, tail) {
    return function(fn) {
        return fn(head, tail);
    };
}

function head(fn) {
    return fn(function(head, tail) {
        return head;
    });
}

function tail(fn) {
    return fn(function(head, tail) {
        return tail;
    });
}

exports.tuple = tuple;
exports.head = head;
exports.tail = tail;

//////////////////////////////////////////////////// test //////////////////

function Employee(name, age, salary) {
    return tuple(name, tuple(age, salary));
}
var name = head;

function age(employee) {
    return head(tail(employee));
}

function salary(employee) {
    return tail(tail(employee));
}

exports.Employee = Employee;
exports.age = age;
exports.name = name;
exports.salary = salary;
