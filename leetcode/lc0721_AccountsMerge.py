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
# Constraints:
#   1 <= accounts.length <= 1000
#   2 <= accounts[i].length <= 10
#   1 <= accounts[i][j] <= 30
#   accounts[i][0] consists of English letters.
#   accounts[i][j] (for j > 0) is a valid email.
from collections import defaultdict
from typing import List


# Disjoint Set Union (DSU) a.k.a. Union Find
# T/S: O(N*log(k)), O(N), note the log(k) is due to email sorting
# - where N = n*k is total emails, n is accounts, k is average emails in account
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = list(range(n))             # list of account id

        def find(id: int) -> int:
            if uf[id] != id:
                uf[id] = find(uf[id])   # compress the path
            return uf[id]

        email_map = {}
        for id, acc in enumerate(accounts):
            for email in acc[1:]:       # acc[0] is name, acc[1:] are emails
                if email in email_map:  # email already related to other id
                    uf[find(email_map[email])] = id     # union other id to this id
                email_map[email] = id

        email_list = [[] for _ in range(n)]
        for email, id in email_map.items():
            email_list[find(id)].append(email)

        res = []
        for i, acc in enumerate(accounts):
            if email_list[i]:
                res.append([acc[0]] + sorted(email_list[i]))

        return res


# Graph + DFS
# T/S: O(N*log(k)), O(N), note the log(k) is due to email sorting
# - where N is the total number of emails, k is average account length
# Algorighm:
# - first build a graph, with all emails as nodes. for each user, its first email
#   has edges pointing to all its other emails, and its every other email will
#   also has edge pointing back to its first email.
# - when building graph, also create a map to map all emails to user's name.
# - to merge account, just enumerate each email, if it is not visited, then DFS
#   visit the graph, find all related emails for this user.
class Solution1:
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


class Solution2:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(set)  # adjacency list
        email_to_user = {}
        for acc in accounts:
            username = acc[0]
            email0 = acc[1]
            email_to_user[email0] = username
            for email in acc[1:]:
                graph[email0].add(email)
                graph[email].add(email0)
                email_to_user[email] = username
        
        def dfs_visit(email, related_emails):
            related_emails.append(email)
            visited.add(email)
            for e in graph[email]:
                if e not in visited:
                    dfs_visit(e, related_emails)
            
        visited = set()
        res = []
        for email, username in email_to_user.items():
            if email not in visited:
                related_emails = []
                dfs_visit(email, related_emails)
                res.append([username] + sorted(related_emails))

        return res


if __name__ == '__main__':
    def unit_test(sol):
        accounts = [["David","David0@m.co","David1@m.co"],
                    ["David","David3@m.co","David4@m.co"],
                    ["David","David4@m.co","David5@m.co"],
                    ["David","David2@m.co","David3@m.co"],
                    ["David","David1@m.co","David2@m.co"]]
        expected = [["David","David0@m.co","David1@m.co","David2@m.co",
                             "David3@m.co","David4@m.co","David5@m.co"]]
        r = sol.accountsMerge(accounts)
        print(r)
        assert sorted(r) == sorted(expected)

        accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],
                    ["John","johnsmith@mail.com","john00@mail.com"],
                    ["Mary","mary@mail.com"],
                    ["John","johnnybravo@mail.com"]]
        expected = [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
                    ["Mary","mary@mail.com"],
                    ["John","johnnybravo@mail.com"]]
        r = sol.accountsMerge(accounts)
        print(r)
        assert sorted(r) == sorted(expected)

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
        assert sorted(r) == sorted(expected)

    unit_test(Solution())
    unit_test(Solution1())
    unit_test(Solution2())
