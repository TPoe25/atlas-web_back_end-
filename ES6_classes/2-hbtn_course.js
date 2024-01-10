class HolbertonCourse {
  constructor(name, length, students) {
    this._name = name;
    this._length = length;
    this._students = students;
  }

  validateString(value, propName) {
    if (typeof value !== 'string') {
      throw new TypeError(`${propName} must be a string`);
    }
  }

  validateNumber(value, propName) {
    if (typeof value !== 'number') {
      throw new TypeError(`${propName} must be a number`);
    }
  }

  validateArray(value, propName) {
    if (!Array.isArray(value)) {
      throw new TypeError(`${propName} must be an array`);
    }
  }

  get name() {
    return this._name;
  }

  set name(value) {
    this.validateString(value, 'Name');
    this._name = value;
  }

  get length() {
    return this._length;
  }

  set length(value) {
    this.validateNumber(value, 'Length');
    this._length = value;
  }

  get students() {
    return this._students;
  }

  set students(value) {
    this.validateArray(value, 'Students');
    this._students = value;
  }
}

export default HolbertonCourse;
