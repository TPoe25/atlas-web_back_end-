function hasValuesFromArray(set, arr) {
    const allValuesExist = arr.every(value => set.has(value));

    return allValuesExist;
}

export default hasValuesFromArray;
