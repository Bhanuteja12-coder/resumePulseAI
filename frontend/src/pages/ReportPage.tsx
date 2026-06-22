import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import ScoreCircle from "../components/ScoreCircle";
import KeywordChip from "../components/KeywordChip";
import SuggestionCard from "../components/SuggestionCard";
import { deleteReport } from "../services/reportApi";
import { getReport } from "../services/reportApi";
import SkillRadar from "../components/SkillRadar";
import ReportSkeleton from "../components/ReportSkeleton";

export default function ReportPage() {

    const navigate = useNavigate();

    const [error,setError] = useState("");
const handleDelete = async (id:number) => {

    const confirmDelete = confirm(
        "Delete this report?"
    );

    if (!confirmDelete) return;


    try {

        await deleteReport(id);

        alert("Report deleted");

        navigate("/reports");   // go back to reports list


    } catch (err) {

        console.log(err);
        alert("Delete failed");

    }

};
    const { id } = useParams();


    const [report, setReport] =
        useState<any>(null);


    const [loading, setLoading] =
        useState(true);



    useEffect(() => {


        async function load() {


            try {


                const response =
                    await getReport(Number(id));


                setReport(response.data);


            }
            catch (err) {
    console.log(err);
    setError("Failed to load report");
}


            finally {

                setLoading(false);

            }


        }


        load();


    }, [id]);





    if (loading) {

return (

<div className="p-10">

<ReportSkeleton/>

</div>

)

}




    if(error){

return (

<div className="
min-h-screen
flex
items-center
justify-center
">

<div className="
bg-white
p-10
rounded-3xl
shadow
">

<h1 className="text-2xl font-bold text-red-600">

{error}

</h1>


<button
onClick={()=>window.location.reload()}
className="mt-5 bg-indigo-600 text-white px-5 py-2 rounded-xl"
>

Retry

</button>


</div>

</div>

)

}




    return (

        <div className="
min-h-screen
bg-slate-50
p-10
">


            <div className="
mx-auto
max-w-6xl
space-y-8
">



                <h1 className="
text-4xl
font-bold
">

                    Resume Analysis

                </h1>




                <div className="
grid
md:grid-cols-4
gap-6
">



                    <div className="
relative
rounded-3xl
bg-white
p-8
shadow
flex
justify-center
">


                        <ScoreCircle

                            score={
                                report.match_percent
                            }

                        />


                    </div>


<div className="
rounded-3xl
bg-white
p-8
shadow
">

<h2 className="text-2xl font-bold">
Skill Breakdown
</h2>


<SkillRadar />


</div>


                    <div className="
rounded-3xl
bg-white
p-8
shadow
">


                        <h2 className="text-xl font-bold">

                            Match Score

                        </h2>


                        <p className="
mt-5
text-5xl
font-bold
">

                            {report.match_percent}%

                        </p>


                        <p className="text-gray-500">

                            Resume ↔ Job similarity

                        </p>


                    </div>





                    <div className="
rounded-3xl
bg-white
p-8
shadow
">


                        <h2 className="text-xl font-bold">

                            Resume

                        </h2>


                        <p className="mt-5 text-gray-600">

                            Report ID: {report.id}

                        </p>


                        <p className="text-gray-500">

                            Created:

                            {new Date(
                                report.created_at
                            ).toLocaleDateString()}

                        </p>


                    </div>



                </div>







                <div className="
rounded-3xl
bg-white
p-8
shadow
">


                    <h2 className="
text-2xl
font-bold
">

                        Missing Skills

                    </h2>

                    



                    <div className="
mt-5
flex
flex-wrap
gap-3
">


                        {

                            Object.entries(report.gap_analysis).map(
                                ([category, items]: any) => (
                                    <div key={category} className="w-full">

                                        <h3 className="font-semibold text-slate-700 capitalize">
                                            {category}
                                        </h3>


                                        <div className="mt-3 flex flex-wrap gap-3">

                                            {
                                                items.map(
                                                    (skill: string) => (
                                                        <KeywordChip
                                                            key={skill}
                                                            text={skill}
                                                        />
                                                    )
                                                )
                                            }

                                        </div>

                                    </div>
                                )

                            )

                        }


                    </div>


                </div>








                <SuggestionCard

                    items={
                        report.ai_suggestions || []
                    }

                />




                <button
onClick={()=>handleDelete(report.id)}
className="rounded-xl bg-red-600 px-4 py-2 text-white"
>
Delete
</button>
            </div>


        </div>

    )

}