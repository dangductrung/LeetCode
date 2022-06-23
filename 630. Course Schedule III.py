class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        result = []
        courses.sort(key = lambda x: x[1])
        
        for value in courses:
            result.append(value[0])
            if sum(result) > value[1]:
                result.remove(max(result))
        return len(result)