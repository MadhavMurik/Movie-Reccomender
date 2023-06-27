import random
import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"


def main():
    response = requests.get(url)
    html = response.text
    
    soup = BeautifulSoup(html, 'html.parser')
    movietags = soup.select('td.titleColumn')
    inner_movietags = soup.select('td.titleColumn a')
    rating_tags = soup.select('td.posterColumn span[name=ir]')
    
    
    innermovietag0 = inner_movietags[0]
    
    # moviesplit = movietag0.text.split()
    
    def get_year(movietag):
        moviesplit = movietag.text.split()
        year = moviesplit[-1]
        return year
    
    years = [get_year(tag) for tag in movietags]
    actors = [tag['title'] for tag in inner_movietags]
    titles = [tag.text for tag in inner_movietags]
    ratings = [float(tag['data-value'] )for tag in rating_tags]
    
    numMovs = len(titles)
    
    while(True):
        indx = random.randrange(0,numMovs)
            
        print(f'{titles[indx]} - {years[indx]}, Rating: {ratings[indx]}, Starring: {actors[indx]}') 
            
        userIn = input('Do you want another suggestion? (Y / N)')
        if userIn != 'Y' :
            break
            

    

if __name__ == '__main__':
    main() 