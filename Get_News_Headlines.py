import requests

API_KEY = "YOUR_API_KEY_HERE"  # Replace with your NewsAPI key

def get_sources(country, category):
    """Fetch available news sources for a given country and category."""
    url = f"https://newsapi.org/v2/top-headlines/sources?category={category}&country={country}&apiKey={API_KEY}"
    response = requests.get(url)
    return response.json().get("sources", [])

def get_articles(source_id):
    """Fetch top headlines from a specific source."""
    url = f"https://newsapi.org/v2/top-headlines?sources={source_id}&apiKey={API_KEY}"
    response = requests.get(url)
    return response.json().get("articles", [])

def main():
    # Step 1: Get user input
    country = input("Enter the country code (e.g., us, gb, in): ").strip().lower()
    category = input("Enter the category (business, entertainment, general, health, science, sports, technology): ").strip().lower()

    # Step 2: Fetch sources
    sources = get_sources(country, category)
    if not sources:
        print("No sources found for the given country and category.")
        return

    print("\n📌 Available Sources:")
    for idx, source in enumerate(sources, start=1):
        print(f"{idx}. {source.get('id')} - {source.get('name')}")

    # Step 3: Select source
    source_id = input("\nEnter the source ID: ").strip().lower()

    # Step 4: Fetch articles
    articles = get_articles(source_id)
    if not articles:
        print("No articles found for this source.")
        return

    print("\n📰 Top Articles:")
    for idx, article in enumerate(articles, start=1):
        print(f"\nArticle {idx}:")
        print(f"Author      : {article.get('author')}")
        print(f"Title       : {article.get('title')}")
        print(f"Description : {article.get('description')}")
        print(f"URL         : {article.get('url')}")
        print(f"Published At: {article.get('publishedAt')}")

if __name__ == "__main__":
    main()
    
    

