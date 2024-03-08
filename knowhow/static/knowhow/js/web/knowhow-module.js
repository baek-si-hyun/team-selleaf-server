const knowhowService = (() => {

    const getList = async (page, callback) => {
        const response = await fetch(`/knowhow/list/${page}`);
        const knowhows = await response.json();
        if(callback){
            return callback(knowhows);
        }
        return knowhows;
    }

    const Like = async (knowhow_id, member_id, callback) => {
        const response = await fetch(`/knowhow/like/${knowhow_id}/${memberId}`);
        const likes = await response.json();
        if(callback){
            return callback(likes);
        }
        return likes
    }

    return {getList: getList, Like: Like}
})();
