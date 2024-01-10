class Building {
    constructor(sqft) {
        this._sqft = sqft;
        if (this.constructor === Building) {
            throw new TypeError('Abstract class "Building" is not instantiated');
        }

        if (!this.evacuationWarningMessage || typeof this.evacuationWarningMessage !== 'function') {
            throw new TypeError('Class extending Building must override evacuationWarningMessage');
        }
    }

    get sqft() {
        return this._sqft;
    }

    evacuationWarningMessage() {
        throw new Error('EvacuationWarningMessage method must be implemented by subclasses');
    }
}

export default Building;