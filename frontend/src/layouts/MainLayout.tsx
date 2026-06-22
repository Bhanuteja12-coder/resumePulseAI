import { Outlet, Link, NavLink } from "react-router-dom";
import logo from "../assets/logo.png";


export default function MainLayout(){

return (

<div className="
min-h-screen
relative
bg-gradient-to-br
from-slate-50
via-white
to-indigo-50
">


{/* background glow */}

<div className="
absolute
top-20
left-10
h-72
w-72
bg-purple-400
rounded-full
blur-3xl
opacity-20
"/>


<div className="
absolute
bottom-10
right-10
h-72
w-72
bg-indigo-400
rounded-full
blur-3xl
opacity-20
"/>



<nav className="
sticky
top-0
z-50
h-28
bg-white/80
backdrop-blur-xl
shadow-lg
flex
items-center
justify-between
px-10
">


<Link
to="/dashboard"
className="
flex
items-center
gap-4
"
>


<img
src={logo}
className="
h-28
w-28
object-contain
scale-150
"
/>


{/* <div>

<h1 className="
text-3xl
font-extrabold
bg-gradient-to-r
from-indigo-600
to-purple-600
bg-clip-text
text-transparent
">

ResumePulse AI

</h1>


<p className="text-sm text-slate-500">
AI Resume Analyzer
</p>


</div> */}


</Link>





<div className="
flex
gap-8
font-semibold
">


<NavLink
to="/dashboard"
className={({isActive}) =>
isActive
?
"text-indigo-600"
:
"text-slate-600 hover:text-indigo-600"
}
>
Dashboard
</NavLink>



<NavLink
to="/upload"
className={({isActive}) =>
isActive
?
"text-indigo-600"
:
"text-slate-600 hover:text-indigo-600"
}
>
Analyze Resume
</NavLink>



<NavLink
to="/reports"
className={({isActive}) =>
isActive
?
"text-indigo-600"
:
"text-slate-600 hover:text-indigo-600"
}
>
Reports
</NavLink>


</div>


</nav>




<main className="
relative
z-10
p-8
">

<Outlet/>

</main>


</div>

)

}