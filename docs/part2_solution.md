# Part 2: Web Scraping and Summarization Improvement

Problem
----------------------------------------------------------------

The scraper fails when processing complex websites or long content because:

The webpage contains too much unnecessary information (HTML tags, ads, menus).
Long content may exceed the AI model's input limit.


Solution
----------------------------------------------------------------

I will improve the scraper by:

1. Extracting only important content from the webpage.
2. Splitting long content into smaller parts before summarizing.
3. Adding a guardrail to ensure the final summary is short and relevant.


Example flow:
----------------------------------------------------------------

Website
   |
   v
Web Scraper
   |
   v
Clean Content
   |
   v
AI Summarizer
   |
   v
Guardrail Check
   |
   v
Final Summary
  Guardrail

The guardrail will check:

1. Summary length (maximum words)
2. Remove unnecessary information
3. Ensure the summary stays relevant to the source

Example:

def summary_guardrail(summary):
    words = summary.split()

    if len(words) > 200:
        return " ".join(words[:200])

    return summary