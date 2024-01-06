export default function createReportObject(employeeList) {
    return {
      allEmployees: employeeList,
      getNumberOfDepartments: function (allEmployees) {
        return Object.keys(this.allEmployees).length;
      },
  };
}
