import axios from 'axios';

const API_URL = 'http://127.0.0.1:5000/waste';

export const fetchWasteItems = async () => {
    const response = await axios.get(API_URL);
    return response.data;
};

