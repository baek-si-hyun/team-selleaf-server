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

const tradeScrapService = (() => {
  const update = async (tradeId) => {
    await fetch(`/trade-scrap/api/`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json;charset=utf-8',
        'X-CSRFToken': csrf_token
      },
      body: JSON.stringify({'trade_id': tradeId})
    });
  }

  return {update: update}
})()