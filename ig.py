"""
Determines which users are not following you back.
Authors: Rishika Krishna

Input are files in which followers and following are listed.
Output is a sequence of users that don't follow you.
"""

import argparse

def unfollow(following_file,followers_file):
    """
    Reads a file containing a list of arbitrarily ordered users
    and prints the output of those who don't follow back.
    
    args:
        following_file: external .txt file containing the people you follow
        followers_file: external .txt file containing your followers
    returns:
        a sequence of accounts that do not follow you back
    """
    following = [ ]
    for line in following_file:
        following.append(line.strip())

    followers = [ ]
    for line in followers_file:
        followers.append(line.strip())

    for user in following:
        if user not in followers:
            print(user)

def main( ):
    """
    Interaction if run from the command line.
    Usage: python ig.py following_file.txt followers_file.txt
    """
    parser = argparse.ArgumentParser(description="Compare followers and following")
    parser.add_argument('following', type=argparse.FileType('r'),
                        help="Text files containing following list")
    parser.add_argument('followers', type=argparse.FileType('r'),
                        help="Text files containing follower lists")
    args = parser.parse_args()  # gets arguments from command line
    following_file = args.following
    followers_file = args.followers
    unfollow(following_file,followers_file)
    
    
if __name__ == "__main__":
    main( )