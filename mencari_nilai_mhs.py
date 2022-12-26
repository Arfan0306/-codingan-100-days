# Menentukan jumlah mahasiswa dan jumlah mata kuliah
num_students = 5
num_courses = 3

# Membuat list untuk menyimpan nilai mahasiswa
students_grades = []

# Mengisi list dengan nilai mahasiswa
for i in range(num_students):
  # Meminta input nilai mahasiswa dari pengguna
  student_grades = input(f"Masukkan nilai mahasiswa {i+1}: ")
  student_grades = [int(grade) for grade in student_grades.split()]
  students_grades.append(student_grades)

# Mencari nilai rata-rata setiap mahasiswa
for student_grades in students_grades:
  total_grade = 0
  for grade in student_grades:
    total_grade += grade
  average_grade = total_grade / num_courses
  print(f"Nilai rata-rata mahasiswa adalah {average_grade:.2f}")
