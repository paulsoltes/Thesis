from django.db import models

# ✅ Instructor Model (Hardcoded for now but defined for future use)
class Instructor(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

# ✅ Room Model
class Room(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

# ✅ Course Model
class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# ✅ Section Model (Year and Section Letter)
class Section(models.Model):
    year = models.IntegerField(choices=[(1, "1st"), (2, "2nd"), (3, "3rd"), (4, "4th")])
    section = models.CharField(max_length=1, choices=[("A", "A"), ("B", "B"), ("C", "C"), ("D", "D"), ("E", "E")])

    def __str__(self):
        return f"{self.year}-{self.section}"

# ✅ Time Model (Start and End Times)
class Time(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.start_time} - {self.end_time}"

# ✅ Day Model (MW, TTh, FS)
class Day(models.Model):
    name = models.CharField(max_length=10, choices=[("MW", "Monday-Wednesday"), ("TTh", "Tuesday-Thursday"), ("FS", "Friday-Saturday")], unique=True)

    def __str__(self):
        return self.name

# ✅ Semester Model
class Semester(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

# ✅ Year Model
class Year(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

# ✅ Department Model
class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

# ✅ Program Model
class Program(models.Model):
    name = models.CharField(max_length=255, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# ✅ Subject Model (With Details)
class Subject(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    subject_type = models.CharField(max_length=50, choices=[("Lecture", "Lecture"), ("Lab", "Lab")])
    credit = models.IntegerField()
    prerequisite = models.TextField(blank=True, null=True)
    corequisite = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    objectives = models.TextField(blank=True, null=True)
    outcomes = models.TextField(blank=True, null=True)
    resources = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.code} - {self.name}"

# ✅ Schedule Model (Ties Everything Together)
class Schedule(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    time = models.ForeignKey(Time, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subject} - {self.day} - {self.time}"
