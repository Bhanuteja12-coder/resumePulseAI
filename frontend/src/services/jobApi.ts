import axios from "axios";


const API="http://localhost:8000/api";


export const createJob = async(data:any)=>{


return axios.post(
`${API}/jobs/`,
data
);


};