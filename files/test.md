---
permalink: /markdown/
title: "Note"
author_profile: true
redirect_from: 
  - /md/
  - /markdown.html
---

Recall the definition of asymptotically flat manifold, $g = \bar{g} + \sigma$, where $\bar{g}$ is the standard Euclidean metric and $\sigma = O_{k} \left( |x|^{-\tau} \right)$. We will use $\nabla, \nu, H$ and $\bar{\nabla}, \bar{\nu}, \bar{H}$ to express the connection, the unit normal vector, the mean curvature of regular level set $\Sigma_{t} = f(t)$ in $(M,g)$ and $(R^{3} - B_{r_{0}} ,\bar{g})$, respectively. 

Now we calculate the following quantities under the local chart at infinity, 
we can get that

$$
\nu = \frac{\nabla u}{|\nabla u|}, \quad \bar{\nu} = \frac{\bar{\nabla} u}{|\bar{\nabla} u|_{\bar{g}}}.
$$

$$
\begin{aligned}
H =& \operatorname{div}_{\Sigma_{t}} \left( \nu \right) \\
=& \operatorname{div} \left( \nu \right) - g \left( \nabla_{\nu} \nu, \nu \right) \\
=& \operatorname{div} \left( \frac{\nabla u}{|\nabla u|} \right) \\
=& \nabla u \left( \frac{1}{|\nabla u|} \right) + \frac{1}{|\nabla u|} \Delta u \\
=& - \frac{1}{|\nabla u|^{2}} \nabla u \left( |\nabla u| \right) + \frac{1}{|\nabla u|} \Delta u \\
=& - \frac{1}{2|\nabla u|^{3}} \nabla u \left( |\nabla u|^{2} \right) + \frac{1}{|\nabla u|} \Delta u \\
=& - \frac{1}{2|\nabla u|^{2}} \nu \left( g \left( \nabla u, \nabla u \right) \right) + \frac{1}{|\nabla u|} \Delta u \\
=& - \frac{1}{|\nabla u|^{2}} g \left( \nabla_{\nu} \nabla u, \nabla u \right) + \frac{1}{|\nabla u|} \Delta u \\
=& - \frac{1}{|\nabla u|} g \left( \nabla_{\nu} \nabla u, \nu \right) + \frac{1}{|\nabla u|} \Delta u \\
=& - \frac{1}{|\nabla u|} \operatorname{Hess}u \left( \nu, \nu \right) + \frac{1}{|\nabla u|} \Delta u \\
=& \frac{1}{|\nabla u|} \left( \Delta u - \operatorname{Hess}u \left( \nu, \nu \right) \right) \\
=& \frac{1}{|\nabla u|} \left( g^{ij} - \nu^{i}\nu^{j} \right) \operatorname{Hess}u \left( \partial x^{i}, \partial x^{j} \right) \\
\end{aligned}
$$



$$
\lim_{t \rightarrow \infty} \frac{t}{4}\left( 16 \pi - \int_{\Sigma_{t}} H^{2} d \Sigma_{t} \right) \le 8 \pi \mathfrak{m}_{ADM}
$$

