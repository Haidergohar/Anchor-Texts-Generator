import csv
import random

# Define the input and output file paths
input_file = 'anchor_texts.csv'
output_file = 'anchor_texts.csv'

# Define the brand keywords and their proportions
brand_keywords = ["SGSC", "SGSC website", "Visit SGSC"]
brand_keyword_weights = [0.4, 0.35, 0.25]

# Define the generic keywords
generic_keywords = ["here", "this article", "click", "website", "read this", "more info", "learn more", "find out", "discover more", "view website", "check it out", "visit site", "read more", "click here", "go here", "click this", "read here", "visit this", "explore more", "navigate here", "click for more", "browse here", "check this out", "go to website", "go to article", "visit here", "see here", "click to read", "click to view", "click to visit", "go to page", "go to link", "click for details", "go to article", "go to website", "read full article", "read more here", "click to read more", "click to learn more", "click for more info", "click for details", "click for more information", "go to website", "visit website", "visit link", "see website", "explore website", "explore link", "view link", "view website", "find website", "find link", "find article", "navigate website", "navigate link", "navigate article", "access website", "access link", "access article", "proceed to website", "proceed to link", "proceed to article", "get more information", "get more details", "get full article", "get additional information", "get additional details", "get complete article", "get complete details", "get further information", "get further details", "get in-depth article", "get in-depth details", "learn more here", "learn more on this page", "learn more in this article", "discover more here", "discover more on this page", "discover more in this article", "find out more here", "find out more on this page", "find out more in this article", "read more here", "read more on this page", "read more in this article", "click here to read more", "click here for more information", "click here for more details", "click here for full article", "click here for complete details", "click here to learn more", "click here to find out more", "click here to discover more", "click here to read the full article", "click here to access the article", "click here to proceed to the article", "click here to get more information", "click here to get more details", "click here to get the complete article", "click here to get the full details", "click here to learn more on this page", "click here to discover more on this page", "click here to find out more on this page", "click here to read more on this page", "click here for additional information", "click here for additional details", "click here for further information", "click here for further details", "click here for in-depth article", "click here for in-depth details", "read more by clicking here", "learn more by clicking here", "discover more by clicking here", "find out more by clicking here", "get more information by clicking here", "get more details by clicking here", "get full article by clicking here", "get complete details by clicking here", "get further information by clicking here", "get further details by clicking here", "get in-depth article by clicking here", "get in-depth details by clicking here", "learn more by visiting website", "discover more by visiting website", "find out more by visiting website", "read more by visiting website", "get more information by visiting website", "get more details by visiting website", "get full article by visiting website", "get complete details by visiting website", "get further information by visiting website", "get further details by visiting website", "get in-depth article by visiting website", "get in-depth details by visiting website", "learn more by checking out the website", "discover more by checking out the website", "find out more by checking out the website", "read more by checking out the website", "get more information by checking out the website", "get more details by checking out the website", "get full article by checking out the website", "get complete details by checking out the website", "get further information by checking out the website", "get further details by checking out the website", "get in-depth article by checking out the website", "get in-depth details by checking out the website", "learn more by reading this article", "discover more by reading this article", "find out more by reading this article", "read more by reading this article", "get more information by reading this article", "get more details by reading this article", "get full article by reading this article", "get complete details by reading this article", "get further information by reading this article", "get further details by reading this article", "get in-depth article by reading this article", "get in-depth details by reading this article"]

# Read the data from the CSV file
data = []
with open(input_file, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Read the header
    for row in reader:
        data.append(row)

# Get lists of indices to replace
num_rows = len(data)
num_generic_replacements = min(200, num_rows)
num_url_replacements = min(150, num_rows)
num_sgsc_additions = min(100, num_rows)  # Assuming we add "SGSC" to 100 anchor texts
num_brand_replacements = min(100, num_rows)

# Ensure we do not exceed the total number of rows
total_replacements = min(num_generic_replacements + num_url_replacements + num_sgsc_additions + num_brand_replacements, num_rows)
print(total_replacements)
# Shuffle and select indices for each replacement type
indices = list(range(num_rows))
random.shuffle(indices)

#print(indices)

# Assign indices for each replacement type
generic_replacement_indices = indices[:num_generic_replacements]
url_replacement_indices = indices[num_generic_replacements:num_generic_replacements + num_url_replacements]
sgsc_addition_indices = indices[num_generic_replacements + num_url_replacements:num_generic_replacements + num_url_replacements + num_sgsc_additions]
brand_replacement_indices = indices[num_generic_replacements + num_url_replacements + num_sgsc_additions:total_replacements]

# print("Generic Indices")
# print(generic_replacement_indices)
# print("URL Indices")
# print(url_replacement_indices)
# print("SGSC Addition Indices")
# print(sgsc_addition_indices)
# print("Brand Indices")
# print(brand_replacement_indices)

# Replace the selected anchor texts with generic keywords
i = 1
for index in generic_replacement_indices:
    new_anchor_text = random.choice(generic_keywords)
    data[index][0] = new_anchor_text
    i += 1
print("Starting Printing...")
print(str(i) + " [" + str(index) +"]")

j = 1
# Add "SGSC" to some anchor texts
for index in sgsc_addition_indices:
    data[index][0] = f"{data[index][0]} SGSC"
    j += 1
print(str(j) + " [" + str(index) +"]")


l = 1
# Replace the selected anchor texts with brand keywords based on the specified proportions
for index in brand_replacement_indices:
    new_anchor_text = random.choices(brand_keywords, brand_keyword_weights)[0]
    data[index][0] = new_anchor_text
    l +=1
print(str(l) + " [" + str(index) +"]")

m = 1
# Replace the selected anchor texts with naked URLs
for index in url_replacement_indices:
    naked_url = data[index][1]
    data[index][0] = naked_url
    m += 1
print(str(m) + " [" + str(index) +"]")



k = 1
# Write the modified data back to a CSV file
with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)  # Write the header
    writer.writerows(data)  # Write the modified data
    k += 1
print(str(k) + " [" + str(index) +"]")

print(f"Data has been modified and saved to {output_file}.")

