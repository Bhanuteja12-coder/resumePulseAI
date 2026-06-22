import axios from "axios";
import { getToken } from "../utils/auth";


const API = "http://localhost:8000/api";


export const getReport = async (id: number) => {

    return axios.get(
        `${API}/reports/${id}/`,
        {
            headers: {
                Authorization: `Bearer ${getToken()}`
            }
        }
    );

};


export const analyzeResume = async (
    resume_id: number,
    job_description_id: number
) => {

    return axios.post(
        `${API}/resumes/analyze/`,
        {
            resume_id,
            job_description_id
        },
        {
            headers: {
                Authorization: `Bearer ${getToken()}`
            }
        }
    );

};

export const deleteReport = async(id:number)=>{

    return axios.delete(
        `${API}/reports/${id}/delete/`,
        {
            headers:{
                Authorization:`Bearer ${getToken()}`
            }
        }
    );

};