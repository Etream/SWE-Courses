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
        
        # Default values for keys if smth is missing
        code = None
        credit = None
        title = None
        raw_prereq = None
                
        course_title = block.select_one('span.courseblocktitle')
        
        if course_title:
            title_text = course_title.get_text(separator=" ", strip=True).replace("\xa0", " ")
            
            elements = [element.strip() for element in re.split(r'\[|\]', title_text) if element.strip()]    # Using Regex, split() and strip() to split the course title
            
            # Since there might not be mathcing prereqs, NameError and others can occur, fix
            
            # Check the length
            if len(elements) >= 3:
                code = elements[0]
                credit = elements[1]
                title = elements[2]
            
        
                
        course_prereq = block.select_one('div.coursedescadditional')
                
        if course_prereq:  
            
            prereq_desc = course_prereq.get_text(separator=" ", strip=True).replace("\xa0", " ")
                        
            match = re.search(r"Prerequisite\(s\):\s*(.*?)(?=\b(?:Lectures|Laboratory|Precludes|Also listed)\b|$)", prereq_desc) 
            
            # Now use match.group(1) for value of key "raw_prerequisites"
            if match:
                raw_prereq = match.group(1).strip()
    
        courses_dict = {   # put the course elements into dict, elements index match with the split text; match for raw prereq
                    
                "code": code,
                "credit": credit,
                "title": title,
                "raw_prerequisites": raw_prereq
                    
            }
        
        courses_list.append(courses_dict)
        
    course_json = json.dumps(courses_list)  #convert to json
    
    print(course_json)

        
        
if __name__ == "__main__":
  soup = get_course_page()
  if soup:
    print("Successfully fetched Carleton COMP page!")
    parse_course_data(soup)