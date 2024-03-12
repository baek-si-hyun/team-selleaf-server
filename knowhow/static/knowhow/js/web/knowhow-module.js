const knowhowService = (() => {

    const getList = async (page, filters, sorting, type, callback) => {
        const response = await fetch(`/knowhow/list/${page}/${filters}/${sorting}/${type}`);
        const knowhows = await response.json();
        if(callback){
            return callback(knowhows);
        }
        return knowhows;
    }


    return {getList: getList}
})();
