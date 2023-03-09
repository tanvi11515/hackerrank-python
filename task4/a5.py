def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:i + min(len(sub_string), (len(string) - i))] == sub_string:
            count += 1
    return count