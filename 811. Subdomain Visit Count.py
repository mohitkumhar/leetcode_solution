class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = {}
        for cp in cpdomains:
            visits, domain = cp.split(' ')
            visits = int(visits)
            subdomain = domain.split('.')

            for i in range(len(subdomain)):
                parts = '.'.join(subdomain[i:])
                if parts in counter:
                    counter[parts] += visits
                else:
                    counter[parts] = visits

        result = []
        for key, values in counter.items():
            result.append(f"{values} {key}")
        return result
