"""
A program to extract domains mentioned in text files

Free software under the MIT license
NOTE: some of this code was drafted using ChatGPT

(This module docstring was added to appease pylint.)
"""

from urllib.parse import urlparse
import os


def extract_domains_from_file(file_path):
    """
    Extracts a list of domains from a given file
    Input type: str
    Output type: {str}
    """
    # input validation
    if not isinstance(file_path, str):
        raise TypeError("file_path should be a str; got {type(file_path)} instead")

    # open the file
    with open(file_path, "r") as file:
        passage = file.read()
        words = passage.split()

        # extract links
        links = []
        for word in words:
            if word.startswith("http://") or word.startswith("https://"):
                links.append(word.strip(".,"))

        # extract domains
        domains_in_passage = {urlparse(link).netloc for link in links}

        return domains_in_passage


def extract_domains_from_file_list(file_list):
    """
    Extracts a list of domains from several files
    Input type: [str]
    Output type: {str: int}
    """
    # input validation
    if not isinstance(file_list, list):
        raise TypeError("file_list should be a list; got {type(file_list)} instead")

    # prep
    result = {}

    # main loop
    for some_file in file_list:
        domains_in_this_file = extract_domains_from_file(some_file)

        # joining dicts together
        for domain in domains_in_this_file:
            if domain in result:
                result[domain] += 1
            else:
                result[domain] = 1

    return result


def make_domains_by_count_dict(domain_counts):
    """
    Inverts the domain_counts dictionary

    Input type {str: int}, interpreted as {domain: count}

    Output type  {int: [str]}, interpreted as {count: [domain]}
    """
    # input validation
    if not isinstance(domain_counts, dict):
        raise TypeError("domain_counts should be a dict; got type {type(domain_counts)} instead")

    # main loop
    domains_by_popularity = {}
    for domain, count in domain_counts.items():
        if count in domains_by_popularity:
            domains_by_popularity[count].append(domain)
        else:
            domains_by_popularity[count] = [domain]

    # sort items in result
    for count in domains_by_popularity.keys():
        domains_by_popularity[count].sort()

    # return
    return domains_by_popularity


def print_domains_by_popularity(domains_by_popularity, threshold = 50):
    """
    Prints domains_by_popularity dictionary in a pretty way
    (this should be taken from make_domains_by_count_dict)
    Input type: dict, (int, None)?

    Threshold prevents long lists in each section
    """
    # input validation
    if not isinstance(domains_by_popularity, dict):
        raise TypeError("domains_by_popularity should be a dict; got type {type(domains_by_popularity)} instead")
    elif not isinstance(threshold, (int, None)):
        raise TypeError("threshold should be an int or None; got type {type(threshold)} instead")
    elif isinstance(threshold, int):
        if threshold < 0:
            raise ValueError("threshold should be nonnegative; got {threshold} instead")

    # prepare for main logic
    counts = list(domains_by_popularity.keys())
    counts = sorted(counts, reverse=True)
    counts_by_count = {
        count: len(domains) for count, domains in domains_by_popularity.items()
    }

    # print statistics
    print("=== STATISTICS ===\n")
    for count in counts:
        print(f"{count} mentions: {counts_by_count[count]} domains total")

    # print domains
    for count in counts:
        print(f"\n=== {count} MENTIONS ===\n{counts_by_count[count]} domains total\n")
        if threshold is None or counts_by_count[count] >= threshold:
            print("[long list omitted]")
        else:
            for domain in domains_by_popularity[count]:
                print(domain)


# main code
if __name__ == "__main__":
    # getting list of files from same directory
    passage_files = []
    FOLDER_PATH = os.getcwd()
    for filename in os.listdir(FOLDER_PATH):
        if filename.endswith(".txt"):
            passage_files.append(os.path.join(FOLDER_PATH, filename))

    # invoking the functions
    my_domain_counts = extract_domains_from_file_list(passage_files)
    my_domains_by_popularity = make_domains_by_count_dict(my_domain_counts)
    print_domains_by_popularity(my_domains_by_popularity)
