This code sequence is written to generate thousands of anchor text for your website URLs for the purpose to use in backlinks.

The file sequence to execute is as follow:

1. python_anchor_text_generator.py
2. python_anchor_text_generator.py


------------------------------------------------------------------------------------------------------------------------------------

1. python_anchor_text_generator.py

In this file we need to provide urls of our website and anchor texts arrays and provide the number of anchor texts list we want to generate.

We can generate the achor texts by this chatgpt prompt:

"""Im providing you the list of my website's URLs. Pick their article topic after ending the main domain and generate the anchor text for their backlinks. Suppose the URL is "https://sassagrantstatuscheck.co.za/sassa-status-check-failed/", here the topic is "sassa-status-check-failed". You need to generate an array in format like:

"topic": ["keyword1", :keyword2"], etc..

each topic array should have 20 anchor texts, it should include main targeted keywords, LSI keywords and also include single word keywords and some natural looking anchr texts. The format should be array like "topic": ["keyword 1", "keyword 2"], and there should not be line break in array, should be in single line.

The URLs are following:
[Provide list of URLs Here..]"""

------------------------------------------------------------------------------------------------------------------------------------

2. python_anchor_text_generator.py
In this file we need to add our brand keywords. It will do the following:

200 anchor texts are replaced with keywords from the generic_keywords array.
150 anchor texts are replaced with their corresponding naked URLs.
"SGSC" is added to 100 anchor texts that are not naked URLs.
100 anchor texts are replaced with the brand keywords ("SGSC", "SGSC website", "Visit SGSC") in the specified proportions.

We can control the numbers of each type of links from variables and functions
