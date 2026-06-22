import { useNavigate } from "react-router-dom";
import { clearToken } from "../utils/auth";


const DashboardPage = () => {

const navigate = useNavigate();


const handleLogout = () => {
 clearToken();
 navigate("/login");
};


return (

<div className="
min-h-screen
bg-gradient-to-br
from-indigo-50
via-white
to-purple-100
p-10
">


<div className="
mx-auto
max-w-6xl
space-y-8
">



{/* Hero */}

<div className="
rounded-3xl
bg-gradient-to-r
from-indigo-600
to-purple-600
p-10
text-white
shadow-2xl
">


<div className="
flex
justify-between
items-start
">


<div>

<h1 className="
text-5xl
font-extrabold
">
ResumePulse AI
</h1>


<p className="
mt-3
text-lg
opacity-90
">
AI powered resume matching platform
</p>


</div>



<button
onClick={handleLogout}
className="
rounded-xl
bg-white/20
px-5
py-3
backdrop-blur
hover:bg-white/30
transition
"
>
Logout
</button>


</div>



</div>





{/* Cards */}

<div className="
grid
md:grid-cols-3
gap-6
">



<button
onClick={()=>navigate("/upload")}
className="
group
rounded-3xl
bg-white
p-8
text-left
shadow-xl
border
hover:-translate-y-2
transition
"
>


<div className="
text-4xl
">
📄
</div>


<h2 className="
mt-5
text-2xl
font-bold
">
Upload Resume
</h2>


<p className="
mt-2
text-slate-500
">
Analyze your resume against job description
</p>


<span className="
mt-5
inline-block
text-indigo-600
font-semibold
">
Start →
</span>


</button>





<button
onClick={()=>navigate("/reports")}
className="
group
rounded-3xl
bg-white
p-8
text-left
shadow-xl
border
hover:-translate-y-2
transition
"
>


<div className="
text-4xl
">
📊
</div>


<h2 className="
mt-5
text-2xl
font-bold
">
Reports
</h2>


<p className="
mt-2
text-slate-500
">
View previous AI analysis
</p>


<span className="
mt-5
inline-block
text-purple-600
font-semibold
">
View →
</span>


</button>





<button
className="
rounded-3xl
bg-white
p-8
text-left
shadow-xl
border
hover:-translate-y-2
transition
"
>


<div className="
text-4xl
">
👤
</div>


<h2 className="
mt-5
text-2xl
font-bold
">
Profile
</h2>


<p className="
mt-2
text-slate-500
">
Manage account
</p>


</button>


</div>






{/* Status */}

<div className="
rounded-3xl
bg-white
p-8
shadow-xl
border
">


<h2 className="
text-2xl
font-bold
">
System Status
</h2>


<div className="
mt-5
flex
gap-4
flex-wrap
">


<div className="
rounded-xl
bg-green-100
px-5
py-3
text-green-700
font-semibold
">
✓ API Connected
</div>


<div className="
rounded-xl
bg-blue-100
px-5
py-3
text-blue-700
font-semibold
">
✓ AI Ready
</div>


<div className="
rounded-xl
bg-purple-100
px-5
py-3
text-purple-700
font-semibold
">
✓ PostgreSQL
</div>


</div>


</div>



</div>


</div>


)

}


export default DashboardPage;