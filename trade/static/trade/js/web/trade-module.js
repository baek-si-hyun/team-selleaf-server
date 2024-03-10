const tradeService = (() => {

    const getList = async (page, callback) => {
        const response = await fetch(`/trade/total/${page}`);
        const trades = await response.json();
        if(callback){
            return callback(trades);
        }
        return trades;
    }

    return {getList: getList}
})();