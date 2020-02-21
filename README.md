# Image Search Python Package

[![Build Status](https://travis-ci.org/misaelbg/image_search.svg?branch=master)](https://travis-ci.org/misaelbg/image_search)

A simple python package for saving images from Bing and Google without using API keys. This package utilizes web browsers to help scrape images found on web searches. 

This should only be used for educational and personal purposes only. I am not responsible for any issues that may arise by scraping such sources. All images are copyrighted and owned by their respective owners, I do not claim any ownership.

Ensure you have the [appropriate version](https://sites.google.com/a/chromium.org/chromedriver/downloads) of ChromeDriver on your machine if you would like to scrape from Google Images.

## Usage

	usage: image_search [-h] [--limit LIMIT] [--json] [--url URL]
                    [--adult-filter-off]
                    engine query

**Example:** Google Images

	image_search google cat --limit 10 --json

This will download 10 cat images and metadata from Google Images.

**Example:** Bing Images

	image_search bing dog --limit 10 --json
