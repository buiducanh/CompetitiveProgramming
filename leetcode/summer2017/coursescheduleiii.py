class Solution(object):
    MAX_TIME = 10**4

    def scheduleCourseRecursion(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        max_courses = [[-1 for j in range(self.MAX_TIME)] for i in range(len(courses))]
        # sort by end time
        sorted_courses = sorted(courses, key=lambda x: x[1])
        def schedule(i, time):
            if max_courses[i][time] != -1:
                return max_courses[i][time]
            if i == len(courses) - 1:
                if time + sorted_courses[i][0] <= sorted_courses[i][1]:
                    return 1
                else:
                    return 0
            taken = 0
            if time + sorted_courses[i][0] <= sorted_courses[i][1]:
                taken = schedule(i + 1, time + sorted_courses[i][0]) + 1
            not_taken = schedule(i + 1, time)

            max_courses[i][time] = max(taken, not_taken)

            return max_courses[i][time]
        return schedule(0, 0)

    def scheduleCourseIterativeHeap(self, courses):
        import heapq
        taken = []
        time = 0
        for course in sorted(courses, key=lambda x: x[1]):
            if time + course[0] <= course[1]:
                heapq.heappush(taken, (-course[0],) +  (course[1],))
                time += course[0]
            else:
                longest_course = heapq.heappop(taken)
                if course[0] > -longest_course[0]:
                    heapq.heappush(taken, longest_course)
                    continue
                time = time + longest_course[0] + course[0]
                heapq.heappush(taken, (-course[0],) + (course[1],))
        return len(taken)


inp = open("coursescheduleiii.inp")
courses = []
for line in inp:
    courses.append(list(map(int, line.strip().split())))

    print(Solution().scheduleCourseRecursion(courses))
