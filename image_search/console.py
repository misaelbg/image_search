from . import Bing, Google
import argparse

def main():
    parser = argparse.ArgumentParser(
    description="Scrape images from the internet.")
    parser.add_argument(
        "engine", help="Which search engine should be used? (Bing/Google)")
    parser.add_argument(
        "query", help="Query that should be used to scrape images.")
    parser.add_argument(
        "--limit", help="Amount of images to be scraped.", default=1000, required=False)
    parser.add_argument("--json", help="Should image metadata be downloaded?",
                        action='store_true', required=False)
    parser.add_argument(
        "--url", help="Google: Scrape images from a google image search link", required=False)  # Google Specific
    parser.add_argument("--adult-filter", help="Disable adult filter",
                        action='store_true', required=False)  # Bing Specific
    args = parser.parse_args()

    if str(args.engine).lower() == 'google':
        search_engine = Google.Engine()
    elif str(args.engine).lower() == 'bing':
        search_engine = Bing.Engine()
    
    results = search_engine.search_images(
        query=args.query, delta=int(args.limit), adult_content=args.adult_filter)

if __name__=="__main__":
    main()