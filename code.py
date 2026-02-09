def containsNearbyAlmostDuplicate(nums, k, t):
    if k < 0 or t < 0:
        return False
    bucket_map = {}
    index_map = {}
    for i in range(len(nums)):
        # Remove the element out of window
        remove_index = i - k - 1
        if remove_index >= 0:
            if remove_index in index_map:
                old_bucket = index_map[remove_index]
                if old_bucket in bucket_map and bucket_map[old_bucket][1] == remove_index:
                    del bucket_map[old_bucket]
