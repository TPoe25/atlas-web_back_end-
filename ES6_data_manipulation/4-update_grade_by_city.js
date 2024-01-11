function updateStudentGradeByCity(students, city, newGrades) {
  const studentsInCity = students.filter((student) => student.location === city);

  const updatedStudents = studentsInCity.map((student) => {
    const matchingGrade = newGrades.find((grade) => grade.studentId === student.id);

    if (matchingGrade) {
      return { ...student, grade: matchingGrade.grade };
    }
    return { ...student, grade: 'N/A' };
  });

  return updatedStudents;
}

export default updateStudentGradeByCity;
