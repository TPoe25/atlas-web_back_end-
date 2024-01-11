export default function createEmployeesObject(departmentName, employees) {
  const departmentObject = {};
  departmentObject[departmentName] = employees;
  return departmentObject;
}
