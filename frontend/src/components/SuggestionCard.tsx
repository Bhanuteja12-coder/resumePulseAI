type Props = {
    items: string[];
};


export default function SuggestionCard({items}:Props){


return (

<div className="rounded-3xl bg-white p-8 shadow">


<h2 className="text-2xl font-bold">
🤖 Gemini Suggestions
</h2>


<div className="mt-5 space-y-3">


{
items?.length > 0 ? (

items.map((item,index)=>(

<div
key={index}
className="
rounded-xl
bg-indigo-50
p-4
"
>

{item}

</div>

))


) : (

<p className="text-gray-500">
No suggestions generated
</p>

)

}


</div>


</div>

)

}