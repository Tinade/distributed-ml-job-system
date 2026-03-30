from models.job import Job
from workers.worker import process_job

queue = []

job = Job(1, "process_data", {"data": [1, 2, 3]})

# Step 1: Add job ONCE
queue.append(job)

# Step 2: Worker processes queue
while queue:
    job = queue.pop(0)

    # retry loop INSIDE processing
    while job.status != "success" and job.status != "failed":
        process_job(job)

print("Final Status:", job.status)
print("Retries:", job.retries)














def duplicate(nums):

    slow = 0
    fast = 1
    while fast < len(nums):
        res = []
        if nums[slow] == nums[fast]:
            fast += 1
            
        else:
            slow += 1
            nums[slow] = nums[fast]
            res.append(nums[slow])
            fast += 1
    return res














def is_palindrome(s):
    left = 0
    right = len(s) -1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -=1
    return True

















