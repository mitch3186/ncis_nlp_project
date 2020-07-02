from bs4 import BeautifulSoup
import requests
import pandas as pd

url_list = ['https://subslikescript.com/series/NCIS-364845','https://subslikescript.com/series/The_Shield-286486',
'https://subslikescript.com/series/Bosch-3502248']

def make_ep_list (url):
	ep_list = []

	url1 = url 
	respond = requests.get(url1)
	titles = respond.text
	soup = BeautifulSoup(titles, "html.parser")
	titles_list = soup.find('div',class_='series_seasons').find_all('a')
	for link in soup.find_all('a'):
		ep_list.append(link.get('href'))
	
    
    for i, num in enumerate(ep_list):
    	for url in url_list:
    		ep_list[i] = num.replace(url,'')
    ep_list = ep_list [5:]
	return ep_list




def script_data(show, ep_list):
    script_df = []
    url = 'https://subslikescript.com/series/{}'
    
    for ep in ep_list:
        ep_title = ep
        response = requests.get(url.format(ep))
        page = response.text
        soup = BeautifulSoup(page, 'lxml')
        
        scripts = [{
                    'ep_id': show + ep_title,
                    'dialogue':soup.find(class_='full-script')
                   }]
            
                
        script_df.extend(scripts)
     
    df =  pd.DataFrame(script_df)
    df = df[['ep_id', 'dialogue']]
    df = df[:-1]
    
    return df
