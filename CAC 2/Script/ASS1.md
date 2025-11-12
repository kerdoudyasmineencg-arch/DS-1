<img src="yasmine_kerdoud.ipynb" style="height:464px;margin-right:432px"/>
YASMINE KERDOUD 
CAC 2
22005999
Bank Marketing : Donated on 2/13/2012
Dataset Description: Bank Marketing
Description of the Chosen Dataset: Bank Marketing

The dataset I selected is called Bank Marketing, originally donated on February 13, 2012. It contains data related to direct marketing campaigns conducted by a Portuguese banking institution. These campaigns were carried out through phone calls, and the main goal of the analysis is to predict whether a client will subscribe to a term deposit (the target variable “y”, which can be “yes” or “no”).

In these marketing campaigns, more than one contact with the same client was often necessary to determine if they would eventually subscribe to the bank’s product.

There are four versions of the dataset available:

bank-additional-full.csv – Contains all 41,188 records with 20 input variables, ordered chronologically from May 2008 to November 2010.

bank-additional.csv – A 10% random sample of the full dataset, with 4,119 observations and the same 20 input variables.

bank-full.csv – Another complete version but with 17 input variables (an older version of the dataset).

bank.csv – A 10% random sample of the “bank-full” dataset, also with 17 inputs.

The smaller datasets were created to allow researchers to test computationally demanding algorithms, such as Support Vector Machines (SVMs), more efficiently.

Main Objective

The main purpose of this dataset is to classify whether or not a client will subscribe to a term deposit based on socio-economic, demographic, and campaign-related variables.

Dataset Metadata Overview

Domain: Business / Banking

Task Type: Classification

Number of Instances: 41,188 (for the full version)

Number of Features: 20

Target Variable: y (subscription to a term deposit: yes/no)

Data Characteristics: Multivariate, sequential, real-world data

Time Period: May 2008 – November 2010

Country: Portugal

Data Source: UCI Machine Learning Repository

Repository Link: https://archive.ics.uci.edu/ml/datasets/Bank+Marketing

Context and Purpose

This dataset was created to analyze the effectiveness of direct marketing campaigns and to help banks improve their customer targeting strategies. By applying machine learning models, it is possible to identify the profiles of clients who are more likely to subscribe to a term deposit, thus making marketing efforts more efficient.

<img src="télécharger.png" style="height:464px;margin-right:432px"/>
This histogram shows the age distribution of clients, separated by their subscription status.
Most clients in the dataset are between 30 and 40 years old, with a visible peak around age 32–35.
Clients who did not subscribe (blue line) dominate across all age ranges, but those who did subscribe (orange line) show a slightly higher relative frequency among older clients, particularly between 40 and 60 years old.

This trend may indicate that middle-aged clients are more likely to subscribe to a term deposit, possibly because they are in a more stable financial situation and more interested in secure investment products compared to younger clients.

<img src="télécharger (2).png" style="height:464px;margin-right:432px"/>
This chart presents the distribution of the variable pdays, which represents the number of days since a client was last contacted from a previous campaign (excluding those who were never contacted, indicated by -1).

We can see that for clients who did not subscribe (blue line), pdays are more widely spread and concentrated around certain peaks, especially between 100 and 400 days.
For those who did subscribe (orange line), the frequency is generally lower but more concentrated toward smaller pdays values, indicating that clients who were contacted more recently in previous campaigns were more likely to subscribe.

This suggests that recency of contact plays an important role in the success of marketing efforts — the more recently a client was reached, the higher the chance of subscription.

<img src="télécharger (3).png" style="height:464px;margin-right:432px"/>
This chart shows the proportion of clients who subscribed to a term deposit, grouped by marital status (divorced, married, single).
We can observe that in all three categories, the majority of clients did not subscribe (blue part), while only a small fraction did subscribe (orange part).
However, the subscription rate appears slightly higher among single clients, compared to married and divorced ones.
This may suggest that younger or single individuals could be more open to financial products like term deposits, possibly due to fewer family-related financial commitments or higher flexibility in savings decisions.

