import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_topic_titles(parsed_doc):
    selection_title_class= 'f3 lh-condensed mb-0 mt-1 Link--primary' #Class containing topic names
    topic_title_p_tags= parsed_doc.find_all('p',class_=selection_title_class)
    topic_titles=[]; #We are creating a list which will store only the name of the topics excluding the unnecessary information
    for tag in topic_title_p_tags:
        topic_titles.append(tag.text)
    return topic_titles

def get_topic_description(parsed_doc):
    selection_title_description_class= 'f5 color-fg-muted mb-0 mt-1' #Class containing topic description
    topic_title_description_p_tags= parsed_doc.find_all('p',class_=selection_title_description_class)
    topic_description=[]; #We are creating a list which will store only the description of the topics excluding the unnecessary information
    for description in topic_title_description_p_tags:
        topic_description.append(description.text.strip())
    return topic_description

def get_topic_url(parsed_doc):
    topic_link_class= 'no-underline flex-1 d-flex flex-column' #So the class containing topic and its description was in a 'p_tag' and they further are under a 'a_tag' which contains the 'href' which contains the topic links so that we can further navigate inside a topic page and view it in detail
    topic_link_class_a_tags= parsed_doc.find_all('a',class_=topic_link_class)
    topic_links=[]; #We are creating a list which will store only the links of the topics excluding the unnecessary information
    base_url= 'https://github.com'
    for link in topic_link_class_a_tags:
        topic_links.append(base_url + link['href'])
    return topic_links

def main_scrape_topics():
    topics_url= 'https://github.com/topics'  # Link from where we are going to scrape information
    response= requests.get(topics_url)       # Downloading the url whom we are going to scrape
#print(response.status_code) #Checking the status code of our response to see whether it successfully
                            #responded. If status code is from 200-299 then its successful.
    page_contents= response.text  # Instead of using "print(len(response.text))" to print entire page content print upto a specific limit by declaring a varialbe 
#print(page_contents[:1000]) 
    with open('GitWebpage.html', 'w', encoding='utf-8') as f:
        f.write(page_contents)     # Saving the page content to a file with utf-8 encoding
    parsed_doc= BeautifulSoup(page_contents,'html.parser') #Parseing in case of web means extracting the exact and specific information from a web page which is required by someone
#print(parsed_doc)
    topics_dict={
        'Titles': get_topic_titles(parsed_doc),
        'Description': get_topic_description(parsed_doc),
        'Topic Links': get_topic_url(parsed_doc)
    }
    return pd.DataFrame(topics_dict)

#print(main_scrape_topics())
#Now we want to get information of the repositories for each topic

def get_topic_page(topic_links):
    #Now our Task is to Get infromation from inside of a particular topic page
    response=requests.get(topic_links)
    topics_doc= BeautifulSoup(response.text,'html.parser')
    return topics_doc

def repo_stars_integer(stars_str):
    stars_str= stars_str.strip()
    if stars_str[-1] == 'k':
        #stars_str[:-1]# This will give 101 instead of 101k
        return int(float(stars_str[:-1]))*1000 #It will give us 101000 as output
    return int(stars_str) #If string dont have k in its end then simply convert str into int and return it.

def get_repository_information(repository_tag,repository_stars):
    a_tags= repository_tag.find_all('a')
    username= a_tags[0].text.strip()
    repo_name= a_tags[1].text.strip()
    repo_url= 'https://github.com' + a_tags[1]['href']
    repo_stars= repo_stars_integer(repository_stars.text)
    return username,repo_name,repo_stars,repo_url

def get_topics_repository(topics_doc):
    
    #We first tried to find all the usernames of a topic repository which were under a-tag but unfortunately they werent in a class so we went to the parent of a tag which was h3 tag and it did had a class and it have both username and repository name so we used it
    repository_tag= topics_doc.find_all('h3',class_='f3 color-fg-muted text-normal lh-condensed')
    repository_stars= topics_doc.find_all('span',class_='Counter js-social-count')

    topics_repository_dict={'Username': [],'Repository Name': [],'Stars': [],'Repository Link': []}

    for i in range(len(repository_tag)):
        repository_info=get_repository_information(repository_tag[i],repository_stars[i])
        topics_repository_dict['Username'].append(repository_info[0])
        topics_repository_dict['Repository Name'].append(repository_info[1])
        topics_repository_dict['Stars'].append(repository_info[2])
        topics_repository_dict['Repository Link'].append(repository_info[3])

    return pd.DataFrame(topics_repository_dict)

def scrape_single_topic(topic_link, topic_name):
    topic_page = get_topic_page(topic_link)
    topic_df = get_topics_repository(topic_page)
    topic_df.to_csv(f'{topic_name}.csv', index=None)

def scrape_topic_repos():
    topic_df = main_scrape_topics()
    for index, row in topic_df.iterrows():
        scrape_single_topic(row['Topic Links'], row['Titles'])

scrape_topic_repos()   