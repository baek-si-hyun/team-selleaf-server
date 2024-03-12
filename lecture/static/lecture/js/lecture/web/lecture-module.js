const lectureService = (() => {

    const getList = async (page, filters, sorting, type, callback) => {
        const response = await fetch(`/lecture/total/${page}/`);
        const lectures = await response.json();
        if(callback){
            return callback(lectures);
        }
        return lectures;
    }


    return {getList: getList}
})();


const lectureScrapService = (() => {
  const update = async (lectureId) => {
    await fetch(`/lecture-scrap/api/`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json;charset=utf-8',
        'X-CSRFToken': csrf_token
      },
      body: JSON.stringify({'lecture_id': lectureId})
    });
  }

  return {update: update}
})()

const scrapCountService = (() => {

    const scrapCount = async (lecture_id, onlineStatus, callback) => {
        let endpoint = "";
        if (onlineStatus) {
            endpoint = `/lecture/detail/online?id=${lecture_id}`;
        } else {
            endpoint = `/lecture/detail/offline?id=${lecture_id}`;
        }

        const response = await fetch(endpoint);
        const lectures = await response.json();
        if(callback){
            return callback(lectures);
        }
        return lectures;
    }

    return {scrapCount: scrapCount}
})();