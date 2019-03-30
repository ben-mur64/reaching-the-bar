# Reaching the Bar - Law School Analyzation Tool

## General Project Overview

This project was created for the yHack 2019. It blends various elements of data analysis and gui programming.
The goal is to have a simple yet stylish app that allows people to put in their own preferences as to what they are looking for in a law school. It then takes these preferences, gets data from Law School Transparency, and runs the data through an algorithm, then gives them a report on which law schools they should shoot for based on their own preferences and LSAT score.

### Step by Step Breakdown

* Prompts the user to rank their preferences on various characteristics of a law school.
* Uses these preferences combined with an algorithm to generate scores for each law school.
* Takes the scores of the law schools and graphs them relative to the 75th percentile LSAT.
* Asks for the user's LSAT score and gives them the top six scoring law schools that they have a chance to be accepted into.

## Specific Pieces

* Web Scraper
* Graphing Engine
* Web Front End/GUI Front End

## To-Do List

* Divvy up tasks, who's going to work on what:
  * Ben - Web Crawler, General Architecture, Algorithm?
  * Neal - Algorithm, Design, Look and Feel
  * Corbin - Front End?, Algorithm? Graphing?

## Decisions Made

* We're using a web interface.
* Corbin can write the front end in Javascript.
* I'm writing the back end in Python.