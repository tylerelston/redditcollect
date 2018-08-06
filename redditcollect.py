#todo: store post IDs alongside results, check for current results doc,
# cache posts already parsed through and update file with new posts
import praw

# logging into praw
reddit = praw.Reddit(client_id = 'YOUR_CLIENTID',
                     client_secret = 'YOUR_SECRET',
                     username = 'YOUR_USERNAME',
                     password = 'YOUR_PASSWORD',
                     user_agent = 'redditcollect')

subreddit = reddit.subreddit('gamedev') # sub to search through
query = 'free' # keyword to search for
sortBy = 'top' # sort by top,hot,new,controversial, relevance
limited = None # amount of results to limit the search to
minScore = 0 # minimum score of post
out = 'results.txt' # file to store output

posts = []
for submission in subreddit.search(query, sort=sortBy, limit=limited):
    if submission.score >= minScore:
        p = '[{}] {} {}'.format(str(submission.score), submission.title, submission.url)
        posts.append(p)
    
print('Collected',str(len(posts)),'posts.')

f = open(out, 'w')
for post in posts:
    f.write(post)
    f.write('\n\n')
f.close()

print('Results written to',out)
