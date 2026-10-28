from bs4 import BeautifulSoup # beautiful soup for parsing CU courses
import requests # later for our URL

# First: need to get the URL for soft eng related courses

URL = "https://calendar.carleton.ca/undergrad/courses/SYSC/"

# Need to be able to get to the URL and tell the user if it fails

def get_course_page():
    response = requests.get(URL)
    if response.status_code != 200:
        print(f"Failed to fetch page: {response.status_code}")
        return None
    
    return BeautifulSoup(response.text, 'html.parser')

def parse_courses(soup):
  # TODO: You need to inspect the HTML structure of Carleton's calendar
  # and find how individual courses and their prerequisites are wrapped.
  # Hint: Look for divs, blocks, or class names containing course details.
  
  # Find all nested elements across the page
  course_titles = soup.select('div.courseblock span.courseblocktitle')
  
  
  for title in course_titles:
    print(title.text)

def parse_prereq(soup):
    
    course_prereq = soup.find_all('div', class_="courseblock")
    
    for prereq in course_prereq:
        
        course_block = prereq.select_one('div.coursedescadditional')
        
        if course_block:
            for line in course_block.get_text(separator="\n").splitlines():
                if line.strip().startswith("Prerequisite(s):"):
                    print(line.strip())
            

if __name__ == "__main__":
  soup = get_course_page()
  if soup:
    print("Successfully fetched Carleton COMP page!")
    #parse_courses(soup)
    parse_prereq(soup)