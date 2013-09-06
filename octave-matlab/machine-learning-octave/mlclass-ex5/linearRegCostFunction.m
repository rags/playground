function [J, grad] = linearRegCostFunction(X, y, theta, lambda)
%LINEARREGCOSTFUNCTION Compute cost and gradient for regularized linear 
%regression with multiple variables
%   [J, grad] = LINEARREGCOSTFUNCTION(X, y, theta, lambda) computes the 
%   cost of using theta as the parameter for linear regression to fit the 
%   data points in X and y. Returns the cost in J and the gradient in grad

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
withoutThetaZero = theta(2:size(theta,1),:);
XTheta_y = X * theta - y;
J = 1/(2*m) * sum(XTheta_y .^ 2) + (lambda/(2*m)) * sum(withoutThetaZero.^2);
grad = 1/m * X' * (XTheta_y)  .+ (lambda/m) * [zeros(1, size(theta,2)); withoutThetaZero];

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost and gradient of regularized linear 
%               regression for a particular choice of theta.
%
%               You should set J to the cost and grad to the gradient.
%












% =========================================================================

#grad = grad(:);

end
