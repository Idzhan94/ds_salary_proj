# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 14:04:06 2021

@author: idzha
"""

import glassdoor_scraper as gs
import pandas as pd

path = "C:/Users/idzha/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist',1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)

