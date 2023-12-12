"""
Author:     Blake McBride (blakepm2@illinois.edu)
Created:    12/12/2023

Overview:   This file contains a script to open sampled webpages for demoing Historian
"""

# import standard modules
import webbrowser

# create list of sample webpages from a variety of topics
sampleWebpages = [
    
    # computer science webpages
    "https://joinhandshake.com/blog/students/top-10-jobs-for-computer-science-majors/",
    "https://www.zdnet.com/education/computers-tech/best-careers-with-computer-science-degree/",
    "https://undergrad.cs.umd.edu/what-computer-science",
    
    # software engineering webpages
    "https://www.forbes.com/advisor/education/become-software-engineer/",
    "https://www.mtu.edu/cs/undergraduate/software/what/",
    "https://www.cnbc.com/2019/06/14/how-much-google-facebook-other-tech-giants-pay-software-engineers.html",
    
    # basketball webpages
    "https://www.britannica.com/list/the-10-greatest-basketball-players-of-all-time",
    "https://www.breakthroughbasketball.com/basics/basics.html",
    
    # recipes webpages
    "https://www.allrecipes.com/recipe/12682/apple-pie-by-grandma-ople/",
    "https://www.recipetineats.com/chicken-sharwama-middle-eastern/"
    
    
]

if __name__ == '__main__':
    
    # open all of the sample webpages in the browser
    for webpage in sampleWebpages:
        webbrowser.open(webpage)