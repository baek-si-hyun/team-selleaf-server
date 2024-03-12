const knowhowService = (() => {

    const getList = async (page, filters, sorting, type, callback) => {
        const response = await fetch(`/knowhow/list/${page}/${filters}/${sorting}/${type}`);
        const knowhows = await response.json();
        if(callback){
            return callback(knowhows);
        }
        return knowhows;
    }

    const getLikeScrap = async (knowhow_id, member_id, status, callback) => {
        const response = await fetch(`/knowhow/like/scrap/${knowhow_id}/${member_id}/${status}`);
        const ls = await response.json();
        if (callback){
            return callback(ls);
        }
        return ls;

    }


    return {getList: getList, getLikeScrap: getLikeScrap}
})();
