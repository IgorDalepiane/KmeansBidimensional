# KmeansBidimensional
This code is the application of the knowledge acquired during the Machine Learning class at Unipampa University, with professor Marcelo Resende Thielo.

In this code I am using python 3 for execution.

To run it with the current dataset, just type the command below in your terminal.

```
py kmeans.py
```

It will show you the clusters with their respective centers, like the image below:

![alt text](https://media.discordapp.net/attachments/761743510197895199/781589449888235540/unknown.png" Plotted results")

And to see which elements belong to which cluster, it is necessary to use gnuplot.

```
gnuplot> plot "clusters/0.dat","clusters/1.dat","clusters/2.dat","clusters/3.dat","clusters/4.dat","clusters/5.dat"
```

And the result will be this:

![alt text](https://media.discordapp.net/attachments/761743510197895199/781589491713572925/unknown.png" Gnuplot results")

:)
