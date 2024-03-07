const knowhowService = (() => {
    const getList = async (page, callback) => {
        const response = await fetch(`/knowhow/list/${page}`);
        const knowhows = await response.json();
        if(callback){
            return callback(knowhows);
        }
        return knowhows;
    }

    return {getList: getList}
})();
