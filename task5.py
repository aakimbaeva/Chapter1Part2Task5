class1 = int(input('Students in class A: '))
class2 = int(input('Students in class B: '))
class3 = int(input('Students in class C: '))
print('School needs', (class1+class2+class3) // 2 + (class1+class2+class3) % 2, 'desks in total.')
