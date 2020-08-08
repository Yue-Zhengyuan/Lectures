## Conformal Ward Identity


The three Ward Identity above can be combined into a single equation.
Given an arbitrary conformal coordinates change
$x^{\nu}\to x^{\nu}+\epsilon
^{\nu}(x)$, we get

$\partial_{\mu}\left(\epsilon_{\nu}T^{\mu \nu}\right)=\epsilon_{\nu}\partial_{\mu}T^{\mu \nu}+\left(\partial_{\mu}\epsilon_{\nu}\right)T^{\mu
 \nu}$

To exploit the properties of conformal transformations

$\frac{1}{2}\left(\partial_{\mu}\epsilon_{\nu}+\partial_{\nu}\epsilon_{\mu}\right)=\frac{1}{2}\left(\partial_{\rho}\epsilon^{\rho}\right)\eta
_{\mu \nu}$

$\frac{1}{2}\left(\partial_{\mu}\epsilon_{\nu}-\partial_{\nu}\epsilon_{\mu}\right)=\frac{1}{2}\epsilon^{\alpha  \beta}\partial_{\alpha
}\epsilon_{\beta}\epsilon_{\mu \nu}$

(here $\frac{1}{2}\partial_{\rho}\epsilon^{\rho}$ is the local scale
factor $f(x)$, and
$\frac{1}{2}\epsilon^{\alpha  \beta}\partial_{\alpha
}\epsilon_{\beta}$ is the local rotation angle) we rewrite the second
term

$\partial_{\mu}\left(\epsilon_{\nu}T^{\mu \nu}\right)=\epsilon_{\nu}\partial_{\mu}T^{\mu \nu}+\frac{1}{2}\left(\partial_{\mu}\epsilon
_{\nu}+\partial_{\nu}\epsilon_{\mu}\right)T^{\mu \nu}+\frac{1}{2}\left(\partial_{\mu}\epsilon_{\nu}-\partial_{\nu}\epsilon_{\mu}\right)T^{\mu
 \nu}\\
=\epsilon_{\nu}\partial_{\mu}T^{\mu \nu}+\frac{1}{2}\left(\partial_{\rho}\epsilon^{\rho}\right)\eta_{\mu \nu}T^{\mu \nu}+\frac{1}{2}\epsilon
^{\alpha  \beta}\partial_{\alpha}\epsilon_{\beta}\epsilon_{\mu \nu}T^{\mu \nu}$

$$
\delta_{\epsilon, \bar{\epsilon}}
\langle X \rangle
= \frac{1}{2\pi i} \left(
    - \oint_C dz \, \epsilon(z) \langle T(z) X \rangle
    + \oint_{\bar{C}} d\bar{z} \, \bar{\epsilon}(\bar{z}) \langle \bar{T}(\bar{z}) X \rangle
\right)
$$

where $X = \phi(w_1, \bar{w}_1) \cdots \phi(w_n, \bar{w}_n)$. The counter-clockwise contour $C \, (\bar{C})$need to enclose all the positions $w_i \, (\bar{w_i})$ appearing in $X$. 