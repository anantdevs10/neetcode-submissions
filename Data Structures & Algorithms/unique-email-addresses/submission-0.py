class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        prefix = []

        for i in range(len(emails)):
            local, domain = emails[i].split("@")
            local = local.split("+")[0]
            local = local.replace(".", "")
            prefix.append((local, domain))
        return len(set(prefix))
        