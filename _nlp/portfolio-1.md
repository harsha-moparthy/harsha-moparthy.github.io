---
title: "Sentiment Analysis"
excerpt: "Sentiment Analysis on Movie Reviews<br/><img src='https://getthematic.com/assets/img/sentiment-analysis/fine-grained.png' width='500' height='300'>"
collection: nlp
---

## Problem Statement
The Rotten Tomatoes movie review dataset is a corpus of movie reviews used for sentiment analysis, originally collected by Pang and Lee. In their work on sentiment treebanks, Socher et al used Amazon's Mechanical Turk to create fine-grained labels for all parsed phrases in the corpus. This project presents employs sentiment-analysis ideas on the Rotten Tomatoes dataset. Label phrases on a scale of five values: negative, somewhat negative, neutral, somewhat positive, positive. Obstacles like sentence negation, sarcasm, terseness, language ambiguity, and many others make this task very challenging.

## Approach-1
Used state of the art models i.e transformer models in sentiment analysis. Used English-Language Sentiment Classification model SiEBERT(https://huggingface.co/siebert/sentiment-roberta-large-english) which is finetuned on RoBERTa-large for predicting binary sentiments.. Employed transfer learning and trained model on five classes with AdamW as optimizer. Achieved a accuracy of 0.69842 by training on only 3 epochs.Second one being twitter-roberta-base from hugging face. Achieved a accuracy of 0.70551.

## Approach-2
Traditional Naive Bayes model 

