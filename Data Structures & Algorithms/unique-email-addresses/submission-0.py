class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hashset = set()
        for i in range(len(emails)):
            email = ""
            curr = emails[i]
            flag = False
            for j in range(len(curr)):
                if curr[j] == "@":
                    email += curr[j:]
                    break
                elif flag:
                    continue
                elif curr[j] == ".":
                    continue
                elif curr[j] == "+":
                    flag = True
                email += curr[j]
            if email in hashset:
                continue
            else:
                hashset.add(email)
        return len(hashset)

            