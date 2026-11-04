from bs4 import BeautifulSoup # beautiful soup for parsing CU courses
import requests 
import re # Regex 
import json # Create json file 


URL = "https://calendar.carleton.ca/undergrad/courses/SYSC/"


def get_course_page():
    response = requests.get(URL)
    if response.status_code != 200:
        print(f"Failed to fetch page: {response.status_code}")
        return None
    
    return BeautifulSoup(response.text, 'html.parser')


def parse_course_data(soup):
    
    course_blocks = soup.find_all('div', class_="courseblock")
    
    courses_list = []   # init a list for the json
    
    for block in course_blocks:
        
        code = None
        credit = None
        title = None
        raw_prereq = None
                
        course_title = block.select_one('span.courseblocktitle')
        
        if course_title:
            title_text = course_title.get_text(separator=" ", strip=True).replace("\xa0", " ")
            
            elements = [element.strip() for element in re.split(r'\[|\]', title_text) if element.strip()]    
            
            if len(elements) >= 3:
                code = elements[0]
                credit = elements[1]
                title = elements[2]
            
        course_prereq = block.select_one('div.coursedescadditional')
                
        if course_prereq:  
            
            prereq_desc = course_prereq.get_text(separator=" ", strip=True).replace("\xa0", " ")
                        
            match = re.search(r"Prerequisite\(s\):\s*(.*?)(?=\b(?:Lectures|Laboratory|Precludes|Also listed)\b|$)", prereq_desc) 
            
            # For React DAG, we need to get all the prerequisites in a cleaner list for the nodes 
            
            #TODO: We'll use Regex to find the 'XXXX ####' pattern all course codes have and find them in the raw_prereq test.
            
            
            if match:
                raw_prereq = match.group(1).strip()
                
        # Check if the raw_prereq has string in it
        
        if raw_prereq:
            prereq_parsed = re.findall(r"([A-Z]{4}\s*\d{4})", raw_prereq)
    
        courses_dict = {
                    
                "code": code,
                "credit": credit,
                "title": title,
                "raw_prerequisites": raw_prereq,
                "prerequisites" : prereq_parsed  # This will be our clean list for React DAG
                    
            }
        
        courses_list.append(courses_dict)
    
    
    
    with open("course_parse.json", mode="w", encoding="utf-8") as file:
        json.dump(courses_list, file, indent = 3)
  
        
if __name__ == "__main__":
  soup = get_course_page()
  if soup:
    print("Successfully fetched Carleton COMP page!")
    parse_course_data(soup)