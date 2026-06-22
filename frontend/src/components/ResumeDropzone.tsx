import {useState} from "react";


export default function ResumeDropzone({
    onFile
}:{
    onFile:(file:File)=>void
}){


const [name,setName]=useState("");



function handleChange(
e:React.ChangeEvent<HTMLInputElement>
){

const file=e.target.files?.[0];


if(!file)return;


const allowed=[
".pdf",
".docx"
];


const ext=file.name.substring(
file.name.lastIndexOf(".")
);


if(!allowed.includes(ext)){
alert("Only PDF and DOCX allowed");
return;
}


setName(file.name);

onFile(file);

}



return (

<div className="rounded-3xl border-2 border-dashed p-8 text-center">


<h2 className="text-xl font-semibold">
Upload Resume
</h2>


<p className="text-gray-500">
Drag PDF/DOCX or click
</p>


<input
type="file"
accept=".pdf,.docx"
className="mt-5"
onChange={handleChange}
/>


{
name &&
<p className="mt-3">
{name}
</p>
}


</div>

)

}