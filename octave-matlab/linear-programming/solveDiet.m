function solveDiet(sense)
    for i=1:size(argv,1)
      load(argv(){i});
    end
    
    constraints = [-nutrients'; nutrients';];
    upperBounds = [-bounds(:,1); bounds(:,2)];
    if exist('otherConstraints','var')
     constraints = [constraints; otherConstraints];
     upperBounds = [upperBounds; otherConstraintUpperBounds];
    end
    if ~exist('sense','var'), sense=1; end
    [xmin,fmin] = minimizeCost(constraints, upperBounds, costs, sense);
    printf("Min diet cost: %f\n", fmin);
    printf("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    optimalFoodCosts = xmin .* costs;
    for i=1:length(xmin)
        printf("%s %f @ %f\n", foodLabels(i,:),xmin(i),optimalFoodCosts(i));
    end
    printf("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    optimalNutrients = nutrients' * xmin;
    for i = 1:size(nutrientLabels,1)
      printf("%s %f\n", nutrientLabels(i,:),optimalNutrients(i));
    end
end


