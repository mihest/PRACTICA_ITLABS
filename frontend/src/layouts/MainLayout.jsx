import {Outlet} from "react-router-dom";
import Header from "../components/Header.jsx";
import {useState} from "react";
import Loader from "../components/Loader.jsx";
import {LoadingContext} from "../context/LoadingContext.jsx";

const MainLayout = ({children}) => {
    const [loading, setLoading] = useState(true);

    return (
        <LoadingContext.Provider value={{ loading, setLoading }}>
            <div className="flex flex-col h-[1080px] bg-[#F2E5CC] relative py-[80px]">
                <div className="w-full h-[1080px] bg-[url('/background.png')] bg-center bg-no-repeat opacity-40 absolute top-0 left-0 z-1" />
                <div className="absolute top-0 right-0 z-50 h-[1080px] w-[150px] pointer-events-none bg-gradient-to-l from-[#F2E5CC]/100 to-[#F2E5CC]/0" />
                <Header className="z-2 ms-[80px]" />
                <main className="flex flex-1 z-2">
                    {children}
                </main>
                {loading && (
                    <Loader className="z-2"></Loader>
                )}

            </div>
        </LoadingContext.Provider>
    )
}
export default MainLayout