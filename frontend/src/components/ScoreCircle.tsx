type Props = {
    score:number;
};


export default function ScoreCircle({score}:Props){


const radius = 70;
const circumference = 2*Math.PI*radius;

const offset =
circumference -
(score/100)*circumference;


return (

<div className="flex justify-center">


<svg
width="180"
height="180"
className="rotate-[-90deg]"
>


<circle

cx="90"
cy="90"
r={radius}

strokeWidth="14"

fill="transparent"

className="text-slate-200"

stroke="currentColor"

/>


<circle

cx="90"
cy="90"
r={radius}

strokeWidth="14"

fill="transparent"

strokeLinecap="round"

stroke="currentColor"

className="text-indigo-600"

strokeDasharray={circumference}

strokeDashoffset={offset}

/>


</svg>


<div className="absolute mt-16 text-3xl font-bold">

{score}%

</div>


</div>

)

}