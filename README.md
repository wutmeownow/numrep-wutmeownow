# numrep

Starter code for numerical representation exercise

Add your files here.

## Overflows and Underflows
If I were to check the limits on ints in python, there would be no end because they are generically precise and unbound.

## Bessel Functions
According to Landau, the lower recursion formula is more accurate since it accumulates smaller errors as it iterates down in l. Since larger l values have larger roundoff errors, the result's error will have larger relative contributions versus from iterating down in small l values.

## Numerical Differentiation

1) In my plots of the relative error versus step size h, I find the minimum error for the forward difference method is around 10^-7 which is close to the text's value of 3x10^-8. This minimum is at step size h on the order of 10^-8, which matches what the text expects. For the central difference method, I have a minimum error on the order of 10^-11, which is at the same order the text predicts. In the case of the extrapolated difference method, if the minimum relative error should be roughly the machine error divided by the step size, as estimated by the text, I would expect (10^-15 / 10^-2) = 10^-13 to be the minimum, which can be seen in the plot. Therefore, my results do roughly agree with the predictions in the text. Forward (larger h) of these minimums the algorithmic error dominates while at smaller h the rounding error dominates.

2) The slopes of the relative error in the regime where algorithmic error dominates do agree with the model's predictions. The forward difference method grows slower w.r.t. h versus the central difference method, and the same is true for the central difference method versus the extrapolated difference method. These growth rates correspond to O(h), O(h^2), and O(h^4), as predicted by the text.

