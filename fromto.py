import sys
import csv

def make_dict_from_text_file(text_file):
    # This function uses a context managet to open the designated text file
    # and stores its contents into an IO wrapper object.
    with open(text_file, "r") as in_text_file:
        # The following are the four dictionaries that will store its respective contents. 
        user_from = dict()
        user_to = dict()
        host_from = dict()
        host_to = dict()
        # For each line of the Text IO wrapper,...
        for line in in_text_file:
            # ... filter out those lines that start with ("FROM: ").
            if line.startswith("From: "):
                # Split the line into a list on default whitespace.
                list_of_words = line.split()
                # Split the list on a specified character "@"
                # and assign its halves into variables.
                username, host = list_of_words[1].split("@")
                # Place each vaiable into its corresponding dictionaries.
                user_from[username] = user_from.get(username, 0) + 1
                host_from[host] = host_from.get(host, 0) + 1
            # ... filter out those lines that start with ("TO: ").
            elif line.startswith("To: "):
                # Split the line into a list on default whitespace.
                list_of_words = line.split()
                # Split the list on a specified character "@"
                # and assign its halves into variables.
                username, host = list_of_words[1].split("@")
                # Place each vaiable into its corresponding dictionaries.
                user_to[username] = user_to.get(username, 0) + 1
                host_to[host] = host_to.get(host, 0) + 1
    # Return the four dictionaries.
    return user_from, user_to, host_from, host_to

if __name__ == "__main__":
    # Make four dictionaries from the designated textfile.
    uf, ut, hf, ht = make_dict_from_text_file("mbox-short.txt")
    # Use the csv writer to print the results to the terminal.
    cw = csv.writer(sys.stdout)
    # The following are the results produced by the program.
    print("--- FROM USER ---")
    cw.writerows(sorted(uf.items()))
    print("--- FROM HOST ---")
    cw.writerows(sorted(hf.items()))
    print("--- TO USER ---")
    cw.writerows(sorted(ut.items()))
    print("--- TO HOST ---")
    cw.writerows(sorted(ht.items()))
    
    