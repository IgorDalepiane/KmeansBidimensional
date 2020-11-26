# KmeansBidimensional
This code is the application of the knowledge acquired during the Machine Learning class at Unipampa University, with professor Marcelo Resende Thielo.

In this code I am using python 3 for execution.

To run it with the current dataset, just type the command below in your terminal.

```
py kmeans.py
```

It will show you the clusters with their respective centers, like the image below:

![PlottedResults](https://user-images.githubusercontent.com/9628068/100392138-58aacd80-3014-11eb-9d71-a9c245b31783.png)

And to see which elements belong to which cluster, it is necessary to use gnuplot.

```
gnuplot> plot "clusters/0.dat","clusters/1.dat","clusters/2.dat","clusters/3.dat","clusters/4.dat","clusters/5.dat"
```

And the result will be this:

![GnuplotResults](https://user-images.githubusercontent.com/9628068/100392159-6b250700-3014-11eb-95c9-cd8a7febabf9.png)

:)
