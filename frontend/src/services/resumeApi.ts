import { authApi } from "./axios";
import {getToken} from "../utils/auth";

export const uploadResume = async (file: File) => {

    const formData = new FormData();

    formData.append(
        "file",
        file
    );


    return authApi.post(
        "/../resumes/upload/",
        formData,
        {
            headers:{
                "Content-Type":"multipart/form-data"
            }
        }
    );
};


export const analyzeResume = async (
    resume_id:number,
    job_description_id:number
)=>{

    return authApi.post(
        "/../resumes/analyze/",
        {
            resume_id,
            job_description_id
        }
    );

};

export const deleteReport = async(id:number)=>{

    return authApi.delete(
        `/../resumes/reports/${id}/delete/`
    );

};