# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site
# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')
slide_elem.find('div', class_='content_title')

# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'

# ### Mars Facts
df = pd.read_html('https://galaxyfacts-mars.com')[0]

df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)

df.to_html()

browser.quit()



# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.item', wait_time=1)

# 2. Create a list to hold the images and titles.
html = browser.html
sphere_soup = soup(html, 'html.parser')
spears_soup = sphere_soup.findAll('div', class_='item')

# 3. Write code to retrieve the image urls and titles for each hemisphere.
hemisphere_image_urls = []
#hemisphere_image_urls.columns=['img_url', 'title']
for item in spears_soup:
    sphere_title = item.find('h3').get_text()    
    sphere_image_name = item.find('img', class_='thumb').get('src')
    sphere_img_url = f'https://marshemispheres.com/{sphere_image_name}'    
    hemisphere_image_urls.append({'img_url':sphere_img_url, 'title':sphere_title})    


# 4. Print the list that holds the dictionary of each image url and title.
# hemisphere_image_urls

# 5. Quit the browser
browser.quit()

