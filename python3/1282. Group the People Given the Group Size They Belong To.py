class Solution:

    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        from collections import defaultdict

        persons = defaultdict(list)
        for idx, group_size in enumerate(groupSizes):
            persons[group_size].append(idx)

        results = list()
        for size, person_list in persons.items():
            sub_person_list = person_list
            while len(sub_person_list) != 0:
                results.append(sub_person_list[:size])
                sub_person_list = list() if len(sub_person_list) == size else sub_person_list[size:]

        return results
