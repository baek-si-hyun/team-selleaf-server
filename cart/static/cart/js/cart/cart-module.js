const cartService = (()=>{
    const getList = async (cart_id, callback) =>{
        const response = await fetch(`/cart/list/${cart_id}`);
        const details = await response.json();
        if (callback){
            return callback(details)
        }
        return details

    };

    const remove = async (detailId) => {
        await fetch(`/cart/${detailId}/`, {
            method: 'delete',
            headers: {
                'Content-Type': 'application/json;charset=utf-8',
                'X-CSRFToken': csrf_token
            }
        });
    }

    const select = async (detailId, callback) =>{
        const response = await fetch(`/cart/${detailId}`);
        const detail = await response.json();
        if (callback){
            return callback(detail)
        }
        return detail
    };

    const selectCancel = async (targetId, callback) =>{
        const response = await fetch(`cart/${targetId}`);
        const target = await response.json();
        if (callback){
            return callback(target)
        }
        return target
    }


    return {getList:getList, remove:remove, select:select}

})()