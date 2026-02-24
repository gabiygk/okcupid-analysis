# Performing Gender in the Digital Marketplace: A Computational Analysis of OkCupid Profiles

A micro research project exploring how men and women present themselves differently on dating apps, and what these differences reveal about contemporary norms of masculinity and femininity.

## Overview

This project analyzes the [OkCupid 60k Profiles dataset](https://www.kaggle.com/datasets/andrewmvd/okcupid-profiles) using Python-based NLP and machine learning to study gendered self-presentation in digital dating culture. The focus is a specific microculture: young, highly educated, mostly straight urban professionals in the Bay Area (~95% Bay Area, ~70% under 35, ~66% college-educated or higher).

Rather than asking what gender norms look like in general, this project asks: **how do gender norms operate among people who consider themselves progressive and tech-oriented — and who imagine themselves as resisting traditional stereotypes?**

## Research Question

> How do self-descriptions on OkCupid profiles differ by gender, and what do these patterns reveal about norms of masculinity versus femininity in contemporary digital dating culture?

## Methods

- **Text preprocessing** — tokenization, lemmatization, stopword removal, standardization by gender
- **Word frequency analysis** — most common terms among men vs. women
- **Gender-predictive vocabulary** — identifying words strongly associated with each gender
- **Topic modeling** — discovering thematic clusters (e.g., "status," "warmth," "lifestyle")
- **Sentiment & emotion analysis** — comparing emotional tone and expressiveness across genders
- **Logistic regression classifier** — predicts whether a sentence is "male-coded" or "female-coded"
- **Cross-tabulations** — gender vs. body type, reproductive intentions, and other profile metadata

## Key Findings

- Men's profiles cluster around competence, autonomy, and activity (e.g., *software, engineer, motorcycle, guitar*)
- Women's profiles cluster around relationality, warmth, and emotional expressiveness (e.g., *love, family, dancing, yoga*)
- Women averaged **6.5 emotional words per profile** vs. **4.1 for men**
- The gender classifier predicts gender from single, mundane sentences with high accuracy — revealing how deeply scripted and predictable gendered self-presentation is

## Theoretical Framework

- **Judith Butler** — gender as repeated performative act (*Gender Trouble*)
- **Eva Illouz** — online dating as a romantic marketplace where identity is "branded" (*Why Love Hurts*, 2012)
- **Ferrara & Vergarra** — emotional norms of masculinity and the feminization of emotional labor ("The Male Friendship Recession")
- **Davis & Mitchell** — heterosexuality as a historically constructed system of norms (*Heterosexual Histories*)

## Video Presentation

Watch the full project walkthrough and live demo of the gender classifier:

[![Project Video](https://img.youtube.com/vi/qQy7Qh_Sb4c/0.jpg)](https://youtu.be/qQy7Qh_Sb4c)

## Data

Primary source: [OkCupid 60k Profiles](https://www.kaggle.com/datasets/andrewmvd/okcupid-profiles) (publicly available on Kaggle)
