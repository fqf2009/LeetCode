# Given a url startUrl and an interface HtmlParser, implement 
# a web crawler to crawl all links that are under the same 
# hostname as startUrl. 
# Return all urls obtained by your web crawler in any order.
# Your crawler should:
#   Start from the page: startUrl
#   Call HtmlParser.getUrls(url) to get all urls from a webpage of given url.
#   Do not crawl the same link twice.
#   Explore only the links that are under the same hostname as startUrl.
# As shown in the example url above, the hostname is example.org. 
# For simplicity sake, you may assume all urls use http protocol without 
# any port specified. For example, the urls http://leetcode.com/problems 
# and http://leetcode.com/contest are under the same hostname, while 
# urls http://example.org/test and http://example.com/abc are not under 
# the same hostname.
# The HtmlParser interface is defined as such: 
#   interface HtmlParser {
#     // Return a list of all urls from a webpage of given url.
#     public List<String> getUrls(String url);
#   }
# Constraints:
#   1 <= urls.length <= 1000
#   1 <= urls[i].length <= 300
#   startUrl is one of the urls.
#   Hostname label must be from 1 to 63 characters long, including the dots, may contain only the ASCII letters from 'a' to 'z', digits  from '0' to '9' and the hyphen-minus character ('-').
#   The hostname may not start or end with the hyphen-minus character ('-'). 
#   See:  https://en.wikipedia.org/wiki/Hostname#Restrictions_on_valid_hostnames
#   You may assume there're no duplicates in url library.


# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
from collections import deque
from typing import List


class HtmlParser(object):
   def getUrls(self, url):
       """
       :type url: str
       :rtype List[str]
       """

# BFS
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def getDomain(url: str):
            return url.split('/')[2]

        res = set()
        dq = deque([startUrl])
        domain = getDomain(startUrl)
        while dq:
            url = dq.popleft()
            if getDomain(url) == domain and url not in res:
                res.add(url)
                dq.extend(htmlParser.getUrls(url))  # type: ignore

        return list(res)
