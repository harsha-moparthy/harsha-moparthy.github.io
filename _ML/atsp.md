---
title: "Travelling Salesman Problem"
excerpt: "Tackling TSP using machine learning techniques<br/><img src='/images/heatmap.png'>"
collection: ML
---

## Description
The travelling salesman problem, also known as the travelling salesperson problem (TSP), asks the following question: "Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?" It is an NP-hard problem in combinatorial optimization, important in theoretical computer science and operations research. A recent [2024] blog post was written on survey of TSP [here](http://localhost:4000/posts/2012/08/blog-post-4/)

## Research Overview
In particular, recent advances in graph neural network techniques [Bruna et al., 2013, Defferrard
et al., 2016, Sukhbaatar et al., 2016, Kipf and Welling, 2016, Hamilton et al., 2017] are a good fit for
the task because they naturally operate on the graph structure of these problems. 

Recently proposed deep learning approaches for the 2D Euclidean TSP combine graph neural
networks with autoregressive decoding to output TSP tours one node at a time using the sequence-tosequence framework [Vinyals et al., 2015, Bello et al., 2016] or an attention mechanism [Deudon
et al., 2018, Kool et al., 2019]

## Approach-1
Started with implementing this paper "An Effecient Graph Convolutional Network Technique for TSP" by Joshi et al.
<iframe src="https://nbviewer.org/github/harsha-moparthy/TSP/blob/main/Approach-1.ipynb" width="150%" height="600px">
</iframe>

