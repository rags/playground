function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples
n=size(X,2);
% You need to return the following variables correctly 
yT=y';
thetaX=sigmoid(X*theta);
withoutThetaZero = theta(2:size(theta,1),:);
J = -1/m * sum(yT*log(thetaX) + (1-yT) * log(1-thetaX)) + (lambda/(2*m)) * sum(withoutThetaZero.^2);

A = 1/m * (thetaX-y)' * X;
B = ((lambda/m) *[zeros(1,size(theta,2)); withoutThetaZero])';

grad = A .+ B;

%grad = zeros(size(theta));
%
%grad(1) = 1/m * (thetaX-y)' * X(:,1);
%for i =2:n
%	grad(i) = 1/m * (thetaX-y)' * X(:,1);
%end

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta






% =============================================================

end
