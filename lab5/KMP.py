from functools import wraps
import time


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print('\t'f'Function {func.__name__}{args}, took {total_time:.10f} seconds')
        return result
    return timeit_wrapper

@timeit
def KMP(text, pattern):
    if text is None or pattern is None or len(text) < len(pattern):
        return [0]

    chars = list(pattern)
    lsp = [0] * (len(pattern) + 1)

    for i in range(1, len(pattern)):
        j = lsp[i + 1]
        while j > 0 and chars[j] is not chars[i]:
            j = lsp[j]
        if j > 0 or chars[j] == chars[i]:
            lsp[i + 1] = j + 1

    j = 0
    for i in range(len(text)):
        if j < len(pattern) and text[i] == pattern[j]:
            j = j + 1
            if j == len(pattern):
                print('\t''Pattern match index is: ', (i - j + 1))
        elif j > 0:
            j = lsp[j]


if __name__ == '__main__':
    string = 'ABCABAABCABAC'
    patern = 'CAB'
    KMP(string, patern)

    print('\t')
    string1 = 'aaaasaaaasasaaaaaassaaaaaaaasaaasaasdaaasaaaaaaaaasaaaaaaaaasaaaaaaaaasaaaaaaaaas'
    pattern1 = 'asd'
    KMP(string1, pattern1)