from typing import List, Optional

# Given a list of accounts where each element accounts[i] is a list of strings, where
# the first element accounts[i][0] is a name, and the rest of the elements are emails
# representing emails of the account. Now, we would like to merge these accounts. Two
# accounts definitely belong to the same person if there is some common email to both 
# accounts. Note that even if two accounts have the same name, they may belong to 
# different people as people could have the same name. A person can have any number of 
# accounts initially, but all of their accounts definitely have the same name.
# After merging the accounts, return the accounts in the following format: the first 
# element of each account is the name, and the rest of the elements are emails in 
# sorted order. The accounts themselves can be returned in any order.

# First build a graph, with all emails as nodes. for each user, its first email has
# edges pointing to all its others emails, and its every other email will also has
# edge pointing back to its first email.
# To merge account, just enumerate each email, if it is not visited, then use DFS,
# i.e. depth first search, find all related emails for this user.
# Time Complexity: O(N) where N is the number of emails.
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def dfsRelatedEmails(email, emails):
            visited[email] = True
            emails.append(email)
            for e in graph[email]:
                if not visited[e]:
                    dfsRelatedEmails(e, emails)

        graph = {}
        email_to_user = {}
        for acc in accounts:
            user = acc[0]
            emails = acc[1:]
            e0 = emails[0]
            graph.setdefault(e0, set())
            email_to_user[e0] = user
            for e in emails[1:]:
                graph[e0].add(e)
                graph.setdefault(e, set()).add(e0)
                email_to_user[e] = user

        visited = {e: False for e in graph}
        res = []
        for e, user in email_to_user.items():
            if visited[e]:
                continue
            emails = []
            dfsRelatedEmails(e, emails)
            acc = [user]
            acc.extend(sorted(emails))
            res.append(acc)

        return res


if __name__ == '__main__':
    sol = Solution()

    accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],
                ["John","johnsmith@mail.com","john00@mail.com"],
                ["Mary","mary@mail.com"],
                ["John","johnnybravo@mail.com"]]
    expected = [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
                ["Mary","mary@mail.com"],
                ["John","johnnybravo@mail.com"]]
    r = sol.accountsMerge(accounts)
    print(r)
    assert(sorted(r) == sorted(expected))

    accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],
                ["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],
                ["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],
                ["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],
                ["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
    expected = [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],
                ["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],
                ["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],
                ["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],
                ["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
    r = sol.accountsMerge(accounts)
    print(r)
    assert(sorted(r) == sorted(expected))
