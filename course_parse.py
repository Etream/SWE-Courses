from bs4 import BeautifulSoup # beautiful soup for parsing CU courses
import requests 
import re # Regex 

# First: need to get the URL for soft eng related courses

URL = "https://calendar.carleton.ca/undergrad/courses/SYSC/"

# Need to be able to get to the URL and tell the user if it fails

def get_course_page():
    response = requests.get(URL)
    if response.status_code != 200:
        print(f"Failed to fetch page: {response.status_code}")
        return None
    
    return BeautifulSoup(response.text, 'html.parser')

#TODO: Clean up code b/c it handles two separate loops


def parse_course_data(soup):
    # Get the courseblock containers
    
    course_blocks = soup.find_all('div', class_="courseblock")
    
    for block in course_blocks:
        
        # titles and title elements for each iteration of courseblocks
        
        course_title = block.select_one('span.courseblocktitle')
        
        
        if course_title:
            title_text = course_title.get_text(separator=" ", strip=True).replace("\xa0", " ")
            print(f"\n----- {title_text} -----")
        
        # Clean up the description of the prerequisites for each iteration
                
        course_prereq = block.select_one('div.coursedescadditional')
                
        if course_prereq:  #Switching to Regex instead of index, because text is getting cutoff when new line
            prereq_desc = course_prereq.get_text(separator=" ", strip=True)
            
            # Use Regex to find "Prerequisite(s):" and get every text after until next keyword
            
            match = re.search(r"Prerequisite\(s\):\s*(.*?)(?=\b(?:Lectures|Laboratory|Precludes|Also listed)\b|$)", prereq_desc) 
            
            if match:
                print(f"Prerequisite(s): {match.group(1).strip()}")
            
            
        
            

if __name__ == "__main__":
  soup = get_course_page()
  if soup:
    print("Successfully fetched Carleton COMP page!")
    parse_course_data(soup)