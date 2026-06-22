import { useState, FormEvent } from "react";
import { Link, useNavigate } from "react-router-dom";
import { authApi } from "../services/axios";
import axios from "axios";
import { setToken } from "../utils/auth";


const RegisterPage = () => {

    const navigate = useNavigate();

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");

    const [error, setError] = useState("");
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
        event.preventDefault();

        setError("");


        if (password !== confirmPassword) {

            setError("Passwords do not match.");

            return;
        }


        setLoading(true);


        try {


            // Register user

            await authApi.post("/register/", {

                email,

                first_name: "User",

                last_name: "User",

                password,

                password2: confirmPassword,

            });



            // Login after successful register

            const loginResponse = await authApi.post("/login/", {

                email,

                password,

            });



            // Save JWT

            setToken(loginResponse.data.access);


            localStorage.setItem(
                "refresh",
                loginResponse.data.refresh
            );


            navigate("/dashboard");


        } catch (err) {


            if (axios.isAxiosError(err)) {


                const data = err.response?.data;


                const message =
                    data?.email?.[0] ||
                    data?.password?.[0] ||
                    data?.detail ||
                    "Registration failed. Try again.";


                setError(message);


            } else {


                setError(
                    "Registration failed. Try again."
                );


            }


        } finally {

            setLoading(false);

        }

    };



    return (

        <div className="flex min-h-screen items-center justify-center px-4 py-12">


            <div className="w-full max-w-md rounded-3xl bg-white p-10 shadow-xl">


                <h1 className="text-3xl font-semibold text-slate-900">
                    Create Account
                </h1>


                <p className="mt-2 text-slate-500">
                    Join ResumePulseAI
                </p>



                <form
                    onSubmit={handleSubmit}
                    className="mt-8 space-y-5"
                >


                    <input

                        type="email"

                        placeholder="Email"

                        required

                        className="w-full rounded-2xl border p-3"

                        value={email}

                        onChange={
                            (e)=>setEmail(e.target.value)
                        }

                    />



                    <input

                        type="password"

                        placeholder="Password"

                        required

                        minLength={8}

                        className="w-full rounded-2xl border p-3"

                        value={password}

                        onChange={
                            (e)=>setPassword(e.target.value)
                        }

                    />



                    <input

                        type="password"

                        placeholder="Confirm Password"

                        required

                        minLength={8}

                        className="w-full rounded-2xl border p-3"

                        value={confirmPassword}

                        onChange={
                            (e)=>setConfirmPassword(e.target.value)
                        }

                    />



                    {error && (

                        <p className="rounded-xl bg-red-50 p-3 text-red-700">

                            {error}

                        </p>

                    )}




                    <button

                        type="submit"

                        disabled={loading}

                        className="w-full rounded-2xl bg-indigo-600 p-3 text-white hover:bg-indigo-700 disabled:opacity-60"

                    >

                        {
                            loading
                            ? "Creating account..."
                            : "Create account"
                        }

                    </button>



                </form>




                <p className="mt-6 text-center text-sm text-slate-500">

                    Already have an account?{" "}


                    <Link

                        to="/login"

                        className="font-semibold text-indigo-600"

                    >

                        Login

                    </Link>


                </p>


            </div>


        </div>

    );

};


export default RegisterPage;