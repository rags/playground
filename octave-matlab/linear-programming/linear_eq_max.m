
load(argv(){1});
[xmin,fmin] = minimizeCost(A,b,c);
printf("\nMin x:");
printf(" %f ",xmin);
printf("\noptimal value: %f\n",fmin);


