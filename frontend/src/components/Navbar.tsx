import { Link, useNavigate } from "react-router-dom";
import { clearToken } from "../utils/auth";


export default function Navbar() {

    const navigate = useNavigate();


    const logout = () => {
        clearToken();
        navigate("/login");
    };


    return (

        <nav className="
        w-full
        bg-white
        shadow-sm
        border-b
        px-8
        py-4
        flex
        justify-between
        items-center
        ">


            {/* Logo */}

            <Link
                to="/dashboard"
                className="
                flex
                items-center
                gap-3
                "
            >

                <div className="
                h-10
                w-10
                rounded-xl
                bg-indigo-600
                flex
                items-center
                justify-center
                text-white
                font-bold
                "
                >
                    RP
                </div>


                <span className="
                text-2xl
                font-bold
                text-slate-900
                ">
                    ResumePulse AI
                </span>


            </Link>





            {/* Navigation */}


            <div className="
            flex
            gap-6
            items-center
            ">


                <Link
                    to="/dashboard"
                    className="text-slate-600 hover:text-indigo-600"
                >
                    Dashboard
                </Link>


                <Link
                    to="/upload"
                    className="text-slate-600 hover:text-indigo-600"
                >
                    Upload
                </Link>



                <Link
                    to="/reports"
                    className="text-slate-600 hover:text-indigo-600"
                >
                    Reports
                </Link>



                <button
                    onClick={logout}
                    className="
                    rounded-xl
                    bg-red-600
                    px-4
                    py-2
                    text-white
                    hover:bg-red-700
                    "
                >
                    Logout
                </button>



            </div>


        </nav>

    )
}