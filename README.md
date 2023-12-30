# domain-extractor

This is a relatively simple program to extract all domain names mentioned in a folder of text files.

## Usage

1. Install Python or a Python-supporting IDE if you don't have it already.
2. Collect texts you want to analyze, and save each one as a text file, using the *.txt* extension, and all in the same folder at the top level.
3. Download and/or copy/paste this program and save it in the same folder.
4. Run the program in your Python shell. The results will appear on your screen immediately.
6. For further information on the links, type `my_domain_counts` or `my_domains_by_popularity` into your Python shell after the output has finished printing.

NOTE: this program should be cross-platform, though I've only tested it on MacOS with IDLE so far.

## Why and how did I make this program?

As an avid user of Manifold Markets, I've been noticing that much of the website's spam (see [manifold.markets/admin/reports] for a full list) consists of user profiles with promotional text, often including a large number of links to the (presumed) owner's other accounts, and no activity. This made me wonder about what domains were used in these links the most. Hence this program was written!

This program was initially written with the help of **ChatGPT**, though some of it I wrote myself. I then linted it extensively using **pylint**.

## Extending this program

Please email me at [duckmaster0@protonmail.com]; I am happy to get personal emails. Alternatively, just fork my repo!
