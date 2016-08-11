class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version_one = version1.split(".")
        version_two = version2.split(".")
        
        while len(version_one) != len(version_two):
            if len(version_one) > len(version_two):
                version_two.append(0)
            else:
                version_one.append(0)
        
        for index, num in enumerate(version_one):
            version_number_one = int(num)
            version_number_two = int(version_two[index])
            
            if version_number_one > version_number_two:
                return 1
            elif version_number_one < version_number_two:
                return -1
            else:
                continue
        return 0
            