import { useState } from "react";
import ResumeDropzone from "../components/ResumeDropzone";
import { uploadResume, analyzeResume } from "../services/resumeApi";
import { createJob } from "../services/jobApi";
import { useNavigate } from "react-router-dom";

export default function UploadResumePage() {


    const [file, setFile] = useState<File | null>(null);

    const [title, setTitle] = useState("");
    const [company, setCompany] = useState("");
    const [location, setLocation] = useState("");
    const [description, setDescription] = useState("");

    const [loading, setLoading] = useState(false);

    const navigate = useNavigate();

    async function submit(e: React.FormEvent) {

        e.preventDefault();


        if (!file) {
            alert("Upload resume");
            return;
        }


        setLoading(true);


        try {


            // upload resume

            const resumeRes =
                await uploadResume(file);



            const resumeId =
                resumeRes.data.id;



            // create job

            const jobRes =
                await createJob({

                    title,
                    company,
                    location,
                    description

                });


            const jobId =
                jobRes.data.id;



            // analyze

            const report =
                await analyzeResume(
                    resumeId,
                    jobId
                );


            
            navigate(
                `/report/${report.data.id}`
            );


            alert(
                `Match ${report.data.match_percent}%`
            );



        } catch (err) {

            console.log(err);

            alert("Something went wrong");

        }

        finally {

            setLoading(false);

        }


    }



    return (

        <div className="
min-h-screen
p-10
bg-gradient-to-br
from-indigo-50
via-white
to-purple-100
">


            <form
                onSubmit={submit}
                className="mx-auto max-w-xl rounded-3xl bg-white/80
backdrop-blur-xl
border
border-white
rounded-3xl
p-10
shadow-2xl"
            >


                <h1 className="text-3xl font-bold">
                    Resume Analyzer
                </h1>


                <div className="mt-6">

                    <ResumeDropzone
                        onFile={setFile}
                    />

                </div>



                <input
                    className="mt-5 w-full rounded-xl
border
border-slate-200
p-4
outline-none
focus:ring-2
focus:ring-indigo-500"
                    placeholder="Job title"
                    onChange={
                        e => setTitle(e.target.value)
                    }
                />



                <input
                    className="mt-3 w-full border p-3"
                    placeholder="Company"
                    onChange={
                        e => setCompany(e.target.value)
                    }
                />



                <input
                    className="mt-3 w-full border p-3"
                    placeholder="Location"
                    onChange={
                        e => setLocation(e.target.value)
                    }
                />



                <textarea

                    className="mt-3 w-full border p-3"

                    rows={6}

                    placeholder="Paste job description"

                    onChange={
                        e => setDescription(e.target.value)
                    }

                />



                <button

                    disabled={loading}

                    className="mt-5 w-full rounded-xl bg-gradient-to-r
from-indigo-600
to-purple-600
p-4
text-white
rounded-xl
shadow-lg
hover:scale-[1.02]
transition"

                >

                    {
                        loading
                            ?
                            "Analyzing..."
                            :
                            "Analyze Resume"
                    }


                </button>



            </form>


        </div>

    )

}