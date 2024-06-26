import requests
import csv

def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder and prints post titles.
    """

    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()

    for post in posts:
      print(f"{post['title']}")

def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder and saves them to a CSV file.
    """

    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    if response.status_code == 200:
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