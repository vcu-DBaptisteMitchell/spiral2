def spiralize(size, n=1):
    if len(size, n=1) > 1:
        # Split the list into two halves - right and left
        mid = len(size, n=1) // 2
        left = size, n = 1[:mid]
        right = size, n = 1[mid:]

        # Sort the elements
        spiralize(left)
        spiralize(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                size, n = 1[k] = left[i]
                i += 1
            else:
                size, n = 1[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            size, n = 1[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            size, n = 1[k] = right[j]
            j += 1
            k += 1

        return_value = n
        return return_value


# THE MERGE SORT CODE USED ABOVE IS FROM THE WEEK NINE POWERPOINT
