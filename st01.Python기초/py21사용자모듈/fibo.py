# �Ǻ���ġ ���� ���
def fib(n):    	# �Ǻ���ġ ���� ���
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()


def fib2(n): 	# �Ǻ���ġ ������ ����Ʈ�� ��ȯ
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
	
	
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
