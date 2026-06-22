import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { authApi } from "../services/axios";


export default function ReportsDashboard(){

    const navigate = useNavigate();

    const [reports,setReports] = useState<any[]>([]);
    const [search,setSearch] = useState("");


    useEffect(()=>{

        loadReports();

    },[]);



    const loadReports = async()=>{

        try{

            const res = await authApi.get(
                "/../reports/"
            );


            setReports(
                res.data.results || res.data
            );

        }
        catch(err){

            console.log(err);

        }

    };



    const filteredReports = reports.filter(report => {

    const text = `

        ${report.id}
        ${report.match_percent}
        ${report.job_description?.title || ""}
        ${report.job_description?.company || ""}
        ${report.job_description?.description || ""}

    `.toLowerCase();


    return text.includes(search.toLowerCase());

});



    return (

        <div className="
bg-white
rounded-3xl
shadow-xl
p-6
border
border-slate-100
hover:-translate-y-2
transition
">


            <h1 className="text-4xl font-bold">
                Reports Dashboard
            </h1>


            <input

                className="mt-6 w-full rounded-xl border p-3"

                placeholder="Search reports..."

                value={search}

                onChange={
                    e=>setSearch(e.target.value)
                }

            />



            <div className="mt-8 grid md:grid-cols-3 gap-6">


            {
                filteredReports.map(report=>(


                <div

                key={report.id}

                onClick={()=>
                    navigate(`/report/${report.id}`)
                }

                className="
                cursor-pointer
                rounded-3xl
                bg-white
                p-6
                shadow
                hover:scale-105
                "

                >


                    <h2 className="text-xl font-bold">
                        Report #{report.id}
                    </h2>


                    <p className="mt-5 text-5xl font-bold">

                        {report.match_percent}%

                    </p>


                    <p className="mt-3 text-gray-500">

                    {new Date(
                        report.created_at
                    ).toLocaleDateString()}

                    </p>


                </div>


                ))

            }


            </div>


        </div>

    )
}