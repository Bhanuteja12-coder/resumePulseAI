import {
    Radar,
    RadarChart,
    PolarGrid,
    PolarAngleAxis,
    ResponsiveContainer
} from "recharts";


export default function SkillRadar(){

    const data = [
        {
            skill:"Skills",
            value:80
        },
        {
            skill:"Tools",
            value:65
        },
        {
            skill:"Experience",
            value:55
        },
        {
            skill:"Projects",
            value:70
        },
        {
            skill:"ATS",
            value:75
        }
    ];


    return (

        <div className="h-80 w-full">


        <ResponsiveContainer>

        <RadarChart data={data}>


            <PolarGrid />


            <PolarAngleAxis
                dataKey="skill"
            />


            <Radar
                dataKey="value"
                fillOpacity={0.6}
            />


        </RadarChart>


        </ResponsiveContainer>


        </div>

    )

}