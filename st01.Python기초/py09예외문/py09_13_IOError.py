try:
    fname = input("���� �̸��� �Է��ϼ���: ")
    infile = open(fname, "r") 
except IOError:
    print("���� " + fname + "�� �߰��� �� �����ϴ�.")


try:
   fh = open("testfile", "w")
   fh.write("�׽�Ʈ �����͸� ���Ͽ� ���ϴ�!!")
except IOError:
   print("Error: ������ ã�� �� ���ų� �����͸� �� �� �����ϴ�. ")
else:
   print("���Ͽ� ���������� ����Ͽ����ϴ�. ")
   fh.close()

try:
   f = open("test.txt", "w" )
   f.write("�׽�Ʈ �����͸� ���Ͽ� ���ϴ�!!")
   # ���� ������ �����Ѵ�. 
except IOError:
   print("Error: ������ ã�� �� ���ų� �����͸� �� �� �����ϴ�. ")
finally:
   f.close()
