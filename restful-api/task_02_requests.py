import requests
import csv
import json

def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder and prints post titles.
    """

    url = "https://jsonplaceholder.typicode.com/posts"
    
    #requests get
    response = requests.get(url)
    #print status
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        
        for post in posts:
            print(f"{post['title']}")
    else:
        print("Failed to fetch posts.")

def fetch_and_save_posts():
        """
        """
        url = "https://jsonplaceholder.typicode.com/posts"
        
        #request get 
        response = requests.get(url)
        
        if response.status_code == 200:
            """
            
            """
            #convert input to json
            posts = response.json()
            
            # Structure data into list of dictionaries
            formatted_posts = []
            for post in posts:
                formatted_posts.append({
                    "id": post["id"],
                    "title": post["title"],
                    "body": post["body"]
                })
                
            # Write data to CSV file
            with open("posts.csv", "w", newline="") as csvfile:
                fieldnames = ["id", "title", "body"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(formatted_posts)