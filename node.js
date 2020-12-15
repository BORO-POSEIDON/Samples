const axios = require('axios');

(async () => {

    const API_KEY = "user_api_key_here";
    const API_URL = "https://poseidon.boroinc.com/api";

    const SITE_KEY = "6LeWwRkUAAAAAOBsau7KpuC9AV-6J8mhw4AjC3Xz";
    const SITE_URL = "https://www.supremenewyork.com/";

    let instance = axios.create({
        baseURL: API_URL,
        headers: {
            'X-Api-Key': API_KEY
        }
    });

    let { data } = await instance.post(API_URL + '/solve/request', {
        site_key: SITE_KEY,
        site_url: SITE_URL,
        requester: "Developer Sample"
    });

    let solveId = data.id;

    let status = 'pending', token;
    while(status == 'pending' || status == 'started') {
        let { data } = await instance.post(API_URL + '/solve/check', {
            solveId: solveId.toString()
        });

        ({ status, token } = data);
    }
    
    console.log("Status:", status);
    
    if(token)
        console.log("Token:", token);

})();
