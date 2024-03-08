const postService = (()=>{
    const getList = async (member_id, callback) =>{
        const response = await fetch(`/member/mypost/`);
        const posts = await response.json();
        if (callback){
            return callback(posts)
        }
        return posts

    };

    return {getList:getList}
})()