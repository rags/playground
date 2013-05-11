function [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters)
%GRADIENTDESCENT Performs gradient descent to learn theta
%   theta = GRADIENTDESENT(X, y, theta, alpha, num_iters) updates theta by 
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
J_history = zeros(num_iters, 1);
%fprintf("*******\nX=")
%disp(size(X));
%fprintf("y=")
%disp(size(y));
%fprintf("theta , size(theta)=")
%disp(theta)
%disp(size(theta))
%fprintf("apha=")
%disp(alpha);
%fprintf("*******")
XT=X'
for iter = 1:num_iters

    % ====================== YOUR CODE HERE ======================
    % Instructions: Perform a single gradient step on the parameter vector
    %               theta. 
    %
    % Hint: While debugging, it can be useful to print out the values
    %       of the cost function (computeCost) and gradient here.
    %


	%disp(size(diff));
	theta = theta - alpha * (1/m) * (XT * (X*theta-y))

    % ============================================================

    % Save the cost J in every iteration    
	%disp(sprintf('after iteration %d',iter))
	%size(X)
	%size(y)
	%size(theta)
	%theta
    J_history(iter) = computeCost(X, y, theta);

end

end
